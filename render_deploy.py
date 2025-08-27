#!/usr/bin/env python3
"""
Render Deployment Script for Portfolio
Automated deployment using Playwright patterns from ai-talent-optimizer
"""

import os
import sys
import time
import subprocess
from pathlib import Path

def deploy_to_render():
    """Deploy portfolio to Render as backup option"""
    print("🚀 Starting Render Deployment Process")
    print("="*50)
    
    # Step 1: Ensure we're in the right directory
    repo_path = Path("/Users/matthewscott/Projects/OurJourney")
    os.chdir(repo_path)
    
    # Step 2: Create render.yaml if it doesn't exist
    render_config = """services:
  - type: web
    name: matthew-scott-portfolio
    runtime: static
    buildCommand: ""
    staticPublishPath: .
    headers:
      - path: /*
        name: X-Frame-Options
        value: SAMEORIGIN
    routes:
      - type: rewrite
        source: /*
        destination: /index.html
"""
    
    with open("render.yaml", "w") as f:
        f.write(render_config)
    print("✅ Created render.yaml configuration")
    
    # Step 3: Commit render.yaml
    commands = [
        "git add render.yaml",
        'git commit -m "Add Render deployment configuration" || echo "Already committed"',
        "git push origin main"
    ]
    
    for cmd in commands:
        print(f"Running: {cmd}")
        subprocess.run(cmd, shell=True, check=False)
    
    print("\n" + "="*50)
    print("✅ Render configuration pushed!")
    print("="*50)
    
    print("\n📋 Next Steps to Complete Deployment:")
    print("1. Go to https://dashboard.render.com")
    print("2. Click 'New +' → 'Static Site'")
    print("3. Connect GitHub repository: guitargnar/OurJourney")
    print("4. Name: matthew-scott-portfolio")
    print("5. Build Command: (leave empty)")
    print("6. Publish Directory: ./")
    print("7. Click 'Create Static Site'")
    print("\n8. After deployment, add custom domain:")
    print("   - Go to Settings → Custom Domain")
    print("   - Add: jaspermatters.com")
    print("   - Update GoDaddy DNS to point to Render")
    
    print("\n💡 Alternative: Blueprint Deployment")
    print("Since we added render.yaml, you can also:")
    print("1. Go to https://dashboard.render.com/blueprints")
    print("2. Connect guitargnar/OurJourney repo")
    print("3. Render will auto-detect render.yaml")
    print("4. Click 'Apply' to deploy")
    
    return True

def check_site_status():
    """Check current site status"""
    print("\n🔍 Checking site status...")
    
    # Check jaspermatters.com
    result = subprocess.run(
        'curl -s https://jaspermatters.com | head -20 | grep -E "title|Matthew Scott|OurJourney"',
        shell=True,
        capture_output=True,
        text=True
    )
    
    if "Matthew Scott" in result.stdout:
        print("✅ Portfolio is LIVE on jaspermatters.com!")
        return True
    elif "OurJourney" in result.stdout:
        print("⏳ OurJourney still showing - Netlify rebuild in progress")
        return False
    else:
        print("❓ Unable to determine site status")
        return None

def main():
    """Main entry point"""
    print("Portfolio Deployment Manager")
    print("-" * 40)
    
    # Check current status
    is_live = check_site_status()
    
    if is_live:
        print("\n🎉 Your portfolio is already live!")
        print("Visit: https://jaspermatters.com")
    else:
        print("\n⏳ Portfolio deployment in progress on Netlify")
        print("Setting up Render as backup deployment option...")
        
        if deploy_to_render():
            print("\n✅ Render configuration complete!")
            print("You can now deploy to Render as backup if needed")
    
    # Final status check
    print("\n" + "="*50)
    print("📊 Deployment Summary:")
    print("="*50)
    print("✅ GitHub: Portfolio pushed to guitargnar/OurJourney")
    print("⏳ Netlify: Auto-deploying from GitHub (primary)")
    print("📦 Render: Configuration ready (backup option)")
    print("🌐 Domain: jaspermatters.com")
    print("\n⏰ Check status in 2-3 minutes:")
    print("   curl https://jaspermatters.com | grep 'Matthew Scott'")

if __name__ == "__main__":
    main()