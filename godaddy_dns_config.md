# GoDaddy DNS Configuration for jaspermatters.com

## ✅ Current Status
- **Domain**: jaspermatters.com is LIVE on Netlify!
- **Current IPs**: 18.208.88.157, 98.84.224.111 (AWS/Netlify)
- **SSL**: Active (Let's Encrypt via Netlify)

## 🎯 GoDaddy DNS Settings

### Login to GoDaddy:
1. Go to https://account.godaddy.com
2. Click "My Products"
3. Find jaspermatters.com
4. Click "DNS" or "Manage DNS"

### Current DNS Records to Verify/Update:

```
Type    Name    Value                   TTL
----    ----    -----                   ---
A       @       75.2.60.5               600
CNAME   www     [your-site].netlify.app 3600
```

### For Optimal Netlify Setup:

**Delete all existing A, AAAA, and CNAME records for @ and www**

**Then add these:**

```
Type    Name    Value                           TTL
----    ----    -----                           ---
A       @       75.2.60.5                       600
CNAME   www     eloquent-kepler-5d6c9f.netlify.app   3600
```

### Alternative: Using Netlify DNS (Recommended)

1. In Netlify Dashboard:
   - Go to Domains → jaspermatters.com
   - Click "Set up Netlify DNS"
   - Copy the 4 nameservers provided

2. In GoDaddy:
   - Go to DNS Settings
   - Click "Change Nameservers"
   - Select "Enter my own nameservers"
   - Add Netlify's nameservers:
     ```
     dns1.p04.nsone.net
     dns2.p04.nsone.net
     dns3.p04.nsone.net
     dns4.p04.nsone.net
     ```

## 🚀 Render Setup (For Redundancy)

If you want to add Render as a backup:

1. **Deploy to Render**:
   ```bash
   cd /Users/matthewscott/Projects/portfolio-website
   git init
   git add .
   git commit -m "Portfolio with Render config"
   git remote add origin https://github.com/guitargnar/portfolio-website.git
   git push -u origin main
   ```

2. **On Render Dashboard**:
   - New → Static Site
   - Connect GitHub repo
   - Deploy

3. **Add to DNS** (Multi-CDN Setup):
   ```
   Type    Name    Value                   TTL     Priority
   ----    ----    -----                   ---     --------
   A       @       75.2.60.5               300     Primary (Netlify)
   A       @       [Render IP]             300     Secondary
   ```

## 📊 Verify Configuration

### Check DNS Propagation:
```bash
# Check A records
dig jaspermatters.com +short

# Check CNAME
dig www.jaspermatters.com +short

# Check nameservers
dig jaspermatters.com NS +short

# Full DNS report
dig jaspermatters.com ANY
```

### Test Site Access:
```bash
# Test root domain
curl -I https://jaspermatters.com

# Test www subdomain
curl -I https://www.jaspermatters.com

# Test SSL certificate
openssl s_client -connect jaspermatters.com:443 -servername jaspermatters.com < /dev/null
```

## 🔒 Security Headers (Already Configured)

Your netlify.toml includes:
- X-Frame-Options: SAMEORIGIN
- X-Content-Type-Options: nosniff
- X-XSS-Protection: 1; mode=block
- Content-Security-Policy: Configured
- HTTPS redirects: Active

## 📈 Performance Monitoring

### Free Monitoring Services:
1. **UptimeRobot**: https://uptimerobot.com
   - Add monitor for https://jaspermatters.com
   - Set check interval: 5 minutes
   - Alert via email/SMS

2. **Netlify Analytics** (in dashboard):
   - Page views
   - Bandwidth usage
   - Top pages
   - Geographic data

3. **Google Analytics** (optional):
   Add to index.html:
   ```html
   <!-- Google tag (gtag.js) -->
   <script async src="https://www.googletagmanager.com/gtag/js?id=G-XXXXXXXXXX"></script>
   <script>
     window.dataLayer = window.dataLayer || [];
     function gtag(){dataLayer.push(arguments);}
     gtag('js', new Date());
     gtag('config', 'G-XXXXXXXXXX');
   </script>
   ```

## 🎯 Quick Actions

### Update Portfolio Content:
1. Make changes locally
2. Push to GitHub
3. Netlify auto-deploys

### Force Deploy:
```bash
# Netlify CLI
netlify deploy --prod --dir=.

# Or trigger in dashboard
# Deploys → Trigger Deploy
```

### Clear Cache:
```bash
# Clear Netlify cache
netlify deploy --prod --dir=. --skip-cache

# Clear browser cache
# Chrome: Cmd+Shift+R (Mac) / Ctrl+Shift+R (Windows)
```

## ✨ Success Indicators

- [x] jaspermatters.com loads portfolio
- [x] HTTPS/SSL active
- [x] www redirects to root domain
- [x] Mobile responsive
- [x] Fast load time (<2 seconds)
- [x] All assets loading
- [x] Contact links working

## 📞 Support Contacts

- **Netlify Support**: https://www.netlify.com/support/
- **GoDaddy Support**: 1-480-505-8877
- **Render Support**: https://render.com/docs

Your portfolio is LIVE and professional at jaspermatters.com! 🎉