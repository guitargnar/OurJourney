#!/usr/bin/env python3
"""
Create premium portfolio visuals using Python
Elevates the portfolio with professional graphics
"""

import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance
import numpy as np
from pathlib import Path
import colorsys
import math

class PremiumPortfolioVisuals:
    """Generate high-quality portfolio visuals"""
    
    def __init__(self):
        self.output_dir = Path("/Users/matthewscott/Projects/OurJourney/premium_assets")
        self.output_dir.mkdir(exist_ok=True)
        
        # Premium color palette
        self.colors = {
            'primary_blue': (91, 95, 255),
            'primary_purple': (139, 92, 246),
            'gradient_start': (102, 126, 234),
            'gradient_end': (118, 75, 162),
            'dark': (26, 26, 46),
            'light': (247, 247, 255),
            'accent': (0, 217, 255),
            'success': (16, 185, 129),
            'warning': (245, 158, 11)
        }
        
        self.projects = {
            'ziggy': {
                'title': 'ZIGGY',
                'subtitle': 'AI Consciousness Research',
                'description': 'Metacognitive Evolution Simulator',
                'stats': ['Theory of Mind', 'Neural Modeling', 'Python'],
                'color_scheme': 'purple',
                'icon': 'brain'
            },
            'mirador': {
                'title': 'MIRADOR',
                'subtitle': 'Enterprise AI Orchestration',
                'description': '78 Models, Sub-10s Routing',
                'stats': ['95+ Components', 'Production Scale', 'ROI Tracking'],
                'color_scheme': 'blue',
                'icon': 'network'
            },
            'security': {
                'title': 'SECURITY COPILOT',
                'subtitle': 'AI-Powered Threat Detection',
                'description': '98% Accuracy in Real-Time',
                'stats': ['Phishing Detection', 'API Framework', 'Real-time'],
                'color_scheme': 'green',
                'icon': 'shield'
            },
            'legalstream': {
                'title': 'LEGALSTREAM',
                'subtitle': 'Document Processing Platform',
                'description': 'AI-Powered Legal Analysis',
                'stats': ['OCR Integration', 'Docker', 'Full-Stack'],
                'color_scheme': 'indigo',
                'icon': 'document'
            },
            'chord': {
                'title': 'CHORD GENERATOR',
                'subtitle': 'Music AI Technology',
                'description': 'Interactive Music Theory',
                'stats': ['Audio Processing', 'Music Theory', 'Visualization'],
                'color_scheme': 'purple',
                'icon': 'music'
            }
        }
    
    def create_gradient_background(self, width, height, color_scheme='blue'):
        """Create a premium gradient background"""
        img = Image.new('RGB', (width, height))
        draw = ImageDraw.Draw(img)
        
        # Define gradient colors based on scheme
        schemes = {
            'blue': (self.colors['primary_blue'], self.colors['gradient_end']),
            'purple': (self.colors['primary_purple'], self.colors['gradient_start']),
            'green': ((16, 185, 129), (59, 130, 246)),
            'indigo': ((79, 70, 229), (147, 51, 234))
        }
        
        start_color, end_color = schemes.get(color_scheme, schemes['blue'])
        
        # Create smooth gradient
        for i in range(height):
            ratio = i / height
            r = int(start_color[0] * (1 - ratio) + end_color[0] * ratio)
            g = int(start_color[1] * (1 - ratio) + end_color[1] * ratio)
            b = int(start_color[2] * (1 - ratio) + end_color[2] * ratio)
            draw.rectangle([(0, i), (width, i + 1)], fill=(r, g, b))
        
        # Add noise texture for premium feel
        noise = Image.new('L', (width, height))
        noise_draw = ImageDraw.Draw(noise)
        for _ in range(5000):
            x = np.random.randint(0, width)
            y = np.random.randint(0, height)
            brightness = np.random.randint(200, 255)
            noise_draw.point((x, y), fill=brightness)
        
        noise = noise.filter(ImageFilter.GaussianBlur(radius=1))
        img = Image.blend(img, Image.new('RGB', (width, height), (255, 255, 255)), 0.05)
        
        return img
    
    def draw_neural_network(self, draw, x_start, y_start, width, height, color):
        """Draw a neural network visualization"""
        layers = [4, 6, 6, 3]  # Nodes per layer
        layer_spacing = width // (len(layers) + 1)
        
        nodes = []
        for layer_idx, num_nodes in enumerate(layers):
            layer_nodes = []
            x = x_start + layer_spacing * (layer_idx + 1)
            node_spacing = height // (num_nodes + 1)
            
            for node_idx in range(num_nodes):
                y = y_start + node_spacing * (node_idx + 1)
                layer_nodes.append((x, y))
                
                # Draw node with glow effect
                for radius in range(15, 0, -1):
                    opacity = int(255 * (radius / 15) * 0.3)
                    glow_color = (*color, opacity) if len(color) == 3 else color
                    draw.ellipse(
                        [x - radius, y - radius, x + radius, y + radius],
                        fill=glow_color[:3] if opacity < 255 else glow_color,
                        outline=None
                    )
            
            nodes.append(layer_nodes)
        
        # Draw connections
        for layer_idx in range(len(layers) - 1):
            for node1 in nodes[layer_idx]:
                for node2 in nodes[layer_idx + 1]:
                    # Draw connection with gradient opacity
                    draw.line([node1, node2], fill=(*color, 100), width=1)
    
    def draw_network_hub(self, draw, center_x, center_y, radius, color):
        """Draw a network hub visualization"""
        # Central hub
        draw.ellipse(
            [center_x - 30, center_y - 30, center_x + 30, center_y + 30],
            fill=color, outline='white', width=3
        )
        
        # Orbiting nodes
        num_nodes = 8
        for i in range(num_nodes):
            angle = (2 * math.pi * i) / num_nodes
            x = center_x + radius * math.cos(angle)
            y = center_y + radius * math.sin(angle)
            
            # Node
            draw.ellipse([x - 15, y - 15, x + 15, y + 15], fill=color, outline='white', width=2)
            
            # Connection to hub
            draw.line([(center_x, center_y), (x, y)], fill=(*color, 150), width=2)
            
            # Secondary connections
            next_angle = (2 * math.pi * ((i + 1) % num_nodes)) / num_nodes
            next_x = center_x + radius * math.cos(next_angle)
            next_y = center_y + radius * math.sin(next_angle)
            draw.line([(x, y), (next_x, next_y)], fill=(*color, 100), width=1)
    
    def draw_shield_icon(self, draw, x, y, size, color):
        """Draw a shield security icon"""
        points = [
            (x, y - size),  # Top center
            (x + size * 0.8, y - size * 0.8),  # Top right
            (x + size * 0.9, y - size * 0.3),  # Right upper
            (x + size * 0.9, y + size * 0.3),  # Right lower
            (x, y + size),  # Bottom center
            (x - size * 0.9, y + size * 0.3),  # Left lower
            (x - size * 0.9, y - size * 0.3),  # Left upper
            (x - size * 0.8, y - size * 0.8),  # Top left
        ]
        
        # Shield with gradient effect
        draw.polygon(points, fill=color, outline='white', width=3)
        
        # Check mark inside
        check_points = [
            (x - size * 0.3, y),
            (x - size * 0.1, y + size * 0.3),
            (x + size * 0.4, y - size * 0.3)
        ]
        draw.line(check_points, fill='white', width=4, joint='curve')
    
    def create_project_card(self, project_key, project_data):
        """Create a premium project card visual"""
        width, height = 1200, 675  # 16:9 aspect ratio
        
        # Create base image with gradient
        img = self.create_gradient_background(width, height, project_data['color_scheme'])
        draw = ImageDraw.Draw(img, 'RGBA')
        
        # Add glass morphism effect overlay
        overlay = Image.new('RGBA', (width, height), (255, 255, 255, 0))
        overlay_draw = ImageDraw.Draw(overlay)
        
        # Glass card background
        card_rect = [50, 50, width - 50, height - 50]
        overlay_draw.rounded_rectangle(
            card_rect, radius=30,
            fill=(255, 255, 255, 30),
            outline=(255, 255, 255, 60),
            width=2
        )
        
        # Apply blur for glass effect
        overlay = overlay.filter(ImageFilter.GaussianBlur(radius=2))
        img = Image.alpha_composite(img.convert('RGBA'), overlay)
        draw = ImageDraw.Draw(img)
        
        # Draw visualization based on project type
        if project_data['icon'] == 'brain':
            self.draw_neural_network(draw, 600, 150, 500, 400, self.colors['accent'])
        elif project_data['icon'] == 'network':
            self.draw_network_hub(draw, 850, 350, 150, self.colors['primary_blue'])
        elif project_data['icon'] == 'shield':
            self.draw_shield_icon(draw, 850, 350, 100, self.colors['success'])
        
        # Add text with fallback font
        try:
            title_font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 72)
            subtitle_font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 36)
            desc_font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 24)
        except:
            title_font = ImageFont.load_default()
            subtitle_font = ImageFont.load_default()
            desc_font = ImageFont.load_default()
        
        # Title
        draw.text((100, 100), project_data['title'], fill='white', font=title_font)
        
        # Subtitle
        draw.text((100, 200), project_data['subtitle'], fill=(230, 230, 255), font=subtitle_font)
        
        # Description
        draw.text((100, 260), project_data['description'], fill=(200, 200, 255), font=desc_font)
        
        # Stats badges
        badge_y = height - 150
        for i, stat in enumerate(project_data['stats']):
            badge_x = 100 + (i * 250)
            # Badge background
            draw.rounded_rectangle(
                [badge_x, badge_y, badge_x + 200, badge_y + 40],
                radius=20, fill=(255, 255, 255, 40),
                outline=(255, 255, 255, 80), width=1
            )
            # Badge text
            draw.text((badge_x + 20, badge_y + 10), stat, fill='white', font=desc_font)
        
        # Save the image
        output_path = self.output_dir / f"{project_key}_premium_card.png"
        img.save(output_path, 'PNG', quality=95)
        print(f"✅ Created premium card: {output_path}")
        
        return output_path
    
    def create_hero_avatar(self):
        """Create a professional avatar/logo"""
        size = 500
        img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
        draw = ImageDraw.Draw(img)
        
        # Create gradient circle
        for i in range(size // 2, 0, -1):
            ratio = i / (size // 2)
            r = int(self.colors['primary_blue'][0] * ratio + self.colors['primary_purple'][0] * (1 - ratio))
            g = int(self.colors['primary_blue'][1] * ratio + self.colors['primary_purple'][1] * (1 - ratio))
            b = int(self.colors['primary_blue'][2] * ratio + self.colors['primary_purple'][2] * (1 - ratio))
            
            draw.ellipse(
                [size//2 - i, size//2 - i, size//2 + i, size//2 + i],
                fill=(r, g, b)
            )
        
        # Add initials
        try:
            font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 180)
        except:
            font = ImageFont.load_default()
        
        draw.text((size//2 - 85, size//2 - 90), "MS", fill='white', font=font)
        
        # Add glow effect
        img = img.filter(ImageFilter.GaussianBlur(radius=2))
        
        # Save
        output_path = self.output_dir / "hero_avatar.png"
        img.save(output_path, 'PNG')
        print(f"✅ Created hero avatar: {output_path}")
        
        return output_path
    
    def create_tech_logos(self):
        """Create stylized tech stack logos"""
        techs = {
            'Python': self.colors['primary_blue'],
            'Docker': self.colors['accent'],
            'AWS': self.colors['warning'],
            'React': self.colors['accent'],
            'Node.js': self.colors['success']
        }
        
        for tech, color in techs.items():
            img = Image.new('RGBA', (200, 200), (0, 0, 0, 0))
            draw = ImageDraw.Draw(img)
            
            # Background circle
            draw.ellipse([10, 10, 190, 190], fill=(*color, 30), outline=color, width=3)
            
            # Tech initial
            try:
                font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 72)
            except:
                font = ImageFont.load_default()
            
            draw.text((100 - 20, 100 - 35), tech[0], fill=color, font=font)
            
            # Save
            output_path = self.output_dir / f"tech_{tech.lower()}.png"
            img.save(output_path, 'PNG')
            print(f"✅ Created tech logo: {output_path}")
    
    def generate_all_visuals(self):
        """Generate all premium portfolio visuals"""
        print("\n🎨 Generating Premium Portfolio Visuals")
        print("=" * 50)
        
        # Create project cards
        print("\n📸 Creating project cards...")
        for key, project in self.projects.items():
            self.create_project_card(key, project)
        
        # Create hero avatar
        print("\n👤 Creating hero avatar...")
        self.create_hero_avatar()
        
        # Create tech logos
        print("\n🔧 Creating tech logos...")
        self.create_tech_logos()
        
        print("\n" + "=" * 50)
        print("✅ All premium visuals created!")
        print(f"📁 Output directory: {self.output_dir}")
        
        # Create integration HTML
        self.create_integration_guide()
        
        return self.output_dir
    
    def create_integration_guide(self):
        """Create HTML guide for integrating visuals"""
        html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <title>Premium Portfolio Visuals Integration</title>
    <style>
        body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; 
               padding: 40px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); }}
        .container {{ max-width: 1200px; margin: 0 auto; background: white; 
                     padding: 40px; border-radius: 20px; }}
        h1 {{ color: #5B5FFF; }}
        .visual-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(400px, 1fr)); 
                       gap: 20px; margin: 40px 0; }}
        .visual-card {{ border: 1px solid #e0e0e0; border-radius: 10px; overflow: hidden; }}
        .visual-card img {{ width: 100%; height: auto; display: block; }}
        .visual-card h3 {{ padding: 10px 20px; margin: 0; background: #f5f5f5; }}
        code {{ background: #f5f5f5; padding: 20px; display: block; border-radius: 5px; 
               overflow-x: auto; margin: 10px 0; }}
    </style>
</head>
<body>
    <div class="container">
        <h1>🎨 Premium Portfolio Visuals</h1>
        <p>High-quality visuals generated for your portfolio. Copy the integration code below.</p>
        
        <h2>Project Cards</h2>
        <div class="visual-grid">
"""
        
        # Add project cards
        for key in self.projects.keys():
            img_path = f"premium_assets/{key}_premium_card.png"
            html += f"""
            <div class="visual-card">
                <img src="{img_path}" alt="{self.projects[key]['title']}">
                <h3>{self.projects[key]['title']}</h3>
            </div>
"""
        
        html += """
        </div>
        
        <h2>Integration Code</h2>
        <h3>Update Your HTML</h3>
        <code>
&lt;!-- Replace gradient backgrounds with actual visuals --&gt;
&lt;div class="project-card" style="background-image: url('premium_assets/ziggy_premium_card.png');"&gt;
    &lt;div class="project-overlay"&gt;
        &lt;h3&gt;ZIGGY&lt;/h3&gt;
        &lt;p&gt;AI Consciousness Research&lt;/p&gt;
    &lt;/div&gt;
&lt;/div&gt;
        </code>
        
        <h3>Add Hero Avatar</h3>
        <code>
&lt;!-- Add to hero section --&gt;
&lt;div class="hero-avatar"&gt;
    &lt;img src="premium_assets/hero_avatar.png" alt="Matthew Scott"&gt;
&lt;/div&gt;
        </code>
        
        <h3>CSS Enhancements</h3>
        <code>
/* Glass morphism effect */
.project-card {
    background-size: cover;
    background-position: center;
    position: relative;
    overflow: hidden;
}

.project-overlay {
    background: rgba(255, 255, 255, 0.1);
    backdrop-filter: blur(10px);
    border: 1px solid rgba(255, 255, 255, 0.2);
    padding: 30px;
    height: 100%;
}

/* Premium hover effect */
.project-card:hover {
    transform: translateY(-10px) scale(1.02);
    box-shadow: 0 20px 40px rgba(0, 0, 0, 0.2);
}
        </code>
    </div>
</body>
</html>
"""
        
        # Save integration guide
        guide_path = self.output_dir / "integration_guide.html"
        with open(guide_path, 'w') as f:
            f.write(html)
        
        print(f"\n📖 Integration guide created: {guide_path}")
        print("   Open this file in your browser to see all visuals and integration code")

if __name__ == "__main__":
    generator = PremiumPortfolioVisuals()
    generator.generate_all_visuals()