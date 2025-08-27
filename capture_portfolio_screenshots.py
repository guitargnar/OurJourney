#!/usr/bin/env python3
"""
Capture comprehensive screenshots of portfolio using Puppeteer
"""

import asyncio
import os
from datetime import datetime
from pyppeteer import launch

async def capture_portfolio_screenshots():
    """Capture all portfolio sections and elements"""
    
    # Portfolio URL
    url = "https://poetic-halva-844a3a.netlify.app"
    
    # Create screenshots directory
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    screenshot_dir = f"/Users/matthewscott/Projects/OurJourney/portfolio_screenshots_{timestamp}"
    os.makedirs(screenshot_dir, exist_ok=True)
    
    print(f"📸 Starting portfolio screenshot capture")
    print(f"📁 Saving to: {screenshot_dir}")
    print("="*50)
    
    # Launch browser
    browser = await launch({
        'headless': True,
        'args': ['--no-sandbox', '--disable-setuid-sandbox'],
        'defaultViewport': {'width': 1920, 'height': 1080}
    })
    
    page = await browser.newPage()
    
    try:
        # Navigate to portfolio
        print(f"\n🌐 Loading portfolio: {url}")
        await page.goto(url, {'waitUntil': 'networkidle2', 'timeout': 30000})
        await page.waitFor(2000)  # Wait for animations
        
        # 1. Full page screenshot
        print("\n📸 Capturing full page...")
        await page.screenshot({
            'path': f'{screenshot_dir}/01_full_page.png',
            'fullPage': True
        })
        print("   ✅ Full page captured")
        
        # 2. Hero section
        print("\n📸 Capturing hero section...")
        await page.screenshot({
            'path': f'{screenshot_dir}/02_hero_section.png',
            'clip': {'x': 0, 'y': 0, 'width': 1920, 'height': 900}
        })
        
        # 3. Navigation bar
        print("📸 Capturing navigation...")
        nav_element = await page.querySelector('nav')
        if nav_element:
            await nav_element.screenshot({
                'path': f'{screenshot_dir}/03_navigation_bar.png'
            })
            print("   ✅ Navigation captured")
        
        # 4. About section
        print("\n📸 Capturing About section...")
        await page.evaluate('document.getElementById("about").scrollIntoView()')
        await page.waitFor(1000)
        about_element = await page.querySelector('#about')
        if about_element:
            await about_element.screenshot({
                'path': f'{screenshot_dir}/04_about_section.png'
            })
            print("   ✅ About section captured")
        
        # 5. Projects section
        print("\n📸 Capturing Projects section...")
        await page.evaluate('document.getElementById("projects").scrollIntoView()')
        await page.waitFor(1000)
        projects_element = await page.querySelector('#projects')
        if projects_element:
            await projects_element.screenshot({
                'path': f'{screenshot_dir}/05_projects_section.png'
            })
            print("   ✅ Projects section captured")
        
        # 6. Individual project cards
        print("\n📸 Capturing individual project cards...")
        project_cards = await page.querySelectorAll('.project-card')
        for i, card in enumerate(project_cards[:5], 1):
            await card.screenshot({
                'path': f'{screenshot_dir}/06_project_card_{i}.png'
            })
            print(f"   ✅ Project card {i} captured")
        
        # 7. Skills section
        print("\n📸 Capturing Skills section...")
        await page.evaluate('document.getElementById("skills").scrollIntoView()')
        await page.waitFor(1000)
        skills_element = await page.querySelector('#skills')
        if skills_element:
            await skills_element.screenshot({
                'path': f'{screenshot_dir}/07_skills_section.png'
            })
            print("   ✅ Skills section captured")
        
        # 8. Contact section
        print("\n📸 Capturing Contact section...")
        await page.evaluate('document.getElementById("contact").scrollIntoView()')
        await page.waitFor(1000)
        contact_element = await page.querySelector('#contact')
        if contact_element:
            await contact_element.screenshot({
                'path': f'{screenshot_dir}/08_contact_section.png'
            })
            print("   ✅ Contact section captured")
        
        # 9. Clickable elements (buttons)
        print("\n📸 Capturing clickable elements...")
        
        # Get all buttons
        buttons = await page.querySelectorAll('button, a.btn, .btn')
        button_count = len(buttons)
        print(f"   Found {button_count} buttons")
        
        for i, button in enumerate(buttons[:10], 1):  # Capture first 10 buttons
            try:
                await button.screenshot({
                    'path': f'{screenshot_dir}/09_button_{i}.png'
                })
            except:
                pass  # Some buttons might not be visible
        
        # 10. Mobile responsive views
        print("\n📸 Capturing mobile responsive views...")
        
        # iPhone view
        await page.setViewport({'width': 375, 'height': 812})
        await page.waitFor(1000)
        await page.screenshot({
            'path': f'{screenshot_dir}/10_mobile_iphone.png',
            'fullPage': False
        })
        print("   ✅ iPhone view captured")
        
        # iPad view
        await page.setViewport({'width': 768, 'height': 1024})
        await page.waitFor(1000)
        await page.screenshot({
            'path': f'{screenshot_dir}/11_tablet_ipad.png',
            'fullPage': False
        })
        print("   ✅ iPad view captured")
        
        # Desktop view
        await page.setViewport({'width': 1920, 'height': 1080})
        await page.waitFor(1000)
        await page.screenshot({
            'path': f'{screenshot_dir}/12_desktop_view.png',
            'fullPage': False
        })
        print("   ✅ Desktop view captured")
        
        # 11. Hover states (simulate hover on project cards)
        print("\n📸 Capturing hover states...")
        await page.setViewport({'width': 1920, 'height': 1080})
        await page.evaluate('document.getElementById("projects").scrollIntoView()')
        await page.waitFor(1000)
        
        first_card = await page.querySelector('.project-card')
        if first_card:
            await page.hover('.project-card')
            await page.waitFor(500)
            await page.screenshot({
                'path': f'{screenshot_dir}/13_hover_state.png',
                'clip': {'x': 0, 'y': 400, 'width': 1920, 'height': 800}
            })
            print("   ✅ Hover state captured")
        
        # 12. Navigation menu items
        print("\n📸 Capturing navigation menu items...")
        nav_links = await page.querySelectorAll('nav a, nav button')
        print(f"   Found {len(nav_links)} navigation items")
        
        # 13. Footer
        print("\n📸 Capturing footer...")
        footer_element = await page.querySelector('footer')
        if footer_element:
            await footer_element.screenshot({
                'path': f'{screenshot_dir}/14_footer.png'
            })
            print("   ✅ Footer captured")
        
        # Generate summary
        print("\n" + "="*50)
        print("✅ Screenshot capture complete!")
        print(f"📁 Screenshots saved to: {screenshot_dir}")
        print("\n📊 Captured elements:")
        print("   • Full page view")
        print("   • Hero section")
        print("   • Navigation bar")
        print("   • About section")
        print("   • Projects section (with individual cards)")
        print("   • Skills section")
        print("   • Contact section")
        print("   • Clickable buttons")
        print("   • Mobile responsive views (iPhone, iPad)")
        print("   • Hover states")
        print("   • Footer")
        
        # Create index HTML for easy viewing
        html_content = f"""<!DOCTYPE html>
<html>
<head>
    <title>Portfolio Screenshots - {timestamp}</title>
    <style>
        body {{ font-family: Arial, sans-serif; margin: 20px; background: #f5f5f5; }}
        h1 {{ color: #333; }}
        .screenshot {{ margin: 20px 0; border: 1px solid #ddd; background: white; padding: 10px; }}
        img {{ max-width: 100%; height: auto; display: block; }}
        .title {{ font-weight: bold; margin-bottom: 10px; color: #555; }}
    </style>
</head>
<body>
    <h1>Portfolio Screenshots - Matthew Scott</h1>
    <p>Captured: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}</p>
    <p>URL: <a href="{url}">{url}</a></p>
"""
        
        # Add all screenshots
        for filename in sorted(os.listdir(screenshot_dir)):
            if filename.endswith('.png'):
                html_content += f"""
    <div class="screenshot">
        <div class="title">{filename.replace('.png', '').replace('_', ' ').title()}</div>
        <img src="{filename}" alt="{filename}">
    </div>
"""
        
        html_content += """
</body>
</html>"""
        
        with open(f'{screenshot_dir}/index.html', 'w') as f:
            f.write(html_content)
        
        print(f"\n🌐 View all screenshots: {screenshot_dir}/index.html")
        
    except Exception as e:
        print(f"\n❌ Error capturing screenshots: {e}")
    
    finally:
        await browser.close()

# Run the async function
if __name__ == "__main__":
    print("Portfolio Screenshot Capture Tool")
    print("-" * 40)
    asyncio.run(capture_portfolio_screenshots())