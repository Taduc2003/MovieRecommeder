from django.http import HttpResponse
from .models import Rating
from ml import tasks as ml_tasks
from django.views.decorators.http import require_http_methods
from django.contrib.contenttypes.models import ContentType
from django.http import JsonResponse
from django.views.decorators.http import require_GET
from django.contrib.auth import get_user_model
from movies.models import Movie

# API: Lấy danh sách phim user đã rating


@require_GET
def api_rated_movies(request):
    user_id = request.GET.get('user_id')
    if not user_id:
        return JsonResponse({'error': 'Missing user_id'}, status=400)
    try:
        user = get_user_model().objects.get(pk=user_id)
    except get_user_model().DoesNotExist:
        return JsonResponse({'error': 'User not found'}, status=404)
    # Lấy các rating của user cho phim
    from django.contrib.contenttypes.models import ContentType
    movie_ctype = ContentType.objects.get(app_label='movies', model='movie')
    ratings = Rating.objects.filter(
        user=user, content_type=movie_ctype, active=True)
    movie_ids = ratings.values_list('object_id', flat=True)
    movies = Movie.objects.filter(pk__in=movie_ids)
    movie_dict = {m.id: m for m in movies}
    rated_list = []
    for r in ratings:
        m = movie_dict.get(r.object_id)
        if m:
            rated_list.append({
                'id': m.id,
                'title': m.title,
                'overview': m.overview if hasattr(m, 'overview') else '',
                'rating': r.value,
            })
    return JsonResponse({'rated_movies': rated_list})


@require_http_methods(['POST'])
def rate_movie_view(request):
    if not request.htmx:
        return HttpResponse("Not Allowed", status=400)
    object_id = request.POST.get('object_id')
    rating_value = request.POST.get("rating_value")
    if object_id is None or rating_value is None:
        response = HttpResponse("Skipping", status=200)
        response['HX-Trigger'] = 'did-skip-movie'
        return response
    user = request.user
    message = "You must <a href='/accounts/login'>login</a> to rate this."
    if user.is_authenticated:
        message = "<span class='bg-danger text-light py-1 px-3 rounded'>An error occured.</div>"
        ctype = ContentType.objects.get(app_label='movies', model='movie')
        rating_obj = Rating.objects.create(
            content_type=ctype, object_id=object_id, value=rating_value, user=user)
        if rating_obj.content_object is not None:
            total_new_suggestions = request.session.get(
                "total-new-suggestions") or 0
            items_rated = request.session.get('items-rated') or 0
            items_rated += 1
            request.session['items-rated'] = items_rated
            print('items_rated', items_rated)
            if items_rated % 5 == 0:
                print("trigger new suggestions")
                users_ids = [user.id]
                ml_tasks.batch_users_prediction_task.apply_async(kwargs={
                    "users_ids": users_ids,
                    "start_page": total_new_suggestions,
                    "max_pages": 10
                })
            message = "<span class='bg-success text-light py-1 px-3 rounded'>Rating saved!</div>"
            response = HttpResponse(message, status=200)
            response['HX-Trigger-After-Settle'] = 'did-rate-movie'
            return response
    return HttpResponse(message, status=200)
