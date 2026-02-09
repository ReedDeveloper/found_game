import pygame
import os

class Energy:
    def __init__(self, project_root):
        self.current_energy = 50
        self.max_energy = 50
        
        # Load Resource
        image_path = os.path.join(project_root, 'pic', 'ui', 'energy_back.png')
        try:
            if os.path.exists(image_path):
                self.image = pygame.image.load(image_path)
                # Resize to 20x20 as requested
                self.image = pygame.transform.smoothscale(self.image, (20, 20))
            else:
                print(f"Warning: Energy background not found at {image_path}")
                self.image = pygame.Surface((20, 20))
                self.image.fill((50, 50, 50))
        except Exception as e:
            print(f"Error loading energy background: {e}")
            self.image = pygame.Surface((20, 20))
            self.image.fill((50, 50, 50))
            
        self.rect = self.image.get_rect()
        
        # Font Setup
        # SysFont("SimLi", 28)
        try:
            # Check if SimLi is available, otherwise fallback
            # Pygame SysFont names might be lowercased or specific
            self.font = pygame.font.SysFont("simli", 28)
        except:
            self.font = pygame.font.Font(None, 28)
            
        self.text_color = (198, 114, 34) # Orange

        # Countdown Setup
        try:
            self.countdown_font = pygame.font.SysFont("SimHei", 16)
        except:
            self.countdown_font = pygame.font.Font(None, 16)
            
        self.recover_timer = 59 # 倒计时从59开始
        self.last_update_time = pygame.time.get_ticks()

    def has_energy(self):
        return self.current_energy > 0

    def consume(self, amount=1):
        if self.current_energy >= amount:
            self.current_energy -= amount
            return True
        return False

    def update(self):
        # 如果体力未满，进行恢复逻辑
        if self.current_energy < self.max_energy:
            current_time = pygame.time.get_ticks()
            # 检查是否过了1秒 (1000ms)
            if current_time - self.last_update_time >= 1000:
                self.recover_timer -= 1
                self.last_update_time = current_time
                
                # 倒计时结束
                if self.recover_timer < 0:
                    self.current_energy += 1
                    # 重置倒计时
                    self.recover_timer = 59
                    # 如果回满了，也可以把timer重置或者怎样，但下一次update会自动判断 < max_energy
        else:
            # 体力已满，重置计时器状态，以便下次消耗后重新开始
            self.recover_timer = 59
            self.last_update_time = pygame.time.get_ticks() # 保持更新避免突然跳变

    def draw(self, screen, anchor_rect):
        """
        Draws the energy bar above the anchor_rect (main button).
        """
        # Prepare Text
        text_str = f"{self.current_energy}/{self.max_energy}"
        text_surf = self.font.render(text_str, True, self.text_color)
        
        # Prepare Countdown Text (if needed)
        countdown_surf = None
        if self.current_energy < self.max_energy:
            count_str = f"{self.recover_timer}s"
            countdown_surf = self.countdown_font.render(count_str, True, self.text_color)
        
        # Layout dimensions
        icon_w, icon_h = 20, 20 # Fixed size
        gap = 5
        text_w, text_h = text_surf.get_size()
        
        total_w = icon_w + gap + text_w
        total_h = max(icon_h, text_h)
        
        # If countdown exists, add it to layout
        if countdown_surf:
            cd_w, cd_h = countdown_surf.get_size()
            total_w += gap + cd_w
            total_h = max(total_h, cd_h)
        
        # Calculate position for the group to be centered above anchor_rect
        group_center_x = anchor_rect.centerx
        group_bottom_y = anchor_rect.top - 5
        
        # Group Rectangle (for alignment calculation)
        start_x = group_center_x - total_w // 2
        group_rect = pygame.Rect(start_x, 0, total_w, total_h)
        group_rect.bottom = group_bottom_y
        
        # Icon Position
        self.rect.left = start_x
        self.rect.centery = group_rect.centery
        
        # Text Position
        text_rect = text_surf.get_rect()
        text_rect.left = self.rect.right + gap
        text_rect.centery = group_rect.centery
        
        # Draw
        screen.blit(self.image, self.rect)
        screen.blit(text_surf, text_rect)
        
        # Draw Countdown
        if countdown_surf:
            cd_rect = countdown_surf.get_rect()
            cd_rect.left = text_rect.right + gap
            cd_rect.centery = group_rect.centery
            screen.blit(countdown_surf, cd_rect)
