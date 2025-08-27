#!/usr/bin/env python3
"""
Verify portfolio deployment status
"""

import subprocess
import time
import sys

def check_site(url):
    """Check site content"""
    cmd = f'curl -s {url} | head -100'
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    return result.stdout

def main():
    print("🔍 Portfolio Deployment Verification")
    print("=" * 50)
    
    checks = [
        ("https://jaspermatters.com", "Primary domain"),
        ("https://ourjourney.netlify.app", "Netlify direct URL"),
    ]
    
    for url, desc in checks:
        print(f"\n📍 Checking {desc}: {url}")
        print("-" * 40)
        
        content = check_site(url)
        
        # Check for portfolio content
        if "Matthew Scott" in content and "AI/ML Engineer" in content:
            print("✅ Portfolio is LIVE!")
            print("   - Found: Matthew Scott - AI/ML Engineer")
            if "ZIGGY" in content:
                print("   - Projects loading correctly")
        elif "OurJourney" in content:
            print("⏳ Still showing OurJourney")
            print("   - Deployment may still be in progress")
        else:
            print("❓ Unknown content")
        
        # Show title
        for line in content.split('\n'):
            if '<title>' in line:
                print(f"   - Title: {line.strip()}")
                break
    
    print("\n" + "=" * 50)
    print("💡 Troubleshooting Tips:")
    print("=" * 50)
    
    print("\nIf still showing OurJourney:")
    print("1. Clear browser cache (Cmd+Shift+R)")
    print("2. Check Netlify dashboard for build status")
    print("3. Try incognito/private browser window")
    print("4. Wait 2-3 more minutes for DNS propagation")
    
    print("\nManual deployment options:")
    print("1. Netlify: netlify deploy --prod --dir=.")
    print("2. Vercel: vercel --prod")
    print("3. Render: Use dashboard.render.com")
    
    print("\n🔄 To force cache clear:")
    print("curl -H 'Cache-Control: no-cache' https://jaspermatters.com")

if __name__ == "__main__":
    main()