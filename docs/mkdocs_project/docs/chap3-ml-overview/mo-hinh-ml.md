# Mô hình Machine Learning được áp dụng

## SVD (Singular Value Decomposition)

### Đặc điểm chính

| Thuộc tính | Giá trị |
|-----------|--------|
| **Framework** | Surprise (scikit-surprise) |
| **Kỹ thuật** | Matrix Factorization |
| **Tham số chủ yếu** | `n_epochs` (số lần lặp training, mặc định = 20) |

### Lý do chọn SVD

✅ Hiệu quả cao cho bài toán collaborative filtering  
✅ Ít overfitting so với các phương pháp khác  
✅ Hỗ trợ implicit/explicit ratings  
✅ Dễ tune hyperparameters  
✅ Cho prediction nhanh (O(1) complexity)  

## Metrics đánh giá

### Chính

- **RMSE (Root Mean Squared Error)**: Đo sai số bình phương trung bình
- **MAE (Mean Absolute Error)**: Đo sai số tuyệt đối trung bình
- **Cross-validation**: 4-fold CV để tránh overfitting

### Threshold hiệu suất

- RMSE < 1.0 được coi là tốt
- Model được export với tên `model-{acc_label}` (ví dụ: model-85 tức RMSE = 0.85)

## Hybrid Approach

Hệ thống sử dụng **Hybrid Recommendation** kết hợp:

1. **Collaborative Filtering** (từ ratings)
   - Dự đoán: mức độ liên quan cá nhân (`value`)
   - Nguồn: lịch sử xếp hạng của user & users tương tự

2. **Content-based Sorting** (theo phim)
   - Xếp hạng: độ phổ biến phim (`score`)
   - Công thức: `score = average_rating × rating_count`

### Quy trình gợi ý

```
1. Sử dụng SVD dự đoán rating cho mỗi (user, movie)
   ↓
2. Sắp xếp theo prediction score (value) DESC
   ↓
3. Lọc movie mà user chưa xếp hạo
   ↓
4. Sắp xếp theo movie popularity (score) DESC
   ↓
5. Trả về top 50 gợi ý
```

## Hyperparameters SVD

```python
SVD(
    n_factors=100,      # Số latent factors
    n_epochs=20,        # Số epoch training
    lr_all=0.005,       # Learning rate
    reg_all=0.02,       # Regularization parameter
    verbose=True
)
```
