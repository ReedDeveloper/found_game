import pygame

class ScaleButton:
    def __init__(self, x, y, image_path, scale_factor=1.0, press_scale=0.9, animation_speed=0.2):
        self.original_image = pygame.image.load(image_path)
        
        # Apply initial scale_factor to get the "base" size
        base_w = int(self.original_image.get_width() * scale_factor)
        base_h = int(self.original_image.get_height() * scale_factor)
        self.base_image = pygame.transform.smoothscale(self.original_image, (base_w, base_h))
        
        self.rect = self.base_image.get_rect(topleft=(x, y))
        self.center = self.rect.center
        
        self.current_scale = 1.0
        self.target_scale = 1.0
        self.press_scale = press_scale
        self.animation_speed = animation_speed
        
        self.is_pressed = False

    def update(self):
        # Tween logic: Smoothly interpolate current_scale towards target_scale
        if abs(self.current_scale - self.target_scale) > 0.01:
            self.current_scale += (self.target_scale - self.current_scale) * self.animation_speed
        else:
            self.current_scale = self.target_scale

    def draw(self, surface):
        # Calculate size based on current dynamic scale (relative to base_image)
        # Note: self.current_scale fluctuates between 1.0 and self.press_scale
        
        if self.current_scale != 1.0:
            new_w = int(self.base_image.get_width() * self.current_scale)
            new_h = int(self.base_image.get_height() * self.current_scale)
            
            # Avoid 0 size
            new_w = max(1, new_w)
            new_h = max(1, new_h)
            
            scaled_img = pygame.transform.smoothscale(self.base_image, (new_w, new_h))
            scaled_rect = scaled_img.get_rect(center=self.center)
            surface.blit(scaled_img, scaled_rect)
        else:
            surface.blit(self.base_image, self.rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.is_pressed = True
                self.target_scale = self.press_scale
                return True
                
        elif event.type == pygame.MOUSEBUTTONUP:
            # Regardless of where we release, we restore the scale
            # But we only return "Click Action" if we released INSIDE the button
            # and we were the one who pressed it.
            if self.is_pressed:
                self.is_pressed = False
                self.target_scale = 1.0
                # If released inside, it's a valid click (but we usually trigger on DOWN for responsiveness, 
                # or UP for accuracy. Requirement says "点击以后...图片会缩小,放开又会恢复".
                # Usually actions trigger on Down or Up. 
                # Let's return True on DOWN as implemented above, or maybe simpler:
                # Just handle animation state here. The return value indicates "Action Triggered".
                
        return False
        
    def is_clicked(self, event):
        # Helper to check click specifically on DOWN for action triggering
        # while handle_event manages the animation state.
        # Actually, let's combine them.
        # If we want the action to happen on DOWN:
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                return True
        return False
