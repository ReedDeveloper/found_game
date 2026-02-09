import pygame
import os
import math

try:
    from src.const import POWER_WEIGHTS, LEVEL_POWER_WEIGHT
except ImportError:
    from const import POWER_WEIGHTS, LEVEL_POWER_WEIGHT

class Power:
    def __init__(self, project_root, x, y, width, height):
        self.current_power = 0
        self.target_power = 0
        self.display_power = 0 # For animation
        self.rect = pygame.Rect(x, y, width, height)
        
        # Load Background
        path = os.path.join(project_root, 'pic', 'ui', 'powerback.png')
        if os.path.exists(path):
            self.image = pygame.image.load(path)
            self.image = pygame.transform.smoothscale(self.image, (width, height))
        else:
            self.image = pygame.Surface((width, height))
            self.image.fill((100, 0, 0)) # Reddish fallback
            
        # Font
        try:
            self.font = pygame.font.SysFont("隶书", 36, bold=True)
        except:
            self.font = pygame.font.Font(None, 36)
            
        self.text_color = (255, 215, 0) # Gold
        
    def calculate_power(self, level, equipment_dict):
        """
        Calculate total power based on level and equipment.
        equipment_dict: {part: item_data}
        """
        total = 0
        
        # 1. Level Power
        total += level * LEVEL_POWER_WEIGHT
        
        # 2. Equipment Power
        for part, item in equipment_dict.items():
            # Base Attrs
            for key, val in item.get('base_attrs', {}).items():
                weight = POWER_WEIGHTS.get(key, 1.0)
                total += val * weight
                
            # Extend Attrs
            for key, val in item.get('extend_attrs', {}).items():
                weight = POWER_WEIGHTS.get(key, 1.0)
                total += val * weight
                
        self.target_power = int(total)
        
    def update(self):
        # Tween Animation
        if self.display_power != self.target_power:
            diff = self.target_power - self.display_power
            # Simple lerp or fixed step?
            # User asked for "smooth animation like exp"
            # If diff is large, step large.
            step = diff * 0.1
            if abs(step) < 1:
                step = 1 if step > 0 else -1
            
            self.display_power += step
            
            # Snap if close
            if abs(self.target_power - self.display_power) < 1:
                self.display_power = self.target_power
                
    def draw_text_with_outline(self, text, font, color, outline_color, pos, screen):
        x, y = pos
        # Draw outline (offsets)
        for dx, dy in [(-1,-1), (-1,1), (1,-1), (1,1), (0,1), (0,-1), (1,0), (-1,0)]:
            surf = font.render(text, True, outline_color)
            screen.blit(surf, (x+dx, y+dy))
            
        # Draw main text
        surf = font.render(text, True, color)
        screen.blit(surf, (x, y))

    def draw(self, screen):
        # Draw Background
        screen.blit(self.image, self.rect)
        
        # Draw Text "战力 12345"
        text = f"战力 {int(self.display_power)}"
        text_surf = self.font.render(text, True, self.text_color)
        
        # Center text
        text_rect = text_surf.get_rect(center=self.rect.center)
        
        self.draw_text_with_outline(text, self.font, self.text_color, (0, 0, 0), text_rect.topleft, screen)
