# Cách triển khai mô hình vào hệ thống

## Cấu trúc lưu trữ mô hình

```
media/
└── ml/
    └── models/
        └── surprise/
            ├── latest.pkl      (current model in use)
            ├── model-85.pkl    (version history, RMSE = 0.85)
            ├── model-82.pkl    (version history, RMSE = 0.82)
            └── model-88.pkl    (version history, RMSE = 0.88)
```

## Load & Inference

**Trong Django views, utils, hoặc tasks:**

```python
from ml.utils import load_model

# Load latest model
model = load_model(model_type='surprise', model_ext='pkl')

# Make prediction for a specific user-movie pair
pred_rating = model.predict(uid=user_id, iid=movie_id).est
```

## Tích hợp vào Django ORM

**Lưu predictions vào Suggestion model:**

```python
from suggestions.models import Suggestion
from django.contrib.contenttypes.models import ContentType

ctype = ContentType.objects.get(app_label='movies', model='movie')

# Create or update suggestion
Suggestion.objects.update_or_create(
    user_id=user_id,
    object_id=movie_id,
    content_type=ctype,
    defaults={
        'value': pred_rating,  # Prediction score
        'active': True
    }
)
```

## API Endpoint

**URL Configuration (urls.py):**

```python
from django.urls import path
from suggestions.views import api_suggestions

urlpatterns = [
    path('api/suggestions/', api_suggestions, name='api_suggestions'),
]
```

**Example request:**
```
GET /api/suggestions/?user_id=123
```

**Example response:**
```json
{
  "suggestions": [
    {
      "id": 550,
      "title": "Fight Club",
      "overview": "An insomniac office worker and a devil-may-care..."
    },
    {
      "id": 278,
      "title": "The Shawshank Redemption",
      "overview": "Two imprisoned men bond over a number of years..."
    },
    ...
  ]
}
```

## Frontend Integration

**Using JavaScript/Fetch API:**

```javascript
async function getSuggestions(userId) {
  const response = await fetch(`/api/suggestions/?user_id=${userId}`);
  const data = await response.json();
  
  // Display suggestions
  data.suggestions.forEach(movie => {
    console.log(`${movie.title}: ${movie.overview}`);
  });
}

// Usage
getSuggestions(123);
```

**Using HTMX (included in project):**

```html
<div hx-get="/api/suggestions/?user_id=123"
     hx-trigger="load"
     hx-swap="innerHTML">
  Loading suggestions...
</div>
```

## Performance Optimization

### Singleton Pattern

```python
# Load model once at startup
from django.apps import AppConfig

class MlConfig(AppConfig):
    name = 'ml'
    
    def ready(self):
        from ml.utils import load_model
        self.model = load_model()  # Cache model in memory
```

### Prediction Latency

- **Single prediction**: O(1) latency (~1-5ms per prediction)
- **Batch mode**: Process 1000+ predictions in parallel
- **Caching**: Store frequent predictions in Redis

### Database Optimization

```python
# Add indexes to models
class Suggestion(models.Model):
    user = ForeignKey(User)
    object_id = PositiveIntegerField()
    
    class Meta:
        indexes = [
            models.Index(fields=['user', 'object_id']),
            models.Index(fields=['user', 'did_rate']),
        ]
```

### Caching Strategy

```python
from django.core.cache import cache

def get_suggestions_cached(user_id, timeout=3600):
    cache_key = f'suggestions_{user_id}'
    suggestions = cache.get(cache_key)
    
    if suggestions is None:
        suggestions = api_suggestions(user_id)
        cache.set(cache_key, suggestions, timeout)
    
    return suggestions
```

## Model Versioning

**Track model changes:**

```python
from django.db import models

class ModelVersion(models.Model):
    version_name = CharField(max_length=50)  # e.g., 'model-85'
    rmse = FloatField()
    mae = FloatField()
    created_at = DateTimeField(auto_now_add=True)
    is_active = BooleanField(default=False)
    
    def activate(self):
        # Deactivate all others
        ModelVersion.objects.filter(is_active=True).update(is_active=False)
        # Activate this version
        self.is_active = True
        self.save()
```
