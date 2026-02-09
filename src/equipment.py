import pygame
import random
import os
import math

# Adjust path to allow importing from src when running from main
# main.py adds src to path, so we can import const directly if we are in src
# BUT if we import as "from src.const", it expects src to be a package in path.
# Since main.py does "sys.path.append(current_dir)", 'const' is directly importable as 'const'.
# However, equip_cfg.py might use "from src.const" inside it.
# Let's try to fix imports based on context.

try:
    from src.const import EquipPart, QualityColor, AttributeType, POWER_WEIGHTS, TIPS_X, TIPS_Y, UI_EQUIP_PANEL_HEIGHT
    from src.equip_cfg import EQUIP_CFG
except ImportError:
    from const import EquipPart, QualityColor, AttributeType, POWER_WEIGHTS, TIPS_X, TIPS_Y, UI_EQUIP_PANEL_HEIGHT
    from equip_cfg import EQUIP_CFG

class EquipTips:
    def __init__(self, x=None, y=None, width=300, height=350): # Defaults to None, will use CONST if not provided
        # Use provided coords or fallback to constants
        real_x = x if x is not None else TIPS_X
        real_y = y if y is not None else TIPS_Y
        self.rect = pygame.Rect(real_x, real_y, width, height)
        self.visible = False
        self.item_data = None
        self.compare_item = None # Source item for comparison
        self.clicked_source = False # If True, showing source item (no buttons)
        
        # Fonts
        try:
            self.title_font = pygame.font.SysFont("simhei", 20)
            self.content_font = pygame.font.SysFont("simhei", 18)
        except:
            self.title_font = pygame.font.Font(None, 20)
            self.content_font = pygame.font.Font(None, 18)
            
        # Arrows
        self.up_arrow = self._load_arrow("up_arrow.png")
        self.down_arrow = self._load_arrow("down_arrow.png")
        
        # Buttons
        self.buttons = {}
        self._load_buttons()
        
    def _load_arrow(self, name):
        path = os.path.join("pic", "ui", name)
        if os.path.exists(path):
            try:
                img = pygame.image.load(path)
                w, h = img.get_size()
                # Scale based on font size (approx 16-18px height)
                target_h = 16 
                scale = target_h / h
                new_w = int(w * scale)
                return pygame.transform.smoothscale(img, (new_w, target_h))
            except:
                pass
        return None

    def _load_buttons(self):
        def load_btn(name, size):
            path = os.path.join("pic", "ui", name)
            if not os.path.exists(path):
                surf = pygame.Surface(size)
                surf.fill((100, 100, 100))
                pygame.draw.rect(surf, (200, 200, 200), surf.get_rect(), 2)
                return surf
            try:
                img = pygame.image.load(path)
                return pygame.transform.smoothscale(img, size)
            except:
                return pygame.Surface(size)

        self.btn_imgs = {
            "equip": load_btn("equip_btn.png", (130, 60)), # Match Replace size for consistency
            "split": load_btn("split_btn.png", (130, 60)), # 1.3x approx
            "replace": load_btn("replace_btn.png", (130, 60)) # 1.3x approx
        }
        
        # Enhancement Buttons
        def load_enhance_btn(name):
            path = os.path.join("pic", "ui", name)
            target_width = 100
            
            if not os.path.exists(path):
                # Placeholder: 100x30 colored rect
                surf = pygame.Surface((target_width, 30))
                if "qianghua" in name: surf.fill((200, 100, 100))
                elif "qiangyin" in name: surf.fill((150, 150, 200))
                elif "linghua" in name: surf.fill((100, 200, 100))
                elif "lingyin" in name: surf.fill((200, 200, 100))
                return surf
            try:
                img = pygame.image.load(path)
                w, h = img.get_size()
                if h > 0:
                    ratio = w / h
                    target_height = int(target_width / ratio)
                else:
                    target_height = 30
                return pygame.transform.smoothscale(img, (target_width, target_height))
            except:
                return pygame.Surface((target_width, 30))

        self.enhance_btns = {
            "qianghua": load_enhance_btn("qianghua.png"),
            "qiangyin": load_enhance_btn("qiangyin.png"),
            "linghua": load_enhance_btn("linghua.png"),
            "lingyin": load_enhance_btn("lingyin.png")
        }
        
        self.btn_rects = {}

    def show(self, item_data, is_slot_occupied, compare_item=None, clicked_source=False, enhancements=None):
        self.item_data = item_data
        self.visible = True
        self.is_slot_occupied = is_slot_occupied
        self.compare_item = compare_item
        self.clicked_source = clicked_source
        self.enhancements = enhancements or {'qianghua': 0, 'qiangyin': 0, 'linghua': 0, 'lingyin': 0}
        
    def calculate_power(self, item, enhancements=None):
        total = 0
        if not item: return 0
        
        # Apply Enhancements
        qh_lv = enhancements.get('qianghua', 0) if enhancements else 0
        qy_lv = enhancements.get('qiangyin', 0) if enhancements else 0
        lh_lv = enhancements.get('linghua', 0) if enhancements else 0
        ly_lv = enhancements.get('lingyin', 0) if enhancements else 0
        
        # Base Attrs
        for key, val in item.get('base_attrs', {}).items():
            # QiangHua: +1% per level
            val = val * (1 + qh_lv / 100.0)
            # QiangYin: +1 per level
            val += qy_lv
            
            total += val * POWER_WEIGHTS.get(key, 1.0)
            
        # Extend Attrs
        for key, val in item.get('extend_attrs', {}).items():
            # LingHua: +1% per level
            val = val * (1 + lh_lv / 100.0)
            # LingYin: +1 per level
            val += ly_lv
            
            total += val * POWER_WEIGHTS.get(key, 1.0)
            
        return int(total)

    def hide(self):
        self.visible = False

    def handle_event(self, event):
        if not self.visible:
            return None
        if event.type == pygame.MOUSEBUTTONDOWN:
            for key, rect in self.btn_rects.items():
                if rect.collidepoint(event.pos):
                    return key
        return None

    def draw(self, screen):
        if not self.visible or not self.item_data:
            return
            
        # Draw Background
        tips_surf = pygame.Surface((self.rect.width, self.rect.height), pygame.SRCALPHA)
        pygame.draw.rect(tips_surf, (0, 0, 0, 220), tips_surf.get_rect(), border_radius=5)
        pygame.draw.rect(tips_surf, (255, 255, 255), tips_surf.get_rect(), 1, border_radius=5)
        
        self.btn_rects = {}
        
        # Prepare Data
        name = self.item_data['name']
        quality = self.item_data.get('quality', 0)
        part = self.item_data['position']
        base_attrs = self.item_data['base_attrs']
        ext_attrs = self.item_data['extend_attrs']
        
        # Power Compare
        new_power = self.calculate_power(self.item_data, self.enhancements if self.clicked_source else None)
        # Old power (equipped item) needs enhancements too if we are comparing?
        # But `show` passes `compare_item`. Usually `compare_item` comes from panel.
        # But we don't pass `compare_enhancements` yet.
        # Assuming `compare_item` is raw item data.
        # If we want accurate comparison, we should pass enhancement data of the equipped slot.
        # However, `show` only takes `enhancements` which is for the CURRENT item being shown.
        # If showing Source, `enhancements` is source enhancements.
        # If showing New Drop, `enhancements` is None (drops have no enhancements).
        # But `compare_item` (Source) DOES have enhancements.
        # We need to fetch source enhancements for comparison.
        # Let's assume calculate_power handles None gracefully.
        # Ideally we should pass `compare_enhancements` to `show` as well.
        # For now, let's ignore enhancements on comparison for drops (since they apply to the SLOT, dropping item doesn't change slot enhancement).
        # Actually, if I replace item, the slot enhancement stays.
        # So "New Power" = New Item Base + Slot Enhancement.
        # "Old Power" = Old Item Base + Slot Enhancement.
        # So enhancement applies to BOTH sides of comparison equally!
        # So difference is just (New Base - Old Base) * Multipliers + (New Flat - Old Flat).
        # But wait, % multiplier affects Base. If New Base > Old Base, then % multiplier amplifies the gain.
        # So we SHOULD include enhancements in both calculations.
        
        # If clicked_source is True, we are showing equipped item. new_power uses self.enhancements.
        # If clicked_source is False (Drop), we are comparing Drop vs Equipped.
        # Both would occupy the SAME slot, so they would inherit the SAME enhancements.
        # So we should use `self.enhancements` (which should be passed as current slot enhancements) for BOTH.
        
        old_power = self.calculate_power(self.compare_item, self.enhancements)
        # Note: If self.enhancements is None (not passed), both get 0.
        # When showing drop, we need to pass the slot's current enhancement to `show`.
        
        power_diff = new_power - old_power
        
        # 1. Name
        name_color = QualityColor.get_color_by_rank(quality)
        name_surf = self.title_font.render(name, True, name_color)
        tips_surf.blit(name_surf, (10, 10))
        name_width = name_surf.get_width()
        
        # Power Diff Text next to Name
        # Only show if not clicked_source (meaning it's a new item) AND compare_item exists
        arrow_x_offset = 220 # Align with arrows, increased for 300 width
        
        if not self.clicked_source and self.compare_item:
            diff_text = ""
            diff_color = (255, 255, 255)
            if power_diff > 0:
                diff_text = f"+{power_diff}"
                diff_color = (124, 177, 136) # Green
            elif power_diff < 0:
                diff_text = f"{power_diff}"
                diff_color = (224, 105, 85) # Red
            
            if diff_text:
                diff_surf = self.content_font.render(diff_text, True, diff_color)
                # Position right after name with small padding
                tips_surf.blit(diff_surf, (10 + name_width + 10, 12))

        # 2. Part Name
        part_name = EquipPart.get_name(part)
        part_surf = self.content_font.render(part_name, True, (200, 200, 200))
        part_rect = part_surf.get_rect(topright=(self.rect.width - 10, 10))
        tips_surf.blit(part_surf, part_rect)
        
        # 3. Power Value
        power_val = self.calculate_power(self.item_data, self.enhancements)
        power_str = f"战力: {power_val}"
        power_surf = self.content_font.render(power_str, True, (255, 215, 0)) # Gold color
        tips_surf.blit(power_surf, (10, 35))
        
        # 4. Attributes
        y_offset = 65
        def get_attr_name(key):
            for attr in AttributeType:
                if attr.key == key: return attr.value
            return key
            
        def draw_arrow(key, val, y_pos):
            # Compare with old item
            if not self.clicked_source and self.compare_item:
                old_val = self.compare_item.get('base_attrs', {}).get(key, 0) + \
                          self.compare_item.get('extend_attrs', {}).get(key, 0)
                # Wait, base and extend are separate dicts.
                # We need to know if this key is from base or extend to compare correctly?
                # Actually, usually an attribute appears in one or the other.
                # But just in case, let's look it up in both.
                
                # Check base
                old_base = self.compare_item.get('base_attrs', {}).get(key, 0)
                old_ext = self.compare_item.get('extend_attrs', {}).get(key, 0)
                # If current key is in base_attrs of new item, compare with base_attrs of old item?
                # Or compare total? "如果它的值比【源装备】中的属性高"
                # Usually compares same type.
                # Let's compare total of that attribute type.
                
                # However, we are iterating keys of new item.
                # If new item has "attack: 10", and old item has "attack: 5", show up arrow.
                # Simple logic: compare val with old_val of same key.
                
                # Get old val for this key (check both base and ext)
                old_val_for_key = self.compare_item.get('base_attrs', {}).get(key)
                if old_val_for_key is None:
                    old_val_for_key = self.compare_item.get('extend_attrs', {}).get(key, 0)
                
                if val > old_val_for_key:
                    if self.up_arrow: tips_surf.blit(self.up_arrow, (arrow_x_offset, y_pos))
                elif val < old_val_for_key:
                    if self.down_arrow: tips_surf.blit(self.down_arrow, (arrow_x_offset, y_pos))

        # Draw Separator
        pygame.draw.line(tips_surf, (100, 100, 100), (10, y_offset), (self.rect.width - 10, y_offset), 1)
        y_offset += 10
        
        # Helper to draw attrs
        def draw_attrs_section(title, attrs, y_pos, is_base=True):
            # Title
            enhance_text = ""
            if is_base:
                qh = self.enhancements.get('qianghua', 0)
                if qh > 0: enhance_text = f"+{qh}%"
            else:
                lh = self.enhancements.get('linghua', 0)
                if lh > 0: enhance_text = f"+{lh}%"
            
            title_str = title
            t_surf = self.content_font.render(title_str, True, (200, 200, 200))
            tips_surf.blit(t_surf, (10, y_pos))
            
            if enhance_text:
                e_surf = self.content_font.render(enhance_text, True, (0, 255, 0)) # Green
                tips_surf.blit(e_surf, (10 + t_surf.get_width() + 5, y_pos))
            
            y_pos += 25
            
            if not attrs:
                return y_pos
                
            for k, v in attrs.items():
                name = get_attr_name(k)
                
                # Apply Flat Enhancement
                flat_add = 0
                if is_base:
                    flat_add = self.enhancements.get('qiangyin', 0)
                else:
                    flat_add = self.enhancements.get('lingyin', 0)
                
                # Calculate Final Value for Display
                # Base * (1+%) + Flat
                pct_add = 0
                if is_base:
                    pct_add = self.enhancements.get('qianghua', 0)
                else:
                    pct_add = self.enhancements.get('linghua', 0)
                    
                final_val = int(v * (1 + pct_add/100.0) + flat_add)
                
                # Determine color based on attribute key
                # Green for Hit/Dodge, Blue for Crit/CritDef, Red/Gold for Atk/HP?
                # User image:
                # "内功防御 13" -> White text, Green arrow
                # "闪避 9" -> Green text, Green arrow
                # "血上限 96" -> Green text, Green arrow
                # It seems stats that have value > 0 are green? Or specific stats?
                # "命中和闪避(绿色); 暴击和暴防(蓝色)" (from attribute panel request)
                # Let's use AttributeType colors.
                
                attr_color = (255, 255, 255) # Default White
                if k in ["hit", "dodge"]:
                    attr_color = (124, 177, 136) # Green
                elif k in ["crit", "crit_defense"]:
                    attr_color = (100, 180, 255) # Blue
                elif k in ["hp"]:
                    attr_color = (224, 105, 85) # Red (But user image shows green? Maybe because it's an UPGRADE?)
                    # In Tips, usually static color for stat type.
                    # Or Green if it's an "Extend Attribute" (green text in image "闪避", "血上限" are likely extend attrs)?
                    # Image shows:
                    # White: "内功防御 13" (Base Attr?)
                    # Green: "闪避 9", "血上限 96" (Extend Attrs?)
                    # Let's follow this logic: Base = White, Extend = Green/Blue/Red based on type?
                    # Or just: Base = White, Extend = Color by Type.
                
                if not is_base:
                    # Extend Attrs coloring
                    if k == "hp": attr_color = (124, 177, 136) # Green in user image
                    elif k in ["outer_attack", "inner_attack"]: attr_color = (255, 215, 0) # Gold
                    elif k in ["outer_defense", "inner_defense"]: attr_color = (255, 255, 255)
                    # Keep hit/dodge/crit logic
                
                attr_str = f"{name} {final_val}"
                attr_surf = self.content_font.render(attr_str, True, attr_color)
                tips_surf.blit(attr_surf, (10, y_pos))
                
                if flat_add > 0:
                    flat_str = f"+{flat_add}"
                    flat_surf = self.content_font.render(flat_str, True, (0, 255, 0))
                    tips_surf.blit(flat_surf, (10 + attr_surf.get_width() + 5, y_pos))

                # Logic to draw comparison arrows
                # Calculate Old Val (for comparison)
                old_final_val = 0
                has_old_val = False
                
                if not self.clicked_source and self.compare_item:
                    # Find base or extend
                    old_base = self.compare_item.get('base_attrs', {}).get(k)
                    old_ext = self.compare_item.get('extend_attrs', {}).get(k)
                    
                    raw_old = 0
                    is_old_base = False
                    if old_base is not None:
                        raw_old = old_base
                        is_old_base = True
                        has_old_val = True
                    elif old_ext is not None:
                        raw_old = old_ext
                        is_old_base = False
                        has_old_val = True
                    
                    if has_old_val:
                        # Apply Enhancements to Old Val
                        # Use self.enhancements
                        flat_add_old = 0
                        pct_add_old = 0
                        
                        if is_old_base:
                            flat_add_old = self.enhancements.get('qiangyin', 0)
                            pct_add_old = self.enhancements.get('qianghua', 0)
                        else:
                            flat_add_old = self.enhancements.get('lingyin', 0)
                            pct_add_old = self.enhancements.get('linghua', 0)
                            
                        old_final_val = int(raw_old * (1 + pct_add_old/100.0) + flat_add_old)
                        
                        # Draw Comparison Text
                        diff = final_val - old_final_val
                        if diff != 0:
                            diff_color = (124, 177, 136) if diff > 0 else (224, 105, 85) # Green / Red
                            arrow = "↑" if diff > 0 else "↓"
                            diff_str = f"({arrow}{abs(diff)})"
                            
                            diff_surf = self.content_font.render(diff_str, True, diff_color)
                            
                            # Position: After Value (and after Flat Add if exists)
                            x_pos = 10 + attr_surf.get_width() + 5
                            if flat_add > 0:
                                x_pos += flat_surf.get_width() + 5
                                
                            tips_surf.blit(diff_surf, (x_pos, y_pos))

                y_pos += 20
            return y_pos + 10

        # Base Attrs
        y_offset = draw_attrs_section("基础属性", self.item_data.get('base_attrs', {}), y_offset, True)
        
        # Extend Attrs
        y_offset = draw_attrs_section("扩展属性", self.item_data.get('extend_attrs', {}), y_offset, False)
            
        # --- Buttons ---
        if not self.clicked_source:
            btn_y = self.rect.height - 60
            
            # Calculate layout for Split/Replace first to determine "Replace" position
            gap = 20
            split_img = self.btn_imgs["split"] # 130
            replace_img = self.btn_imgs["replace"] # 130
            total_w = split_img.get_width() + replace_img.get_width() + gap # 280
            start_x = (self.rect.width - total_w) // 2 # (300-280)/2 = 10
            
            replace_x = start_x + split_img.get_width() + gap # 10 + 130 + 20 = 160
            
            if not self.is_slot_occupied:
                img = self.btn_imgs["equip"]
                # Position Equip button exactly where Replace button would be
                # for muscle memory / clicking convenience
                img_rect = img.get_rect(left=replace_x, top=btn_y)
                tips_surf.blit(img, img_rect)
                
                global_rect = img_rect.copy()
                global_rect.x += self.rect.x
                global_rect.y += self.rect.y
                self.btn_rects["equip"] = global_rect
            else:
                split_rect = split_img.get_rect(left=start_x, top=btn_y)
                replace_rect = replace_img.get_rect(left=replace_x, top=btn_y)
                
                tips_surf.blit(split_img, split_rect)
                tips_surf.blit(replace_img, replace_rect)
                
                g_split = split_rect.copy()
                g_split.x += self.rect.x
                g_split.y += self.rect.y
                self.btn_rects["split"] = g_split
                
                g_replace = replace_rect.copy()
                g_replace.x += self.rect.x
                g_replace.y += self.rect.y
                self.btn_rects["replace"] = g_replace
        else:
            # Show Enhancement Buttons inside tips (Right Side)
            # Start below title area
            start_y = 70
            gap = 5
            keys = ["qianghua", "qiangyin", "linghua", "lingyin"]
            
            # Align to right edge
            for idx, key in enumerate(keys):
                btn_img = self.enhance_btns[key]
                # Right align
                x = self.rect.width - btn_img.get_width()
                y = start_y + idx * (btn_img.get_height() + gap)
                
                tips_surf.blit(btn_img, (x, y))
                
                # Store GLOBAL rect
                g_rect = pygame.Rect(self.rect.x + x, self.rect.y + y, btn_img.get_width(), btn_img.get_height())
                self.btn_rects[key] = g_rect

        # --- Enhancement Buttons (Right Side) ---
        # REMOVED: Handled above in else block
            
        return tips_surf


