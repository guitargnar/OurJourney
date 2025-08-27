# 🚨 URGENT: Deploy Portfolio to Replace OurJourney

## Current Situation
- **jaspermatters.com** = OurJourney password site (NEEDS REPLACING)
- **Your portfolio** = Ready in this folder

## Option 1: Direct to Render (5 minutes)

### Step 1: Create GitHub Repo
1. Go to https://github.com/new
2. Repository name: `portfolio-website`
3. Make it Public
4. Don't initialize with README
5. Click "Create repository"

### Step 2: Push Code
```bash
cd /Users/matthewscott/Projects/portfolio-website
git remote add origin https://github.com/guitargnar/portfolio-website.git
git push -u origin main
```

### Step 3: Connect to Render
1. Login to https://dashboard.render.com
2. Find your jaspermatters.com service (showing OurJourney)
3. Go to Settings
4. Change Repository: `guitargnar/portfolio-website`
5. Branch: `main`
6. Publish Directory: `./`
7. Click "Save Changes"
8. Click "Manual Deploy" → "Deploy"

## Option 2: New Render Service (If can't find OurJourney)

1. https://dashboard.render.com
2. New → Static Site
3. Connect GitHub repository: `guitargnar/portfolio-website`
4. Name: `jaspermatters`
5. Build Command: (leave empty)
6. Publish Directory: `./`
7. Click "Create Static Site"
8. Add custom domain: jaspermatters.com

## Option 3: Use Netlify Instead (Faster)

Since you're already on Netlify CLI:

```bash
# Deploy directly
cd /Users/matthewscott/Projects/portfolio-website
npx netlify deploy --prod --dir=.

# Link to jaspermatters.com in Netlify dashboard
```

## 📁 Your Files Are Ready

Everything is in: `/Users/matthewscott/Projects/portfolio-website/`

- ✅ index.html (portfolio page)
- ✅ styles.css (professional design)
- ✅ script.js (animations)
- ✅ assets/ (all images)
- ✅ All Humana references removed

## 🔍 Verify After Deploy

```bash
# Check if updated (should see "Matthew Scott" not "OurJourney")
curl https://jaspermatters.com | head -50
```

## ⏰ Timeline
- Deploy NOW (August 27)
- Separation agreement: August 30
- Need professional site for job search

## 💡 Quick Fix If Stuck

Just drag the entire folder to:
- https://app.netlify.com/drop
- Or https://surge.sh
- Or https://vercel.com

Then update DNS in GoDaddy to point to new host.