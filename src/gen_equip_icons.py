import os
import sys
import random
import math
from PIL import Image, ImageDraw, ImageOps

# Ensure we can import from src
sys.path.append(os.getcwd())

try:
    from src.equip_cfg import EQUIP_CFG
    from src.const import EquipPart, WeaponType, QualityColor
except ImportError:
    # Fallback if running from inside src
    sys.path.append(os.path.dirname(os.getcwd()))
    from src.equip_cfg import EQUIP_CFG
    from src.const import EquipPart, WeaponType, QualityColor

OUTPUT_DIR = os.path.join("pic", "equipments")
ICON_SIZE = 128

def ensure_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)

def hex_to_rgb(hex_val):
    # If QualityColor returns tuple, use it. 
    # Based on const.py read, it returns tuples like (180, 180, 180)
    return hex_val

def apply_tint(color, factor):
    r, g, b = color
    return (
        max(0, min(255, int(r * factor))),
        max(0, min(255, int(g * factor))),
        max(0, min(255, int(b * factor)))
    )

def get_random_points(center, radius, num_points, irregularity, seed):
    random.seed(seed)
    points = []
    for i in range(num_points):
        angle = (i / num_points) * 2 * math.pi
        r = radius + random.uniform(-irregularity, irregularity)
        x = center[0] + r * math.cos(angle)
        y = center[1] + r * math.sin(angle)
        points.append((x, y))
    return points

