
import pygame
import os

try:
    from src.const import UI_SIDEBAR_X, UI_ATTR_PANEL_Y, UI_ATTR_PANEL_HEIGHT, AttributeType
except ImportError:
    from const import UI_SIDEBAR_X, UI_ATTR_PANEL_Y, UI_ATTR_PANEL_HEIGHT, AttributeType

class AttributePanel:
    def __init__(self):
        # Resident in sidebar
        self.rect = pygame.Rect(UI_SIDEBAR_X, UI_ATTR_PANEL_Y, 300, UI_ATTR_PANEL_HEIGHT)
        self.target_stats = {}
        self.current_stats = {}
        
        # Fonts
        try:
            self.font = pygame.font.SysFont("simhei", 20)
            self.label_font = pygame.font.SysFont("simhei", 18)
        except:
            self.font = pygame.font.Font(None, 24)
            self.label_font = pygame.font.Font(None, 20)
            
        # Colors
        self.colors = {
            "hp": (224, 105, 85),          # Red
            "gold": (255, 215, 0),         # Gold (Outer)
            "orange": (255, 165, 0),       # Orange (Inner)
            "green": (124, 177, 136),      # Green (Hit/Dodge)
            "blue": (100, 180, 255)        # Blue (Crit/Crit Def)
        }

    def update_stats(self, stats):
        self.target_stats = stats
        # If first time, init current_stats
        if not self.current_stats:
             for k, v in stats.items():
                 self.current_stats[k] = 0 # Start from 0 for intro animation? Or v?
                 # Let's start from 0 for effect

    def update(self):
        for key, target_val in self.target_stats.items():
            current_val = self.current_stats.get(key, 0)
            
            if current_val != target_val:
                diff = target_val - current_val
                # Tween speed
                step = diff * 0.1
                
                if abs(step) < 0.5:
                    if abs(diff) < 0.5:
                        current_val = target_val
                    else:
                        current_val += (1 if diff > 0 else -1)
                else:
                    current_val += step
                    
                self.current_stats[key] = current_val

    def draw(self, screen):
        # Draw Background (Similar to EquipTips)
        s = pygame.Surface((self.rect.width, self.rect.height), pygame.SRCALPHA)
        pygame.draw.rect(s, (0, 0, 0, 180), s.get_rect(), border_radius=5)
        pygame.draw.rect(s, (100, 100, 100), s.get_rect(), 1, border_radius=5)
        
        # Title
        title = self.font.render("属性面板", True, (255, 255, 255))
        title_rect = title.get_rect(centerx=self.rect.width//2, top=10)
        s.blit(title, title_rect)
        
        y_offset = 50
        line_height = 35
        
        # Row 1: Max HP (Red)
        hp = int(self.current_stats.get('hp', 0))
        hp_text = f"血上限: {hp}"
        hp_surf = self.label_font.render(hp_text, True, self.colors['hp'])
        s.blit(hp_surf, (20, y_offset))
        y_offset += line_height
        
        # Helper to draw a row with 2 items
        def draw_row(label1, val1, label2, val2, color):
            t1 = f"{label1}: {int(val1)}"
            t2 = f"{label2}: {int(val2)}"
            
            s1 = self.label_font.render(t1, True, color)
            s2 = self.label_font.render(t2, True, color)
            
            s.blit(s1, (20, y_offset))
            s.blit(s2, (160, y_offset))
            
        # Row 2: Outer Atk & Outer Def (Gold)
        draw_row("外功攻击", self.current_stats.get('outer_attack', 0),
                 "外功防御", self.current_stats.get('outer_defense', 0),
                 self.colors['gold'])
        y_offset += line_height

        # Row 3: Inner Atk & Inner Def (Orange)
        draw_row("内功攻击", self.current_stats.get('inner_attack', 0),
                 "内功防御", self.current_stats.get('inner_defense', 0),
                 self.colors['orange'])
        y_offset += line_height

        # Row 4: Hit & Dodge (Green)
        draw_row("命中", self.current_stats.get('hit', 0),
                 "闪避", self.current_stats.get('dodge', 0),
                 self.colors['green'])
        y_offset += line_height

        # Row 5: Crit & Crit Def (Blue)
        draw_row("暴击", self.current_stats.get('crit', 0),
                 "暴防", self.current_stats.get('crit_defense', 0),
                 self.colors['blue'])
        y_offset += line_height

        screen.blit(s, self.rect)
