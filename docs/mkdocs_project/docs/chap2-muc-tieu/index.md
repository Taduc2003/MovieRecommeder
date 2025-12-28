# Chương II: Mục tiêu

## 1. Mục tiêu tổng quát

Phát triển một hệ thống web hoàn chỉnh kết hợp Django, Machine Learning, và MLOps để:

1. Cung cấp gợi ý phim được cá nhân hóa cho người dùng
2. Xây dựng quy trình MLOps hiệu quả để huấn luyện, triển khai và duy trì mô hình ML
3. Tự động hóa các tác vụ ML thông qua Celery Task Queue
4. Giám sát và đánh giá liên tục hiệu suất mô hình
5. Triển khai hệ thống trên Docker cho sự nhất quán và dễ bảo trì

## 2. Mục tiêu cụ thể

### Chuẩn bị dữ liệu

- Load dữ liệu phim từ The Movies Dataset (Kaggle)
- Tạo tập dữ liệu ratings từ người dùng thực tế hoặc fake users

### Huấn luyện mô hình

- Sử dụng Surprise SVD (Singular Value Decomposition) với cross-validation
- Đạt RMSE < 1.0 trên tập test
- Tối ưu hóa n_epochs để cân bằng giữa độ chính xác và thời gian training

### Dự đoán và gợi ý

- Sinh ra gợi ý cho tất cả người dùng trên tất cả các phim phổ biến
- Loại bỏ các phim người dùng đã xếp hạng
- Xếp hạng gợi ý theo mức độ liên quan (value) và độ phổ biến phim (score)

### Tự động hóa

- Tạo Celery Beat task để huấn luyện lại mô hình định kỳ
- Tạo Celery Worker để thực thi batch prediction
- Quản lý task results trong database

### Triển khai và duy trì

- Docker Compose orchestration với PostgreSQL, Redis, Web, Worker
- API endpoint để lấy gợi ý cho user cụ thể
- Monitoring hiệu suất mô hình qua metrics (RMSE, MAE)
