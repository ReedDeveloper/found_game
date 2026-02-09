import pygame

class ExpBar:
    def __init__(self, x, y, width, height, max_exp=100):
        self.rect = pygame.Rect(x, y, width, height)
        self.max_exp = max_exp
        self.target_exp = 0
        self.current_exp = 0
        self.speed = 0.05
        self.border_radius = height // 2
        
        # Pre-render the rainbow gradient surface
        self.gradient_surface = self._create_rainbow_gradient(width, height)
        
        # Font for text
        # Try to use a font that supports Chinese, fallback to default
        try:
            self.font = pygame.font.SysFont("simhei", 20)
        except:
            self.font = pygame.font.Font(None, 20)
            
    def _create_rainbow_gradient(self, width, height):
        surface = pygame.Surface((width, height), pygame.SRCALPHA)
        colors = [
            (255, 0, 0),    # Red
            (255, 165, 0),  # Orange
            (255, 255, 0),  # Yellow
            (0, 128, 0),    # Green
            (0, 255, 255),  # Cyan
            (0, 0, 255),    # Blue
            (128, 0, 128)   # Purple
        ]
        
        section_width = width / (len(colors) - 1)
        
        for i in range(len(colors) - 1):
            start_color = colors[i]
            end_color = colors[i + 1]
            for x in range(int(section_width)):
                # Calculate interpolation factor
                t = x / section_width
                r = start_color[0] + (end_color[0] - start_color[0]) * t
                g = start_color[1] + (end_color[1] - start_color[1]) * t
                b = start_color[2] + (end_color[2] - start_color[2]) * t
                
                # Draw vertical line
                pygame.draw.line(surface, (int(r), int(g), int(b)), 
                               (int(i * section_width + x), 0), 
                               (int(i * section_width + x), height))
                               
        return surface

    def add_exp(self, amount):
        self.target_exp += amount
        if self.target_exp > self.max_exp:
            self.target_exp = self.max_exp

    def update(self):
        if self.current_exp < self.target_exp:
            self.current_exp += (self.target_exp - self.current_exp) * self.speed
            if abs(self.target_exp - self.current_exp) < 0.1:
                self.current_exp = self.target_exp

    def draw(self, screen):
        # 1. Draw background (gray/black container)
        pygame.draw.rect(screen, (50, 50, 50), self.rect, border_radius=self.border_radius)
        
        # 2. Draw filled portion (Gradient)
        if self.current_exp > 0:
            fill_width = int((self.current_exp / self.max_exp) * self.rect.width)
            if fill_width > 0:
                # Create a subsurface of the gradient based on fill width
                # We need to handle the rounded corners for the fill too
                # A simple way is to create a mask or just draw rect with border radius
                # But blitting a surface doesn't support border_radius directly.
                # Alternative: Draw the gradient surface onto a temporary surface with colorkey/alpha
                
                # Simplified approach for rounded fill:
                # Create a temp surface for the fill
                temp_surface = pygame.Surface((fill_width, self.rect.height), pygame.SRCALPHA)
                
                # Blit the relevant part of gradient
                temp_surface.blit(self.gradient_surface, (0, 0), (0, 0, fill_width, self.rect.height))
                
                # To clip it to rounded rectangle is complex in pure pygame without advanced masking
                # For now, let's just draw the rounded rect using a solid color to test, 
                # OR draw the gradient but strictly clipped.
                
                # Better approach for "Rounded Gradient Bar":
                # 1. Create a mask surface with rounded rect (white on transparent)
                # 2. Blit gradient on it using blend mode?
                # OR simpler: just draw the gradient rect and then draw the border over it? 
                # But the right edge of the fill shouldn't be rounded unless it's full?
                # Usually progress bars are rounded on left, flat on right (unless full).
                
                # Let's stick to a simpler implementation for MVP:
                # Just blit the gradient surface cropped.
                # If we really need rounded corners for the fill:
                
                # Create a master surface for the bar
                bar_surf = pygame.Surface((self.rect.width, self.rect.height), pygame.SRCALPHA)
                
                # Draw rounded rect mask (white)
                pygame.draw.rect(bar_surf, (255, 255, 255), bar_surf.get_rect(), border_radius=self.border_radius)
                
                # Create the fill content
                fill_content = pygame.Surface((self.rect.width, self.rect.height), pygame.SRCALPHA)
                fill_content.blit(self.gradient_surface, (0, 0))
                
                # Clear the part that is not filled yet
                empty_rect = pygame.Rect(fill_width, 0, self.rect.width - fill_width, self.rect.height)
                fill_content.fill((0,0,0,0), empty_rect) # Make empty part transparent
                
                # Multiply fill_content with bar_surf (mask)
                # BLEND_RGBA_MIN is useful if mask is white (255) and we want to keep color, 
                # but transparency (0) should stay transparent.
                
                bar_surf.blit(fill_content, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)
                
                screen.blit(bar_surf, self.rect.topleft)

        # 3. Draw Border
        pygame.draw.rect(screen, (200, 200, 200), self.rect, 2, border_radius=self.border_radius)

        # 4. Draw Text
        text_surf = self.font.render(f"修为 {int(self.current_exp)}/{self.max_exp}", True, (255, 255, 255))
        text_rect = text_surf.get_rect(center=self.rect.center)
        screen.blit(text_surf, text_rect)
