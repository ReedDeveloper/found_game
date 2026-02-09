
try:
    from src.const import AttributeType, BASE_STATS_CONFIG, EXT_STATS_CONFIG
except ImportError:
    from const import AttributeType, BASE_STATS_CONFIG, EXT_STATS_CONFIG

def calculate_total_stats(level, equipment_dict):
    """
    Calculate total stats based on level and equipment.
    Returns a dict {AttributeType.key: value}
    """
    # Initialize with 0
    stats = {attr.key: 0 for attr in AttributeType}
    
    # 1. Base Stats from Level (Optional, currently user didn't specify base stats from level, 
    # but usually HP grows with level. Let's assume some base HP?)
    # User said: "第一排显示血上限(例如血上限200,红色字)"
    # Let's give a base HP of 100 + level * 10?
    # User prompt doesn't specify base stats formula, only that attributes come from equipment.
    # But for a game, level usually gives stats.
    # "等级从0开始,升级就是值加一...大级对应的是修仙等级"
    # Previous prompt mentions "Level power weight = 10".
    # Let's just sum equipment stats for now, and maybe add a small base HP so it's not 0.
    stats['hp'] = 100 + level * 10
    
    # 2. Equipment Stats
    for part, item in equipment_dict.items():
        # Base Attrs
        for key, val in item.get('base_attrs', {}).items():
            stats[key] = stats.get(key, 0) + val
            
        # Extend Attrs
        for key, val in item.get('extend_attrs', {}).items():
            stats[key] = stats.get(key, 0) + val
            
    return stats
