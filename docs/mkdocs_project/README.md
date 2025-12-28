# Documentation

Báo cáo Hệ thống gợi ý phim kết hợp (Hybrid Movie Recommendation System) được triển khai với **MkDocs** + **Material Theme**.

## Cài đặt

```bash
pip install -r requirements.txt
```

## Khởi động

```bash
mkdocs serve
```

Truy cập: http://127.0.0.1:8000/

## Build

```bash
mkdocs build
```

Output: `site/` folder

## Cấu trúc

- `docs/chap1-gioi-thieu/` - Giới thiệu
- `docs/chap2-muc-tieu/` - Mục tiêu
- `docs/chap3-ml-overview/` - ML Overview
- `docs/chap4-deployment/` - Deployment & Operations  
- `docs/chap5-conclusion/` - Kết luận

## Deploy

GitHub Actions tự động deploy lên GitHub Pages khi push lên `main` branch.

View live at: [https://Taduc2003.github.io/MovieRecommeder/](https://Taduc2003.github.io/MovieRecommeder/)
