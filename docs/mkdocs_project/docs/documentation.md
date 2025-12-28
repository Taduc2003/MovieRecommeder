# Tài liệu Dự án

## Tổng quan

Dự án **Movie Recommender System** sử dụng **MkDocs** để tạo tài liệu kỹ thuật hoàn chỉnh, hiện đại và dễ bảo trì.

## Cấu trúc Documentation

### Cây thư mục

```
docs/
├── mkdocs_project/
│   ├── mkdocs.yml                    # Cấu hình chính
│   ├── requirements.txt              # Dependencies
│   ├── README.md                     # Hướng dẫn sử dụng
│   └── docs/
│       ├── index.md                  # Trang chủ
│       ├── documentation.md          # File này
│       ├── chap1-gioi-thieu/
│       │   └── index.md
│       ├── chap2-muc-tieu/
│       │   └── index.md
│       ├── chap3-ml-overview/
│       │   ├── bai-toan-ml.md
│       │   ├── du-lieu.md
│       │   ├── mo-hinh-ml.md
│       │   └── quy-trinh-huan-luyen.md
│       ├── chap4-deployment/
│       │   ├── quy-trinh-training.md
│       │   ├── deployment.md
│       │   ├── moi-truong.md
│       │   └── monitoring.md
│       ├── chap5-conclusion/
│       │   └── index.md
│       ├── assets/
│       │   └── logo.png              # Logo Đại học Bách Khoa
│       └── css/
│           └── custom.css
│
└── Báo cáo đồ án ML OPS.md           # Báo cáo tổng hợp

```

## Công nghệ

| Công cụ | Phiên bản | Tác dụng |
|---------|----------|---------|
| **MkDocs** | 1.5.3 | Static site generator |
| **Material Theme** | 9.5.9 | Modern responsive theme |
| **Python** | 3.8+ | Runtime environment |
| **GitHub Pages** | - | Free static hosting |
| **GitHub Actions** | - | CI/CD automation |

## Cách sử dụng

### 1. Cài đặt

```bash
cd docs/mkdocs_project
pip install -r requirements.txt
```

### 2. Chạy Development Server

```bash
mkdocs serve
```

Truy cập: **http://127.0.0.1:8000/**

Server sẽ tự động reload khi bạn chỉnh sửa file markdown.

### 3. Build Static Site

```bash
mkdocs build
```

Output: `site/` folder chứa HTML, CSS, JS sẵn để deploy.

### 4. Quản lý Nội dung

Tất cả các file markdown nằm trong folder `docs/`. Chỉnh sửa bất kỳ file nào:

- Markdown files tự động parse
- Links tự động chuyển đổi
- Search index tự động update

### 5. Thêm Trang Mới

1. Tạo file `.md` trong thư mục thích hợp
2. Thêm vào `mkdocs.yml` trong section `nav:`

```yaml
nav:
  - Home: index.md
  - My New Page: my-new-page.md  # <- Thêm dòng này
```

3. Restart server hoặc rebuild

## GitHub Actions CI/CD

### Workflow 1: Test Build (test-build.yml)

**Trigger:** Pull Request vào `main` branch

```yaml
on:
  pull_request:
    branches:
      - main
    paths:
      - 'docs/mkdocs_project/**'
```

**Chức năng:**
- ✅ Kiểm tra build (strict mode)
- ✅ Phát hiện lỗi markdown
- ✅ Kiểm tra links hỏng
- ✅ Upload build log
- ✅ Comment kết quả vào PR

**Kết quả:**
- ❌ Build failed → PR blocked
- ✅ Build success → Có thể merge

### Workflow 2: Deploy (deploy.yml)

**Trigger:** Push vào `main` branch

```yaml
on:
  push:
    branches:
      - main
    paths:
      - 'docs/mkdocs_project/**'
```

**Chức năng:**
- ✅ Build MkDocs
- ✅ Upload artifact
- ✅ Deploy lên GitHub Pages
- ✅ Site tự động update

## Quy trình Development

### Workflow Recommended

```
1. Tạo branch mới
   git checkout -b feature/update-docs

2. Chỉnh sửa documentation
   - Edit .md files
   - Test: mkdocs serve

3. Commit & push
   git add docs/mkdocs_project/
   git commit -m "Update: Add new documentation"
   git push origin feature/update-docs

4. Tạo Pull Request
   - GitHub Actions chạy test-build.yml
   - Check results (xanh ✅ = OK)

5. Merge PR
   - Merge vào main
   - GitHub Actions chạy deploy.yml
   - Site tự động update (~2 phút)
```

## Features

### ✅ Material Design Theme

- **Responsive Layout:** Desktop, tablet, mobile
- **Dark Mode:** Automatic detect hoặc manual toggle
- **Full-text Search:** Tìm kiếm nhanh
- **Navigation Tabs:** Easy navigation

### ✅ Markdown Extensions

- **Math Equations:** $E = mc^2$ (KaTeX)
- **Code Highlighting:** Syntax highlighting
- **Tables:** Full markdown table support
- **Admonitions:** Note, warning, danger boxes
- **Tabs:** Tabbed content
- **Task Lists:** Checkboxes

### ✅ Performance

- **Fast Build:** ~2 seconds
- **Offline Search:** Không cần internet
- **SEO Friendly:** Proper meta tags
- **Lightweight:** Minimal JS/CSS

## Customization

### Thay đổi Theme Color

File: `mkdocs.yml`

```yaml
theme:
  palette:
    - scheme: default
      primary: blue        # <- Thay đổi màu primary
      accent: blue         # <- Thay đổi màu accent
```

Màu sẵn có: red, pink, purple, indigo, blue, cyan, teal, green, lime, yellow, amber, orange, deep-orange, brown, grey, blue-grey

### Thêm Logo

Đặt file logo PNG vào `docs/assets/logo.png`:

```yaml
theme:
  logo: assets/logo.png
  favicon: assets/logo.png
```

### Thêm Custom CSS

Tạo file `docs/css/custom.css` và link trong `mkdocs.yml`:

```yaml
extra_css:
  - css/custom.css
```

## Deployment

### GitHub Pages

Site tự động deploy khi push vào `main` branch.

**URL:** https://Taduc2003.github.io/MovieRecommeder/

**Điều kiện:**
- Repository settings → Pages → Source = "GitHub Actions"
- Workflow `deploy.yml` chạy thành công

### Custom Domain

Nếu muốn dùng custom domain:

1. Thêm file `CNAME` trong `docs/mkdocs_project/docs/`
2. Content: `your-domain.com`
3. Cấu hình DNS record trỏ tới GitHub Pages

## Troubleshooting

### Build fails

```bash
# Clear cache
rm -rf site/
# Rebuild
mkdocs build
```

### Custom CSS không load

- Check path: `docs/css/custom.css`
- Ensure `extra_css:` trong mkdocs.yml

### Server port đang dùng

```bash
mkdocs serve --dev-addr 0.0.0.0:8001
```

### Search không hoạt động

Ensure `plugins.search` trong mkdocs.yml

## Resources

- [MkDocs Documentation](https://www.mkdocs.org/)
- [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)
- [Markdown Guide](https://www.markdownguide.org/)
- [GitHub Pages Docs](https://docs.github.com/en/pages)

## Liên hệ

- **Repository:** https://github.com/Taduc2003/MovieRecommeder
- **Course:** IT5414 - VẬN HÀNH HỆ THỐNG HỌC MÁY
- **University:** Đại học Bách Khoa Hà Nội
