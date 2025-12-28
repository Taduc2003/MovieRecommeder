# Quy trình training và cập nhật mô hình

## Kiến trúc tổng thể

```
User Web Interface
        ↓
Django Views/APIs
        ↓
Celery Task Queue
        ↓
Worker Process
        ↓
ML Pipeline (Train/Predict)
        ↓
Model Store (filesystem) & Suggestion DB
```

## Training Pipeline

**Trigger:** Manual hoặc Celery Beat scheduler

```python
# Celery task
@shared_task
def train_surprise_model_task(n_epochs=20):
    ml_utils.train_surprise_model(n_epochs=n_epochs)
```

**Workflow:**
```
1. export_ratings_dataset()       # Get ratings from DB
   ↓
2. get_data_loader()             # Convert to Surprise format
   ↓
3. SVD.fit(trainset)             # Train model
   ↓
4. accuracy.rmse(predictions)    # Evaluate
   ↓
5. export_model()                # Save model pickle
   ↓
6. batch_users_prediction_task() # Trigger batch prediction
```

## Batch Prediction Pipeline

**Trigger:** Celery Beat scheduler hoặc manual

```python
@shared_task
def batch_users_prediction_task(users_ids=None, start_page=0, offset=50):
    model = ml_utils.load_model()
    ctype = ContentType.objects.get(app_label='movies', model='movie')
    
    movie_ids = Movie.objects.all().popular().values_list('id')[start_page:start_page+offset]
    
    for movie_id in movie_ids:
        for user_id in users_ids:
            # Skip if already suggested recently
            if suggestion_exists_recently(user_id, movie_id):
                continue
            
            # Predict rating
            pred = model.predict(uid=user_id, iid=movie_id).est
            
            # Save suggestion
            Suggestion.objects.update_or_create(
                user_id=user_id,
                object_id=movie_id,
                content_type=ctype,
                defaults={'value': pred}
            )
    
    # Recursive call for next page
    if start_page < max_pages:
        batch_users_prediction_task.delay(
            start_page=start_page+offset-1
        )
```

## Suggestion Retrieval (API)

```python
def api_suggestions(request):
    user_id = request.GET.get('user_id')
    
    # Get suggestions that user hasn't rated
    suggestion_qs = Suggestion.objects.filter(
        user=user_id,
        did_rate=False
    )
    
    # Sort by prediction score
    movie_ids = suggestion_qs.order_by('-value').values_list('object_id')
    
    # Get movies and sort by popularity
    movies = Movie.objects.filter(pk__in=movie_ids).order_by('-score')[:50]
    
    return JsonResponse({
        'suggestions': [
            {
                'id': m.id,
                'title': m.title,
                'overview': m.overview
            }
            for m in movies
        ]
    })
```

## Cập nhật mô hình

| Thuộc tính | Chi tiết |
|-----------|---------|
| **Trigger** | Hàng ngày hoặc hàng tuần (Celery Beat) |
| **Điều kiện** | Khi có ratings mới từ người dùng |
| **Quy trình** | 1. Train → 2. Evaluate → 3. Update latest.pkl → 4. Batch predict |

## Celery Configuration

```python
# settings.py
CELERY_BROKER_URL = 'redis://localhost:6379'
CELERY_RESULT_BACKEND = 'django-db'
CELERY_BEAT_SCHEDULER = 'django_celery_beat.schedulers.DatabaseScheduler'

# Scheduled tasks
CELERY_BEAT_SCHEDULE = {
    'train-model-daily': {
        'task': 'ml.tasks.train_surprise_model_task',
        'schedule': crontab(hour=2, minute=0),
        'args': (20,)
    },
    'batch-predict-daily': {
        'task': 'ml.tasks.batch_users_prediction_task',
        'schedule': crontab(hour=3, minute=0),
    }
}
```
