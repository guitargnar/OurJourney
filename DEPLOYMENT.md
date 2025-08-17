# 🚀 OurJourney Deployment Guide

This guide will help you deploy OurJourney to jaspermatters.com so Katie can access it from anywhere!

## Prerequisites
- [ ] Supabase account (free)
- [ ] Render account (free)
- [ ] Netlify account (you have this)
- [ ] GitHub repository (already set up)

## Step 1: Database Setup (Supabase)

1. **Create Supabase Account**
   - Go to https://supabase.com
   - Sign up with your email
   - Create a new project called "ourjourney"

2. **Get Database Connection String**
   - Go to Settings → Database
   - Copy the "Connection string" (URI format)
   - It looks like: `postgresql://postgres:[password]@db.[project].supabase.co:5432/postgres`

3. **Create .env File**
   ```bash
   cp .env.example .env
   ```
   - Edit .env and paste your connection string as DATABASE_URL
   - Set AUTH_PASSWORD to something you and Katie will remember

4. **Run Migration**
   ```bash
   npm run migrate
   ```
   This will copy your existing data to PostgreSQL!

## Step 2: Backend Deployment (Render)

1. **Create Render Account**
   - Go to https://render.com
   - Sign up with GitHub

2. **Deploy Backend**
   - Click "New +" → "Web Service"
   - Connect your GitHub repo
   - Settings:
     - Name: `ourjourney-api`
     - Root Directory: `.` (leave blank)
     - Build Command: `npm install`
     - Start Command: `npm start`
     - Plan: Free

3. **Add Environment Variables**
   In Render dashboard, add:
   - `DATABASE_URL` - Your Supabase connection string
   - `NODE_ENV` - `production`
   - `CORS_ORIGIN` - `https://jaspermatters.com`
   - `AUTH_PASSWORD` - Your shared password

4. **Get Backend URL**
   - After deploy, copy your backend URL
   - It will be: `https://ourjourney-api.onrender.com`

## Step 3: Frontend Deployment (Netlify)

1. **Update Frontend Environment**
   - Go to frontend directory
   - Create `.env.production`:
   ```
   VITE_API_URL=https://ourjourney-api.onrender.com
   ```

2. **Build Frontend**
   ```bash
   cd frontend
   npm run build
   ```

3. **Deploy to Netlify**
   
   **Option A: Via Netlify Dashboard**
   - Log into Netlify
   - Drag the `frontend/dist` folder to Netlify
   - Configure domain as subdomain: `ourjourney.jaspermatters.com`
   
   **Option B: Via Netlify CLI**
   ```bash
   npm install -g netlify-cli
   netlify login
   netlify deploy --dir=frontend/dist --prod
   ```

4. **Configure Domain**
   - In Netlify → Domain Settings
   - Add custom domain: `ourjourney.jaspermatters.com`
   - Or use path: `jaspermatters.com/ourjourney`

5. **Set Environment Variables in Netlify**
   - Go to Site Settings → Environment Variables
   - Add: `VITE_API_URL` = `https://ourjourney-api.onrender.com`

## Step 4: Test Everything

1. **Visit Your Site**
   - Go to https://jaspermatters.com/ourjourney
   - Enter your shared password
   - Test creating an event
   - Check from Katie's phone!

## 🎉 You're Live!

Katie can now:
- Access from her phone at jaspermatters.com/ourjourney
- Add events, ideas, and memories
- See real-time updates
- View custody schedule
- Plan date nights!

## Troubleshooting

### "Cannot connect to database"
- Check DATABASE_URL in Render environment variables
- Make sure Supabase project is active

### "Authentication failed"
- Verify AUTH_PASSWORD is same in backend and what you're entering
- Check CORS_ORIGIN matches your domain

### "Not loading on phone"
- Clear browser cache
- Try incognito/private mode
- Check if backend is running (may take 30s to wake up on free tier)

## Maintenance

### Backup Data
```bash
# Export from PostgreSQL
pg_dump $DATABASE_URL > backup.sql
```

### Update Code
1. Push to GitHub
2. Render auto-deploys backend
3. Rebuild and redeploy frontend to Netlify

## Cost Summary
- **Supabase**: Free (500MB storage)
- **Render**: Free (spins down after 15min inactivity)
- **Netlify**: Free (100GB bandwidth/month)
- **Total**: $0/month! 🎉

## Next Steps
- [ ] Add PWA manifest for mobile app feel
- [ ] Enable offline mode
- [ ] Add photo uploads
- [ ] Set up automated backups

---

**Need help?** The community is here:
- Supabase Discord: https://discord.supabase.com
- Render Community: https://community.render.com
- Netlify Forums: https://answers.netlify.com