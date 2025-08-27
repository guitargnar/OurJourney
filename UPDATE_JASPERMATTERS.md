# 🚨 URGENT: Update jaspermatters.com

## Current Issue
- **jaspermatters.com** is showing the OurJourney password-protected site
- Your professional portfolio needs to replace it immediately

## Quick Manual Deployment (2 minutes)

### Option 1: Netlify Drop (Easiest - No Login Required)
1. Open https://app.netlify.com/drop
2. Drag the entire `/Users/matthewscott/Projects/portfolio-website` folder
3. Wait for upload (30 seconds)
4. Click "Claim this site"
5. Go to Site Settings → Domain Management
6. Add custom domain: jaspermatters.com
7. Done! Site will update in 5-10 minutes

### Option 2: Netlify Dashboard (If you have login)
1. Login to https://app.netlify.com
2. Find the site connected to jaspermatters.com
3. Go to Deploys → Drag and drop your site folder
4. Or use "Deploy settings" → Link to Git repository

### Option 3: Command Line (Now that you're logged in)
```bash
# Link to existing site
npx netlify link

# Choose "Link this directory to an existing project"
# Select the project that has jaspermatters.com

# Then deploy
npx netlify deploy --prod --dir=.
```

## Files Ready for Deployment

All files are in: `/Users/matthewscott/Projects/portfolio-website/`

✅ index.html - Main portfolio page
✅ styles.css - Professional styling  
✅ script.js - Interactive features
✅ assets/ - All images and graphics
✅ netlify.toml - Optimized configuration

## Verify Deployment

After deploying, check:
```bash
# Test if updated
curl https://jaspermatters.com | grep "Matthew Scott"

# Should see your name, not "OurJourney"
```

## Alternative: GitHub Auto-Deploy

1. Push to GitHub:
```bash
git remote add origin https://github.com/guitargnar/portfolio-website.git
git push -u origin main
```

2. In Netlify Dashboard:
   - Site Settings → Build & Deploy
   - Link repository → GitHub
   - Choose guitargnar/portfolio-website
   - Auto-deploys enabled

## 🔥 Why This is Urgent

- Separation agreement deadline: August 30 (3 days)
- Current site shows personal content (OurJourney)
- Professional portfolio needed for job applications
- All Humana references already sanitized

## Support

If you need help:
- Netlify Support: https://answers.netlify.com/
- Deploy manually: https://app.netlify.com/drop
- The portfolio is 100% ready - just needs to be uploaded!