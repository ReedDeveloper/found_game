import pygame
import os
import math

class Level:
    def __init__(self, project_root, screen_width, screen_height):
        self.level = 0
        self.project_root = project_root
        self.SCREEN_WIDTH = screen_width
        self.SCREEN_HEIGHT = screen_height
        
        # Rank Names
        self.major_ranks = ['炼气', '筑基', '结丹', '元婴', '化神', '炼虚', '合体', '大乘', '渡劫', '金仙']
        
        # Load Images
        self.images = self._load_images()
        
        # Fonts
        self._init_fonts()

        # Animation State
        self.anim_offset_y = 0
        self.base_y = 0 # Will be calculated based on image size difference
        
        # Interaction State
        self.hover_scale = 1.0
        self.target_hover_scale = 1.0
        self.rect = pygame.Rect(0, 0, 0, 0) # Current image rect

        # Cycling Animation State
        self.is_cycling = False
        self.cycle_start_time = 0
        self.cycle_duration = 0
        self.cycle_current_idx = 0
        self.last_cycle_update = 0
        self.cycle_speed = 100 # ms per frame

        
    def _load_images(self):
        images = []
        immort_dir = os.path.join(self.project_root, 'pic', 'immort')
        
        # We expect images 1.png to 10.png corresponding to the 10 ranks
        # Rank 0 -> 1.png, Rank 1 -> 2.png, etc.
        for i in range(1, 11):
            image_path = os.path.join(immort_dir, f"{i}.png")
            try:
                if os.path.exists(image_path):
                    img = pygame.image.load(image_path)
                    # Scale logic (same as previous main.py)
                    original_rect = img.get_rect()
                    # Scale to 0.9x Screen Height to keep it within window during animation
                    target_height = int(self.SCREEN_HEIGHT * 0.9)
                    scale_factor = target_height / original_rect.height
                    new_width = int(original_rect.width * scale_factor)
                    new_height = target_height
                    img = pygame.transform.smoothscale(img, (new_width, new_height))
                    images.append(img)
                else:
                    print(f"Level system warning: Image not found {image_path}")
                    # Create a placeholder surface if image missing
                    target_height = int(self.SCREEN_HEIGHT * 0.9)
                    surf = pygame.Surface((400, target_height))
                    surf.fill((50, 50, 50))
                    images.append(surf)
            except Exception as e:
                print(f"Error loading image {image_path}: {e}")
                target_height = int(self.SCREEN_HEIGHT * 0.9)
                surf = pygame.Surface((400, target_height))
                surf.fill((50, 50, 50))
                images.append(surf)
        
        # Calculate base_y to center the enlarged image vertically
        if images:
             # Assuming all images are scaled to same height
             img_h = images[0].get_height()
             self.base_y = (self.SCREEN_HEIGHT - img_h) // 2
             
        return images

    def _init_fonts(self):
        # Try to load LiShu (SimLi), fallback to SimHei, then default
        available_fonts = pygame.font.get_fonts()
        font_name = "simli" if "simli" in available_fonts else "simhei"
        
        try:
            self.major_font = pygame.font.SysFont(font_name, 110)
            self.minor_font = pygame.font.SysFont(font_name, 60)
        except:
            self.major_font = pygame.font.Font(None, 110)
            self.minor_font = pygame.font.Font(None, 60)

    def level_up(self):
        if self.level < 89: # Max level 99 (Rank 9, Step 9)? 10 ranks * 9 steps = 90 levels (0-89)?
            # User says: Major = level/9, Minor = level%9 + 1.
            # 10 Major Ranks. Indices 0-9.
            # So Max Level corresponds to Major Rank 9, Minor Rank 9.
            # Major 9 = level // 9 => level can be 81 to 89.
            # If level is 89: 89//9 = 9 (金仙), 89%9+1 = 9 (9阶).
            # So max level should be 89.
            self.level += 1
            print(f"Level Up! Now Level {self.level}")

    def start_cycle_anim(self, duration=1000):
        self.is_cycling = True
        self.cycle_start_time = pygame.time.get_ticks()
        self.cycle_duration = duration
        self.cycle_current_idx = 0
        self.last_cycle_update = pygame.time.get_ticks()

    def handle_event(self, event):
        if event.type == pygame.MOUSEMOTION:
            if self.rect.collidepoint(event.pos):
                self.target_hover_scale = 1.1
            else:
                self.target_hover_scale = 1.0
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                # Return battle info: (rank_level)
                major_idx = self.level // 9
                return major_idx
        return None

    def update(self, exp_bar):
        current_time = pygame.time.get_ticks()

        # 0. Update Hover Scale (Tween)
        if self.hover_scale != self.target_hover_scale:
            diff = self.target_hover_scale - self.hover_scale
            if abs(diff) < 0.005:
                self.hover_scale = self.target_hover_scale
            else:
                self.hover_scale += diff * 0.1

        # 1. Update Animation (Tween/Physics logic)
        # Vertical Damped Vibration (Breathing)
        t = current_time / 1000.0
        amplitude = 20 # Pixels
        frequency = 2  # Rad/s
        self.anim_offset_y = amplitude * math.sin(frequency * t)

        # 2. Update Cycling Animation
        if self.is_cycling:
            if current_time - self.cycle_start_time > self.cycle_duration:
                self.is_cycling = False
            else:
                if current_time - self.last_cycle_update > self.cycle_speed:
                    self.cycle_current_idx = (self.cycle_current_idx + 1) % len(self.images)
                    self.last_cycle_update = current_time

        # 3. Check for level up condition
        # Using a small threshold for float comparison or just check >= max
        if exp_bar.current_exp >= exp_bar.max_exp - 0.1: # Tolerance for float
             self.level_up()
             # Reset Exp
             exp_bar.current_exp = 0
             exp_bar.target_exp = 0

    def _draw_text_with_outline(self, surface, text, font, pos, color=(255, 255, 255), outline_color=(0, 0, 0), outline_width=2):
        text_surface = font.render(text, True, color)
        w, h = text_surface.get_size()
        
        # Draw outline by drawing text at offsets
        for dx in range(-outline_width, outline_width + 1):
            for dy in range(-outline_width, outline_width + 1):
                if dx != 0 or dy != 0:
                    outline_surf = font.render(text, True, outline_color)
                    surface.blit(outline_surf, (pos[0] + dx, pos[1] + dy))
        
        # Draw main text
        surface.blit(text_surface, pos)
        return w, h # Return size for layout if needed

    def _draw_vertical_text(self, surface, text, font, top_left, color=(255, 255, 255), outline_color=(0, 0, 0)):
        x, y = top_left
        line_height = font.get_linesize() * 0.8 # Slightly tighter for vertical
        
        for char in text:
            # Center char horizontally relative to the column?
            # Or just draw. Let's just draw.
            char_surf = font.render(char, True, color)
            cw, ch = char_surf.get_size()
            
            # Outline
            for dx in range(-2, 3):
                for dy in range(-2, 3):
                    if dx != 0 or dy != 0:
                         o_surf = font.render(char, True, outline_color)
                         surface.blit(o_surf, (x + dx, y + dy))
            
            surface.blit(char_surf, (x, y))
            y += ch # Move down

    def draw(self, screen):
        # 1. Calculate Ranks
        if self.is_cycling:
            # During cycling, we show random/cycling images
            # But what about text? User only said "图片进行循环切换"
            # Let's show the cycling image but keep text consistent with actual level?
            # Or maybe text should also match the image?
            # If I cycle images (1-10), they correspond to major ranks.
            # Let's match major_idx to cycling image for visual consistency.
            major_idx = self.cycle_current_idx
        else:
            major_idx = self.level // 9
            # Clamp major_idx to prevent index out of range if level goes beyond design
            major_idx = min(major_idx, len(self.major_ranks) - 1)
            
        minor_val = (self.level % 9) + 1
        
        # 2. Draw Image (Left aligned)
        # Use image corresponding to Major Rank
        # Images list 0->1.png, 1->2.png...
        if major_idx < len(self.images):
            img = self.images[major_idx]
            
            # Apply Animation Offset
            draw_y = self.base_y + self.anim_offset_y
            
            # Apply Hover Scale
            if self.hover_scale != 1.0:
                w, h = img.get_size()
                new_w = int(w * self.hover_scale)
                new_h = int(h * self.hover_scale)
                scaled_img = pygame.transform.smoothscale(img, (new_w, new_h))
                
                # Center scaling
                draw_x = (w - new_w) // 2
                draw_y -= (new_h - h) // 2 # Adjust y to center
                
                screen.blit(scaled_img, (draw_x, draw_y))
                self.rect = pygame.Rect(draw_x, draw_y, new_w, new_h)
                
                # Update rect for text logic
                img_rect = self.rect.copy()
            else:
                screen.blit(img, (0, draw_y))
                self.rect = pygame.Rect(0, draw_y, img.get_width(), img.get_height())
                img_rect = self.rect.copy()
        else:
            img_rect = pygame.Rect(0,0,0,0)

        # 3. Draw Major Rank Text (Vertical, Left side)
        # Position: Left side of the screen, maybe with some padding.
        # "在屏幕左边绘制"
        major_name = self.major_ranks[major_idx]
        # Let's put it at x=50, y=centered or top?
        # Vertical centering usually looks best.
        # 2 chars * 110 size approx 220 height.
        text_x = 50
        text_y = 100 
        self._draw_vertical_text(screen, major_name, self.major_font, (text_x, text_y))

        # 4. Draw Minor Rank Text (Horizontal, Center of Image)
        # "在序列帧等级的图片中心绘制...几阶"
        minor_text = f"{minor_val}阶"
        
        # Calculate text size first to center
        text_surf = self.minor_font.render(minor_text, True, (255, 255, 255))
        tw, th = text_surf.get_size()
        
        # Center of image
        # Assuming image is at (0,0) with size img.get_size()
        if major_idx < len(self.images):
             # Use img_rect which includes animation offset and scale
             img_x, img_y = img_rect.topleft
             img_w, img_h = img_rect.width, img_rect.height
             
             center_x = img_x + img_w // 2
             center_y = img_y + img_h // 2
             
             # Adjust for text size
             draw_x = center_x - tw // 2
             draw_y = center_y - th // 2
             
             self._draw_text_with_outline(screen, minor_text, self.minor_font, (draw_x, draw_y))
