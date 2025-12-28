# ✨ GitHub Actions Setup - Quick Guide

## 🎯 Tổng quan

Tôi đã tạo **2 GitHub Actions workflows** để:
- ✅ **Tự động deploy** MkDocs lên GitHub Pages
- ✅ **Test build** trước khi merge PR

---

## 📦 2 Workflows

### 1. `deploy.yml` - Production Deploy

```yaml
Trigger: Push to main/master
Action: Build → Test → Deploy to GitHub Pages
Result: Site live at github.io
```

### 2. `test-build.yml` - PR Check

```yaml
Trigger: Pull Request to main/master
Action: Build in strict mode → Comment result on PR
Result: Catch errors before merge
```

---

## 🚀 Setup (5 phút)

### Step 1: Push to GitHub

```bash
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/MovieRecommender.git
git push -u origin main
```

### Step 2: Enable GitHub Pages

1. Repo **Settings** → **Pages**
2. Source: **GitHub Actions**
3. **Save**

### Step 3: Done! ✅

Workflows auto-trigger on push. Check **Actions** tab to monitor.

---

## 🔄 Workflow

```
Edit file → git push → GitHub Actions trigger
              ↓
         Build MkDocs
              ↓
         Test & verify
              ↓
         Deploy to GitHub Pages
              ↓
🌐 Live at: https://username.github.io/MovieRecommender/
```

---

## 📊 What's Created

```
.github/workflows/
├── deploy.yml                    # Main deployment workflow
├── test-build.yml                # PR test workflow
└── DEPLOYMENT_GUIDE.md           # Detailed guide
```

---

## 🎨 How It Works

**On Push to Main:**
1. ✅ Checkout code
2. ✅ Setup Python 3.11
3. ✅ Install mkdocs
4. ✅ Build site
5. ✅ Deploy to GitHub Pages

**On Pull Request:**
1. ✅ Build with strict checks
2. ✅ Report results on PR
3. ✅ Block merge if fails

---

## 🌐 Site URL

```
https://YOUR_USERNAME.github.io/MovieRecommender/
```

Replace `YOUR_USERNAME` with your GitHub username.

---

## 🔍 Monitor Deployment

1. Go to **Actions** tab
2. See workflow status:
   - 🟢 Success
   - 🟡 In progress
   - ❌ Failed

---

## 📝 Next Steps

1. **Push to GitHub:**
   ```bash
   git push origin main
   ```

2. **Watch Actions tab:**
   - See workflow run
   - Wait for 🟢 Success

3. **Visit site:**
   ```
   https://username.github.io/MovieRecommender/
   ```

4. **Future updates:**
   - Edit files in `docs/mkdocs_project/`
   - Push to main
   - Auto-deploy 🚀

---

## 💡 Tips

| Task | Command |
|------|---------|
| **Manual trigger** | Actions tab → Run workflow |
| **View logs** | Click workflow run → View logs |
| **Test locally** | `cd docs/mkdocs_project && mkdocs serve` |
| **Force deploy** | Edit `deploy.yml` and push |

---

## ✅ Checklist

- [ ] Repo on GitHub
- [ ] `.github/workflows/` created with 2 files
- [ ] GitHub Pages enabled
- [ ] Push main branch
- [ ] See 🟢 in Actions tab
- [ ] Site live

---

**🎉 Automatic deployment ready!**

Every push to `main` will auto-deploy your MkDocs site!