class IconGenerator:
    def __init__(self):
        self.canvas_size = ICON_SIZE
        self.center = (ICON_SIZE // 2, ICON_SIZE // 2)
        
    def generate(self, item_data):
        item_id = item_data['id']
        name = item_data['name']
        quality = item_data.get('quality', 0)
        part = item_data['position']
        
        # Determine Background Color
        bg_color = QualityColor.get_color_by_rank(quality)
        
        # Create Image
        img = Image.new('RGB', (self.canvas_size, self.canvas_size), bg_color)
        draw = ImageDraw.Draw(img)
        
        # Seed random for consistency
        random.seed(item_id)
        
        # Determine Main Color (Lighter/Darker version of BG or Metallic)
        main_color = (220, 220, 220) # Default metallic gray
        accent_color = apply_tint(bg_color, 1.5) # Highlight
        
        # Draw Base Shape based on Part
        self.draw_item(draw, part, name, item_id, main_color, accent_color)
        
        # Set Item Effect (ID ...1xx)
        # Check if hundreds digit is 1: (10000100 -> 100 -> 1)
        if (item_id // 100) % 10 == 1:
            self.draw_set_border(draw)
            
        # Save
        filename = f"{item_id}.png"
        img.save(os.path.join(OUTPUT_DIR, filename))
        
    def draw_set_border(self, draw):
        # Green border effect (green + bold)
        green = (0, 255, 0) # Pure Green
        # Draw a thicker border (5px)
        for i in range(5):
            draw.rectangle(
                [i, i, self.canvas_size-1-i, self.canvas_size-1-i], 
                outline=green, 
                width=1
            )
            
    def draw_item(self, draw, part, name, item_id, color, accent):
        # Perturbation for variants
        seed = item_id
        
        if part == EquipPart.WEAPON:
            self.draw_weapon(draw, name, seed, color, accent)
        elif part == EquipPart.HELMET:
            self.draw_helmet(draw, seed, color, accent)
        elif part == EquipPart.ARMOR:
            self.draw_armor(draw, seed, color, accent)
        elif part == EquipPart.RING:
            self.draw_ring(draw, seed, color, accent)
        elif part == EquipPart.NECKLACE or part == EquipPart.AMULET:
            self.draw_necklace(draw, seed, color, accent)
        elif part == EquipPart.BOOTS:
            self.draw_boots(draw, seed, color, accent)
        elif part == EquipPart.GLOVES or part == EquipPart.BRACER:
            self.draw_gloves(draw, seed, color, accent)
        elif part == EquipPart.BELT:
            self.draw_belt(draw, seed, color, accent)
        elif part == EquipPart.SHOULDER:
            self.draw_shoulder(draw, seed, color, accent)
        elif part == EquipPart.ARTIFACT:
            self.draw_artifact(draw, seed, color, accent)
        else:
            # Fallback circle
            draw.ellipse([32, 32, 96, 96], outline=color, width=2)

    def draw_weapon(self, draw, name, seed, color, accent):
        # Detect Weapon Type
        w_type = None
        for wt in WeaponType:
            if WeaponType.get_name(wt) in name:
                w_type = wt
                break
        
        cx, cy = self.center
        
        if w_type == WeaponType.SWORD:
            # Diagonal Sword
            # Blade
            draw.line([(30, 98), (98, 30)], fill=color, width=8)
            # Tip
            draw.polygon([(98, 30), (105, 23), (90, 38)], fill=color)
            # Handle
            draw.line([(25, 103), (40, 88)], fill=accent, width=6)
            # Guard
            draw.line([(35, 93), (50, 78)], fill=accent, width=12)
            
        elif w_type == WeaponType.BLADE: # 刀 (Curved Blade)
            # Curved
            points = []
            for t in range(20, 100, 5):
                x = t
                y = 128 - t - (math.sin(t/30) * 15)
                points.append((x, y))
            draw.line(points, fill=color, width=10)
            # Handle
            draw.line([(20, 108), (35, 93)], fill=accent, width=8)

        elif w_type == WeaponType.BOW:
            # Arc
            bbox = [30, 30, 98, 98]
            draw.arc(bbox, 135, 315, fill=color, width=5)
            # String
            draw.line([(35, 35), (35, 93)], fill=(200, 200, 200), width=1)
            
        elif w_type == WeaponType.SPEAR:
            # Long shaft
            draw.line([(20, 108), (108, 20)], fill=accent, width=4)
            # Head
            draw.polygon([(100, 28), (115, 13), (110, 35)], fill=color)

        elif w_type == WeaponType.STAFF:
            # Stick
            draw.line([(64, 20), (64, 108)], fill=accent, width=6)
            # Orb on top
            draw.ellipse([54, 10, 74, 30], fill=color)

        elif w_type == WeaponType.CROSSBOW:
            # T shape roughly
            draw.line([(44, 64), (84, 64)], fill=color, width=4) # Bow part
            draw.line([(64, 44), (64, 84)], fill=accent, width=4) # Stock
            
        elif w_type == WeaponType.HALBERD: # 戟
            # Like spear but with side blade
            draw.line([(30, 98), (98, 30)], fill=accent, width=5)
            draw.polygon([(90, 38), (105, 23), (110, 35)], fill=color) # Tip
            draw.pieslice([75, 25, 105, 55], 0, 90, fill=color) # Side blade
            
        else:
            # Generic Weapon (Axe-ish)
            draw.line([(30, 98), (98, 30)], fill=accent, width=6)
            draw.rectangle([80, 20, 100, 40], fill=color)

    def draw_helmet(self, draw, seed, color, accent):
        # Dome shape
        bbox = [34, 34, 94, 94]
        draw.pieslice(bbox, 180, 0, fill=color, outline=accent)
        # Visor
        draw.line([(34, 64), (94, 64)], fill=accent, width=2)
        draw.rectangle([54, 64, 74, 84], fill=accent)

    def draw_armor(self, draw, seed, color, accent):
        # Chest plate
        draw.polygon([
            (34, 30), (94, 30), # Shoulders
            (84, 100), (44, 100) # Waist
        ], fill=color, outline=accent)
        # Emblem
        draw.ellipse([54, 45, 74, 65], fill=accent)

    def draw_ring(self, draw, seed, color, accent):
        # Circle with gem
        draw.ellipse([44, 44, 84, 84], outline=color, width=6)
        # Gem
        draw.polygon([(64, 38), (70, 44), (64, 50), (58, 44)], fill=accent)

    def draw_necklace(self, draw, seed, color, accent):
        # V chain
        draw.line([(44, 30), (64, 70), (84, 30)], fill=color, width=2)
        # Pendant
        draw.ellipse([54, 70, 74, 90], fill=accent)

    def draw_boots(self, draw, seed, color, accent):
        # Boot shape (L)
        draw.polygon([
            (44, 30), (64, 30), # Leg top
            (64, 80), (84, 80), # Foot
            (84, 94), (44, 94)  # Sole
        ], fill=color, outline=accent)

    def draw_gloves(self, draw, seed, color, accent):
        # Mitten shape
        draw.rectangle([44, 44, 84, 84], fill=color)
        draw.ellipse([44, 34, 84, 54], fill=color) # Fingers
        draw.ellipse([34, 54, 54, 74], fill=accent) # Thumb

    def draw_belt(self, draw, seed, color, accent):
        # Rectangle strip
        draw.rectangle([34, 54, 94, 74], fill=color)
        # Buckle
        draw.rectangle([59, 54, 69, 74], fill=accent)

    def draw_shoulder(self, draw, seed, color, accent):
        # Curved pauldron
        draw.pieslice([34, 44, 94, 104], 180, 0, fill=color)
        draw.line([(34, 74), (94, 74)], fill=accent, width=2)

    def draw_artifact(self, draw, seed, color, accent):
        # Mysterious shape (diamond)
        draw.polygon([
            (64, 34), (94, 64), (64, 94), (34, 64)
        ], fill=color, outline=accent)
        # Inner glow
        draw.ellipse([54, 54, 74, 74], fill=accent)

def main():
    print(f"Generating icons to {OUTPUT_DIR}...")
    ensure_dir(OUTPUT_DIR)
    
    generator = IconGenerator()
    
    count = 0
    for item in EQUIP_CFG:
        generator.generate(item)
        count += 1
        
    print(f"Generated {count} icons.")

if __name__ == "__main__":
    main()
