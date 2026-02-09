from src.const import EquipPart, Rank, AttributeType, QualityColor, BASE_STATS_CONFIG, EXT_STATS_CONFIG, EquipmentType, EQUIP_TYPE_MAP, WeaponType
import random

class EquipItem:
    def __init__(self, item_id, name, part, rank_val, equip_type, base_stats, ext_stats):
        self.item_id = item_id
        self.name = name
        self.part = part        # Enum: EquipPart
        self.rank_val = rank_val # int: 0-9
        self.equip_type = equip_type # Enum: EquipmentType
        self.base_stats = base_stats # Dict: {key: value}
        self.ext_stats = ext_stats   # Dict: {key: value}

    def to_dict(self):
        return {
            "id": self.item_id,
            "name": self.name,
            "quality": self.rank_val,
            "position": self.part,
            "type": self.equip_type,
            "base_attrs": self.base_stats,
            "extend_attrs": self.ext_stats
        }

    def __repr__(self):
        return str(self.to_dict())

def get_base_attribute_value(attr_type, rank_val):
    """
    根据属性类型和品阶计算基础数值
    """
    # 基础数值定义 (0阶数值)
    base_values = {
        AttributeType.OUTER_ATK: 20,
        AttributeType.INNER_ATK: 20,
        AttributeType.OUTER_DEF: 10,
        AttributeType.INNER_DEF: 10,
        AttributeType.HIT: 10,
        AttributeType.DODGE: 10,
        AttributeType.CRIT: 10,
        AttributeType.CRIT_DEF: 10,
        AttributeType.MAX_HP: 100
    }
    
    val = base_values.get(attr_type, 10)
    # 成长公式: 基础 * (品阶 + 1) * 1.2 (系数)
    # 例如: 0阶=24, 1阶=48, 9阶=240
    return int(val * (rank_val + 1) * 1.2)

def get_ext_attribute_value(attr_type, rank_val):
    """
    根据属性类型和品阶计算扩展数值 (通常略低于基础属性或作为补充)
    """
    # 扩展属性系数略低
    base_val = get_base_attribute_value(attr_type, rank_val)
    return int(base_val * 0.8)

