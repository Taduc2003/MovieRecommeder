# Theo dõi và đánh giá hoạt động của mô hình

## Metrics chính

### Training Metrics

| Metric | Mô tả | Target |
|--------|-------|--------|
| **RMSE** | Root Mean Squared Error | < 1.0 |
| **MAE** | Mean Absolute Error | < 0.8 |
| **Cross-validation** | 4-fold CV score | Ổn định |

### Inference Metrics

| Metric | Mô tả | Target |
|--------|-------|--------|
| **Latency** | Thời gian per prediction | < 5ms |
| **Throughput** | Predictions per second | > 1000/s |
| **Accuracy** | % predictions matching actual | > 70% |

## Monitoring Celery Tasks

### Kiểm tra task results

```python
from django_celery_results.models import TaskResult

# Get all tasks
all_tasks = TaskResult.objects.all()

# Filter by status
successful = TaskResult.objects.filter(status='SUCCESS')
failed = TaskResult.objects.filter(status='FAILURE')
pending = TaskResult.objects.filter(status='PENDING')

# Get task details
latest_task = TaskResult.objects.latest('date_done')
print(f"Task ID: {latest_task.task_id}")
print(f"Status: {latest_task.status}")
print(f"Result: {latest_task.result}")
print(f"Runtime: {latest_task.date_done - latest_task.date_created}")
```

### Task Status Distribution

```python
from django.db.models import Count

status_dist = TaskResult.objects.values('status').annotate(count=Count('id'))
# Output:
# [
#     {'status': 'SUCCESS', 'count': 145},
#     {'status': 'FAILURE', 'count': 3},
#     {'status': 'RETRY', 'count': 1}
# ]
```

## Model Performance Tracking

### Log training results

```python
def train_and_log_metrics():
    from ml.utils import train_surprise_model, export_ratings_dataset, get_data_loader
    from surprise.model_selection import cross_validate
    from surprise import SVD
    
    # Load data
    dataset = export_ratings_dataset()
    loaded_data = get_data_loader(dataset)
    
    # Cross-validation
    model = SVD(n_epochs=20, verbose=True)
    cv_results = cross_validate(
        model,
        loaded_data,
        measures=['RMSE', 'MAE'],
        cv=4,
        verbose=True
    )
    
    # Extract metrics
    rmse_mean = cv_results['test_rmse'].mean()
    rmse_std = cv_results['test_rmse'].std()
    mae_mean = cv_results['test_mae'].mean()
    mae_std = cv_results['test_mae'].std()
    
    # Log to database
    print(f"RMSE: {rmse_mean:.3f} ± {rmse_std:.3f}")
    print(f"MAE: {mae_mean:.3f} ± {mae_std:.3f}")
    
    # Optional: Save to database for historical tracking
    from ml.models import ModelMetrics
    ModelMetrics.objects.create(
        rmse_mean=rmse_mean,
        rmse_std=rmse_std,
        mae_mean=mae_mean,
        mae_std=mae_std,
        n_epochs=20
    )
```

## Suggestion Quality Metrics

### Acceptance Rate

```python
from django.db.models import Count, Q
from suggestions.models import Suggestion

# Calculate acceptance rate
total_suggestions = Suggestion.objects.filter(active=True).count()
accepted_suggestions = Suggestion.objects.filter(did_rate=True).count()

acceptance_rate = (accepted_suggestions / total_suggestions * 100) if total_suggestions > 0 else 0
print(f"Suggestion acceptance rate: {acceptance_rate:.1f}%")
```

### Rating Correlation

```python
from django.db.models import Avg
from suggestions.models import Suggestion

# Compare predicted vs actual ratings
ratings_given = Suggestion.objects.filter(did_rate=True)

avg_prediction = ratings_given.aggregate(Avg('value'))['value__avg']
avg_actual = ratings_given.aggregate(Avg('rating_value'))['rating_value__avg']

print(f"Avg predicted: {avg_prediction:.2f}")
print(f"Avg actual: {avg_actual:.2f}")
print(f"Difference: {abs(avg_prediction - avg_actual):.2f}")
```

