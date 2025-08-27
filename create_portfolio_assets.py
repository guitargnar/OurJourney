#!/usr/bin/env python3
"""
Generate professional portfolio assets using Adobe tools and Python
Creates high-quality images for projects, skills, and visual elements
"""

import os
import json
import subprocess
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import numpy as np

class PortfolioAssetGenerator:
    def __init__(self):
        self.portfolio_dir = Path("/Users/matthewscott/Projects/portfolio-website")
        self.assets_dir = self.portfolio_dir / "assets"
        self.assets_dir.mkdir(exist_ok=True)
        
        # Define brand colors matching the portfolio
        self.colors = {
            'primary': '#2563EB',
            'secondary': '#7C3AED',
            'accent': '#10B981',
            'dark': '#0F172A',
            'light': '#F8FAFC',
            'gradient_start': '#667eea',
            'gradient_end': '#764ba2'
        }
        
        # Project data with descriptions
        self.projects = {
            'ziggy': {
                'title': 'ZIGGY',
                'subtitle': 'Metacognitive Evolution Simulator',
                'description': 'AI consciousness research system',
                'tech': ['Python', 'Advanced ML', 'Cognitive Modeling'],
                'color': '#7C3AED'
            },
            'mirador': {
                'title': 'Mirador',
                'subtitle': 'Enterprise AI Agent System',
                'description': '95+ component production system',
                'tech': ['Python', 'AI Agents', 'Business Intelligence'],
                'color': '#2563EB'
            },
            'security_copilot': {
                'title': 'Security Copilot',
                'subtitle': 'AI-Powered Threat Detection',
                'description': 'Production phishing detection system',
                'tech': ['Python', 'Cybersecurity AI', 'Real-time Processing'],
                'color': '#10B981'
            },
            'legalstream': {
                'title': 'LegalStream Platform',
                'subtitle': 'AI Document Processing',
                'description': 'Full-stack legal technology platform',
                'tech': ['Node.js', 'Docker', 'OCR Technology'],
                'color': '#F59E0B'
            },
            'chord_generator': {
                'title': 'Enhanced Chord Generator',
                'subtitle': 'Music AI System',
                'description': 'AI-powered music composition',
                'tech': ['Python', 'Music AI', 'Audio Processing'],
                'color': '#EF4444'
            }
        }
    
    def hex_to_rgb(self, hex_color):
        """Convert hex color to RGB tuple"""
        hex_color = hex_color.lstrip('#')
        return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
    
    def create_gradient_image(self, width, height, color1, color2):
        """Create a gradient image"""
        img = Image.new('RGB', (width, height))
        draw = ImageDraw.Draw(img)
        
        c1 = self.hex_to_rgb(color1)
        c2 = self.hex_to_rgb(color2)
        
        for y in range(height):
            ratio = y / height
            r = int(c1[0] * (1 - ratio) + c2[0] * ratio)
            g = int(c1[1] * (1 - ratio) + c2[1] * ratio)
            b = int(c1[2] * (1 - ratio) + c2[2] * ratio)
            draw.line([(0, y), (width, y)], fill=(r, g, b))
        
        return img
    
    def create_project_card(self, project_key, project_data):
        """Create a professional project card image"""
        width, height = 800, 600
        
        # Create base gradient
        img = self.create_gradient_image(width, height, 
                                        project_data['color'], 
                                        self.colors['dark'])
        
        # Add overlay pattern
        draw = ImageDraw.Draw(img, 'RGBA')
        
        # Add circuit pattern overlay
        for i in range(0, width, 50):
            for j in range(0, height, 50):
                if np.random.random() > 0.7:
                    draw.ellipse([i-2, j-2, i+2, j+2], 
                               fill=(255, 255, 255, 30))
                    if np.random.random() > 0.5 and i < width-50:
                        draw.line([(i, j), (i+50, j)], 
                                fill=(255, 255, 255, 20), width=1)
                    if np.random.random() > 0.5 and j < height-50:
                        draw.line([(i, j), (i, j+50)], 
                                fill=(255, 255, 255, 20), width=1)
        
        # Try to use system font, fallback to default
        try:
            title_font = ImageFont.truetype('/System/Library/Fonts/Helvetica.ttc', 48)
            subtitle_font = ImageFont.truetype('/System/Library/Fonts/Helvetica.ttc', 24)
            desc_font = ImageFont.truetype('/System/Library/Fonts/Helvetica.ttc', 18)
        except:
            title_font = ImageFont.load_default()
            subtitle_font = ImageFont.load_default()
            desc_font = ImageFont.load_default()
        
        # Add text with shadow effect
        shadow_offset = 3
        
        # Title shadow
        draw.text((52, 52), project_data['title'], 
                 font=title_font, fill=(0, 0, 0, 100))
        # Title
        draw.text((50, 50), project_data['title'], 
                 font=title_font, fill=(255, 255, 255, 255))
        
        # Subtitle
        draw.text((50, 120), project_data['subtitle'], 
                 font=subtitle_font, fill=(255, 255, 255, 200))
        
        # Description
        draw.text((50, 170), project_data['description'], 
                 font=desc_font, fill=(255, 255, 255, 180))
        
        # Tech stack badges
        badge_y = height - 100
        badge_x = 50
        for tech in project_data['tech'][:3]:
            # Badge background
            bbox = draw.textbbox((0, 0), tech, font=desc_font)
            width_text = bbox[2] - bbox[0]
            
            draw.rounded_rectangle([badge_x, badge_y, 
                                   badge_x + width_text + 20, badge_y + 30],
                                  radius=15, fill=(255, 255, 255, 40))
            draw.text((badge_x + 10, badge_y + 6), tech, 
                     font=desc_font, fill=(255, 255, 255, 220))
            badge_x += width_text + 40
        
        # Save image
        filename = f"{project_key}_card.png"
        img.save(self.assets_dir / filename, quality=95)
        print(f"✅ Created {filename}")
        
        return filename
    
    def create_hero_background(self):
        """Create an animated-style hero background"""
        width, height = 1920, 1080
        
        # Create base gradient
        img = self.create_gradient_image(width, height,
                                        self.colors['gradient_start'],
                                        self.colors['gradient_end'])
        
        # Add neural network pattern
        draw = ImageDraw.Draw(img, 'RGBA')
        
        # Create nodes
        nodes = []
        for _ in range(30):
            x = np.random.randint(100, width-100)
            y = np.random.randint(100, height-100)
            nodes.append((x, y))
            # Draw node
            draw.ellipse([x-5, y-5, x+5, y+5], 
                        fill=(255, 255, 255, 100))
            draw.ellipse([x-3, y-3, x+3, y+3], 
                        fill=(255, 255, 255, 200))
        
        # Connect some nodes
        for i, node1 in enumerate(nodes):
            for j, node2 in enumerate(nodes[i+1:], i+1):
                dist = np.sqrt((node1[0]-node2[0])**2 + (node1[1]-node2[1])**2)
                if dist < 300:
                    opacity = int(100 * (1 - dist/300))
                    draw.line([node1, node2], 
                            fill=(255, 255, 255, opacity), width=1)
        
        # Apply slight blur for depth
        img = img.filter(ImageFilter.GaussianBlur(radius=1))
        
        # Save
        filename = "hero_background.png"
        img.save(self.assets_dir / filename, quality=95)
        print(f"✅ Created {filename}")
        
        return filename
    
    def create_skill_icons(self):
        """Create professional skill category icons"""
        skills = {
            'ai_ml': {'icon': '🧠', 'color': '#7C3AED'},
            'programming': {'icon': '💻', 'color': '#2563EB'},
            'devops': {'icon': '🚀', 'color': '#10B981'},
            'domains': {'icon': '🎯', 'color': '#F59E0B'}
        }
        
        for skill_key, skill_data in skills.items():
            width, height = 200, 200
            
            # Create circular gradient
            img = Image.new('RGBA', (width, height), (0, 0, 0, 0))
            draw = ImageDraw.Draw(img)
            
            # Draw gradient circle
            color_rgb = self.hex_to_rgb(skill_data['color'])
            for i in range(100, 0, -1):
                opacity = int(255 * (i/100))
                draw.ellipse([100-i, 100-i, 100+i, 100+i],
                           fill=(*color_rgb, opacity))
            
            # Save
            filename = f"skill_{skill_key}.png"
            img.save(self.assets_dir / filename)
            print(f"✅ Created {filename}")
    
    def create_favicon(self):
        """Create a professional favicon"""
        sizes = [16, 32, 64, 128, 256]
        
        for size in sizes:
            img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
            draw = ImageDraw.Draw(img)
            
            # Create gradient background
            color1 = self.hex_to_rgb(self.colors['primary'])
            color2 = self.hex_to_rgb(self.colors['secondary'])
            
            # Draw rounded square with gradient
            draw.rounded_rectangle([0, 0, size, size], 
                                  radius=size//4, 
                                  fill=color1)
            
            # Add "MS" text
            try:
                font_size = size // 3
                font = ImageFont.truetype('/System/Library/Fonts/Helvetica.ttc', font_size)
            except:
                font = ImageFont.load_default()
            
            draw.text((size//4, size//3), "MS", 
                     font=font, fill=(255, 255, 255, 255))
            
            # Save
            filename = f"favicon_{size}x{size}.png"
            img.save(self.assets_dir / filename)
            print(f"✅ Created {filename}")
    
    def generate_all_assets(self):
        """Generate all portfolio assets"""
        print("🎨 Generating Portfolio Assets...")
        print("=" * 50)
        
        # Create project cards
        print("\n📦 Creating Project Cards...")
        for key, data in self.projects.items():
            self.create_project_card(key, data)
        
        # Create hero background
        print("\n🌟 Creating Hero Background...")
        self.create_hero_background()
        
        # Create skill icons
        print("\n🎯 Creating Skill Icons...")
        self.create_skill_icons()
        
        # Create favicons
        print("\n🔰 Creating Favicons...")
        self.create_favicon()
        
        # Create assets manifest
        manifest = {
            'projects': list(self.projects.keys()),
            'assets': os.listdir(self.assets_dir),
            'colors': self.colors,
            'generated': True
        }
        
        with open(self.assets_dir / 'manifest.json', 'w') as f:
            json.dump(manifest, f, indent=2)
        
        print("\n✨ All assets generated successfully!")
        print(f"📁 Assets saved to: {self.assets_dir}")
        
        return True

if __name__ == "__main__":
    generator = PortfolioAssetGenerator()
    generator.generate_all_assets()