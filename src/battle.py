
import pygame
import os
import random
import math

try:
    from src.monster_cfg import MONSTER_CFG
    from src.drop_cfg import DROP_CFG
    from src.item_cfg import ITEM_CFG
    from src.const import SCREEN_WIDTH, SCREEN_HEIGHT
except ImportError:
    from monster_cfg import MONSTER_CFG
    from drop_cfg import DROP_CFG
    from item_cfg import ITEM_CFG
    from const import SCREEN_WIDTH, SCREEN_HEIGHT

class Battle:
    def __init__(self, project_root, player_stats, rank_level):
        self.project_root = project_root
        self.player_stats = player_stats
        self.rank_level = rank_level
        self.finished = False
        self.dropped_items = [] # List of item_id
        
        # Determine Monster
        monster_id = 20000 + rank_level
        self.monster_data = next((m for m in MONSTER_CFG if m['id'] == monster_id), MONSTER_CFG[0])
        
        # Drop Config
        self.drop_config = DROP_CFG.get(monster_id)
        
        # Load Images
        self.bg_img = self._load_bg(rank_level)
        # Normalize height to 300px for consistency
        self.player_img = self._load_img('pic/ui/battlerole.png', target_height=300)
        self.monster_img = self._load_img(self.monster_data['image'], target_height=300)
        
        # Battle Entities
        self.player = {
            'hp': player_stats.get('hp', 100),
            'max_hp': player_stats.get('hp', 100),
            'x': 200,
            # Align bottom to ground (approx y=600 for ground level in 1440x810, usually bottom third)
            # If img height is 300, y=400 puts bottom at 700. Seems okay.
            'y': 400,
            'start_x': 200,
            'img': self.player_img,
            'stats': player_stats
        }
        
        monster_stats = self.monster_data['attributes']
        self.monster = {
            'hp': monster_stats.get('hp', 100),
            'max_hp': monster_stats.get('hp', 100),
            'x': 1000,
            'y': 400,
            'start_x': 1000,
            'img': self.monster_img,
            'stats': monster_stats
        }
        
        # State Machine
        self.state = 'WAITING' # WAITING, PLAYER_MOVE, PLAYER_RETURN, ENEMY_MOVE, ENEMY_RETURN, WIN, LOSE
        self.state_timer = 0
        self.turn_delay = 1000 # ms
        
        # Fonts
        self.font = pygame.font.SysFont("simhei", 24)
        
    def _load_bg(self, rank):
        # 0-8. png
        rank = min(rank, 8)
        path = os.path.join(self.project_root, 'pic', 'ui', 'battlescn', f'{rank}.png')
        if os.path.exists(path):
            img = pygame.image.load(path)
            return pygame.transform.smoothscale(img, (SCREEN_WIDTH, SCREEN_HEIGHT))
        return pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))

    def _load_img(self, rel_path, target_height=None):
        path = os.path.join(self.project_root, rel_path)
        if os.path.exists(path):
            img = pygame.image.load(path)
            w, h = img.get_size()
            
            if target_height:
                scale = target_height / h
                new_w = int(w * scale)
                img = pygame.transform.smoothscale(img, (new_w, target_height))
            
            return img
        return pygame.Surface((100, 100))

    def handle_event(self, event):
        if self.state in ['WIN', 'LOSE']:
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.finished = True
                return True
        return False

    def calculate_damage(self, attacker_stats, defender_stats):
        # Hit Check
        hit = attacker_stats.get('hit', 0)
        dodge = defender_stats.get('dodge', 0)
        
        # Simple formula: Chance = 1 - (dodge / (dodge + hit*2))
        # If dodge is high, hit chance lowers.
        # Ensure minimum hit chance 20%
        hit_chance = 1.0
        if dodge > 0:
            hit_chance = 1.0 - (dodge / (dodge + hit * 2 + 1))
        
        if random.random() > hit_chance:
            return 0, "Miss"
            
        # Damage
        atk = attacker_stats.get('outer_attack', 0) + attacker_stats.get('inner_attack', 0)
        defn = defender_stats.get('outer_defense', 0) + defender_stats.get('inner_defense', 0)
        
        dmg = max(1, atk - defn)
        
        # Crit Check
        crit = attacker_stats.get('crit', 0)
        crit_def = defender_stats.get('crit_defense', 0)
        crit_chance = crit / (crit + crit_def * 2 + 100)
        
        is_crit = False
        if random.random() < crit_chance:
            dmg = int(dmg * 1.5)
            is_crit = True
            
        return dmg, "Crit" if is_crit else "Hit"

    def tween_move(self, entity, target_x, duration_ms):
        # Simple linear for now, or ease out
        # We handle movement in update per frame
        # Store animation target
        entity['target_x'] = target_x
        entity['anim_duration'] = duration_ms
        entity['anim_start_time'] = pygame.time.get_ticks()
        entity['start_x_anim'] = entity['x']

    def update(self):
        current_time = pygame.time.get_ticks()
        
        if self.state == 'WAITING':
            if current_time - self.state_timer > self.turn_delay:
                # Start Player Turn
                self.state = 'PLAYER_MOVE'
                self.tween_move(self.player, self.monster['x'] - 150, 400) # Stop before collision
                
        elif self.state == 'PLAYER_MOVE':
            self._process_movement(self.player, 'PLAYER_ATTACK')
            
        elif self.state == 'PLAYER_ATTACK':
            # Deal Damage
            dmg, type = self.calculate_damage(self.player['stats'], self.monster['stats'])
            self.monster['hp'] -= dmg
            print(f"Player hit Monster: {dmg} ({type})")
            
            if self.monster['hp'] <= 0:
                self.monster['hp'] = 0
                self.state = 'WIN'
                self._calculate_drops() # Calculate drops on win
            else:
                self.state = 'PLAYER_RETURN'
                self.tween_move(self.player, self.player['start_x'], 400)
                
        elif self.state == 'PLAYER_RETURN':
            self._process_movement(self.player, 'ENEMY_MOVE')
            
        elif self.state == 'ENEMY_MOVE':
            self.tween_move(self.monster, self.player['x'] + 150, 400)
            self.state = 'ENEMY_MOVING' # Helper state to avoid re-trigger
            
        elif self.state == 'ENEMY_MOVING':
            self._process_movement(self.monster, 'ENEMY_ATTACK')
            
        elif self.state == 'ENEMY_ATTACK':
            dmg, type = self.calculate_damage(self.monster['stats'], self.player['stats'])
            self.player['hp'] -= dmg
            print(f"Monster hit Player: {dmg} ({type})")
            
            if self.player['hp'] <= 0:
                self.player['hp'] = 0
                self.state = 'LOSE'
            else:
                self.state = 'ENEMY_RETURN'
                self.tween_move(self.monster, self.monster['start_x'], 400)
                
        elif self.state == 'ENEMY_RETURN':
            self._process_movement(self.monster, 'WAITING')
            if self.state == 'WAITING':
                self.state_timer = current_time # Reset timer for next turn

    def _calculate_drops(self):
        if not self.drop_config:
            return
            
        cultivation_level = self.monster_data.get('cultivation_level', 0)
        drop_times = cultivation_level // 2 + 1
        
        weights = self.drop_config['drop_p']
        items = self.drop_config['drop_items']
        
        for _ in range(drop_times):
            # Weighted Choice
            # random.choices returns a list
            chosen_item = random.choices(items, weights=weights, k=1)[0]
            if chosen_item != 0:
                self.dropped_items.append(chosen_item)
                print(f"Battle Drop: {chosen_item}")

    def _process_movement(self, entity, next_state):
        current_time = pygame.time.get_ticks()
        elapsed = current_time - entity['anim_start_time']
        duration = entity['anim_duration']
        
        if elapsed >= duration:
            entity['x'] = entity['target_x']
            self.state = next_state
        else:
            # Ease Out Cubic: 1 - pow(1 - t, 3)
            t = elapsed / duration
            ease = 1 - pow(1 - t, 3)
            
            start = entity['start_x_anim']
            target = entity['target_x']
            entity['x'] = start + (target - start) * ease

    def draw(self, screen):
        screen.blit(self.bg_img, (0, 0))
        
        # Draw Player
        screen.blit(self.player['img'], (self.player['x'], self.player['y']))
        self._draw_hp_bar(screen, self.player['x'], self.player['y'] - 20, self.player['hp'], self.player['max_hp'], (0, 255, 0))
        
        # Draw Monster
        screen.blit(self.monster['img'], (self.monster['x'], self.monster['y']))
        self._draw_hp_bar(screen, self.monster['x'], self.monster['y'] - 20, self.monster['hp'], self.monster['max_hp'], (255, 0, 0))
        
        # Draw Result
        if self.state == 'WIN':
            self._draw_result(screen, "win.png")
        elif self.state == 'LOSE':
            self._draw_result(screen, "lose.png")

    def _draw_hp_bar(self, screen, x, y, current, max_val, color):
        width = 100
        height = 10
        ratio = current / max_val
        pygame.draw.rect(screen, (50, 50, 50), (x, y, width, height))
        pygame.draw.rect(screen, color, (x, y, int(width * ratio), height))
        pygame.draw.rect(screen, (255, 255, 255), (x, y, width, height), 1)

    def _draw_result(self, screen, img_name):
        path = os.path.join(self.project_root, 'pic', 'ui', img_name)
        if os.path.exists(path):
            img = pygame.image.load(path)
            # Scale to width 300px
            w, h = img.get_size()
            target_w = 300
            scale = target_w / w
            new_h = int(h * scale)
            img = pygame.transform.smoothscale(img, (target_w, new_h))
            
            # Move up 150px
            center_y = SCREEN_HEIGHT // 2 - 150
            rect = img.get_rect(center=(SCREEN_WIDTH//2, center_y))
            screen.blit(img, rect)
            
            # Draw Drops if WIN
            if img_name == "win.png" and self.dropped_items:
                # Group drops
                drop_counts = {}
                for item_id in self.dropped_items:
                    drop_counts[item_id] = drop_counts.get(item_id, 0) + 1
                
                # Draw icons below victory image
                start_y = rect.bottom + 20
                icon_size = 60
                gap = 20
                total_w = len(drop_counts) * icon_size + (len(drop_counts) - 1) * gap
                start_x = (SCREEN_WIDTH - total_w) // 2
                
                idx = 0
                for item_id, count in drop_counts.items():
                    # Load Icon from ITEM_CFG
                    item_data = ITEM_CFG.get(item_id)
                    if item_data:
                        icon_path = os.path.join(self.project_root, item_data['image'])
                        if os.path.exists(icon_path):
                            icon = pygame.image.load(icon_path)
                            icon = pygame.transform.smoothscale(icon, (icon_size, icon_size))
                            
                            x = start_x + idx * (icon_size + gap)
                            screen.blit(icon, (x, start_y))
                            
                            # Draw Count
                            if count > 1:
                                cnt_surf = self.font.render(str(count), True, (255, 255, 255))
                                cnt_rect = cnt_surf.get_rect(bottomright=(x + icon_size, start_y + icon_size))
                                # Bg for text
                                bg_r = cnt_rect.copy()
                                bg_r.inflate_ip(4, 2)
                                pygame.draw.rect(screen, (0,0,0,150), bg_r)
                                screen.blit(cnt_surf, cnt_rect)
                    idx += 1
            
            # Draw "Click to exit" text
            # Position below drops or image
            text_y = rect.bottom + 100 if (img_name == "win.png" and self.dropped_items) else rect.bottom + 30
            text = self.font.render("点击鼠标退出", True, (255, 255, 255))
            tr = text.get_rect(center=(SCREEN_WIDTH//2, text_y))
            screen.blit(text, tr)