class EquipPanel:
    def __init__(self, x, y, width):
        height = UI_EQUIP_PANEL_HEIGHT
        self.rect = pygame.Rect(x, y, width, height) 
        # Load background
        path = os.path.join("pic", "ui", "euqipback.png")
        if os.path.exists(path):
            self.bg_img = pygame.image.load(path)
            self.bg_img = pygame.transform.smoothscale(self.bg_img, (width, height))
        else:
            self.bg_img = pygame.Surface((width, height))
            self.bg_img.fill((30, 30, 30))
            
        # Slots Definition (3 rows x 4 cols)
        # Row 1: Weapon, Helmet, Armor, Boots
        # Row 2: Belt, Bracer, Gloves, Necklace
        # Row 3: Shoulder, Ring, Artifact, Amulet
        self.slot_map = {
            EquipPart.WEAPON: (0, 0), EquipPart.HELMET: (1, 0), EquipPart.ARMOR: (2, 0), EquipPart.BOOTS: (3, 0),
            EquipPart.BELT: (0, 1),   EquipPart.BRACER: (1, 1), EquipPart.GLOVES: (2, 1), EquipPart.NECKLACE: (3, 1),
            EquipPart.SHOULDER: (0, 2), EquipPart.RING: (1, 2), EquipPart.ARTIFACT: (2, 2), EquipPart.AMULET: (3, 2)
        }
        
        self.equipped_items = {} # part -> item_data
        
        # Enhancement Data (part -> dict)
        # { 'qianghua': 0, 'qiangyin': 0, 'linghua': 0, 'lingyin': 0 }
        self.enhancements = {} 
        for part in EquipPart:
            self.enhancements[part] = {
                'qianghua': 0,
                'qiangyin': 0,
                'linghua': 0,
                'lingyin': 0
            }
        
        # Calculate slot positions
        # Padding
        self.padding_x = 20
        self.padding_y = 10
        self.slot_w = (width - self.padding_x * 5) // 4
        self.slot_h = (height - self.padding_y * 4) // 3
        
        # Fonts
        self.name_font = pygame.font.SysFont("simhei", 14)
        
        # Icons cache
        self.icon_cache = {}

    def get_enhancement(self, part):
        return self.enhancements.get(part, {
            'qianghua': 0, 'qiangyin': 0, 'linghua': 0, 'lingyin': 0
        })

    def update_enhancement(self, part, type_key, level):
        if part in self.enhancements:
            self.enhancements[part][type_key] = level

    def get_slot_rect(self, part):
        if part not in self.slot_map: return None
        col, row = self.slot_map[part]
        
        x = self.rect.x + self.padding_x + col * (self.slot_w + self.padding_x)
        y = self.rect.y + self.padding_y + row * (self.slot_h + self.padding_y)
        return pygame.Rect(x, y, self.slot_w, self.slot_h)

    def equip(self, item_data):
        part = item_data['position']
        self.equipped_items[part] = item_data
        
        # Load icon if needed
        item_id = item_data['id']
        icon_path = os.path.join("pic", "equipments", f"{item_id}.png")
        if os.path.exists(icon_path):
            img = pygame.image.load(icon_path)
            img = pygame.transform.smoothscale(img, (self.slot_w, self.slot_h))
            self.icon_cache[item_id] = img

    def get_equipped_item(self, part):
        return self.equipped_items.get(part)

    def is_occupied(self, part):
        return part in self.equipped_items

    def draw(self, screen):
        screen.blit(self.bg_img, self.rect)
        
        # Draw slots and items
        for part, (col, row) in self.slot_map.items():
            rect = self.get_slot_rect(part)
            # Draw slot placeholder/border
            pygame.draw.rect(screen, (50, 50, 50), rect, 1)
            
            if part in self.equipped_items:
                item = self.equipped_items[part]
                item_id = item['id']
                
                # Draw Icon
                if item_id in self.icon_cache:
                    # Icon fills the slot?
                    # If we want space for text, maybe icon should be slightly smaller or shifted up?
                    # Currently we scale icon to slot_w, slot_h.
                    # Text overlays.
                    screen.blit(self.icon_cache[item_id], rect)
                else:
                    # Fallback text if no icon
                    font = pygame.font.Font(None, 20)
                    text = font.render(item['name'][:2], True, (200, 200, 200))
                    screen.blit(text, rect)
                    
                # Draw Name at bottom
                name = item['name']
                # Simplify name? Remove "炼气·" prefix if too long?
                # "炼气·白虎刀" -> "白虎刀" ?
                # But prefix indicates rank.
                
                name_color = QualityColor.get_color_by_rank(item.get('quality', 0))
                text_surf = self.name_font.render(name, True, name_color)
                
                # Scale if too wide
                if text_surf.get_width() > self.slot_w - 2:
                    scale = (self.slot_w - 2) / text_surf.get_width()
                    new_h = int(text_surf.get_height() * scale)
                    # Don't make it too short
                    if new_h < 8: new_h = 8
                    text_surf = pygame.transform.smoothscale(text_surf, (self.slot_w - 2, new_h))
                
                text_rect = text_surf.get_rect(midbottom=(rect.centerx, rect.bottom - 2))
                
                # Background for text
                bg_rect = text_rect.copy()
                bg_rect.inflate_ip(4, 0)
                s = pygame.Surface((bg_rect.width, bg_rect.height), pygame.SRCALPHA)
                s.fill((0, 0, 0, 180))
                screen.blit(s, bg_rect)
                
                screen.blit(text_surf, text_rect)

