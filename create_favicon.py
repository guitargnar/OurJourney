#!/usr/bin/env python3
"""Create simple favicon without font issues"""

from PIL import Image, ImageDraw

def create_favicon():
    """Create a simple gradient favicon with MS initials"""
    size = 32
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Draw gradient background
    draw.rounded_rectangle([0, 0, size, size], 
                          radius=size//4, 
                          fill=(37, 99, 235, 255))  # Primary blue
    
    # Draw simple MS using lines
    # M
    draw.line([(8, 22), (8, 10)], fill=(255, 255, 255), width=2)
    draw.line([(8, 10), (12, 16)], fill=(255, 255, 255), width=2)
    draw.line([(12, 16), (16, 10)], fill=(255, 255, 255), width=2)
    draw.line([(16, 10), (16, 22)], fill=(255, 255, 255), width=2)
    
    # S
    draw.arc([(18, 10), (24, 16)], 90, 270, fill=(255, 255, 255), width=2)
    draw.arc([(18, 16), (24, 22)], -90, 90, fill=(255, 255, 255), width=2)
    
    # Save
    img.save('/Users/matthewscott/Projects/portfolio-website/assets/favicon.ico')
    img.save('/Users/matthewscott/Projects/portfolio-website/assets/favicon.png')
    print("✅ Created favicon.ico and favicon.png")

if __name__ == "__main__":
    create_favicon()