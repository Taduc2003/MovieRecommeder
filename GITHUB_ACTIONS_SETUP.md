# 🔄 GitHub Actions for MkDocs - Setup Guide

## 📦 Cài đặt workflows

Tôi đã tạo **2 GitHub Actions workflows** cho MkDocs:

### 1️⃣ **deploy.yml** - Tự động deploy

**Chức năng:** Build & deploy MkDocs lên GitHub Pages tự động

**Trigger khi:**
- ✅ Push lên `main` hoặc `master` branch
- ✅ Có changes trong `docs/mkdocs_project/`
- ✅ Manual trigger (Actions tab → Run workflow)

**Quy trình:**
```
1. Checkout code
2. Setup Python 3.11
3. Install mkdocs + material
4. Build site (mkdocs build)
5. Upload artifacts
6. Deploy to GitHub Pages
```

**URL sau deploy:** `https://YOUR_USERNAME.github.io/MovieRecommender/`

---

### 2️⃣ **test-build.yml** - Test build on PR

**Chức năng:** Test xem build có lỗi trước khi merge PR

**Trigger khi:**
- ✅ Push lên PR vào `main`/`master`
- ✅ Có changes trong `docs/mkdocs_project/`
- ✅ Manual trigger

**Quy trình:**
```
1. Checkout code
2. Setup Python
3. Install dependencies
4. Build in strict mode (--strict)
5. Check if build succeeded
6. Comment on PR với result
```

---

## 🚀 Cách setup

### Bước 1: Push repository lên GitHub

```bash
git init
git add .
git commit -m "Initial commit with MkDocs and GitHub Actions"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/MovieRecommender.git
git push -u origin main
```

### Bước 2: Enable GitHub Pages

1. Vào **Settings** → **Pages**
2. **Source:** Chọn **GitHub Actions**
3. Click **Save**

![GitHub Pages Settings](https://i.imgur.com/placeholder.png)

### Bước 3: Check Workflows

1. Vào tab **Actions**
2. Xem **"Deploy MkDocs to GitHub Pages"** workflow
3. Nếu thấy 🟢 **Success** → deploy xong!

---

## 📊 Workflow Status

Theo dõi deployment:

**Actions tab → All workflows:**
- ✅ **Green checkmark** = Deploy successful
- 🟡 **Yellow/spinning** = In progress
- ❌ **Red X** = Failed

Click vào run để xem logs chi tiết.

---

## 🔄 Quy trình làm việc

```
┌─────────────────────┐
│  Edit Markdown      │
│  in docs/           │
└──────────┬──────────┘
           │
           ↓ git push
┌─────────────────────┐
│  GitHub Actions     │
│  trigger            │
└──────────┬──────────┘
           │
           ↓ Test build
┌─────────────────────┐
│  PR: test-build.yml │
│  ✅ If success      │
│  ❌ If fail         │
└──────────┬──────────┘
           │
           ↓ Merge to main
┌─────────────────────┐
│  deploy.yml trigger │
│  Build & deploy     │
└──────────┬──────────┘
           │
           ↓ 🌐 Live
┌─────────────────────┐
│  GitHub Pages       │
│  https://user...    │
└─────────────────────┘
```

---

## 📝 Cách thay đổi

### Cập nhật MkDocs theme/settings

1. Edit `docs/mkdocs_project/mkdocs.yml`
2. Push lên GitHub
3. Workflow tự động trigger → Deploy

### Thêm tài liệu mới

1. Tạo file `docs/mkdocs_project/docs/new-page.md`
2. Update `mkdocs.yml` nav section
3. Push → Automatic deploy

### Sửa code style

1. Edit `docs/mkdocs_project/docs/...`
2. Test local: `mkdocs serve`
3. Push → Auto deploy

---

## 🛠️ Manual Trigger

Muốn deploy mà không cần push?

1. Vào **Actions** tab
2. Chọn **"Deploy MkDocs to GitHub Pages"**
3. Click **"Run workflow"** button
4. Select branch: `main`
5. Click **"Run workflow"**

Workflow sẽ chạy ngay lập tức!

---

## 🔍 Troubleshooting

### ❌ Workflow không chạy

**Kiểm tra:**
1. Branch là `main` hoặc `master`?
2. File path đúng `docs/mkdocs_project/`?
3. `.github/workflows/deploy.yml` có tồn tại?

**Giải pháp:**
```bash
# Kiểm tra file tồn tại
ls -la .github/workflows/
# Output: deploy.yml test-build.yml

# Kiểm tra YAML syntax
python -m yaml .github/workflows/deploy.yml
```

### ❌ Build failed

**Xem logs:**
1. Vào **Actions** tab
2. Click failed run
3. Click **build** job
4. Scroll down để xem error message

**Thường gặp:**
```
ERROR: requirements.txt not found
→ Kiểm tra docs/mkdocs_project/requirements.txt

ERROR: mkdocs: command not found
→ Requirements file không đúng format
```

### ❌ Site không hiện

**Kiểm tra:**
1. **Settings** → **Pages** → Ensure "GitHub Actions" selected
2. Chờ 1-2 phút sau deploy
3. Hard refresh browser: `Ctrl+Shift+R`

---

## 📊 Benefits của GitHub Actions

| Tính năng | Lợi ích |
|-----------|---------|
| **Auto deploy** | Không cần manual build & upload |
| **PR checks** | Test build trước merge |
| **History** | Lưu lại tất cả deployments |
| **Notifications** | Alerts nếu fail |
| **Free** | GitHub Pages free tier |

---

## 💡 Best Practices

### ✅ Do's

```bash
# 1. Test locally before push
cd docs/mkdocs_project
mkdocs build

# 2. Meaningful commit messages
git commit -m "docs: add model architecture diagram"

# 3. Use descriptive PR titles
# Title: "docs: update ML chapter"

# 4. Check Actions status
# After push, go to Actions tab and monitor
```

### ❌ Don'ts

```bash
# ❌ Don't commit to main directly for big changes
# ✅ Use PR instead

# ❌ Don't modify generated site/ folder
# ✅ Only edit source in docs/

# ❌ Don't remove .github/workflows/ folder
# ✅ It's needed for automation
```

---

## 🔗 Useful Commands

```bash
# Test build locally
cd docs/mkdocs_project && mkdocs build

# Test with strict mode (catches warnings)
mkdocs build --strict

# Serve locally
mkdocs serve

# Check GitHub Actions syntax
python -m yaml .github/workflows/deploy.yml

# View git log
git log --oneline -n 10

# Force push (be careful!)
git push --force-with-lease
```

---

## 📍 Site URLs

**Production (GitHub Pages):**
```
https://YOUR_USERNAME.github.io/MovieRecommender/
```

**Local (dev server):**
```
http://127.0.0.1:8000/
```

**PR preview (if configured):**
```
Netlify/Vercel preview URL (optional)
```

---

## ✅ Checklist

- [ ] GitHub repository created
- [ ] `.github/workflows/deploy.yml` in place
- [ ] `.github/workflows/test-build.yml` in place
- [ ] GitHub Pages enabled (Settings → Pages → GitHub Actions)
- [ ] Pushed main branch to remote
- [ ] Actions tab shows successful run
- [ ] Site is live at GitHub Pages URL

---

**🎉 GitHub Actions for automatic MkDocs deployment is ready!**

Next step: Push to GitHub and watch it deploy automatically! 🚀
