# 🚀 Quick Start Guide - MkDocs

## 1️⃣ Cài đặt (1 phút)

```bash
cd docs/mkdocs_project
pip install -r requirements.txt
```

## 2️⃣ Khởi động (10 giây)

```bash
mkdocs serve
```

**Output:**
```
INFO    -  Building documentation...
INFO    -  [10:00:52] Serving on http://127.0.0.1:8000/
```

Truy cập: http://127.0.0.1:8000/ 🌐

## 3️⃣ Chỉnh sửa

Mở bất kỳ file nào trong `docs/` folder:
- `docs/index.md` - Trang chủ
- `docs/chap1-gioi-thieu/index.md` - Chương I
- `docs/chap3-ml-overview/mo-hinh-ml.md` - Mô hình ML
- ...

✨ Server tự động reload khi bạn lưu file!

## 4️⃣ Build

Tạo static website từ source:

```bash
mkdocs build
```

Output: `site/` folder (sẵn sàng deploy)

## 5️⃣ Deploy

### Option A: Local Server
```bash
# Serve static site locally
cd site
python -m http.server 8000
```

### Option B: GitHub Pages
```bash
mkdocs gh-deploy
```

### Option C: Web Hosting
Upload `site/` folder lên web server bất kỳ (Netlify, Vercel, etc.)

---

## 📁 Cấu trúc tệp

```
docs/
├── index.md                          # Trang chủ
├── chap1-gioi-thieu/index.md        # Chương I
├── chap2-muc-tieu/index.md          # Chương II
├── chap3-ml-overview/               # Chương III
│   ├── bai-toan-ml.md
│   ├── du-lieu.md
│   ├── mo-hinh-ml.md
│   └── quy-trinh-huan-luyen.md
├── chap4-deployment/                # Chương IV
│   ├── quy-trinh-training.md
│   ├── deployment.md
│   ├── moi-truong.md
│   └── monitoring.md
└── chap5-conclusion/index.md        # Chương V
```

## 🎯 Các tác vụ phổ biến

### Thêm trang mới

1. Tạo file `docs/new-page.md`
2. Thêm vào `mkdocs.yml`:
```yaml
nav:
  - New Page: new-page.md
```

### Thêm hình ảnh

```markdown
![Alt text](../assets/image.png)
```

### Thêm code block

```markdown
\```python
def hello():
    print("World")
\```
```

### Thêm table

```markdown
| Header 1 | Header 2 |
|----------|----------|
| Cell 1   | Cell 2   |
```

### Thêm math equation

```markdown
Inline: $E = mc^2$

Block:
$$E = mc^2$$
```

---

## ⚙️ Cấu hình (mkdocs.yml)

Các setting chính:

```yaml
site_name: Hybrid Movie Recommendation System
site_language: vi
theme:
  name: material
  palette:
    - scheme: default
      primary: blue
```

Xem [Material Documentation](https://squidfunk.github.io/mkdocs-material/) để tùy chỉnh thêm.

---

## 🆘 Troubleshooting

| Lỗi | Giải pháp |
|-----|----------|
| `Config file 'mkdocs.yml' does not exist` | Chạy lệnh từ `mkdocs_project` folder |
| Port 8000 đang dùng | `mkdocs serve --dev-addr 0.0.0.0:8001` |
| Build fails | `rm -rf site/` rồi `mkdocs build` lại |
| Changes không hiện | Refresh browser hoặc `Ctrl+Shift+R` (hard refresh) |

---

## 📚 Thêm tài liệu

Tất cả file nên:
- Viết bằng **Markdown**
- Có tiêu đề (# Heading)
- Được organize trong folders
- Liệt kê trong `mkdocs.yml` `nav` section

---

## 🔗 Useful Links

- [MkDocs Official](https://www.mkdocs.org/)
- [Material Theme Docs](https://squidfunk.github.io/mkdocs-material/)
- [Markdown Guide](https://www.markdownguide.org/)

---

**Hỗ trợ**: Xem chi tiết trong `mkdocs_project/README.md`
