# GoDaddy DNS Configuration for jaspermatters.com

## Current Status
- **Domain**: jaspermatters.com (registered with GoDaddy)
- **Current Hosting**: Netlify (showing old OurJourney site)
- **Goal**: Point to your portfolio

## Step-by-Step GoDaddy DNS Configuration

### Option 1: Keep Netlify Hosting (Recommended - Already deployed)

1. **Login to GoDaddy**
   - Go to https://www.godaddy.com
   - Click "Sign In" → My Products

2. **Access DNS Settings**
   - Find "jaspermatters.com" in your domains
   - Click "DNS" or "Manage DNS"

3. **Update DNS Records**
   
   **Delete/Update existing A records:**
   - Remove any existing A records pointing elsewhere
   
   **Add Netlify Records:**
   ```
   Type: A
   Name: @
   Value: 75.2.60.5
   TTL: 600
   ```

   **Add CNAME for www:**
   ```
   Type: CNAME
   Name: www
   Value: ourjourney.netlify.app
   TTL: 600
   ```

4. **Save Changes**
   - Click "Save" for all records
   - DNS propagation takes 5-48 hours (usually 1-2 hours)

### Option 2: Switch to Render (Alternative)

1. **First deploy to Render:**
   ```bash
   # From /Users/matthewscott/Projects/OurJourney
   # Go to https://dashboard.render.com
   # Create new Static Site
   # Connect GitHub: guitargnar/OurJourney
   ```

2. **Get Render's DNS values:**
   - In Render dashboard → Settings → Custom Domain
   - Add "jaspermatters.com"
   - Render will provide DNS records

3. **Update GoDaddy DNS:**
   ```
   Type: A
   Name: @
   Value: [Render provides this]
   TTL: 600
   ```

   ```
   Type: CNAME
   Name: www
   Value: [Render provides this]
   TTL: 600
   ```

### Option 3: Use Vercel (Fastest setup)

1. **Deploy to Vercel:**
   ```bash
   cd /Users/matthewscott/Projects/OurJourney
   npx vercel --prod
   ```

2. **Add domain in Vercel:**
   - Go to https://vercel.com/dashboard
   - Select your project → Settings → Domains
   - Add "jaspermatters.com"

3. **Update GoDaddy DNS:**
   ```
   Type: A
   Name: @
   Value: 76.76.21.21
   TTL: 600
   ```

   ```
   Type: CNAME
   Name: www
   Value: cname.vercel-dns.com
   TTL: 600
   ```

## Current DNS Check Commands

```bash
# Check current DNS
nslookup jaspermatters.com
dig jaspermatters.com

# Check what's live
curl -I https://jaspermatters.com

# Force refresh check (bypass cache)
curl -H "Cache-Control: no-cache" https://jaspermatters.com | grep title
```

## Troubleshooting

### If still showing OurJourney after DNS update:

1. **Clear Netlify cache:**
   - Login to Netlify dashboard
   - Find OurJourney site
   - Deploy settings → Clear cache and deploy

2. **Check GoDaddy nameservers:**
   - Should be GoDaddy's default nameservers
   - NOT Netlify's nameservers

3. **Verify records propagated:**
   ```bash
   # Should show new IP
   nslookup jaspermatters.com 8.8.8.8
   ```

## Quick Reference - What You Need

### For Netlify (Current):
- A Record: 75.2.60.5
- CNAME: ourjourney.netlify.app

### For Render:
- Check https://dashboard.render.com after deployment

### For Vercel:
- A Record: 76.76.21.21
- CNAME: cname.vercel-dns.com

## Important Notes

1. **DNS Propagation**: Changes take 1-48 hours
2. **SSL Certificate**: Automatically handled by Netlify/Render/Vercel
3. **Email**: Make sure MX records remain unchanged if you use email

## Your Next Steps

1. Login to GoDaddy now
2. Update DNS records (Option 1 recommended since already on Netlify)
3. Wait 1-2 hours
4. Test with: `curl https://jaspermatters.com | grep "Matthew Scott"`

---

**Support Contacts:**
- GoDaddy Support: 1-480-505-8877
- Netlify Support: https://www.netlify.com/support/
- Domain currently expires: [Check in GoDaddy dashboard]