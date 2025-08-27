#!/usr/bin/env python3
"""
Generate high-quality portfolio assets using Adobe Creative Cloud automation
Elevates the portfolio with professional visuals
"""

import os
import json
import subprocess
from pathlib import Path
from datetime import datetime
import win32com.client if os.name == 'nt' else None  # For Windows Adobe automation

class AdobePortfolioAssetGenerator:
    """Generate professional portfolio assets using Adobe Creative Suite"""
    
    def __init__(self):
        self.output_dir = Path("/Users/matthewscott/Projects/OurJourney/adobe_assets")
        self.output_dir.mkdir(exist_ok=True)
        
        # Adobe color palette for consistency
        self.colors = {
            'primary_blue': '#5B5FFF',
            'primary_purple': '#8B5CF6',
            'gradient_start': '#667EEA',
            'gradient_end': '#764BA2',
            'dark_bg': '#1A1A2E',
            'light_bg': '#F7F7FF',
            'accent': '#00D9FF'
        }
        
        # Project details for visuals
        self.projects = {
            'ziggy': {
                'title': 'ZIGGY',
                'subtitle': 'AI Consciousness Research',
                'icon': 'brain',
                'tech': ['Python', 'ML', 'Neural Networks'],
                'visual_theme': 'neural_network'
            },
            'mirador': {
                'title': 'Mirador',
                'subtitle': 'Enterprise AI Orchestration',
                'icon': 'orchestration',
                'tech': ['78 Models', 'Sub-10s Routing'],
                'visual_theme': 'network_hub'
            },
            'security_copilot': {
                'title': 'Security Copilot',
                'subtitle': 'AI Threat Detection',
                'icon': 'shield',
                'tech': ['98% Accuracy', 'Real-time'],
                'visual_theme': 'security_matrix'
            },
            'legalstream': {
                'title': 'LegalStream',
                'subtitle': 'Document Processing AI',
                'icon': 'document',
                'tech': ['OCR', 'NLP', 'Docker'],
                'visual_theme': 'document_flow'
            },
            'chord_generator': {
                'title': 'Chord Generator',
                'subtitle': 'Music AI Technology',
                'icon': 'music',
                'tech': ['Audio Processing', 'Music Theory'],
                'visual_theme': 'sound_waves'
            }
        }
        
    def generate_photoshop_script(self, project_key, project_data):
        """Generate Adobe Photoshop JSX script for project visuals"""
        
        jsx_script = f"""
// Adobe Photoshop Script - Project Visual for {project_data['title']}
// Creates a professional project card with visual elements

// Create new document
var doc = app.documents.add(1920, 1080, 72, "{project_data['title']}_Visual", NewDocumentMode.RGB);

// Set up gradient background
var startColor = new SolidColor();
startColor.rgb.hexValue = '{self.colors['gradient_start'].replace('#', '')}';
var endColor = new SolidColor();
endColor.rgb.hexValue = '{self.colors['gradient_end'].replace('#', '')}';

// Create gradient layer
var gradientLayer = doc.artLayers.add();
gradientLayer.name = "Gradient Background";

// Apply gradient
var gradientFill = new GradientFill();
gradientFill.angle = 135;
gradientFill.type = GradientType.LINEAR;

// Add title text
var titleLayer = doc.artLayers.add();
titleLayer.kind = LayerKind.TEXT;
titleLayer.name = "{project_data['title']} Title";
var textItem = titleLayer.textItem;
textItem.contents = "{project_data['title']}";
textItem.size = 72;
textItem.font = "Inter-Bold";
textItem.position = [100, 200];

// Add subtitle
var subtitleLayer = doc.artLayers.add();
subtitleLayer.kind = LayerKind.TEXT;
subtitleLayer.name = "Subtitle";
var subtitleText = subtitleLayer.textItem;
subtitleText.contents = "{project_data['subtitle']}";
subtitleText.size = 36;
subtitleText.font = "Inter-Regular";
subtitleText.position = [100, 280];

// Visual theme specific elements
{self._get_visual_theme_jsx(project_data['visual_theme'])}

// Add technology badges
var techY = 900;
{self._generate_tech_badges_jsx(project_data['tech'])}

// Save as PNG
var saveOptions = new PNGSaveOptions();
saveOptions.compression = 0;
saveOptions.interlaced = false;

var file = new File("{self.output_dir}/{project_key}_visual.png");
doc.saveAs(file, saveOptions, true, Extension.LOWERCASE);

// Save as PSD for editing
var psdFile = new File("{self.output_dir}/{project_key}_visual.psd");
doc.saveAs(psdFile);

// Close document
doc.close(SaveOptions.DONOTSAVECHANGES);
"""
        
        # Save JSX script
        script_path = self.output_dir / f"{project_key}_photoshop.jsx"
        with open(script_path, 'w') as f:
            f.write(jsx_script)
        
        print(f"✅ Generated Photoshop script: {script_path}")
        return script_path
    
    def _get_visual_theme_jsx(self, theme):
        """Generate theme-specific visual elements"""
        
        themes = {
            'neural_network': """
// Create neural network visualization
var networkLayer = doc.artLayers.add();
networkLayer.name = "Neural Network";

// Draw interconnected nodes
for (var i = 0; i < 8; i++) {
    for (var j = 0; j < 5; j++) {
        var x = 800 + (i * 120);
        var y = 300 + (j * 120);
        
        // Create node
        var node = doc.pathItems.ellipse(y, x, 40, 40);
        node.filled = true;
        node.fillColor = startColor;
        node.stroked = true;
        node.strokeWidth = 2;
    }
}
""",
            'network_hub': """
// Create hub and spoke network visualization
var hubLayer = doc.artLayers.add();
hubLayer.name = "Network Hub";

// Central hub
var centerX = 960;
var centerY = 540;
var hubSize = 100;

// Draw central hub
var hub = doc.pathItems.ellipse(centerY - hubSize/2, centerX - hubSize/2, hubSize, hubSize);

// Draw spokes
for (var angle = 0; angle < 360; angle += 30) {
    var radians = angle * Math.PI / 180;
    var endX = centerX + Math.cos(radians) * 300;
    var endY = centerY + Math.sin(radians) * 300;
    
    // Create line from center to endpoint
    var spoke = doc.pathItems.add();
    spoke.setEntirePath([[centerX, centerY], [endX, endY]]);
    spoke.stroked = true;
    spoke.strokeWidth = 2;
}
""",
            'security_matrix': """
// Create security matrix visualization
var matrixLayer = doc.artLayers.add();
matrixLayer.name = "Security Matrix";

// Create grid of security elements
for (var row = 0; row < 10; row++) {
    for (var col = 0; col < 15; col++) {
        var x = 700 + (col * 50);
        var y = 200 + (row * 50);
        
        // Random binary text
        var binaryLayer = doc.artLayers.add();
        binaryLayer.kind = LayerKind.TEXT;
        var binaryText = binaryLayer.textItem;
        binaryText.contents = Math.random() > 0.5 ? "1" : "0";
        binaryText.size = 20;
        binaryText.position = [x, y];
        binaryText.color = endColor;
    }
}
""",
            'document_flow': """
// Create document flow visualization
var flowLayer = doc.artLayers.add();
flowLayer.name = "Document Flow";

// Create flowing documents
for (var i = 0; i < 5; i++) {
    var docX = 700 + (i * 150);
    var docY = 400 + (Math.sin(i) * 100);
    
    // Document rectangle
    var docRect = doc.pathItems.rectangle(docY, docX, 100, 140);
    docRect.filled = true;
    docRect.fillColor = startColor;
    docRect.opacity = 80 - (i * 10);
}
""",
            'sound_waves': """
// Create sound wave visualization
var waveLayer = doc.artLayers.add();
waveLayer.name = "Sound Waves";

// Draw waveform
var wavePoints = [];
for (var x = 0; x < 50; x++) {
    var xPos = 700 + (x * 20);
    var yPos = 540 + (Math.sin(x * 0.5) * 100);
    wavePoints.push([xPos, yPos]);
}

var wave = doc.pathItems.add();
wave.setEntirePath(wavePoints);
wave.stroked = true;
wave.strokeWidth = 3;
wave.strokeColor = endColor;
"""
        }
        
        return themes.get(theme, "// Default visual theme")
    
    def _generate_tech_badges_jsx(self, tech_stack):
        """Generate JSX for technology badges"""
        jsx = ""
        for i, tech in enumerate(tech_stack):
            jsx += f"""
var techBadge{i} = doc.artLayers.add();
techBadge{i}.kind = LayerKind.TEXT;
var techText{i} = techBadge{i}.textItem;
techText{i}.contents = "{tech}";
techText{i}.size = 18;
techText{i}.position = [{100 + (i * 150)}, techY];
"""
        return jsx
    
    def generate_illustrator_script(self):
        """Generate Adobe Illustrator script for vector graphics"""
        
        ai_script = f"""
// Adobe Illustrator Script - Portfolio Icons and Vectors
// Creates scalable vector graphics for the portfolio

// Create new document
var doc = app.documents.add();
doc.name = "Portfolio_Icons";

// Set up artboards for each project
var artboardRect = doc.artboards[0].artboardRect;
var width = 500;
var height = 500;

// Function to create project icon
function createProjectIcon(name, index, iconType) {{
    // Create new artboard
    var left = index * (width + 50);
    var top = 0;
    var artboard = doc.artboards.add([left, -top, left + width, -(top + height)]);
    artboard.name = name + "_Icon";
    
    // Create icon based on type
    switch(iconType) {{
        case 'brain':
            createBrainIcon(left + width/2, top + height/2);
            break;
        case 'shield':
            createShieldIcon(left + width/2, top + height/2);
            break;
        case 'document':
            createDocumentIcon(left + width/2, top + height/2);
            break;
        case 'music':
            createMusicIcon(left + width/2, top + height/2);
            break;
        case 'orchestration':
            createNetworkIcon(left + width/2, top + height/2);
            break;
    }}
}}

// Brain icon for ZIGGY
function createBrainIcon(x, y) {{
    var brainPath = doc.pathItems.add();
    brainPath.setEntirePath([
        [x-50, y], [x-40, y-30], [x-20, y-40],
        [x, y-45], [x+20, y-40], [x+40, y-30],
        [x+50, y], [x+40, y+30], [x+20, y+40],
        [x, y+45], [x-20, y+40], [x-40, y+30],
        [x-50, y]
    ]);
    
    var color = new RGBColor();
    color.red = 139;
    color.green = 92;
    color.blue = 246;
    brainPath.fillColor = color;
    brainPath.filled = true;
    brainPath.stroked = true;
    brainPath.strokeWidth = 3;
}}

// Shield icon for Security Copilot
function createShieldIcon(x, y) {{
    var shield = doc.pathItems.add();
    shield.setEntirePath([
        [x, y-60], [x+45, y-45], [x+50, y-20],
        [x+50, y+10], [x+40, y+40], [x, y+60],
        [x-40, y+40], [x-50, y+10], [x-50, y-20],
        [x-45, y-45], [x, y-60]
    ]);
    
    var color = new RGBColor();
    color.red = 91;
    color.green = 95;
    color.blue = 255;
    shield.fillColor = color;
    shield.filled = true;
}}

// Generate icons for all projects
{self._generate_all_project_icons()}

// Export as SVG
var exportOptions = new ExportOptionsSVG();
exportOptions.embedRasterImages = true;
exportOptions.cssProperties = SVGCSSPropertyLocation.PRESENTATIONATTRIBUTES;

var svgFile = new File("{self.output_dir}/portfolio_icons.svg");
doc.exportFile(svgFile, ExportType.SVG, exportOptions);

// Export as PNG for web
var pngExportOptions = new ExportOptionsPNG24();
pngExportOptions.antiAliasing = true;
pngExportOptions.transparency = true;
pngExportOptions.artBoardClipping = true;

for (var i = 0; i < doc.artboards.length; i++) {{
    doc.artboards.setActiveArtboardIndex(i);
    var pngFile = new File("{self.output_dir}/" + doc.artboards[i].name + ".png");
    doc.exportFile(pngFile, ExportType.PNG24, pngExportOptions);
}}

// Save AI file
var aiFile = new File("{self.output_dir}/portfolio_icons.ai");
doc.saveAs(aiFile);
"""
        
        # Save Illustrator script
        script_path = self.output_dir / "illustrator_icons.jsx"
        with open(script_path, 'w') as f:
            f.write(ai_script)
        
        print(f"✅ Generated Illustrator script: {script_path}")
        return script_path
    
    def _generate_all_project_icons(self):
        """Generate icon creation calls for all projects"""
        jsx = ""
        for i, (key, data) in enumerate(self.projects.items()):
            jsx += f'createProjectIcon("{data["title"]}", {i}, "{data["icon"]}");\n'
        return jsx
    
    def generate_after_effects_script(self):
        """Generate After Effects script for animated hero section"""
        
        ae_script = f"""
// Adobe After Effects Script - Animated Hero Section
// Creates professional animations for portfolio hero

// Create new composition
var comp = app.project.items.addComp("Portfolio_Hero_Animation", 1920, 1080, 1, 10, 30);

// Create gradient background
var bgLayer = comp.layers.addSolid([0.4, 0.42, 0.98], "Gradient_Background", 1920, 1080, 1, 10);
bgLayer.property("Effects").addProperty("Gradient Ramp");
bgLayer.property("Effects").property("Gradient Ramp").property("Start of Ramp").setValue([0, 0]);
bgLayer.property("Effects").property("Gradient Ramp").property("End of Ramp").setValue([1920, 1080]);

// Create animated constellation sphere
var sphereLayer = comp.layers.addNull();
sphereLayer.name = "Constellation_Sphere";
sphereLayer.threeDLayer = true;

// Add particles for constellation
for (var i = 0; i < 50; i++) {{
    var particle = comp.layers.addSolid([1, 1, 1], "Star_" + i, 10, 10, 1, 10);
    particle.parent = sphereLayer;
    particle.threeDLayer = true;
    
    // Random position on sphere
    var theta = Math.random() * Math.PI * 2;
    var phi = Math.random() * Math.PI;
    var radius = 300;
    
    particle.position.setValue([
        radius * Math.sin(phi) * Math.cos(theta) + 960,
        radius * Math.sin(phi) * Math.sin(theta) + 540,
        radius * Math.cos(phi)
    ]);
    
    // Add glow
    particle.property("Effects").addProperty("Glow");
    particle.property("Effects").property("Glow").property("Glow Intensity").setValue(2);
}}

// Animate sphere rotation
sphereLayer.property("Rotation").setValueAtTime(0, [0, 0, 0]);
sphereLayer.property("Rotation").setValueAtTime(10, [0, 360, 0]);

// Create animated text
var titleText = comp.layers.addText("Matthew Scott");
titleText.property("Source Text").setValue("Matthew Scott");
var textProp = titleText.property("Source Text");
var textDocument = textProp.value;
textDocument.fontSize = 100;
textDocument.fillColor = [0.36, 0.37, 1];
textDocument.font = "Inter";
textProp.setValue(textDocument);

// Animate text entrance
titleText.property("Position").setValueAtTime(0, [960, -100]);
titleText.property("Position").setValueAtTime(1, [960, 300]);
titleText.property("Position").expression = "smooth(0.1, 0.5)";

// Add statistics counters
var stats = [
    {{number: 109, label: "GitHub Contributions", x: 480}},
    {{number: 78, label: "Models Orchestrated", x: 960}},
    {{number: 26, label: "Public Repos", x: 1440}}
];

for (var j = 0; j < stats.length; j++) {{
    var statLayer = comp.layers.addText("0");
    var statProp = statLayer.property("Source Text");
    
    // Animate number counting
    var expression = 'var endNumber = ' + stats[j].number + ';' +
                    'var duration = 2;' +
                    'var t = Math.min(time, duration);' +
                    'Math.floor(linear(t, 0, duration, 0, endNumber));';
    
    statProp.expression = expression;
    statLayer.position.setValue([stats[j].x, 700]);
}}

// Save project
app.project.save(new File("{self.output_dir}/portfolio_animation.aep"));

// Render composition
var renderQueue = app.project.renderQueue;
var render = renderQueue.items.add(comp);
var outputModule = render.outputModule(1);
outputModule.file = new File("{self.output_dir}/hero_animation.mp4");

// Set output settings
outputModule.format = "H.264";
outputModule.outputModule.applyTemplate("High Quality");

// Start render
renderQueue.render();
"""
        
        # Save After Effects script
        script_path = self.output_dir / "after_effects_animation.jsx"
        with open(script_path, 'w') as f:
            f.write(ae_script)
        
        print(f"✅ Generated After Effects script: {script_path}")
        return script_path
    
    def generate_xd_prototype(self):
        """Generate Adobe XD design file structure"""
        
        xd_config = {
            "name": "Matthew_Scott_Portfolio",
            "artboards": [
                {
                    "name": "Desktop_1920",
                    "width": 1920,
                    "height": 1080,
                    "components": ["Header", "Hero", "Projects", "Skills", "Contact", "Footer"]
                },
                {
                    "name": "Mobile_390",
                    "width": 390,
                    "height": 844,
                    "components": ["MobileHeader", "MobileHero", "MobileProjects", "MobileSkills", "MobileContact"]
                },
                {
                    "name": "Tablet_768",
                    "width": 768,
                    "height": 1024,
                    "components": ["TabletHeader", "TabletHero", "TabletProjects", "TabletSkills", "TabletContact"]
                }
            ],
            "colors": self.colors,
            "typography": {
                "heading1": {"font": "Inter", "size": 72, "weight": "Bold"},
                "heading2": {"font": "Inter", "size": 48, "weight": "SemiBold"},
                "heading3": {"font": "Inter", "size": 32, "weight": "Medium"},
                "body": {"font": "Inter", "size": 18, "weight": "Regular"},
                "caption": {"font": "Inter", "size": 14, "weight": "Regular"}
            },
            "components": {
                "ProjectCard": {
                    "width": 400,
                    "height": 500,
                    "borderRadius": 20,
                    "shadow": "0 10px 40px rgba(0,0,0,0.1)",
                    "hover": "transform: translateY(-10px)"
                },
                "Button": {
                    "padding": "16px 32px",
                    "borderRadius": 8,
                    "primary": self.colors['primary_blue'],
                    "secondary": "transparent"
                },
                "SkillBadge": {
                    "padding": "8px 16px",
                    "borderRadius": 20,
                    "background": self.colors['light_bg'],
                    "border": f"1px solid {self.colors['primary_blue']}"
                }
            }
        }
        
        # Save XD configuration
        config_path = self.output_dir / "xd_design_system.json"
        with open(config_path, 'w') as f:
            json.dump(xd_config, f, indent=2)
        
        print(f"✅ Generated XD design system: {config_path}")
        return config_path
    
    def create_execution_script(self):
        """Create a script to execute all Adobe scripts"""
        
        execution_script = f"""#!/usr/bin/env python3
'''
Execute Adobe Creative Cloud scripts to generate portfolio assets
Requires Adobe CC applications installed
'''

import subprocess
import os
from pathlib import Path

def run_photoshop_scripts():
    '''Execute Photoshop scripts'''
    scripts = Path("{self.output_dir}").glob("*_photoshop.jsx")
    for script in scripts:
        print(f"Running Photoshop script: {{script.name}}")
        if os.name == 'nt':  # Windows
            subprocess.run([
                r"C:\\Program Files\\Adobe\\Adobe Photoshop 2024\\Photoshop.exe",
                str(script)
            ])
        else:  # Mac
            subprocess.run([
                "open", "-a", "Adobe Photoshop 2024",
                str(script)
            ])

def run_illustrator_script():
    '''Execute Illustrator script'''
    script = Path("{self.output_dir}/illustrator_icons.jsx")
    if script.exists():
        print(f"Running Illustrator script: {{script.name}}")
        if os.name == 'nt':  # Windows
            subprocess.run([
                r"C:\\Program Files\\Adobe\\Adobe Illustrator 2024\\Support Files\\Contents\\Windows\\Illustrator.exe",
                str(script)
            ])
        else:  # Mac
            subprocess.run([
                "open", "-a", "Adobe Illustrator 2024",
                str(script)
            ])

def run_after_effects_script():
    '''Execute After Effects script'''
    script = Path("{self.output_dir}/after_effects_animation.jsx")
    if script.exists():
        print(f"Running After Effects script: {{script.name}}")
        if os.name == 'nt':  # Windows
            subprocess.run([
                r"C:\\Program Files\\Adobe\\Adobe After Effects 2024\\AfterFX.exe",
                "-r", str(script)
            ])
        else:  # Mac
            subprocess.run([
                "open", "-a", "Adobe After Effects 2024",
                str(script)
            ])

def main():
    print("🎨 Starting Adobe Creative Cloud asset generation...")
    print("-" * 50)
    
    # Run scripts in order
    print("\\n1. Generating Photoshop visuals...")
    run_photoshop_scripts()
    
    print("\\n2. Generating Illustrator icons...")
    run_illustrator_script()
    
    print("\\n3. Generating After Effects animations...")
    run_after_effects_script()
    
    print("\\n" + "=" * 50)
    print("✅ Asset generation complete!")
    print(f"📁 Assets saved to: {self.output_dir}")
    print("\\n📋 Generated assets:")
    print("  • Project visuals (PSD/PNG)")
    print("  • Vector icons (AI/SVG/PNG)")
    print("  • Hero animation (AEP/MP4)")
    print("  • XD design system (JSON)")

if __name__ == "__main__":
    main()
"""
        
        # Save execution script
        script_path = self.output_dir / "execute_adobe_scripts.py"
        with open(script_path, 'w') as f:
            f.write(execution_script)
        
        # Make executable
        os.chmod(script_path, 0o755)
        
        print(f"✅ Generated execution script: {script_path}")
        return script_path
    
    def generate_all_assets(self):
        """Generate all Adobe asset scripts"""
        print("🎨 Adobe Portfolio Asset Generator")
        print("=" * 50)
        
        # Generate Photoshop scripts for each project
        print("\n📸 Generating Photoshop scripts...")
        for key, project in self.projects.items():
            self.generate_photoshop_script(key, project)
        
        # Generate Illustrator script for icons
        print("\n✏️ Generating Illustrator script...")
        self.generate_illustrator_script()
        
        # Generate After Effects script for animations
        print("\n🎬 Generating After Effects script...")
        self.generate_after_effects_script()
        
        # Generate XD design system
        print("\n🎯 Generating XD design system...")
        self.generate_xd_prototype()
        
        # Create execution script
        print("\n⚡ Creating execution script...")
        exec_script = self.create_execution_script()
        
        print("\n" + "=" * 50)
        print("✅ All Adobe scripts generated successfully!")
        print(f"\n📁 Output directory: {self.output_dir}")
        print(f"\n🚀 To generate assets, run:")
        print(f"   python3 {exec_script}")
        print("\n📝 Manual execution:")
        print("   1. Open each JSX script in respective Adobe app")
        print("   2. File → Scripts → Browse...")
        print("   3. Select and run the script")
        
        return self.output_dir

if __name__ == "__main__":
    generator = AdobePortfolioAssetGenerator()
    generator.generate_all_assets()