# MkDocs Documentation Project

Báo cáo Hệ thống gợi ý phim kết hợp (Hybrid Movie Recommendation System) được triển khai với **MkDocs** + **Material Theme**.

## Cấu trúc dự án

```
mkdocs_project/
├── mkdocs.yml              # Configuration file
├── docs/
│   ├── index.md            # Trang chính
│   ├── chap1-gioi-thieu/
│   │   └── index.md        # Chương I: Giới thiệu
│   ├── chap2-muc-tieu/
│   │   └── index.md        # Chương II: Mục tiêu
│   ├── chap3-ml-overview/
│   │   ├── bai-toan-ml.md
│   │   ├── du-lieu.md
│   │   ├── mo-hinh-ml.md
│   │   └── quy-trinh-huan-luyen.md
│   ├── chap4-deployment/
│   │   ├── quy-trinh-training.md
│   │   ├── deployment.md
│   │   ├── moi-truong.md
│   │   └── monitoring.md
│   └── chap5-conclusion/
│       └── index.md        # Chương V: Kết luận
└── site/                   # Generated static site (build output)
```

## Yêu cầu

- Python 3.8+
- pip

## Cài đặt

```bash
# Cài đặt MkDocs và Material theme
pip install mkdocs mkdocs-material

# Hoặc (nếu chưa cài)
pip install -r requirements.txt
```

## Sử dụng

### 1. Chỉnh sửa tài liệu

Tất cả các file markdown nằm trong thư mục `docs/`. Chỉnh sửa bất kỳ file nào sẽ tự động cập nhật trong server.

### 2. Khởi động development server

```bash
cd mkdocs_project
mkdocs serve
```

Truy cập: http://127.0.0.1:8000/

### 3. Build static site

```bash
mkdocs build
```

Output sẽ được lưu vào thư mục `site/` - có thể deploy lên web server bất kỳ.

### 4. Deploy to GitHub Pages

```bash
mkdocs gh-deploy
```

(Cần cấu hình GitHub repository trước)

## Tính năng

✅ **Material Design Theme**
- Responsive layout
- Dark mode support
- Search functionality
- Navigation tabs

✅ **Markdown Extensions**
- Math equations (KaTeX)
- Code highlighting
- Tables
- Admonitions (notes, warnings)
- Tabs
- Task lists

✅ **Tối ưu hóa**
- Fast build time
- SEO friendly
- Mobile responsive
- Offline search

## Cấu hình MkDocs (mkdocs.yml)

```yaml
site_name: Hybrid Movie Recommendation System
theme:
  name: material
  language: vi
  palette:
    - scheme: default
      primary: blue
    - scheme: slate
      primary: blue

markdown_extensions:
  - pymdownx.arithmatex  # Math support
  - pymdownx.highlight   # Code highlighting
  - tables               # Table support
  - admonition          # Callout boxes
  - ...

plugins:
  - search              # Search functionality
```

## Viết tài liệu

### Heading

```markdown
# H1 Heading
## H2 Heading
### H3 Heading
```

### Bold & Italic

```markdown
**bold** *italic* ***bold italic***
```

### Code

```markdown
`inline code`

\```python
# Code block
def hello():
    print("Hello World")
\```
```

### Tables

```markdown
| Header 1 | Header 2 |
|----------|----------|
| Cell 1   | Cell 2   |
| Cell 3   | Cell 4   |
```

### Math (KaTeX)

```markdown
Inline: $\hat{r}_{ui} = p_u \cdot q_i^T$

Block:
$$\hat{r}_{ui} = p_u \cdot q_i^T$$
```

### Admonitions

```markdown
!!! note
    This is a note

!!! warning
    This is a warning

!!! danger
    This is dangerous
```

### Links

```markdown
[Link text](https://example.com)
[Internal link](../other-page.md)
```

## Mẹo hữu ích

1. **Live reload**: Server tự động reload khi bạn lưu file
2. **Search**: Dùng search box để tìm nhanh nội dung
3. **Mobile preview**: Thử xem trên thiết bị di động để kiểm tra responsive
4. **Copy code**: Người dùng có thể copy code blocks bằng một click

## Troubleshooting

**Lỗi: Config file 'mkdocs.yml' does not exist**
- Đảm bảo chạy lệnh từ trong thư mục `mkdocs_project`

**Server không khởi động**
```bash
# Kiểm tra cổng 8000 có đang sử dụng
mkdocs serve --dev-addr 0.0.0.0:8001
```

**Build fails**
```bash
# Clear cache
rm -rf site/
mkdocs build
```

## Resources

- [MkDocs Documentation](https://www.mkdocs.org/)
- [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)
- [Markdown Guide](https://www.markdownguide.org/)

## Liên hệ

- **Author**: Bùi Anh Đức, Bùi Tá Đức, Nguyễn Hải Phong
- **Course**: VẬN HÀNH HỆ THỐNG HỌC MÁY (IT5414)
- **University**: Đại học Bách Khoa Hà Nội

---

**Generated**: 28 tháng 12 năm 2025
