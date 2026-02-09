
import pygame
import os

try:
    from src.item_cfg import ITEM_CFG
    from src.const import UI_PANEL_X, UI_PANEL_Y, UI_PANEL_WIDTH
    from src.button import ScaleButton
except ImportError:
    from item_cfg import ITEM_CFG
    from const import UI_PANEL_X, UI_PANEL_Y, UI_PANEL_WIDTH
    from button import ScaleButton

class Bag:
    def __init__(self, project_root):
        self.visible = False
        self.rect = pygame.Rect(UI_PANEL_X, UI_PANEL_Y, UI_PANEL_WIDTH, 350) # Same height as tips
        self.project_root = project_root
        
        # Load items (default 1 of each)
        # Structure: {item_id: count}
        self.items = {}
        for item_id in ITEM_CFG:
            self.items[item_id] = 1
            
        # UI Assets
        self.font = pygame.font.SysFont("simhei", 16)
        self.title_font = pygame.font.SysFont("simhei", 20)
        
        # Preload Item Images
        self.item_imgs = {}
        for item_id, data in ITEM_CFG.items():
            path = os.path.join(project_root, data['image'])
            if os.path.exists(path):
                img = pygame.image.load(path)
                # Scale to fit grid cell (e.g. 60x60)
                self.item_imgs[item_id] = pygame.transform.smoothscale(img, (60, 60))
            else:
                s = pygame.Surface((60, 60))
                s.fill((100, 100, 100))
                self.item_imgs[item_id] = s

    def add_item(self, item_id, count=1):
        if item_id in self.items:
            self.items[item_id] += count
        else:
            self.items[item_id] = count

    def remove_item(self, item_id, count=1):
        if item_id in self.items and self.items[item_id] >= count:
            self.items[item_id] -= count
            return True
        return False

    def toggle(self):
        self.visible = not self.visible

    def draw(self, screen):
        if not self.visible:
            return

        # Draw Background (Similar to EquipTips)
        s = pygame.Surface((self.rect.width, self.rect.height), pygame.SRCALPHA)
        pygame.draw.rect(s, (0, 0, 0, 220), s.get_rect(), border_radius=5)
        pygame.draw.rect(s, (100, 100, 100), s.get_rect(), 1, border_radius=5)
        
        # Title
        title = self.title_font.render("背包", True, (255, 255, 255))
        title_rect = title.get_rect(centerx=self.rect.width//2, top=10)
        s.blit(title, title_rect)
        
        # Grid Layout
        # 4 columns? 300 / 4 = 75px. 60px item + 15px gap.
        start_x = 15
        start_y = 50
        gap = 10
        cell_size = 60
        cols = 4
        
        idx = 0
        for item_id, count in self.items.items():
            if count <= 0:
                continue
                
            row = idx // cols
            col = idx % cols
            
            x = start_x + col * (cell_size + gap)
            y = start_y + row * (cell_size + gap)
            
            # Draw Icon
            if item_id in self.item_imgs:
                s.blit(self.item_imgs[item_id], (x, y))
                
            # Draw Frame (Optional quality color)
            # Just simple border for now
            pygame.draw.rect(s, (150, 150, 150), (x, y, cell_size, cell_size), 1)
            
            # Draw Count (Bottom Right)
            if count > 1:
                cnt_surf = self.font.render(str(count), True, (255, 255, 255))
                cnt_rect = cnt_surf.get_rect(bottomright=(x + cell_size - 2, y + cell_size - 2))
                # Add small background for text readability
                bg_rect = cnt_rect.copy()
                bg_rect.inflate_ip(4, 2)
                pygame.draw.rect(s, (0, 0, 0, 150), bg_rect)
                s.blit(cnt_surf, cnt_rect)
                
            idx += 1
            
        screen.blit(s, self.rect)

class BagButton(ScaleButton):
    def __init__(self, right_btn_rect, project_root):
        path = os.path.join(project_root, "pic", "ui", "bagbtn.png")
        
        # Need to load image first to calculate size and position
        # But ScaleButton loads image in __init__.
        # We need to calculate x, y before super().__init__ or adjust after.
        # Let's instantiate at 0,0 then move.
        
        # Scale 0.08
        super().__init__(0, 0, path, scale_factor=0.08)
        
        # Position: Left of right_btn with 10px gap
        # right_btn_rect is the rect of MainBtn
        # self.rect is already sized by ScaleButton.__init__
        
        target_x = right_btn_rect.left - 10 - self.rect.width
        # Align bottoms? Or centers? User didn't specify alignment, just "left of".
        # "正好在mainbtn的左边". Usually implies bottom or center alignment.
        # Let's align bottom for visual consistency.
        target_y = right_btn_rect.bottom - self.rect.height
        
        # Update Rect
        self.rect.topleft = (target_x, target_y)
        self.center = self.rect.center

