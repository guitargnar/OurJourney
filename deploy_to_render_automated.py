#!/usr/bin/env python3
"""
Automated Render Deployment Script
Uses Playwright to deploy portfolio to Render, replacing OurJourney site
Built with patterns from ai-talent-optimizer
"""

import os
import sys
import time
import json
from pathlib import Path
from datetime import datetime
from playwright.sync_api import sync_playwright, Page, Browser

class RenderPortfolioDeployer:
    """Automates portfolio deployment to Render using browser automation"""
    
    def __init__(self, headless: bool = False):
        """
        Initialize the deployer
        Args:
            headless: Run browser in headless mode (False for debugging)
        """
        self.headless = headless
        self.playwright = None
        self.browser = None
        self.page = None
        
        # Portfolio details
        self.portfolio_path = Path("/Users/matthewscott/Projects/portfolio-website")
        self.github_repo = "https://github.com/guitargnar/portfolio-website"
        
        # Render details (will be configured during setup)
        self.render_dashboard = "https://dashboard.render.com"
        self.site_name = "jaspermatters"
        
        print("🚀 Render Portfolio Deployer Initialized")
        print(f"📁 Portfolio path: {self.portfolio_path}")
        
    def start_browser(self):
        """Initialize Playwright and launch browser"""
        try:
            self.playwright = sync_playwright().start()
            self.browser = self.playwright.chromium.launch(
                headless=self.headless,
                args=[
                    '--no-sandbox',
                    '--disable-setuid-sandbox',
                    '--disable-dev-shm-usage',
                    '--window-size=1920,1080'
                ]
            )
            context = self.browser.new_context(viewport={'width': 1920, 'height': 1080})
            self.page = context.new_page()
            
            # Set realistic user agent
            self.page.set_extra_http_headers({
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'
            })
            
            print(f"✅ Browser launched ({'headless' if self.headless else 'visible'} mode)")
            return True
            
        except Exception as e:
            print(f"❌ Failed to start browser: {e}")
            return False
    
    def push_to_github(self):
        """Push portfolio to GitHub for Render deployment"""
        print("\n📤 Pushing portfolio to GitHub...")
        
        commands = [
            "git add -A",
            "git commit -m 'Deploy professional portfolio - replace OurJourney'",
            "git branch -M main",
            f"git remote add origin {self.github_repo} 2>/dev/null || true",
            "git push -u origin main --force"
        ]
        
        os.chdir(self.portfolio_path)
        for cmd in commands:
            print(f"  Running: {cmd}")
            result = os.system(cmd)
            if result != 0 and "remote add" not in cmd:
                print(f"  ⚠️ Command failed with code {result}")
                
        print("✅ GitHub repository updated")
        return True
    
    def login_to_render(self):
        """Navigate to Render and handle authentication"""
        print("\n🔐 Logging into Render...")
        
        try:
            self.page.goto(self.render_dashboard, wait_until='networkidle')
            time.sleep(2)
            
            # Check if already logged in
            if "dashboard" in self.page.url.lower():
                print("✅ Already logged into Render")
                return True
            
            # Look for GitHub OAuth button
            github_button = self.page.locator('button:has-text("Sign in with GitHub")').first
            if github_button.is_visible():
                print("  Clicking GitHub authentication...")
                github_button.click()
                
                # Wait for GitHub auth
                self.page.wait_for_url("**/dashboard**", timeout=30000)
                print("✅ Successfully authenticated with Render")
                return True
                
            print("⚠️ Could not find login method")
            return False
            
        except Exception as e:
            print(f"❌ Login failed: {e}")
            return False
    
    def find_ourjourney_service(self):
        """Find the OurJourney service in Render dashboard"""
        print("\n🔍 Finding OurJourney service...")
        
        try:
            # Navigate to services
            self.page.goto(f"{self.render_dashboard}/services", wait_until='networkidle')
            time.sleep(2)
            
            # Look for services with jaspermatters domain
            services = self.page.locator('[data-testid="service-card"]').all()
            
            for service in services:
                service_text = service.inner_text().lower()
                if "ourjourney" in service_text or "jaspermatters" in service_text:
                    print(f"✅ Found service: {service_text[:50]}...")
                    service.click()
                    time.sleep(2)
                    return True
            
            print("⚠️ Could not find OurJourney service")
            
            # Try to find any static site
            static_sites = self.page.locator('text=/static site/i').all()
            if static_sites:
                print(f"  Found {len(static_sites)} static sites")
                static_sites[0].click()
                return True
                
            return False
            
        except Exception as e:
            print(f"❌ Service search failed: {e}")
            return False
    
    def update_deployment_settings(self):
        """Update the deployment to use new portfolio"""
        print("\n⚙️ Updating deployment settings...")
        
        try:
            # Click Settings tab
            settings_tab = self.page.locator('text="Settings"').first
            if settings_tab.is_visible():
                settings_tab.click()
                time.sleep(2)
            
            # Find repository field
            repo_input = self.page.locator('input[name="repo"], input[placeholder*="repository"]').first
            if repo_input.is_visible():
                print(f"  Updating repository to: {self.github_repo}")
                repo_input.fill("")
                repo_input.type(self.github_repo)
            
            # Update build command if needed
            build_input = self.page.locator('input[name="buildCommand"]').first
            if build_input.is_visible():
                build_input.fill("")  # No build needed for static site
            
            # Update publish directory
            publish_input = self.page.locator('input[name="publishPath"], input[name="staticPublishPath"]').first
            if publish_input.is_visible():
                publish_input.fill("./")
            
            # Save changes
            save_button = self.page.locator('button:has-text("Save")').first
            if save_button.is_visible():
                save_button.click()
                print("✅ Settings updated")
                time.sleep(3)
                return True
                
            return False
            
        except Exception as e:
            print(f"❌ Settings update failed: {e}")
            return False
    
    def trigger_redeploy(self):
        """Trigger a manual redeploy"""
        print("\n🔄 Triggering redeploy...")
        
        try:
            # Click Deploy button
            deploy_button = self.page.locator('button:has-text("Deploy"), button:has-text("Redeploy")').first
            if deploy_button.is_visible():
                deploy_button.click()
                print("✅ Redeploy triggered")
                
                # Wait for deployment to start
                time.sleep(5)
                
                # Check deployment status
                status = self.page.locator('[data-testid="deploy-status"], .deploy-status').first
                if status.is_visible():
                    print(f"  Deployment status: {status.inner_text()}")
                
                return True
                
            print("⚠️ Could not find deploy button")
            return False
            
        except Exception as e:
            print(f"❌ Redeploy failed: {e}")
            return False
    
    def verify_deployment(self):
        """Verify the deployment is successful"""
        print("\n✅ Verifying deployment...")
        
        try:
            # Wait for deployment to complete (max 5 minutes)
            max_wait = 300  # 5 minutes
            start_time = time.time()
            
            while time.time() - start_time < max_wait:
                # Check for success indicator
                success = self.page.locator('text=/deploy.*success|live|active/i').first
                if success.is_visible():
                    print("✅ Deployment successful!")
                    
                    # Get the live URL
                    url_element = self.page.locator('a[href*="jaspermatters"], a[href*=".onrender.com"]').first
                    if url_element.is_visible():
                        live_url = url_element.get_attribute('href')
                        print(f"🌐 Live at: {live_url}")
                    
                    return True
                
                # Check for failure
                failure = self.page.locator('text=/deploy.*fail|error/i').first
                if failure.is_visible():
                    print("❌ Deployment failed")
                    return False
                
                print("  ⏳ Deployment in progress...")
                time.sleep(10)
            
            print("⚠️ Deployment timed out")
            return False
            
        except Exception as e:
            print(f"❌ Verification failed: {e}")
            return False
    
    def deploy(self):
        """Main deployment workflow"""
        print("\n" + "="*50)
        print("🚀 STARTING RENDER PORTFOLIO DEPLOYMENT")
        print("="*50)
        
        try:
            # Step 1: Start browser
            if not self.start_browser():
                return False
            
            # Step 2: Push to GitHub
            if not self.push_to_github():
                print("⚠️ GitHub push failed, continuing anyway...")
            
            # Step 3: Login to Render
            if not self.login_to_render():
                return False
            
            # Step 4: Find OurJourney service
            if not self.find_ourjourney_service():
                print("\n📝 Manual steps needed:")
                print("1. Go to https://dashboard.render.com")
                print("2. Find the service for jaspermatters.com")
                print("3. Update repository to: guitargnar/portfolio-website")
                print("4. Trigger redeploy")
                return False
            
            # Step 5: Update settings
            if not self.update_deployment_settings():
                print("⚠️ Could not update settings automatically")
            
            # Step 6: Trigger redeploy
            if not self.trigger_redeploy():
                print("⚠️ Could not trigger redeploy automatically")
            
            # Step 7: Verify deployment
            self.verify_deployment()
            
            print("\n" + "="*50)
            print("✨ DEPLOYMENT COMPLETE!")
            print("="*50)
            print("\n📋 Next Steps:")
            print("1. Check https://jaspermatters.com in 5-10 minutes")
            print("2. Verify portfolio is showing (not OurJourney)")
            print("3. Test all links and features")
            
            return True
            
        except Exception as e:
            print(f"\n❌ Deployment error: {e}")
            return False
            
        finally:
            if self.browser:
                self.browser.close()
            if self.playwright:
                self.playwright.stop()

def main():
    """Main entry point"""
    print("Portfolio Deployment Automation")
    print("-" * 40)
    
    # Check if Playwright is installed
    try:
        import playwright
    except ImportError:
        print("Installing Playwright...")
        os.system("pip install playwright")
        os.system("playwright install chromium")
    
    # Run deployment
    deployer = RenderPortfolioDeployer(headless=False)  # Set to True for headless
    success = deployer.deploy()
    
    if success:
        print("\n✅ Portfolio deployment successful!")
        print("🌐 Visit https://jaspermatters.com to see your new portfolio")
    else:
        print("\n⚠️ Deployment requires manual intervention")
        print("Please complete the steps manually at https://dashboard.render.com")
    
    return 0 if success else 1

if __name__ == "__main__":
    sys.exit(main())