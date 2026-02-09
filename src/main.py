import pygame
import os
import sys

# Ensure local imports work regardless of run method
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir)

def get_project_root():
    if getattr(sys, 'frozen', False):
        # Running as compiled executable
        # PyInstaller 6+ with onedir: data is in _internal, sys._MEIPASS points to it?
        # Actually sys._MEIPASS points to the internal directory in onefile, but in onedir
        # it might also be set. 
        # But for onedir, usually resources are relative to executable or in _internal.
        # Let's trust sys._MEIPASS if it exists, otherwise use executable dir.
        if hasattr(sys, '_MEIPASS'):
            return sys._MEIPASS
        return os.path.dirname(sys.executable)
    else:
        # Running from source
        return os.path.dirname(current_dir)

from exp import ExpBar
from level import Level
from button import ScaleButton
from energy import Energy
from equipment import EquipmentManager
from power import Power
from attribute import AttributePanel
from stats import calculate_total_stats
from battle import Battle
from bag import Bag, BagButton

def main():
    # 初始化 pygame
    pygame.init()

    # 设置屏幕大小
    WIDTH = 1440
    HEIGHT = 810
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Immort Animation")

    # 设置背景颜色
    BLACK = (0, 0, 0)

    # 路径设置
    project_root = get_project_root()
    
    # --- Level Setup ---
    # Instantiate Level (it handles image loading)
    level_system = Level(project_root, WIDTH, HEIGHT)

    # --- Layout Constants ---
    from const import UI_SIDEBAR_X, UI_COL_WIDTH, UI_POWER_Y, UI_EXP_Y, UI_EQUIP_PANEL_Y, UI_PANEL_X, UI_PANEL_Y
    
    # --- Power System Setup ---
    # Top of the Right Sidebar
    power_system = Power(project_root, UI_SIDEBAR_X, UI_POWER_Y, UI_COL_WIDTH, 50)
    
    # --- ExpBar Setup ---
    # Below Power Bar
    exp_bar = ExpBar(UI_SIDEBAR_X, UI_EXP_Y, UI_COL_WIDTH, 30, max_exp=100)
    
    # --- Equipment Manager Setup ---
    # Below Exp Bar
    # Create a dummy rect for EquipmentManager init if it needs it, or modify EquipmentManager to take x,y
    # EquipmentManager takes exp_bar_rect to determine position. 
    # But now we want specific position UI_EQUIP_PANEL_Y.
    # Let's verify EquipmentManager.__init__ logic. 
    # It does: self.tips = EquipTips(exp_bar_rect.x, 250) ... self.panel = EquipPanel(exp_bar_rect.x, panel_y, exp_bar_rect.width)
    # We should update EquipmentManager to respect our layout or pass a rect that produces the result.
    # If we pass a rect at (UI_SIDEBAR_X, UI_EXP_Y, UI_COL_WIDTH, 30),
    # Then panel_y = rect.bottom + 10 = UI_EXP_Y + 30 + 10 = UI_EXP_Y + 40.
    # Our const UI_EQUIP_PANEL_Y = 150.
    # UI_EXP_Y = 110. 110 + 30 + 10 = 150. MATCHES PERFECTLY.
    exp_rect = pygame.Rect(UI_SIDEBAR_X, UI_EXP_Y, UI_COL_WIDTH, 30)
    equipment_manager = EquipmentManager(exp_rect)
    
    # --- Main Button Setup ---
    # Bottom of Sidebar
    btn_path = os.path.join(project_root, 'pic', 'ui', 'main_btn.png')
    if not os.path.exists(btn_path):
        print(f"Warning: Button image not found at {btn_path}")
        
    try:
        temp_img = pygame.image.load(btn_path)
        img_w, img_h = temp_img.get_size()
        max_size = 150
        scale_w = max_size / img_w
        scale_h = max_size / img_h
        final_scale = min(1.0, scale_w, scale_h)
        btn_w = int(img_w * final_scale)
        btn_h = int(img_h * final_scale)
    except Exception as e:
        print(f"Error loading button image: {e}")
        btn_w, btn_h = 100, 50
        final_scale = 1.0
        
    # Center button in sidebar
    btn_x = UI_SIDEBAR_X + (UI_COL_WIDTH - btn_w) // 2
    btn_y = HEIGHT - btn_h - 50 # 50px margin from bottom
    
    main_btn = ScaleButton(btn_x, btn_y, btn_path, scale_factor=final_scale, press_scale=0.9)
    
    # --- Bag System Setup ---
    bag_system = Bag(project_root)
    bag_btn = BagButton(main_btn.rect, project_root)

    # --- Energy System Setup ---
    # Draws relative to main_btn inside loop, so no setup change needed except init
    energy_system = Energy(project_root)
    
    # Init Power Calculation
    power_system.calculate_power(level_system.level, equipment_manager.panel.equipped_items)

    # --- Attribute Panel Setup ---
    # Uses CONST coordinates internally (Resident in Sidebar)
    attribute_panel = AttributePanel()
    # Initial Stats Update
    current_stats = calculate_total_stats(level_system.level, equipment_manager.panel.equipped_items)
    attribute_panel.update_stats(current_stats)

    # Battle State
    battle_system = None # Only exists during battle

    # 主循环
    running = True
    clock = pygame.time.Clock()
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            # --- BATTLE MODE EVENTS ---
            if battle_system:
                if battle_system.handle_event(event):
                    if battle_system.finished:
                        # Add rewards to bag
                        if battle_system.dropped_items:
                            for item_id in battle_system.dropped_items:
                                bag_system.add_item(item_id, 1)
                            print(f"Added {len(battle_system.dropped_items)} items to bag")
                            
                        battle_system = None # Exit battle
                continue # Skip other events if in battle
            
            # --- NORMAL MODE EVENTS ---
            
            # Level System Events (Battle Start)
            battle_rank = level_system.handle_event(event)
            if battle_rank is not None:
                # Start Battle
                # Get current stats
                player_stats = calculate_total_stats(level_system.level, equipment_manager.panel.equipped_items)
                battle_system = Battle(project_root, player_stats, battle_rank)
                continue

            # 按钮事件处理
            
            # Bag Button
            if bag_btn.handle_event(event):
                if bag_btn.is_clicked(event):
                     bag_system.toggle()

            # 优先处理 Equipment Manager 的事件 (Tips 按钮点击)
            if equipment_manager.handle_event(event, bag_system=bag_system, bag_btn_rect=bag_btn.rect):
                # 如果处理了装备相关事件 (装备/分解/替换)，则不再触发“修炼”
                # Update Power immediately after equip change
                power_system.calculate_power(level_system.level, equipment_manager.panel.equipped_items)
                # Update Stats
                new_stats = calculate_total_stats(level_system.level, equipment_manager.panel.equipped_items)
                attribute_panel.update_stats(new_stats)
            
            elif main_btn.handle_event(event):
                # 如果被点击 (Action Trigger)
                
                # 检查临时背包是否有装备
                if equipment_manager.has_temp_item():
                    print("Inventory Full (Temp Bag)")
                    # Do not consume energy, do not add exp
                    # DO NOT auto-clear now, let user interact with Tips buttons
                    equipment_manager.reshow_temp_tips()
                else:
                    # 检查体力
                    if energy_system.consume(1):
                        exp_bar.add_exp(10)
                        
                        # 生成装备 (Based on Level)
                        # We need current level (0-89). 
                        # Level system stores it as self.level
                        current_level = level_system.level
                        equipment_manager.generate_drop(current_level)
                        
                        # Update Power (Level might have changed? Actually level changes in update loop)
                        # Level up happens in level_system.update. 
                        # We should check power update in main loop or trigger it on level up.
                        # For now, let's recalculate power every frame or just here?
                        # Better: Recalculate power in update loop if level changed?
                        # Or just call it here assuming level might change soon? 
                        # Actually level up happens in level_system.update(exp_bar).
                        
                        print(f"Cultivated! Target Exp: {exp_bar.target_exp}, Remaining Energy: {energy_system.current_energy}")
                    else:
                        print("No Energy!")

        # Update Logic
        if battle_system:
            battle_system.update()
        else:
            exp_bar.update()
            main_btn.update()
            bag_btn.update() # Update bag button animation
            energy_system.update() # Add energy system update
            
            # Check level before update to detect level up
            old_level = level_system.level
            level_system.update(exp_bar)
            if level_system.level > old_level:
                 # Level Up! Recalculate Power
                 power_system.calculate_power(level_system.level, equipment_manager.panel.equipped_items)
                 # Update Stats
                 new_stats = calculate_total_stats(level_system.level, equipment_manager.panel.equipped_items)
                 attribute_panel.update_stats(new_stats)
                 
            equipment_manager.update() # Animation update
            power_system.update() # Power animation update
            attribute_panel.update() # Attribute animation update

        # 填充背景
        screen.fill(BLACK)

        if battle_system:
            battle_system.draw(screen)
        else:
            # 1. 绘制 Level (Background Image & Texts)
            level_system.draw(screen)
    
            # 2. 绘制按钮
            main_btn.draw(screen)
            bag_btn.draw(screen)
            
            # 3. 绘制体力 (在按钮上方)
            energy_system.draw(screen, main_btn.rect)
            
            # 3.5 绘制战力 (在经验条上方)
            power_system.draw(screen)
    
            # 4. 绘制经验条
            exp_bar.draw(screen)
            
            # 5. 绘制装备面板
            equipment_manager.draw_panel(screen)
            
            # 6. 绘制常驻属性面板
            attribute_panel.draw(screen)
            
            # 7. 绘制装备 Tips (如果有) - 浮动在左侧
            # Always call draw_tips to handle visible state internally, and to draw toasts/anims
            equipment_manager.draw_tips(screen)
            
            # 8. 绘制背包 (Z-Index Highest)
            bag_system.draw(screen)

            # 9. Animation is handled in draw_tips now, remove duplicate call
            # equipment_manager.draw_anim(screen)

        # 刷新屏幕
        pygame.display.flip()
        
        # 控制帧率
        clock.tick(60)

    # 退出 pygame
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
