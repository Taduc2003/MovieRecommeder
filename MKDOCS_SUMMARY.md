# 📚 MkDocs Documentation - Hoàn thành

Báo cáo MLOps **Hybrid Movie Recommendation System** đã được chuyển đổi thành trang web tương tác sử dụng **MkDocs** + **Material Theme**.

## 📂 Cấu trúc Project

```
docs/mkdocs_project/
├── mkdocs.yml                    # Cấu hình MkDocs
├── requirements.txt              # Dependencies
├── README.md                      # Hướng dẫn sử dụng
├── docs/                          # Folder chứa tài liệu
│   ├── index.md                  # Trang chủ
│   ├── chap1-gioi-thieu/         # Chương I: Giới thiệu
│   │   └── index.md
│   ├── chap2-muc-tieu/           # Chương II: Mục tiêu
│   │   └── index.md
│   ├── chap3-ml-overview/        # Chương III: ML Overview
│   │   ├── bai-toan-ml.md        • Bài toán ML
│   │   ├── du-lieu.md             • Dữ liệu
│   │   ├── mo-hinh-ml.md          • Mô hình SVD
│   │   └── quy-trinh-huan-luyen.md • Quy trình training
│   ├── chap4-deployment/         # Chương IV: Triển khai
│   │   ├── quy-trinh-training.md • Quy trình training
│   │   ├── deployment.md          • Cách deployment
│   │   ├── moi-truong.md          • Môi trường & công cụ
│   │   └── monitoring.md          • Monitoring & evaluation
│   └── chap5-conclusion/         # Chương V: Kết luận
│       └── index.md
└── site/                         # Generated static website
```

## 🎯 Thống kê

- **12 file Markdown** được tạo
- **~47KB** nội dung tài liệu
- **5 chương chính** với 14 phần nội dung
- **Khả năng responsive** trên tất cả thiết bị

## 🚀 Cách sử dụng

### Khởi động Development Server

```bash
cd docs/mkdocs_project
pip install -r requirements.txt
mkdocs serve
```

**Truy cập:** http://127.0.0.1:8000/

### Build Static Site

```bash
mkdocs build
```

Output: `site/` folder - sẵn sàng deploy

### Deploy to GitHub Pages

```bash
mkdocs gh-deploy
```

## ✨ Tính năng

✅ **Material Design Theme**
- Giao diện hiện đại, responsive
- Dark mode & Light mode
- Navigation tabs & breadcrumbs

✅ **Tìm kiếm thông minh**
- Full-text search across all pages
- Instant results

✅ **Hỗ trợ Markdown mở rộng**
- Math equations: $\hat{r}_{ui} = p_u \cdot q_i^T$
- Syntax highlighting cho code blocks
- Tables, tabs, admonitions
- Task lists

✅ **SEO & Performance**
- Sitemap.xml tự động
- Fast page loads
- Mobile-first design
- Offline search

## 📄 Nội dung chính

### Chương I: Giới thiệu
- Giới thiệu tổng quan về project
- Lý do lựa chọn đề tài
- Phạm vi và đối tượng

### Chương II: Mục tiêu
- Mục tiêu tổng quát
- Mục tiêu cụ thể (5 lĩnh vực)

### Chương III: ML Overview
- **Bài toán ML**: Collaborative Filtering (Rating Prediction)
- **Dữ liệu**: The Movies Dataset (Kaggle)
  - 9,000+ phim
  - 600+ users
  - 100,000+ ratings
- **Mô hình**: SVD (Surprise)
  - RMSE < 1.0
  - 4-fold cross-validation
- **Quy trình huấn luyện**: 7 bước chi tiết

### Chương IV: Triển khai
- **Quy trình training**: Celery tasks, pipelines
- **Deployment**: Model storage, API integration
- **Môi trường**:
  - Django 4.0.7
  - PostgreSQL 13
  - Redis + Celery
  - Docker Compose
  - Gunicorn
- **Monitoring**:
  - RMSE/MAE metrics
  - Celery task tracking
  - Health checks
  - Logging strategy

### Chương V: Kết luận
- ✅ Kết quả đạt được (11 items)
- ❌ Hạn chế (8 items)
- 🚀 Hướng phát triển:
  - Ngắn hạn (1-3 tháng)
  - Trung hạn (3-6 tháng)
  - Dài hạn (6-12 tháng)
  - Quantified goals

## 🛠️ Stack công nghệ

| Công cụ | Phiên bản | Chức năng |
|---------|----------|----------|
| MkDocs | 1.5.3 | Static site generator |
| Material | 9.5.9 | Theme & components |
| Python | 3.8+ | Runtime |
| Markdown | CommonMark | Markup language |

## 📱 Responsive Design

Tài liệu tự động thích ứng với:
- 📱 Mobile (375px+)
- 📱 Tablet (768px+)
- 💻 Desktop (1024px+)
- 🖥️ Large screens (1440px+)

## 🔍 Tìm kiếm

- Full-text search across tất cả pages
- Instant results while typing
- Filter by section
- Offline search support

## 🎨 Customization

Có thể tùy chỉnh:
- Color scheme (primary, accent)
- Language (vi, en, etc.)
- Font families
- Navigation layout
- Custom CSS/JS

Xem `mkdocs.yml` để cấu hình chi tiết

## 📊 File statistics

```
Total Markdown Files: 12
Total Content: ~47KB
Build Time: ~2.5 seconds
Generated Site Size: ~15MB (with assets)
```

## 🔗 Liên kết

- Markdown files: `docs/`
- Configuration: `mkdocs.yml`
- Built site: `site/`
- Dependencies: `requirements.txt`

## ✅ Next steps

1. Chỉnh sửa content trong `docs/` folder
2. `mkdocs serve` để xem thay đổi realtime
3. `mkdocs build` để build production site
4. Deploy `site/` folder lên web server

---

**Ngày tạo:** 28 tháng 12 năm 2025  
**Tác giả:** Bùi Anh Đức, Bùi Tá Đức, Nguyễn Hải Phong  
**Khóa:** IT5414 - VẬN HÀNH HỆ THỐNG HỌC MÁY
