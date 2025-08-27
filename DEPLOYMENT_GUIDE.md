# Deployment Guide - jaspermatters.com

## Current Status
- **Netlify**: Already deployed ✅
- **Render**: Configuration ready
- **GoDaddy**: Domain configuration instructions below

---

## 🚀 Render Deployment

### Step 1: Push to GitHub
```bash
cd /Users/matthewscott/Projects/portfolio-website
git init
git add .
git commit -m "Portfolio with Render configuration"
git branch -M main
git remote add origin https://github.com/guitargnar/portfolio-website.git
git push -u origin main
```

### Step 2: Deploy on Render
1. Go to [https://dashboard.render.com](https://dashboard.render.com)
2. Click "New +" → "Static Site"
3. Connect your GitHub repository
4. Settings:
   - **Name**: matthew-scott-portfolio
   - **Branch**: main
   - **Build Command**: (leave empty)
   - **Publish Directory**: ./
5. Click "Create Static Site"

### Step 3: Add Custom Domain on Render
1. In Render dashboard, go to your site
2. Click "Settings" → "Custom Domains"
3. Add `jaspermatters.com` and `www.jaspermatters.com`
4. Copy the provided DNS records

---

## 🌐 GoDaddy Domain Configuration

### For Netlify (Primary):

1. **Login to GoDaddy**: https://account.godaddy.com
2. Go to **"My Products"** → **"DNS"** for jaspermatters.com
3. **Remove existing records** for @ and www (if any)
4. **Add these records**:

```
Type: A
Name: @
Value: 75.2.60.5
TTL: 600

Type: CNAME
Name: www
Value: [your-site-name].netlify.app
TTL: 600
```

### For Render (Alternative):

If you want to use Render instead:

```
Type: A
Name: @
Value: [Render will provide this]
TTL: 600

Type: A
Name: @
Value: [Render will provide secondary IP]
TTL: 600

Type: CNAME
Name: www
Value: [your-site-name].onrender.com
TTL: 600
```

### For Load Balancing (Both Services):

You can also set up both for redundancy:

```
Type: A
Name: @
Value: 75.2.60.5
TTL: 300

Type: A
Name: @
Value: [Render IP]
TTL: 300

Type: CNAME
Name: www
Value: jaspermatters.com
TTL: 600
```

---

## 📋 DNS Verification

### Check DNS Propagation:
```bash
# Check A records
nslookup jaspermatters.com

# Check CNAME
nslookup www.jaspermatters.com

# Alternative check
dig jaspermatters.com
```

### Online Tools:
- https://www.whatsmydns.net/
- https://dnschecker.org/

---

## ⚙️ SSL Configuration

### Netlify:
1. Go to **Domain Settings** → **HTTPS**
2. Click **"Verify DNS configuration"**
3. Click **"Provision certificate"**
4. Wait 5-10 minutes for Let's Encrypt

### Render:
1. Automatic SSL via Let's Encrypt
2. No configuration needed
3. Activates within minutes of domain verification

---

## 🔧 Troubleshooting

### DNS not propagating?
- Wait 24-48 hours for global propagation
- Clear browser cache
- Try incognito/private browsing
- Flush DNS cache:
  ```bash
  # macOS
  sudo dscacheutil -flushcache
  
  # Windows
  ipconfig /flushdns
  ```

### SSL Certificate Issues?
- Ensure DNS is fully propagated first
- Check HTTPS settings in hosting dashboard
- Force HTTPS redirect in settings

### Site Not Loading?
1. Verify DNS records in GoDaddy
2. Check deployment status in Netlify/Render
3. Ensure no conflicting records
4. Test with: `curl -I https://jaspermatters.com`

---

## 📱 Quick Links

- **Netlify Dashboard**: https://app.netlify.com
- **Render Dashboard**: https://dashboard.render.com
- **GoDaddy DNS**: https://dcc.godaddy.com/domains/
- **GitHub Repo**: https://github.com/guitargnar/portfolio-website

---

## 🎯 Final Checklist

- [ ] Portfolio deployed to Netlify
- [ ] Portfolio deployed to Render
- [ ] GoDaddy DNS configured
- [ ] SSL certificate active
- [ ] www redirect working
- [ ] Mobile responsive test passed
- [ ] All links functional
- [ ] Contact form/links working
- [ ] Resume download working
- [ ] Social links active

---

## 📊 Performance Monitoring

### Uptime Monitoring:
- https://uptimerobot.com (free tier)
- https://www.pingdom.com

### Speed Testing:
- https://pagespeed.web.dev
- https://gtmetrix.com
- https://webpagetest.org

### Expected Scores:
- Performance: 95+
- Accessibility: 100
- Best Practices: 100
- SEO: 100