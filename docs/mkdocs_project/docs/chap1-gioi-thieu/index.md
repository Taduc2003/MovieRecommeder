# Chương I: Giới thiệu

## 1. Giới thiệu tổng quan về project

Hệ thống gợi ý phim (Hybrid Movie Recommendation System) là một ứng dụng web hiện đại xây dựng bằng **Django** kết hợp với công nghệ **Machine Learning (ML)** và **MLOps**. Dự án được phát triển như một hệ thống xử lý các tác vụ asynchronous, cho phép huấn luyện và dự đoán các mô hình ML một cách hiệu quả mà không ảnh hưởng đến trải nghiệm người dùng.

Hệ thống sử dụng kỹ thuật Collaborative Filtering (CF) để phân tích lịch sử xếp hạng của người dùng, từ đó đưa ra các gợi ý phim được cá nhân hóa. Các dự đoán được sinh ra qua mô hình SVD (Singular Value Decomposition) được huấn luyện từ tập dữ liệu công khai từ Kaggle.

## 2. Lý do lựa chọn đề tài

Dự án được lựa chọn để giải quyết bài toán **ML Pipeline Orchestration** chứ không phải bài toán cold-start problem. Lý do chính:

1. **Hiểu rõ quy trình MLOps**: Cần nắm vững cách xây dựng, huấn luyện, triển khai và duy trì mô hình ML trong sản xuất
2. **Tích hợp ML vào sản phẩm thực tế**: Django cho phép tích hợp ML seamlessly vào ứng dụng web
3. **Xử lý tác vụ không đồng bộ**: Sử dụng Celery để quản lý các tác vụ ML nặng mà không chặn request HTTP
4. **Giám sát và đánh giá mô hình**: Theo dõi hiệu suất mô hình qua RMSE, MAE metrics
5. **Tự động cập nhật**: Hệ thống có thể tự động huấn luyện lại mô hình khi có dữ liệu mới

## 3. Phạm vi và đối tượng của project

### Phạm vi

- Xây dựng hệ thống gợi ý phim sử dụng Collaborative Filtering
- Tích hợp Django với ML framework (Surprise)
- Sử dụng Celery + Redis cho task queue và scheduling
- Triển khai bằng Docker và Docker Compose
- Quản lý dữ liệu từ nguồn công khai (Kaggle - The Movies Dataset)

### Đối tượng

- **Người dùng cuối**: Nhận được gợi ý phim được cá nhân hóa
- **Nhà phát triển**: Hiểu rõ quy trình MLOps từ training đến deployment
- **Hệ thống**: Xử lý hàng chục ngàn phim và hàng trăm ngàn đánh giá
