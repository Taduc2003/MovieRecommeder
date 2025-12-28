# Dữ liệu sử dụng trong project

## Nguồn dữ liệu

- **The Movies Dataset** từ Kaggle
- Link: https://www.kaggle.com/datasets/rounakbanik/the-movies-dataset

## Các file dữ liệu chính

| File | Mô tả | Format |
|------|-------|--------|
| `movies_metadata.csv` | Thông tin chi tiết về các bộ phim | CSV |
| `ratings_small.csv` | Tập ratings của người dùng | CSV |
| `links_small.csv` | Ánh xạ movieId giữa các nguồn | CSV |

## Đặc điểm dữ liệu

- **Số lượng phim**: ~9,000+
- **Số lượng người dùng**: ~600+
- **Số lượng ratings**: ~100,000+
- **Phạm vi rating**: 0.5 - 5.0 (cách nhau 0.5)
- Dữ liệu được load vào database Django thông qua management command

## Xử lý dữ liệu

- Làm sạch giá trị NaN trong rating
- Chuẩn hóa rating scale theo min/max từ dữ liệu thực
- Lọc ratings active=True (loại bỏ ratings bị xóa)

## Cấu trúc dữ liệu trong Django ORM

### Movie Model

```python
class Movie(models.Model):
    title = CharField(max_length=120, unique=True)
    overview = TextField()
    release_date = DateField(null=True)
    rating_avg = DecimalField(max_digits=5, decimal_places=2)
    rating_count = IntegerField()
    score = FloatField()  # Tính toán: average_rating × rating_count
    idx = IntegerField()  # Position ID cho embedding
```

### Rating Model

```python
class Rating(models.Model):
    user = ForeignKey(User, on_delete=models.CASCADE)
    value = IntegerField(choices=RatingChoice.choices)  # 1-5
    content_type = ForeignKey(ContentType)
    object_id = PositiveIntegerField()
    active = BooleanField(default=True)
    timestamp = DateTimeField(auto_now_add=True)
```

### Suggestion Model

```python
class Suggestion(models.Model):
    user = ForeignKey(User)
    value = FloatField()  # Prediction score
    object_id = PositiveIntegerField()
    did_rate = BooleanField(default=False)
    rating_value = FloatField(null=True)  # User's actual rating
```