class EquipmentManager:
    def __init__(self, exp_bar_rect):
        self.temp_bag = [] 
        # Use CONST coordinates for Tips
        self.tips = EquipTips() 
        
        # Panel below exp bar
        # NOTE: exp_bar_rect is now the new calculated position from main.py
        # It's at (UI_SIDEBAR_X, UI_EXP_Y, ...)
        # So exp_bar_rect.bottom + 10 IS correct for relative positioning.
        # But we want to ensure it matches UI_EQUIP_PANEL_Y
        # If passed rect is correct, this logic holds.
        panel_y = exp_bar_rect.bottom + 10
        self.panel = EquipPanel(exp_bar_rect.x, panel_y, exp_bar_rect.width)
        
        # Animation State
        self.anim_item = None # {img, start_pos, target_pos, current_pos, speed}
        self.is_animating = False

    def has_temp_item(self):
        return len(self.temp_bag) > 0

    def reshow_temp_tips(self):
        if self.temp_bag:
            item = self.temp_bag[0]
            part = item['position']
            occupied = self.panel.is_occupied(part)
            compare_item = self.panel.get_equipped_item(part)
            self.tips.show(item, occupied, compare_item=compare_item, clicked_source=False)
        
    def generate_drop(self, player_level):
        target_rank = min(player_level // 9, 9)
        candidates = [item for item in EQUIP_CFG if item['quality'] == target_rank]
        
        if candidates:
            item = random.choice(candidates)
            self.temp_bag.append(item)
            print(f"Dropped Item: {item['name']}")
            
            # Show tips
            part = item['position']
            occupied = self.panel.is_occupied(part)
            compare_item = self.panel.get_equipped_item(part)
            self.tips.show(item, occupied, compare_item=compare_item, clicked_source=False)
            return True
        return False
        
    def clear_temp_bag(self):
        self.temp_bag = []
        self.tips.hide()

    def handle_event(self, event, bag_system=None, bag_btn_rect=None):
        # 1. Handle Tips events (Buttons)
        # Note: Tips handles clicks on ITSELF.
        # But Enhancement Buttons are OUTSIDE tips rect.
        # So Tips.handle_event won't catch them usually if it checks rect collide.
        # But Tips.handle_event currently only checks btn_rects.
        
        # Check Enhancement Buttons
        # REMOVED manual check, now handled by tips.handle_event because buttons are inside btn_rects
        
        action = self.tips.handle_event(event)
        if action:
            if action in ["qianghua", "qiangyin", "linghua", "lingyin"]:
                 self.handle_enhance(action, bag_system)
                 return True
                 
            item = self.temp_bag[0] if self.temp_bag else None
            # Only process equip/split if we have a temp item!
            # Actually equip/split buttons only appear if not clicked_source.
            # If clicked_source is True (viewing equipped), action won't be equip/split.
            
            if item:
                if action == "equip" or action == "replace":
                    self.start_equip_anim(item)
                    self.panel.equip(item)
                    self.clear_temp_bag()
                elif action == "split":
                    # Split Logic
                    if bag_system:
                        qty = (item.get('quality', 0) + 1) * 5
                        bag_system.add_item(60000, qty) # 60000 is Meteor Iron
                        print(f"Split Item: Obtained {qty} Meteor Iron")
                    
                    # Animation
                    if bag_btn_rect:
                        self.start_split_anim(item, bag_btn_rect)
                    
                    self.clear_temp_bag()
            return True
            
        # 2. Handle Panel events (Click equipped item to show tips)
        if event.type == pygame.MOUSEBUTTONDOWN:
            clicked_slot = False
            # Check if clicked on any equipped slot
            for part, (col, row) in self.panel.slot_map.items():
                rect = self.panel.get_slot_rect(part)
                if rect and rect.collidepoint(event.pos):
                    clicked_slot = True
                    item = self.panel.get_equipped_item(part)
                    if item:
                        # Show tips for source item (no buttons)
                        enhancements = self.panel.get_enhancement(part)
                        self.tips.show(item, True, compare_item=None, clicked_source=True, enhancements=enhancements)
                        return True
                    else:
                        # If clicking empty slot, hide tips
                        if self.tips.visible:
                            self.tips.visible = False
                            # If we closed tips, and we have a temp bag item, reshow it
                            if self.temp_bag:
                                self.reshow_temp_tips()
                            return True
            
            # 3. Handle Outside Clicks (Close Tips)
            if not clicked_slot and self.tips.visible:
                # Check if clicked inside Tips Rect
                if not self.tips.rect.collidepoint(event.pos):
                    self.tips.visible = False
                    
                    # If we closed tips (e.g. from viewing equipped item), and have pending drop, reshow it
                    if self.temp_bag:
                        self.reshow_temp_tips()
                        
                    return True # Consume event
                        
        return False

    def handle_enhance(self, type_key, bag_system):
        if not bag_system: return
        
        # Determine Item/Cost
        # QiangHua (60000), QiangYin (60100), LingHua (60200), LingYin (60300)
        cost_map = {
            "qianghua": 60000,
            "qiangyin": 60100,
            "linghua": 60200,
            "lingyin": 60300
        }
        name_map = {
            "qianghua": "强化",
            "qiangyin": "强印",
            "linghua": "灵化",
            "lingyin": "灵印"
        }
        
        material_id = cost_map[type_key]
        op_name = name_map[type_key]
        
        # Check Cost
        if not bag_system.remove_item(material_id, 1):
            self.add_toast(f"{op_name}失败: 材料不足", False)
            return
            
        # Get Current Level
        part = self.tips.item_data['position']
        current_enhancements = self.panel.get_enhancement(part)
        current_level = current_enhancements.get(type_key, 0)
        
        # Max Level Check
        if current_level >= 99:
             self.add_toast(f"{op_name}失败: 已达上限", False)
             return

        # Calculate Success Rate
        # "Higher level, higher failure rate"
        # Formula: Base 100%, -1% per level?
        # Level 0 -> 100%
        # Level 50 -> 50%
        # Level 90 -> 10%
        # Min 1%
        success_rate = max(1, 100 - current_level)
        
        import random
        roll = random.randint(1, 100)
        
        if roll <= success_rate:
            # Success
            new_level = current_level + 1
            self.panel.update_enhancement(part, type_key, new_level)
            # Update Tips Data
            self.tips.enhancements[type_key] = new_level
            self.add_toast(f"{op_name}成功! 等级+{new_level}", True)
        else:
            # Fail
            self.add_toast(f"{op_name}失败! (概率{success_rate}%)", False)

    def start_split_anim(self, item, target_rect):
        # Setup animation for split
        start_pos = self.tips.rect.center
        target_pos = target_rect.center
        
        # Load large icon
        icon_path = os.path.join("pic", "equipments", f"{item['id']}.png")
        if os.path.exists(icon_path):
            img = pygame.image.load(icon_path)
            img = pygame.transform.smoothscale(img, (128, 128))
        else:
            img = pygame.Surface((128, 128))
            img.fill((100, 100, 100))
            
        self.anim_item = {
            "img": img,
            "pos": list(start_pos),
            "target": target_pos,
            "type": "split",
            "start_size": 128,
            "end_size": 10,
            "current_size": 128.0,
            "alpha": 255.0,
            "state": "move" # move -> fade
        }
        self.is_animating = True

    def start_equip_anim(self, item):
        # Setup animation
        # Start: Tips center
        start_pos = self.tips.rect.center
        # Target: Slot center
        slot_rect = self.panel.get_slot_rect(item['position'])
        target_pos = slot_rect.center
        
        # Load large icon
        icon_path = os.path.join("pic", "equipments", f"{item['id']}.png")
        if os.path.exists(icon_path):
            img = pygame.image.load(icon_path)
            img = pygame.transform.smoothscale(img, (128, 128))
        else:
            img = pygame.Surface((128, 128))
            img.fill((200, 200, 0))
            
        self.anim_item = {
            "img": img,
            "pos": list(start_pos),
            "target": target_pos,
            "type": "equip", # default type
            "finished": False
        }
        self.is_animating = True

    def update(self):
        if self.is_animating and self.anim_item:
            # Common Logic
            cx, cy = self.anim_item["pos"]
            tx, ty = self.anim_item["target"]
            
            dx = tx - cx
            dy = ty - cy
            dist = math.hypot(dx, dy)
            
            speed = 0.1 # Lerp factor
            
            if self.anim_item.get("type") == "split":
                # Move + Scale Logic
                if self.anim_item["state"] == "move":
                    if dist < 5:
                        self.anim_item["pos"] = list(self.anim_item["target"])
                        self.anim_item["state"] = "fade"
                    else:
                        self.anim_item["pos"][0] += dx * speed
                        self.anim_item["pos"][1] += dy * speed
                        
                        # Scale down while moving
                        # Simple approach: Lerp size too
                        target_size = self.anim_item["end_size"]
                        current_size = self.anim_item["current_size"]
                        self.anim_item["current_size"] += (target_size - current_size) * speed
                        
                elif self.anim_item["state"] == "fade":
                    # Fade out
                    self.anim_item["alpha"] -= 15 # Fade speed
                    if self.anim_item["alpha"] <= 0:
                        self.is_animating = False
                        self.anim_item = None
            else:
                # Default Equip Anim (Just Move)
                if dist < 5:
                    self.is_animating = False
                    self.anim_item = None
                else:
                    self.anim_item["pos"][0] += dx * speed
                    self.anim_item["pos"][1] += dy * speed
                    
                    # Scale down effect?
                    # Maybe scale from 128 to slot size (approx 40-50)
                    # For now just move

    def draw_tips(self, screen):
        if self.tips.visible and self.tips.item_data:
            tips_surf = self.tips.draw(screen)
            screen.blit(tips_surf, self.tips.rect)
            
        self.draw_anim(screen)
        
        # Draw Toast Messages
        self.draw_toasts(screen)

    def draw_toasts(self, screen):
        # Clean up old toasts
        import pygame
        current_time = pygame.time.get_ticks()
        if hasattr(self, 'toasts'):
            self.toasts = [t for t in self.toasts if current_time - t['start_time'] < 2000]
            
            for i, toast in enumerate(self.toasts):
                # Draw at top center
                font = self.tips.title_font
                text = toast['msg']
                color = (0, 255, 0) if toast['success'] else (255, 0, 0)
                
                surf = font.render(text, True, color)
                # Background
                bg_rect = surf.get_rect(center=(screen.get_width()//2, 100 + i*30))
                bg_rect.inflate_ip(20, 10)
                
                s = pygame.Surface((bg_rect.width, bg_rect.height), pygame.SRCALPHA)
                pygame.draw.rect(s, (0, 0, 0, 180), s.get_rect(), border_radius=5)
                screen.blit(s, bg_rect)
                screen.blit(surf, surf.get_rect(center=bg_rect.center))
                
    def add_toast(self, msg, success):
        if not hasattr(self, 'toasts'):
            self.toasts = []
        self.toasts.append({
            'msg': msg,
            'success': success,
            'start_time': pygame.time.get_ticks()
        })
            
    def draw_panel(self, screen):
        self.panel.draw(screen)
        
    def draw_anim(self, screen):
        if self.is_animating and self.anim_item:
            img = self.anim_item["img"]
            
            # Apply dynamic scaling/alpha for split anim
            if self.anim_item.get("type") == "split":
                current_size = int(self.anim_item["current_size"])
                # Avoid 0 size
                if current_size < 1: current_size = 1
                
                # Resize
                if current_size != 128:
                    img = pygame.transform.smoothscale(img, (current_size, current_size))
                
                # Apply Alpha
                if self.anim_item["alpha"] < 255:
                    img.set_alpha(int(self.anim_item["alpha"]))
            
            rect = img.get_rect(center=(int(self.anim_item["pos"][0]), int(self.anim_item["pos"][1])))
            screen.blit(img, rect)