def generate_equip_table():
    equip_list = []
    
    # 定义每个部位的变种数量 (普通散件)
    # 每个部位生成 6 种散件 (index 0-5)
    VARIANT_COUNT = 6
    
    # 定义套装数量 (index 100+)
    # 每个部位生成 3 套套装组件
    SET_COUNT = 3
    
    # 遍历所有品阶 (0-9)
    for rank in Rank:
        rank_val = rank.value
        # 获取该品阶的随机前缀列表
        rank_prefixes = Rank.get_prefix(rank)
        
        # 遍历所有部位 (0-11)
        for part in EquipPart:
            part_val = part.value
            part_base_name = EquipPart.get_name(part)
            
            # --- 1. 生成普通散件 (Variants) ---
            for i in range(VARIANT_COUNT):
                # ID: 1xx yy zzz
                # xx: rank (00-09)
                # yy: part (00-11)
                # zzz: variant index (000-099 reserved for normal items)
                item_id = int(f"1{rank_val:02d}{part_val:02d}{i:03d}")
                
                # 名称生成
                # 轮询前缀
                prefix = rank_prefixes[i % len(rank_prefixes)]
                
                # 如果是武器，根据 index 映射到不同武器类型
                if part == EquipPart.WEAPON:
                    w_types = list(WeaponType)
                    w_type = w_types[i % len(w_types)]
                    w_name = WeaponType.get_name(w_type)
                    name = f"{prefix}{w_name}"
                else:
                    # 对于非武器，也可以加一些修饰词增加变化，这里简单处理，或者用 ABCD 变体
                    # 为了区分不同变体，可以使用更丰富的前缀库，或者后缀
                    # 这里复用 prefix，如果是同一个前缀，加个数字后缀区分?
                    # 或者简单点：前缀 + 部位
                    # 为了让6个变体名字不同，我们假设 rank_prefixes 只有3个
                    # 我们可以加一些后缀如 "·改", "·真" 等，或者循环使用
                    suffix = ""
                    if i >= len(rank_prefixes):
                        suffix = ["·改", "·真", "·灵"][i % 3]
                    name = f"{prefix}{part_base_name}{suffix}"

                # 获取装备类型
                equip_type = EQUIP_TYPE_MAP.get(part, EquipmentType.OFFENSIVE)
                
                # 基础属性
                base_stats = {}
                for attr in BASE_STATS_CONFIG.get(part, []):
                    val = get_base_attribute_value(attr, rank_val)
                    # 散件属性小幅浮动 (95% - 105%)
                    val = int(val * random.uniform(0.95, 1.05))
                    base_stats[attr.key] = base_stats.get(attr.key, 0) + val
                    
                # 扩展属性
                ext_stats = {}
                for attr in EXT_STATS_CONFIG.get(part, []):
                    val = get_ext_attribute_value(attr, rank_val)
                    val = int(val * random.uniform(0.95, 1.05))
                    ext_stats[attr.key] = ext_stats.get(attr.key, 0) + val
                
                item = EquipItem(item_id, name, part, rank_val, equip_type, base_stats, ext_stats)
                equip_list.append(item.to_dict())

            # --- 2. 生成套装组件 (Sets) ---
            # 套装 ID 从 100 开始
            for s in range(SET_COUNT):
                set_index = 100 + s
                item_id = int(f"1{rank_val:02d}{part_val:02d}{set_index:03d}")
                
                # 套装名称
                set_names = ["青龙", "白虎", "朱雀"] # 示例套装名
                set_name_prefix = set_names[s % len(set_names)]
                
                if part == EquipPart.WEAPON:
                    # 套装武器固定一种类型? 或者随机? 这里固定用剑/刀/弓
                    w_type = list(WeaponType)[s % len(WeaponType)]
                    w_name = WeaponType.get_name(w_type)
                    name = f"{Rank.get_name(rank)}·{set_name_prefix}{w_name}"
                else:
                    name = f"{Rank.get_name(rank)}·{set_name_prefix}{part_base_name}"
                
                equip_type = EQUIP_TYPE_MAP.get(part, EquipmentType.OFFENSIVE)
                
                # 套装属性 (通常比散件高 10%)
                base_stats = {}
                for attr in BASE_STATS_CONFIG.get(part, []):
                    val = get_base_attribute_value(attr, rank_val)
                    val = int(val * 1.1)
                    base_stats[attr.key] = base_stats.get(attr.key, 0) + val
                    
                ext_stats = {}
                for attr in EXT_STATS_CONFIG.get(part, []):
                    val = get_ext_attribute_value(attr, rank_val)
                    val = int(val * 1.1)
                    ext_stats[attr.key] = ext_stats.get(attr.key, 0) + val
                
                # 套装额外属性 (1条)
                # 随机选一个非基础非扩展的属性? 或者直接加血/攻
                extra_attr = AttributeType.MAX_HP
                extra_val = get_ext_attribute_value(extra_attr, rank_val)
                ext_stats[extra_attr.key] = ext_stats.get(extra_attr.key, 0) + extra_val
                
                item = EquipItem(item_id, name, part, rank_val, equip_type, base_stats, ext_stats)
                # 标记为套装? 这里结构体没定义 set_id，暂不处理，通过 ID 区分
                equip_list.append(item.to_dict())
            
    return equip_list

if __name__ == "__main__":
    import json
    import os
    
    # 生成数据
    table = generate_equip_table()
    print(f"Generated {len(table)} items.")

    # 准备写入的内容
    # 为了让生成的 Python 文件可读且可被导入，我们需要处理 Enum 的输出
    # 因为直接 json.dump 会把 Enum 变成字符串或报错，或者我们需要自定义 encoder
    # 但这里目标是生成一个 .py 文件，其中包含一个 list 变量
    
    # 我们手动构建字符串
    output_lines = []
    output_lines.append("from src.const import EquipPart, EquipmentType")
    output_lines.append("")
    output_lines.append("EQUIP_CFG = [")
    
    for item in table:
        output_lines.append("    {")
        output_lines.append(f"        'id': {item['id']},")
        output_lines.append(f"        'name': '{item['name']}',")
        output_lines.append(f"        'quality': {item['quality']},")
        output_lines.append(f"        'position': {item['position']},")
        output_lines.append(f"        'type': {item['type']},")
        output_lines.append(f"        'base_attrs': {item['base_attrs']},")
        output_lines.append(f"        'extend_attrs': {item['extend_attrs']}")
        output_lines.append("    },")
        
    output_lines.append("]")
    
    # 写入文件
    file_path = os.path.join(os.path.dirname(__file__), "equip_cfg.py")
    with open(file_path, "w", encoding="utf-8") as f:
        f.write("\n".join(output_lines))
        
    print(f"Successfully generated equip_cfg.py at {file_path}")