### User Engagement

```python
from django.contrib.auth import get_user_model

User = get_user_model()

# Active users (have rated movies)
active_users = User.objects.filter(rating__isnull=False).distinct().count()

# Users who acted on suggestions
engaged_users = User.objects.filter(suggestion__did_rate=True).distinct().count()

print(f"Active users: {active_users}")
print(f"Engaged users: {engaged_users}")
print(f"Engagement rate: {engaged_users/active_users*100:.1f}%")
```

## Health Checks

### Model Availability

```python
from pathlib import Path
from django.conf import settings

def check_model_health():
    model_path = settings.MEDIA_ROOT / "ml/models/surprise/latest.pkl"
    
    if not model_path.exists():
        print("❌ WARNING: No trained model found!")
        return False
    
    size_mb = model_path.stat().st_size / 1024 / 1024
    print(f"✓ Model found: {size_mb:.1f}MB")
    
    # Check model age
    from datetime import datetime, timedelta
    age = datetime.now() - datetime.fromtimestamp(model_path.stat().st_mtime)
    
    if age > timedelta(days=7):
        print(f"⚠️ WARNING: Model is {age.days} days old")
    
    return True
```

### Celery Worker Status

```python
from celery.app.control import Inspect

def check_celery_health():
    inspect = Inspect()
    
    # Check active workers
    stats = inspect.stats()
    
    if not stats:
        print("❌ WARNING: No Celery workers running!")
        return False
    
    print(f"✓ Workers active: {len(stats)}")
    
    # Check active tasks
    active_tasks = inspect.active()
    if active_tasks:
        total_tasks = sum(len(tasks) for tasks in active_tasks.values())
        print(f"  Active tasks: {total_tasks}")
    
    return True
```

### Database Connection

```python
from django.db import connection
from django.db.utils import OperationalError

def check_database_health():
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1")
        print("✓ Database connection OK")
        return True
    except OperationalError as e:
        print(f"❌ Database connection failed: {e}")
        return False
```

## Logging Strategy

### Setup Django Logging

```python
# settings.py
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '{levelname} {asctime} {module} {process:d} {thread:d} {message}',
            'style': '{',
        },
    },
    'handlers': {
        'file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': 'logs/django.log',
            'formatter': 'verbose',
        },
        'ml_file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': 'logs/ml.log',
            'formatter': 'verbose',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'INFO',
            'propagate': True,
        },
        'ml': {
            'handlers': ['ml_file'],
            'level': 'INFO',
            'propagate': False,
        },
    },
}
```

### Log Training Progress

```python
import logging

logger = logging.getLogger('ml')

def train_surprise_model(n_epochs=20):
    logger.info(f"Starting training with n_epochs={n_epochs}")
    
    try:
        dataset = export_ratings_dataset()
        logger.info(f"Loaded {len(dataset)} ratings")
        
        model = SVD(n_epochs=n_epochs)
        trainset = loaded_data.build_full_trainset()
        model.fit(trainset)
        
        logger.info("Model training completed successfully")
    except Exception as e:
        logger.error(f"Training failed: {e}")
        raise
```

## Visualization & Dashboard

### Using Django Admin

- Monitor tasks in `django_celery_results.taskresult`
- View suggestions in `suggestions.suggestion`
- Track model versions in custom `ModelVersion` model

### Using Flower (Celery Monitoring)

```bash
pip install flower
celery -A cfehome flower
# Access at http://localhost:5555
```

### Custom Metrics API

```python
# views.py
@require_GET
def api_metrics(request):
    return JsonResponse({
        'model_status': check_model_health(),
        'celery_status': check_celery_health(),
        'database_status': check_database_health(),
        'suggestion_acceptance': calculate_acceptance_rate(),
        'active_users': count_active_users(),
    })
```
