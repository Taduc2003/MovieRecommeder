# GitHub Actions - MkDocs Deployment Guide

## 🚀 Tự động deploy MkDocs lên GitHub Pages

Workflow này sẽ **tự động build và deploy** tài liệu MkDocs mỗi khi bạn push code lên GitHub.

## 📋 Cài đặt

### Bước 1: Đẩy code lên GitHub

```bash
git init
git add .
git commit -m "Initial commit with MkDocs"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/MovieRecommender.git
git push -u origin main
```

### Bước 2: Cấu hình GitHub Pages

1. Vào **Settings** → **Pages**
2. Source: **GitHub Actions**
3. Deploy branch: **Automatic**

![GitHub Pages Settings](https://docs.github.com/assets/cb-27457/images/help/pages/select-github-actions-as-build-source.png)

### Bước 3: Trigger Deployment

Workflow tự động chạy khi:
- ✅ Push lên `main` hoặc `master` branch
- ✅ Có thay đổi trong `docs/mkdocs_project/**`
- ✅ Push file `.github/workflows/deploy.yml`
- ✅ Click **Run workflow** trong tab Actions (manual trigger)

## 📊 Workflow Details

### File: `.github/workflows/deploy.yml`

```yaml
on:
  push:
    branches: [main, master]
    paths: ['docs/mkdocs_project/**']
  workflow_dispatch:  # Manual trigger

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      1. Checkout code
      2. Setup Python 3.11
      3. Install mkdocs + material theme
      4. Build static site
      5. Upload to GitHub Pages
      6. Deploy to live website
```

## 🔄 Quy trình

```
Bạn edit file Markdown
        ↓
Push lên GitHub
        ↓
GitHub Actions trigger
        ↓
Build MkDocs (mkdocs build)
        ↓
Generate static site
        ↓
Upload artifacts
        ↓
Deploy to GitHub Pages
        ↓
🌐 Site live at: https://username.github.io/MovieRecommender/
```

## 📍 Deploy URL

Sau khi deploy, truy cập:

```
https://YOUR_USERNAME.github.io/MovieRecommender/
```

Hoặc custom domain nếu bạn cấu hình.

## 🛠️ Manual Trigger

Không muốn chờ push? Trigger thủ công:

1. Vào tab **Actions**
2. Chọn workflow **"Deploy MkDocs to GitHub Pages"**
3. Click **"Run workflow"**
4. Chọn branch (main)
5. Click **"Run workflow"**

## 📝 Monitering Deployment

1. Vào **Actions** tab trên GitHub
2. Xem status của workflow:
   - 🟢 **Success** - Deploy xong
   - 🟡 **In Progress** - Đang deploy
   - 🔴 **Failed** - Có lỗi

Click vào run để xem chi tiết logs.

## ⚙️ Advanced Configuration

### Thay đổi Python version

```yaml
- uses: actions/setup-python@v4
  with:
    python-version: '3.12'  # Change here
```

### Thêm extra steps

```yaml
- name: Test build (optional)
  run: |
    cd docs/mkdocs_project
    mkdocs build --strict  # Fail on warnings

- name: Check links (optional)
  run: |
    pip install mkdocs-linkcheck
    # ... linkcheck configuration
```

### Deploy to custom domain

1. Tạo file `docs/CNAME` với content:
```
your-domain.com
```

2. Configure DNS CNAME → `username.github.io`

3. Workflow sẽ tự động deploy với custom domain

## 🔐 Permissions

Workflow cần permissions:
- `contents: read` - Đọc repository
- `pages: write` - Ghi lên GitHub Pages
- `id-token: write` - OIDC token

Tất cả đã được configure trong file.

## 🆘 Troubleshooting

### Workflow không chạy

**Nguyên nhân:** Workflow trigger chưa được set đúng

**Giải pháp:**
1. Kiểm tra file path chính xác trong `on.push.paths`
2. Đảm bảo branch là `main` hoặc `master`
3. Kiểm tra `.github/workflows/deploy.yml` có syntax đúng

### Build failed

**Nguyên nhân:** Thiếu dependencies hoặc syntax error

**Giải pháp:**
1. Xem logs trong Actions tab
2. Kiểm tra `requirements.txt` có đầy đủ
3. Chạy local `mkdocs build` để test

### Site không hiện

**Nguyên nhân:** GitHub Pages chưa được enable

**Giải pháp:**
1. Vào **Settings** → **Pages**
2. Source: **GitHub Actions**
3. Chờ ~1 phút

### Wrong URL

**Nguyên nhân:** Repository name không match với URL

**Nếu URL là:** `https://username.github.io/MovieRecommender/`
**Thì repository phải tên:** `MovieRecommender`

## 📚 Khi nào deploy lại?

Workflow tự động chạy:
- ✅ Khi push lên main/master
- ✅ Khi thay đổi file trong `docs/mkdocs_project/`
- ✅ Khi modify `.github/workflows/deploy.yml`
- ✅ Manual trigger via GitHub Actions UI

## 💡 Best Practices

1. **Test locally first**
   ```bash
   cd docs/mkdocs_project
   mkdocs serve
   ```

2. **Use meaningful commit messages**
   ```bash
   git commit -m "docs: add ML model explanation"
   ```

3. **Check Actions tab**
   - Monitor workflow runs
   - Check for build errors
   - Review deployment status

4. **Keep dependencies updated**
   ```bash
   pip install --upgrade mkdocs mkdocs-material
   pip freeze > requirements.txt
   ```

## 🔗 Useful Links

- [GitHub Actions Docs](https://docs.github.com/en/actions)
- [Deploying to GitHub Pages](https://docs.github.com/en/pages/getting-started-with-github-pages)
- [MkDocs Deployment](https://www.mkdocs.org/user-guide/deploying-your-docs/)

---

## Quick Checklist

- [ ] Repository pushed to GitHub
- [ ] `.github/workflows/deploy.yml` in place
- [ ] GitHub Pages enabled (Settings → Pages → GitHub Actions)
- [ ] Test local build: `mkdocs build`
- [ ] Push changes and watch Actions tab
- [ ] Site live at `https://username.github.io/repo-name/`

✅ **Done! Automatic deployment is ready!**
