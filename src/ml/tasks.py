from django.apps import apps
from django.contrib.contenttypes.models import ContentType
from celery import shared_task
from movies.models import Movie
from profiles import utils as profile_utils
from ratings.models import Rating
from . import utils as ml_utils
from django.utils import timezone
from django.conf import settings
import os
import pytz

# Lưu thời điểm retrain gần nhất vào file (hoặc có thể dùng cache/db)
LAST_RETRAIN_FILE = "local-cdn/media/ml/models/surprise/last_retrain.txt"

# Giờ Việt Nam
vietnam_tz = pytz.timezone('Asia/Ho_Chi_Minh')
now_vn = timezone.now().astimezone(vietnam_tz)


@shared_task
def train_surprise_model_task(n_epochs=20):
    ml_utils.train_surprise_model(n_epochs=n_epochs)


@shared_task
def batch_users_prediction_task(users_ids=None, start_page=0, offset=50, max_pages=1000):
    model = ml_utils.load_model()
    Suggestion = apps.get_model('suggestions', 'Suggestion')
    ctype = ContentType.objects.get(app_label='movies', model='movie')
    end_page = start_page + offset
    if users_ids is None:
        users_ids = profile_utils.get_recent_users()
    movie_ids = Movie.objects.all().popular().values_list(
        'id', flat=True)[start_page:end_page]
    recently_suggested = Suggestion.objects.get_recently_suggested(
        movie_ids, users_ids)
    new_suggestion = []
    if not movie_ids.exists():
        return
    for movie_id in movie_ids:
        users_done = recently_suggested.get(f"{movie_id}") or []
        for u in users_ids:
            if u in users_done:
                # print(movie_id, 'is done for', u, 'user')
                continue
            if u is None:
                continue
            if movie_id is None:
                continue
            pred = model.predict(uid=u, iid=movie_id).est
            data = {
                'user_id': u,
                'object_id': movie_id,
                'value': pred,
                'content_type': ctype
            }
            try:
                obj, _ = Suggestion.objects.get_or_create(
                    user_id=u, object_id=movie_id, content_type=ctype)
            except Suggestion.MultipleObjectsReturned:
                qs = Suggestion.objects.filter(
                    user_id=u, object_id=movie_id, content_type=ctype)
                obj = qs.first()
                to_delete = qs.exclude(id=obj.id)
                to_delete.delete()
            if obj.value != pred:
                obj.value = pred
                obj.save()
    if end_page < max_pages:
        return batch_users_prediction_task(start_page=end_page-1)


def get_last_retrain_time():
    try:
        with open(LAST_RETRAIN_FILE, "r") as f:
            return timezone.datetime.fromisoformat(f.read().strip())
    except Exception:
        return timezone.make_aware(timezone.datetime.min)


def set_last_retrain_time(dt):
    # Tạo thư mục cha nếu chưa tồn tại
    os.makedirs(os.path.dirname(LAST_RETRAIN_FILE), exist_ok=True)
    print("path:", os.path.dirname(LAST_RETRAIN_FILE))
    with open(LAST_RETRAIN_FILE, "w") as f:
        f.write(dt.isoformat())


@shared_task
def check_and_retrain_and_recommend():
    last_retrain = get_last_retrain_time()
    new_ratings = Rating.objects.filter(timestamp__gt=last_retrain).count()
    if new_ratings >= 100:
        train_surprise_model_task()
        set_last_retrain_time(now_vn)
