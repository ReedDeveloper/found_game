
import random
import sys
import os

# Ensure we can import const
sys.path.append(os.getcwd())

try:
    from src.const import Rank, POWER_WEIGHTS
except ImportError:
    # If running directly from src
    sys.path.append(os.path.dirname(os.getcwd()))
    from src.const import Rank, POWER_WEIGHTS

def calculate_power(attrs):
    total = 0
    for key, val in attrs.items():
        weight = POWER_WEIGHTS.get(key, 1.0)
        total += val * weight
    return int(total)

def generate_monsters():
    monsters = []
    
    # Base Stats for Rank 0 (LianQi)
    base_stats = {
        'hp': 3000,
        'outer_attack': 100,
        'inner_attack': 100,
        'outer_defense': 50,
        'inner_defense': 50,
        'hit': 20,
        'dodge': 20,
        'crit': 20,
        'crit_defense': 20
    }
    
    # Growth factors per rank
    # Power usually grows exponentially
    GROWTH = 1.6
    
    for i in range(13):
        # Determine Cultivation Rank
        if i < 10:
            rank_idx = i
            rank_name = Rank.get_name(Rank(i))
            name = f"{rank_name}妖兽"
        else:
            rank_idx = 9 # Cap at JinXian for base, but stats keep growing
            rank_name = Rank.get_name(Rank(9))
            suffixes = ["妖王", "妖皇", "魔神"]
            name = f"{rank_name}{suffixes[i-10]}"
            
        # Calculate Stats
        # Scale = GROWTH ^ i
        scale = pow(GROWTH, i)
        
        # Add some randomness (0.9 - 1.1)
        # But keeping it deterministic for the table is better, or fixed seed.
        # Let's just use fixed scale for the table.
        
        attrs = {}
        for k, v in base_stats.items():
            attrs[k] = int(v * scale)
            
        # Image Path
        # %d from 0 to 9.
        # For 10, 11, 12, user said "0-9 images".
        # We can reuse 7, 8, 9 or loop.
        img_idx = i % 10
        img_path = f"pic/ui/battlemonster/{img_idx}.png"
        
        monster = {
            'id': 20000 + i,
            'name': name,
            'cultivation_level': rank_idx,
            'image': img_path,
            'attributes': attrs,
            'power': calculate_power(attrs)
        }
        monsters.append(monster)
        
    return monsters

def write_cfg(monsters):
    content = "MONSTER_CFG = [\n"
    for m in monsters:
        content += "    {\n"
        content += f"        'id': {m['id']},\n"
        content += f"        'name': '{m['name']}',\n"
        content += f"        'cultivation_level': {m['cultivation_level']},\n"
        content += f"        'image': '{m['image']}',\n"
        content += f"        'attributes': {m['attributes']},\n"
        content += f"        'power': {m['power']}\n"
        content += "    },\n"
    content += "]\n"
    
    with open('src/monster_cfg.py', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Generated src/monster_cfg.py")

if __name__ == "__main__":
    monsters = generate_monsters()
    write_cfg(monsters)
