# Quy trình huấn luyện mô hình

## Tổng quan

```
Ratings từ DB → Pandas DataFrame → Surprise Dataset → SVD Training → Cross-validation → Evaluation → Export Model
```

## Chi tiết các bước

### Bước 1: Chuẩn bị dữ liệu

**Lấy ratings từ Django ORM:**
```python
def export_ratings_dataset():
    ctype = ContentType.objects.get(app_label='movies', model='movie')
    qs = Rating.objects.filter(active=True, content_type=ctype)
    qs = qs.annotate(
        userId=F('user_id'),
        movieId=F('object_id'),
        rating=F('value')
    )
    return qs.values('userId', 'movieId', 'rating')
```

**Chuyển đổi sang Pandas DataFrame:**
```python
def get_data_loader(dataset, columns=['userId', 'movieId', 'rating']):
    import pandas as pd
    df = pd.DataFrame(dataset)
    df['rating'].dropna(inplace=True)
    max_rating, min_rating = df.rating.max(), df.rating.min()
    reader = Reader(rating_scale=(min_rating, max_rating))
    return Dataset.load_from_df(df[columns], reader)
```

### Bước 2: Khởi tạo mô hình

```python
from surprise import SVD

model = SVD(
    n_epochs=20,
    verbose=True,
    lr_all=0.005,
    reg_all=0.02
)
```

### Bước 3: Cross-validation (4-fold)

```python
from surprise.model_selection import cross_validate

cv_results = cross_validate(
    model,
    loaded_data,
    measures=['RMSE', 'MAE'],
    cv=4,
    verbose=True
)

# Kết quả:
# {
#     'test_rmse': [0.85, 0.87, 0.84, 0.86],  # 4 folds
#     'test_mae': [0.65, 0.68, 0.64, 0.67],
#     'fit_time': [...],
#     'test_time': [...]
# }
```

### Bước 4: Fit trên full training set

```python
trainset = loaded_data.build_full_trainset()
model.fit(trainset)
```

### Bước 5: Đánh giá trên test set

```python
from surprise import accuracy

testset = trainset.build_testset()
predictions = model.test(testset)
rmse = accuracy.rmse(predictions, verbose=True)
mae = accuracy.mae(predictions, verbose=True)
```

### Bước 6: Export mô hình

**Serialize model thành pickle:**
```python
def export_model(model, model_name='model', model_type='surprise', model_ext='pkl'):
    with tempfile.NamedTemporaryFile(mode='rb+') as temp_f:
        pickle.dump({"model": model}, temp_f)
        
        # Lưu versioned model
        path = f"ml/models/{model_type}/{model_name}.{model_ext}"
        exports_storages.save(path, File(temp_f))
        
        # Lưu latest symlink
        path_latest = f"ml/models/{model_type}/latest.{model_ext}"
        exports_storages.save(path_latest, File(temp_f), overwrite=True)
```

### Bước 7: Load mô hình cho prediction

```python
def load_model(model_type='surprise', model_ext='pkl'):
    path_latest = settings.MEDIA_ROOT / f"ml/models/{model_type}/latest.{model_ext}"
    with open(path_latest, 'rb') as f:
        model_data = pickle.load(f)
        return model_data.get('model')
```

## Thời gian và hiệu suất

| Metric | Giá trị |
|--------|--------|
| **Training time** | 2-5 phút (với ~100K ratings) |
| **Prediction latency** | 1-5ms per prediction |
| **Batch prediction** | 1000+ predictions/second |
| **Model size** | ~10-50MB (pickle format) |

## Lập lịch training (Celery Beat)

```python
# Settings.py
CELERY_BEAT_SCHEDULE = {
    'train-model-daily': {
        'task': 'ml.tasks.train_surprise_model_task',
        'schedule': crontab(hour=2, minute=0),  # 2:00 AM mỗi ngày
        'args': (20,)  # n_epochs=20
    }
}
```

## Celery Task

```python
# ml/tasks.py
@shared_task
def train_surprise_model_task(n_epochs=20):
    ml_utils.train_surprise_model(n_epochs=n_epochs)
    # Sau khi train xong, tự động trigger batch prediction
    batch_users_prediction_task.delay()
```
