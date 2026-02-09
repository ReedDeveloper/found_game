try:
    from src.const import EquipPart, EquipmentType
except ImportError:
    from const import EquipPart, EquipmentType

EQUIP_CFG = [
    {
        'id': 10000000,
        'name': '炼气剑',
        'quality': 0,
        'position': EquipPart.WEAPON,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'inner_attack': 24, 'outer_attack': 23},
        'extend_attrs': {'hp': 91, 'hit': 8, 'crit': 8}
    },
    {
        'id': 10000001,
        'name': '聚气刀',
        'quality': 0,
        'position': EquipPart.WEAPON,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'inner_attack': 25, 'outer_attack': 23},
        'extend_attrs': {'hp': 93, 'hit': 9, 'crit': 9}
    },
    {
        'id': 10000002,
        'name': '纳灵弓',
        'quality': 0,
        'position': EquipPart.WEAPON,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'inner_attack': 23, 'outer_attack': 24},
        'extend_attrs': {'hp': 96, 'hit': 8, 'crit': 9}
    },
    {
        'id': 10000003,
        'name': '炼气弩',
        'quality': 0,
        'position': EquipPart.WEAPON,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'inner_attack': 23, 'outer_attack': 24},
        'extend_attrs': {'hp': 96, 'hit': 8, 'crit': 8}
    },
    {
        'id': 10000004,
        'name': '聚气枪',
        'quality': 0,
        'position': EquipPart.WEAPON,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'inner_attack': 23, 'outer_attack': 23},
        'extend_attrs': {'hp': 98, 'hit': 8, 'crit': 9}
    },
    {
        'id': 10000005,
        'name': '纳灵棍',
        'quality': 0,
        'position': EquipPart.WEAPON,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'inner_attack': 25, 'outer_attack': 22},
        'extend_attrs': {'hp': 93, 'hit': 9, 'crit': 8}
    },
    {
        'id': 10000100,
        'name': '炼气·青龙剑',
        'quality': 0,
        'position': EquipPart.WEAPON,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'inner_attack': 26, 'outer_attack': 26},
        'extend_attrs': {'hp': 201, 'hit': 9, 'crit': 9}
    },
    {
        'id': 10000101,
        'name': '炼气·白虎刀',
        'quality': 0,
        'position': EquipPart.WEAPON,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'inner_attack': 26, 'outer_attack': 26},
        'extend_attrs': {'hp': 201, 'hit': 9, 'crit': 9}
    },
    {
        'id': 10000102,
        'name': '炼气·朱雀弓',
        'quality': 0,
        'position': EquipPart.WEAPON,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'inner_attack': 26, 'outer_attack': 26},
        'extend_attrs': {'hp': 201, 'hit': 9, 'crit': 9}
    },
    {
        'id': 10001000,
        'name': '炼气护腕',
        'quality': 0,
        'position': EquipPart.BRACER,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'hit': 11},
        'extend_attrs': {'outer_attack': 19, 'inner_attack': 19}
    },
    {
        'id': 10001001,
        'name': '聚气护腕',
        'quality': 0,
        'position': EquipPart.BRACER,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'hit': 12},
        'extend_attrs': {'outer_attack': 19, 'inner_attack': 19}
    },
    {
        'id': 10001002,
        'name': '纳灵护腕',
        'quality': 0,
        'position': EquipPart.BRACER,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'hit': 11},
        'extend_attrs': {'outer_attack': 18, 'inner_attack': 18}
    },
    {
        'id': 10001003,
        'name': '炼气护腕·改',
        'quality': 0,
        'position': EquipPart.BRACER,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'hit': 11},
        'extend_attrs': {'outer_attack': 18, 'inner_attack': 19}
    },
    {
        'id': 10001004,
        'name': '聚气护腕·真',
        'quality': 0,
        'position': EquipPart.BRACER,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'hit': 12},
        'extend_attrs': {'outer_attack': 18, 'inner_attack': 18}
    },
    {
        'id': 10001005,
        'name': '纳灵护腕·灵',
        'quality': 0,
        'position': EquipPart.BRACER,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'hit': 12},
        'extend_attrs': {'outer_attack': 19, 'inner_attack': 19}
    },
    {
        'id': 10001100,
        'name': '炼气·青龙护腕',
        'quality': 0,
        'position': EquipPart.BRACER,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'hit': 13},
        'extend_attrs': {'outer_attack': 20, 'inner_attack': 20, 'hp': 96}
    },
    {
        'id': 10001101,
        'name': '炼气·白虎护腕',
        'quality': 0,
        'position': EquipPart.BRACER,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'hit': 13},
        'extend_attrs': {'outer_attack': 20, 'inner_attack': 20, 'hp': 96}
    },
    {
        'id': 10001102,
        'name': '炼气·朱雀护腕',
        'quality': 0,
        'position': EquipPart.BRACER,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'hit': 13},
        'extend_attrs': {'outer_attack': 20, 'inner_attack': 20, 'hp': 96}
    },
    {
        'id': 10002000,
        'name': '炼气戒指',
        'quality': 0,
        'position': EquipPart.RING,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'inner_attack': 23},
        'extend_attrs': {'hit': 9, 'crit': 9}
    },
    {
        'id': 10002001,
        'name': '聚气戒指',
        'quality': 0,
        'position': EquipPart.RING,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'inner_attack': 23},
        'extend_attrs': {'hit': 8, 'crit': 8}
    },
    {
        'id': 10002002,
        'name': '纳灵戒指',
        'quality': 0,
        'position': EquipPart.RING,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'inner_attack': 23},
        'extend_attrs': {'hit': 9, 'crit': 9}
    },
    {
        'id': 10002003,
        'name': '炼气戒指·改',
        'quality': 0,
        'position': EquipPart.RING,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'inner_attack': 23},
        'extend_attrs': {'hit': 8, 'crit': 8}
    },
    {
        'id': 10002004,
        'name': '聚气戒指·真',
        'quality': 0,
        'position': EquipPart.RING,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'inner_attack': 24},
        'extend_attrs': {'hit': 9, 'crit': 8}
    },
    {
        'id': 10002005,
        'name': '纳灵戒指·灵',
        'quality': 0,
        'position': EquipPart.RING,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'inner_attack': 24},
        'extend_attrs': {'hit': 8, 'crit': 8}
    },
    {
        'id': 10002100,
        'name': '炼气·青龙戒指',
        'quality': 0,
        'position': EquipPart.RING,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'inner_attack': 26},
        'extend_attrs': {'hit': 9, 'crit': 9, 'hp': 96}
    },
    {
        'id': 10002101,
        'name': '炼气·白虎戒指',
        'quality': 0,
        'position': EquipPart.RING,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'inner_attack': 26},
        'extend_attrs': {'hit': 9, 'crit': 9, 'hp': 96}
    },
    {
        'id': 10002102,
        'name': '炼气·朱雀戒指',
        'quality': 0,
        'position': EquipPart.RING,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'inner_attack': 26},
        'extend_attrs': {'hit': 9, 'crit': 9, 'hp': 96}
    },
    {
        'id': 10003000,
        'name': '炼气护符',
        'quality': 0,
        'position': EquipPart.AMULET,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'outer_attack': 23},
        'extend_attrs': {'hit': 9, 'crit': 9}
    },
    {
        'id': 10003001,
        'name': '聚气护符',
        'quality': 0,
        'position': EquipPart.AMULET,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'outer_attack': 25},
        'extend_attrs': {'hit': 8, 'crit': 9}
    },
    {
        'id': 10003002,
        'name': '纳灵护符',
        'quality': 0,
        'position': EquipPart.AMULET,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'outer_attack': 23},
        'extend_attrs': {'hit': 9, 'crit': 8}
    },
    {
        'id': 10003003,
        'name': '炼气护符·改',
        'quality': 0,
        'position': EquipPart.AMULET,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'outer_attack': 24},
        'extend_attrs': {'hit': 8, 'crit': 8}
    },
    {
        'id': 10003004,
        'name': '聚气护符·真',
        'quality': 0,
        'position': EquipPart.AMULET,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'outer_attack': 24},
        'extend_attrs': {'hit': 8, 'crit': 8}
    },
    {
        'id': 10003005,
        'name': '纳灵护符·灵',
        'quality': 0,
        'position': EquipPart.AMULET,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'outer_attack': 23},
        'extend_attrs': {'hit': 8, 'crit': 9}
    },
    {
        'id': 10003100,
        'name': '炼气·青龙护符',
        'quality': 0,
        'position': EquipPart.AMULET,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'outer_attack': 26},
        'extend_attrs': {'hit': 9, 'crit': 9, 'hp': 96}
    },
    {
        'id': 10003101,
        'name': '炼气·白虎护符',
        'quality': 0,
        'position': EquipPart.AMULET,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'outer_attack': 26},
        'extend_attrs': {'hit': 9, 'crit': 9, 'hp': 96}
    },
    {
        'id': 10003102,
        'name': '炼气·朱雀护符',
        'quality': 0,
        'position': EquipPart.AMULET,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'outer_attack': 26},
        'extend_attrs': {'hit': 9, 'crit': 9, 'hp': 96}
    },
    {
        'id': 10004000,
        'name': '炼气头盔',
        'quality': 0,
        'position': EquipPart.HELMET,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 12, 'outer_defense': 11},
        'extend_attrs': {'inner_defense': 8, 'outer_defense': 9}
    },
    {
        'id': 10004001,
        'name': '聚气头盔',
        'quality': 0,
        'position': EquipPart.HELMET,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 12, 'outer_defense': 12},
        'extend_attrs': {'inner_defense': 9, 'outer_defense': 8}
    },
    {
        'id': 10004002,
        'name': '纳灵头盔',
        'quality': 0,
        'position': EquipPart.HELMET,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 11, 'outer_defense': 11},
        'extend_attrs': {'inner_defense': 8, 'outer_defense': 8}
    },
    {
        'id': 10004003,
        'name': '炼气头盔·改',
        'quality': 0,
        'position': EquipPart.HELMET,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 11, 'outer_defense': 12},
        'extend_attrs': {'inner_defense': 9, 'outer_defense': 8}
    },
    {
        'id': 10004004,
        'name': '聚气头盔·真',
        'quality': 0,
        'position': EquipPart.HELMET,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 12, 'outer_defense': 12},
        'extend_attrs': {'inner_defense': 8, 'outer_defense': 9}
    },
    {
        'id': 10004005,
        'name': '纳灵头盔·灵',
        'quality': 0,
        'position': EquipPart.HELMET,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 11, 'outer_defense': 11},
        'extend_attrs': {'inner_defense': 9, 'outer_defense': 8}
    },
    {
        'id': 10004100,
        'name': '炼气·青龙头盔',
        'quality': 0,
        'position': EquipPart.HELMET,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 13, 'outer_defense': 13},
        'extend_attrs': {'inner_defense': 9, 'outer_defense': 9, 'hp': 96}
    },
    {
        'id': 10004101,
        'name': '炼气·白虎头盔',
        'quality': 0,
        'position': EquipPart.HELMET,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 13, 'outer_defense': 13},
        'extend_attrs': {'inner_defense': 9, 'outer_defense': 9, 'hp': 96}
    },
    {
        'id': 10004102,
        'name': '炼气·朱雀头盔',
        'quality': 0,
        'position': EquipPart.HELMET,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 13, 'outer_defense': 13},
        'extend_attrs': {'inner_defense': 9, 'outer_defense': 9, 'hp': 96}
    },
    {
        'id': 10005000,
        'name': '炼气甲胄',
        'quality': 0,
        'position': EquipPart.ARMOR,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 12, 'outer_defense': 12},
        'extend_attrs': {'inner_defense': 9, 'outer_defense': 9}
    },
    {
        'id': 10005001,
        'name': '聚气甲胄',
        'quality': 0,
        'position': EquipPart.ARMOR,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 12, 'outer_defense': 12},
        'extend_attrs': {'inner_defense': 9, 'outer_defense': 8}
    },
    {
        'id': 10005002,
        'name': '纳灵甲胄',
        'quality': 0,
        'position': EquipPart.ARMOR,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 12, 'outer_defense': 11},
        'extend_attrs': {'inner_defense': 9, 'outer_defense': 9}
    },
    {
        'id': 10005003,
        'name': '炼气甲胄·改',
        'quality': 0,
        'position': EquipPart.ARMOR,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 12, 'outer_defense': 11},
        'extend_attrs': {'inner_defense': 9, 'outer_defense': 9}
    },
    {
        'id': 10005004,
        'name': '聚气甲胄·真',
        'quality': 0,
        'position': EquipPart.ARMOR,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 12, 'outer_defense': 11},
        'extend_attrs': {'inner_defense': 9, 'outer_defense': 9}
    },
    {
        'id': 10005005,
        'name': '纳灵甲胄·灵',
        'quality': 0,
        'position': EquipPart.ARMOR,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 11, 'outer_defense': 12},
        'extend_attrs': {'inner_defense': 8, 'outer_defense': 8}
    },
    {
        'id': 10005100,
        'name': '炼气·青龙甲胄',
        'quality': 0,
        'position': EquipPart.ARMOR,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 13, 'outer_defense': 13},
        'extend_attrs': {'inner_defense': 9, 'outer_defense': 9, 'hp': 96}
    },
    {
        'id': 10005101,
        'name': '炼气·白虎甲胄',
        'quality': 0,
        'position': EquipPart.ARMOR,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 13, 'outer_defense': 13},
        'extend_attrs': {'inner_defense': 9, 'outer_defense': 9, 'hp': 96}
    },
    {
        'id': 10005102,
        'name': '炼气·朱雀甲胄',
        'quality': 0,
        'position': EquipPart.ARMOR,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 13, 'outer_defense': 13},
        'extend_attrs': {'inner_defense': 9, 'outer_defense': 9, 'hp': 96}
    },
    {
        'id': 10006000,
        'name': '炼气腰带',
        'quality': 0,
        'position': EquipPart.BELT,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'dodge': 12},
        'extend_attrs': {'crit_defense': 8}
    },
    {
        'id': 10006001,
        'name': '聚气腰带',
        'quality': 0,
        'position': EquipPart.BELT,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'dodge': 12},
        'extend_attrs': {'crit_defense': 9}
    },
    {
        'id': 10006002,
        'name': '纳灵腰带',
        'quality': 0,
        'position': EquipPart.BELT,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'dodge': 12},
        'extend_attrs': {'crit_defense': 8}
    },
    {
        'id': 10006003,
        'name': '炼气腰带·改',
        'quality': 0,
        'position': EquipPart.BELT,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'dodge': 11},
        'extend_attrs': {'crit_defense': 9}
    },
    {
        'id': 10006004,
        'name': '聚气腰带·真',
        'quality': 0,
        'position': EquipPart.BELT,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'dodge': 11},
        'extend_attrs': {'crit_defense': 8}
    },
    {
        'id': 10006005,
        'name': '纳灵腰带·灵',
        'quality': 0,
        'position': EquipPart.BELT,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'dodge': 11},
        'extend_attrs': {'crit_defense': 8}
    },
    {
        'id': 10006100,
        'name': '炼气·青龙腰带',
        'quality': 0,
        'position': EquipPart.BELT,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'dodge': 13},
        'extend_attrs': {'crit_defense': 9, 'hp': 96}
    },
    {
        'id': 10006101,
        'name': '炼气·白虎腰带',
        'quality': 0,
        'position': EquipPart.BELT,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'dodge': 13},
        'extend_attrs': {'crit_defense': 9, 'hp': 96}
    },
    {
        'id': 10006102,
        'name': '炼气·朱雀腰带',
        'quality': 0,
        'position': EquipPart.BELT,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'dodge': 13},
        'extend_attrs': {'crit_defense': 9, 'hp': 96}
    },
    {
        'id': 10007000,
        'name': '炼气护肩',
        'quality': 0,
        'position': EquipPart.SHOULDER,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'dodge': 12},
        'extend_attrs': {'crit_defense': 8}
    },
    {
        'id': 10007001,
        'name': '聚气护肩',
        'quality': 0,
        'position': EquipPart.SHOULDER,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'dodge': 12},
        'extend_attrs': {'crit_defense': 9}
    },
    {
        'id': 10007002,
        'name': '纳灵护肩',
        'quality': 0,
        'position': EquipPart.SHOULDER,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'dodge': 11},
        'extend_attrs': {'crit_defense': 8}
    },
    {
        'id': 10007003,
        'name': '炼气护肩·改',
        'quality': 0,
        'position': EquipPart.SHOULDER,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'dodge': 12},
        'extend_attrs': {'crit_defense': 8}
    },
    {
        'id': 10007004,
        'name': '聚气护肩·真',
        'quality': 0,
        'position': EquipPart.SHOULDER,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'dodge': 12},
        'extend_attrs': {'crit_defense': 9}
    },
    {
        'id': 10007005,
        'name': '纳灵护肩·灵',
        'quality': 0,
        'position': EquipPart.SHOULDER,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'dodge': 12},
        'extend_attrs': {'crit_defense': 8}
    },
    {
        'id': 10007100,
        'name': '炼气·青龙护肩',
        'quality': 0,
        'position': EquipPart.SHOULDER,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'dodge': 13},
        'extend_attrs': {'crit_defense': 9, 'hp': 96}
    },
    {
        'id': 10007101,
        'name': '炼气·白虎护肩',
        'quality': 0,
        'position': EquipPart.SHOULDER,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'dodge': 13},
        'extend_attrs': {'crit_defense': 9, 'hp': 96}
    },
    {
        'id': 10007102,
        'name': '炼气·朱雀护肩',
        'quality': 0,
        'position': EquipPart.SHOULDER,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'dodge': 13},
        'extend_attrs': {'crit_defense': 9, 'hp': 96}
    },
    {
        'id': 10008000,
        'name': '炼气鞋履',
        'quality': 0,
        'position': EquipPart.BOOTS,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 11},
        'extend_attrs': {'dodge': 9}
    },
    {
        'id': 10008001,
        'name': '聚气鞋履',
        'quality': 0,
        'position': EquipPart.BOOTS,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 11},
        'extend_attrs': {'dodge': 8}
    },
    {
        'id': 10008002,
        'name': '纳灵鞋履',
        'quality': 0,
        'position': EquipPart.BOOTS,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 12},
        'extend_attrs': {'dodge': 9}
    },
    {
        'id': 10008003,
        'name': '炼气鞋履·改',
        'quality': 0,
        'position': EquipPart.BOOTS,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 11},
        'extend_attrs': {'dodge': 9}
    },
    {
        'id': 10008004,
        'name': '聚气鞋履·真',
        'quality': 0,
        'position': EquipPart.BOOTS,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 11},
        'extend_attrs': {'dodge': 9}
    },
    {
        'id': 10008005,
        'name': '纳灵鞋履·灵',
        'quality': 0,
        'position': EquipPart.BOOTS,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 11},
        'extend_attrs': {'dodge': 9}
    },
    {
        'id': 10008100,
        'name': '炼气·青龙鞋履',
        'quality': 0,
        'position': EquipPart.BOOTS,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 13},
        'extend_attrs': {'dodge': 9, 'hp': 96}
    },
    {
        'id': 10008101,
        'name': '炼气·白虎鞋履',
        'quality': 0,
        'position': EquipPart.BOOTS,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 13},
        'extend_attrs': {'dodge': 9, 'hp': 96}
    },
    {
        'id': 10008102,
        'name': '炼气·朱雀鞋履',
        'quality': 0,
        'position': EquipPart.BOOTS,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 13},
        'extend_attrs': {'dodge': 9, 'hp': 96}
    },
    {
        'id': 10009000,
        'name': '炼气手套',
        'quality': 0,
        'position': EquipPart.GLOVES,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'outer_defense': 12},
        'extend_attrs': {'dodge': 8}
    },
    {
        'id': 10009001,
        'name': '聚气手套',
        'quality': 0,
        'position': EquipPart.GLOVES,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'outer_defense': 11},
        'extend_attrs': {'dodge': 9}
    },
    {
        'id': 10009002,
        'name': '纳灵手套',
        'quality': 0,
        'position': EquipPart.GLOVES,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'outer_defense': 12},
        'extend_attrs': {'dodge': 9}
    },
    {
        'id': 10009003,
        'name': '炼气手套·改',
        'quality': 0,
        'position': EquipPart.GLOVES,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'outer_defense': 12},
        'extend_attrs': {'dodge': 8}
    },
    {
        'id': 10009004,
        'name': '聚气手套·真',
        'quality': 0,
        'position': EquipPart.GLOVES,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'outer_defense': 11},
        'extend_attrs': {'dodge': 9}
    },
    {
        'id': 10009005,
        'name': '纳灵手套·灵',
        'quality': 0,
        'position': EquipPart.GLOVES,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'outer_defense': 12},
        'extend_attrs': {'dodge': 9}
    },
    {
        'id': 10009100,
        'name': '炼气·青龙手套',
        'quality': 0,
        'position': EquipPart.GLOVES,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'outer_defense': 13},
        'extend_attrs': {'dodge': 9, 'hp': 96}
    },
    {
        'id': 10009101,
        'name': '炼气·白虎手套',
        'quality': 0,
        'position': EquipPart.GLOVES,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'outer_defense': 13},
        'extend_attrs': {'dodge': 9, 'hp': 96}
    },
    {
        'id': 10009102,
        'name': '炼气·朱雀手套',
        'quality': 0,
        'position': EquipPart.GLOVES,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'outer_defense': 13},
        'extend_attrs': {'dodge': 9, 'hp': 96}
    },
    {
        'id': 10010000,
        'name': '炼气项链',
        'quality': 0,
        'position': EquipPart.NECKLACE,
        'type': EquipmentType.HYBRID,
        'base_attrs': {'inner_attack': 23, 'outer_attack': 24},
        'extend_attrs': {'hp': 99, 'inner_defense': 8, 'outer_defense': 8}
    },
    {
        'id': 10010001,
        'name': '聚气项链',
        'quality': 0,
        'position': EquipPart.NECKLACE,
        'type': EquipmentType.HYBRID,
        'base_attrs': {'inner_attack': 25, 'outer_attack': 23},
        'extend_attrs': {'hp': 97, 'inner_defense': 9, 'outer_defense': 8}
    },
    {
        'id': 10010002,
        'name': '纳灵项链',
        'quality': 0,
        'position': EquipPart.NECKLACE,
        'type': EquipmentType.HYBRID,
        'base_attrs': {'inner_attack': 24, 'outer_attack': 23},
        'extend_attrs': {'hp': 92, 'inner_defense': 9, 'outer_defense': 8}
    },
    {
        'id': 10010003,
        'name': '炼气项链·改',
        'quality': 0,
        'position': EquipPart.NECKLACE,
        'type': EquipmentType.HYBRID,
        'base_attrs': {'inner_attack': 23, 'outer_attack': 22},
        'extend_attrs': {'hp': 100, 'inner_defense': 9, 'outer_defense': 9}
    },
    {
        'id': 10010004,
        'name': '聚气项链·真',
        'quality': 0,
        'position': EquipPart.NECKLACE,
        'type': EquipmentType.HYBRID,
        'base_attrs': {'inner_attack': 24, 'outer_attack': 24},
        'extend_attrs': {'hp': 98, 'inner_defense': 9, 'outer_defense': 8}
    },
    {
        'id': 10010005,
        'name': '纳灵项链·灵',
        'quality': 0,
        'position': EquipPart.NECKLACE,
        'type': EquipmentType.HYBRID,
        'base_attrs': {'inner_attack': 24, 'outer_attack': 24},
        'extend_attrs': {'hp': 100, 'inner_defense': 8, 'outer_defense': 9}
    },
    {
        'id': 10010100,
        'name': '炼气·青龙项链',
        'quality': 0,
        'position': EquipPart.NECKLACE,
        'type': EquipmentType.HYBRID,
        'base_attrs': {'inner_attack': 26, 'outer_attack': 26},
        'extend_attrs': {'hp': 201, 'inner_defense': 9, 'outer_defense': 9}
    },
    {
        'id': 10010101,
        'name': '炼气·白虎项链',
        'quality': 0,
        'position': EquipPart.NECKLACE,
        'type': EquipmentType.HYBRID,
        'base_attrs': {'inner_attack': 26, 'outer_attack': 26},
        'extend_attrs': {'hp': 201, 'inner_defense': 9, 'outer_defense': 9}
    },
    {
        'id': 10010102,
        'name': '炼气·朱雀项链',
        'quality': 0,
        'position': EquipPart.NECKLACE,
        'type': EquipmentType.HYBRID,
        'base_attrs': {'inner_attack': 26, 'outer_attack': 26},
        'extend_attrs': {'hp': 201, 'inner_defense': 9, 'outer_defense': 9}
    },
    {
        'id': 10011000,
        'name': '炼气法宝',
        'quality': 0,
        'position': EquipPart.ARTIFACT,
        'type': EquipmentType.HYBRID,
        'base_attrs': {'hit': 12, 'crit': 12},
        'extend_attrs': {'outer_attack': 19, 'inner_attack': 19}
    },
    {
        'id': 10011001,
        'name': '聚气法宝',
        'quality': 0,
        'position': EquipPart.ARTIFACT,
        'type': EquipmentType.HYBRID,
        'base_attrs': {'hit': 11, 'crit': 11},
        'extend_attrs': {'outer_attack': 19, 'inner_attack': 19}
    },
    {
        'id': 10011002,
        'name': '纳灵法宝',
        'quality': 0,
        'position': EquipPart.ARTIFACT,
        'type': EquipmentType.HYBRID,
        'base_attrs': {'hit': 11, 'crit': 11},
        'extend_attrs': {'outer_attack': 18, 'inner_attack': 18}
    },
    {
        'id': 10011003,
        'name': '炼气法宝·改',
        'quality': 0,
        'position': EquipPart.ARTIFACT,
        'type': EquipmentType.HYBRID,
        'base_attrs': {'hit': 12, 'crit': 12},
        'extend_attrs': {'outer_attack': 18, 'inner_attack': 18}
    },
    {
        'id': 10011004,
        'name': '聚气法宝·真',
        'quality': 0,
        'position': EquipPart.ARTIFACT,
        'type': EquipmentType.HYBRID,
        'base_attrs': {'hit': 12, 'crit': 11},
        'extend_attrs': {'outer_attack': 19, 'inner_attack': 18}
    },
    {
        'id': 10011005,
        'name': '纳灵法宝·灵',
        'quality': 0,
        'position': EquipPart.ARTIFACT,
        'type': EquipmentType.HYBRID,
        'base_attrs': {'hit': 12, 'crit': 11},
        'extend_attrs': {'outer_attack': 18, 'inner_attack': 18}
    },
    {
        'id': 10011100,
        'name': '炼气·青龙法宝',
        'quality': 0,
        'position': EquipPart.ARTIFACT,
        'type': EquipmentType.HYBRID,
        'base_attrs': {'hit': 13, 'crit': 13},
        'extend_attrs': {'outer_attack': 20, 'inner_attack': 20, 'hp': 96}
    },
    {
        'id': 10011101,
        'name': '炼气·白虎法宝',
        'quality': 0,
        'position': EquipPart.ARTIFACT,
        'type': EquipmentType.HYBRID,
        'base_attrs': {'hit': 13, 'crit': 13},
        'extend_attrs': {'outer_attack': 20, 'inner_attack': 20, 'hp': 96}
    },
    {
        'id': 10011102,
        'name': '炼气·朱雀法宝',
        'quality': 0,
        'position': EquipPart.ARTIFACT,
        'type': EquipmentType.HYBRID,
        'base_attrs': {'hit': 13, 'crit': 13},
        'extend_attrs': {'outer_attack': 20, 'inner_attack': 20, 'hp': 96}
    },
    {
        'id': 10100000,
        'name': '筑基剑',
        'quality': 1,
        'position': EquipPart.WEAPON,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'inner_attack': 49, 'outer_attack': 49},
        'extend_attrs': {'hp': 195, 'hit': 18, 'crit': 19}
    },
    {
        'id': 10100001,
        'name': '固本刀',
        'quality': 1,
        'position': EquipPart.WEAPON,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'inner_attack': 48, 'outer_attack': 46},
        'extend_attrs': {'hp': 187, 'hit': 18, 'crit': 18}
    },
    {
        'id': 10100002,
        'name': '培元弓',
        'quality': 1,
        'position': EquipPart.WEAPON,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'inner_attack': 48, 'outer_attack': 50},
        'extend_attrs': {'hp': 189, 'hit': 19, 'crit': 19}
    },
    {
        'id': 10100003,
        'name': '筑基弩',
        'quality': 1,
        'position': EquipPart.WEAPON,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'inner_attack': 49, 'outer_attack': 47},
        'extend_attrs': {'hp': 194, 'hit': 19, 'crit': 19}
    },
    {
        'id': 10100004,
        'name': '固本枪',
        'quality': 1,
        'position': EquipPart.WEAPON,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'inner_attack': 48, 'outer_attack': 48},
        'extend_attrs': {'hp': 195, 'hit': 18, 'crit': 18}
    },
    {
        'id': 10100005,
        'name': '培元棍',
        'quality': 1,
        'position': EquipPart.WEAPON,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'inner_attack': 49, 'outer_attack': 50},
        'extend_attrs': {'hp': 186, 'hit': 18, 'crit': 19}
    },
    {
        'id': 10100100,
        'name': '筑基·青龙剑',
        'quality': 1,
        'position': EquipPart.WEAPON,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'inner_attack': 52, 'outer_attack': 52},
        'extend_attrs': {'hp': 403, 'hit': 20, 'crit': 20}
    },
    {
        'id': 10100101,
        'name': '筑基·白虎刀',
        'quality': 1,
        'position': EquipPart.WEAPON,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'inner_attack': 52, 'outer_attack': 52},
        'extend_attrs': {'hp': 403, 'hit': 20, 'crit': 20}
    },
    {
        'id': 10100102,
        'name': '筑基·朱雀弓',
        'quality': 1,
        'position': EquipPart.WEAPON,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'inner_attack': 52, 'outer_attack': 52},
        'extend_attrs': {'hp': 403, 'hit': 20, 'crit': 20}
    },
    {
        'id': 10101000,
        'name': '筑基护腕',
        'quality': 1,
        'position': EquipPart.BRACER,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'hit': 23},
        'extend_attrs': {'outer_attack': 36, 'inner_attack': 36}
    },
    {
        'id': 10101001,
        'name': '固本护腕',
        'quality': 1,
        'position': EquipPart.BRACER,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'hit': 24},
        'extend_attrs': {'outer_attack': 38, 'inner_attack': 36}
    },
    {
        'id': 10101002,
        'name': '培元护腕',
        'quality': 1,
        'position': EquipPart.BRACER,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'hit': 22},
        'extend_attrs': {'outer_attack': 39, 'inner_attack': 36}
    },
    {
        'id': 10101003,
        'name': '筑基护腕·改',
        'quality': 1,
        'position': EquipPart.BRACER,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'hit': 22},
        'extend_attrs': {'outer_attack': 37, 'inner_attack': 38}
    },
    {
        'id': 10101004,
        'name': '固本护腕·真',
        'quality': 1,
        'position': EquipPart.BRACER,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'hit': 24},
        'extend_attrs': {'outer_attack': 37, 'inner_attack': 39}
    },
    {
        'id': 10101005,
        'name': '培元护腕·灵',
        'quality': 1,
        'position': EquipPart.BRACER,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'hit': 24},
        'extend_attrs': {'outer_attack': 39, 'inner_attack': 36}
    },
    {
        'id': 10101100,
        'name': '筑基·青龙护腕',
        'quality': 1,
        'position': EquipPart.BRACER,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'hit': 26},
        'extend_attrs': {'outer_attack': 41, 'inner_attack': 41, 'hp': 192}
    },
    {
        'id': 10101101,
        'name': '筑基·白虎护腕',
        'quality': 1,
        'position': EquipPart.BRACER,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'hit': 26},
        'extend_attrs': {'outer_attack': 41, 'inner_attack': 41, 'hp': 192}
    },
    {
        'id': 10101102,
        'name': '筑基·朱雀护腕',
        'quality': 1,
        'position': EquipPart.BRACER,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'hit': 26},
        'extend_attrs': {'outer_attack': 41, 'inner_attack': 41, 'hp': 192}
    },
    {
        'id': 10102000,
        'name': '筑基戒指',
        'quality': 1,
        'position': EquipPart.RING,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'inner_attack': 46},
        'extend_attrs': {'hit': 19, 'crit': 18}
    },
    {
        'id': 10102001,
        'name': '固本戒指',
        'quality': 1,
        'position': EquipPart.RING,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'inner_attack': 46},
        'extend_attrs': {'hit': 19, 'crit': 19}
    },
    {
        'id': 10102002,
        'name': '培元戒指',
        'quality': 1,
        'position': EquipPart.RING,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'inner_attack': 48},
        'extend_attrs': {'hit': 18, 'crit': 19}
    },
    {
        'id': 10102003,
        'name': '筑基戒指·改',
        'quality': 1,
        'position': EquipPart.RING,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'inner_attack': 49},
        'extend_attrs': {'hit': 19, 'crit': 18}
    },
    {
        'id': 10102004,
        'name': '固本戒指·真',
        'quality': 1,
        'position': EquipPart.RING,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'inner_attack': 45},
        'extend_attrs': {'hit': 18, 'crit': 19}
    },
    {
        'id': 10102005,
        'name': '培元戒指·灵',
        'quality': 1,
        'position': EquipPart.RING,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'inner_attack': 47},
        'extend_attrs': {'hit': 18, 'crit': 19}
    },
    {
        'id': 10102100,
        'name': '筑基·青龙戒指',
        'quality': 1,
        'position': EquipPart.RING,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'inner_attack': 52},
        'extend_attrs': {'hit': 20, 'crit': 20, 'hp': 192}
    },
    {
        'id': 10102101,
        'name': '筑基·白虎戒指',
        'quality': 1,
        'position': EquipPart.RING,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'inner_attack': 52},
        'extend_attrs': {'hit': 20, 'crit': 20, 'hp': 192}
    },
    {
        'id': 10102102,
        'name': '筑基·朱雀戒指',
        'quality': 1,
        'position': EquipPart.RING,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'inner_attack': 52},
        'extend_attrs': {'hit': 20, 'crit': 20, 'hp': 192}
    },
    {
        'id': 10103000,
        'name': '筑基护符',
        'quality': 1,
        'position': EquipPart.AMULET,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'outer_attack': 46},
        'extend_attrs': {'hit': 18, 'crit': 18}
    },
    {
        'id': 10103001,
        'name': '固本护符',
        'quality': 1,
        'position': EquipPart.AMULET,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'outer_attack': 47},
        'extend_attrs': {'hit': 18, 'crit': 18}
    },
    {
        'id': 10103002,
        'name': '培元护符',
        'quality': 1,
        'position': EquipPart.AMULET,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'outer_attack': 47},
        'extend_attrs': {'hit': 18, 'crit': 18}
    },
    {
        'id': 10103003,
        'name': '筑基护符·改',
        'quality': 1,
        'position': EquipPart.AMULET,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'outer_attack': 46},
        'extend_attrs': {'hit': 19, 'crit': 18}
    },
    {
        'id': 10103004,
        'name': '固本护符·真',
        'quality': 1,
        'position': EquipPart.AMULET,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'outer_attack': 50},
        'extend_attrs': {'hit': 18, 'crit': 18}
    },
    {
        'id': 10103005,
        'name': '培元护符·灵',
        'quality': 1,
        'position': EquipPart.AMULET,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'outer_attack': 47},
        'extend_attrs': {'hit': 19, 'crit': 19}
    },
    {
        'id': 10103100,
        'name': '筑基·青龙护符',
        'quality': 1,
        'position': EquipPart.AMULET,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'outer_attack': 52},
        'extend_attrs': {'hit': 20, 'crit': 20, 'hp': 192}
    },
    {
        'id': 10103101,
        'name': '筑基·白虎护符',
        'quality': 1,
        'position': EquipPart.AMULET,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'outer_attack': 52},
        'extend_attrs': {'hit': 20, 'crit': 20, 'hp': 192}
    },
    {
        'id': 10103102,
        'name': '筑基·朱雀护符',
        'quality': 1,
        'position': EquipPart.AMULET,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'outer_attack': 52},
        'extend_attrs': {'hit': 20, 'crit': 20, 'hp': 192}
    },
    {
        'id': 10104000,
        'name': '筑基头盔',
        'quality': 1,
        'position': EquipPart.HELMET,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 24, 'outer_defense': 24},
        'extend_attrs': {'inner_defense': 19, 'outer_defense': 18}
    },
    {
        'id': 10104001,
        'name': '固本头盔',
        'quality': 1,
        'position': EquipPart.HELMET,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 25, 'outer_defense': 24},
        'extend_attrs': {'inner_defense': 19, 'outer_defense': 19}
    },
    {
        'id': 10104002,
        'name': '培元头盔',
        'quality': 1,
        'position': EquipPart.HELMET,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 24, 'outer_defense': 23},
        'extend_attrs': {'inner_defense': 18, 'outer_defense': 18}
    },
    {
        'id': 10104003,
        'name': '筑基头盔·改',
        'quality': 1,
        'position': EquipPart.HELMET,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 23, 'outer_defense': 24},
        'extend_attrs': {'inner_defense': 19, 'outer_defense': 18}
    },
    {
        'id': 10104004,
        'name': '固本头盔·真',
        'quality': 1,
        'position': EquipPart.HELMET,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 23, 'outer_defense': 23},
        'extend_attrs': {'inner_defense': 18, 'outer_defense': 18}
    },
    {
        'id': 10104005,
        'name': '培元头盔·灵',
        'quality': 1,
        'position': EquipPart.HELMET,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 23, 'outer_defense': 23},
        'extend_attrs': {'inner_defense': 18, 'outer_defense': 18}
    },
    {
        'id': 10104100,
        'name': '筑基·青龙头盔',
        'quality': 1,
        'position': EquipPart.HELMET,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 26, 'outer_defense': 26},
        'extend_attrs': {'inner_defense': 20, 'outer_defense': 20, 'hp': 192}
    },
    {
        'id': 10104101,
        'name': '筑基·白虎头盔',
        'quality': 1,
        'position': EquipPart.HELMET,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 26, 'outer_defense': 26},
        'extend_attrs': {'inner_defense': 20, 'outer_defense': 20, 'hp': 192}
    },
    {
        'id': 10104102,
        'name': '筑基·朱雀头盔',
        'quality': 1,
        'position': EquipPart.HELMET,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 26, 'outer_defense': 26},
        'extend_attrs': {'inner_defense': 20, 'outer_defense': 20, 'hp': 192}
    },
    {
        'id': 10105000,
        'name': '筑基甲胄',
        'quality': 1,
        'position': EquipPart.ARMOR,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 24, 'outer_defense': 24},
        'extend_attrs': {'inner_defense': 18, 'outer_defense': 18}
    },
    {
        'id': 10105001,
        'name': '固本甲胄',
        'quality': 1,
        'position': EquipPart.ARMOR,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 24, 'outer_defense': 24},
        'extend_attrs': {'inner_defense': 18, 'outer_defense': 19}
    },
    {
        'id': 10105002,
        'name': '培元甲胄',
        'quality': 1,
        'position': EquipPart.ARMOR,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 24, 'outer_defense': 24},
        'extend_attrs': {'inner_defense': 19, 'outer_defense': 19}
    },
    {
        'id': 10105003,
        'name': '筑基甲胄·改',
        'quality': 1,
        'position': EquipPart.ARMOR,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 24, 'outer_defense': 23},
        'extend_attrs': {'inner_defense': 19, 'outer_defense': 18}
    },
    {
        'id': 10105004,
        'name': '固本甲胄·真',
        'quality': 1,
        'position': EquipPart.ARMOR,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 23, 'outer_defense': 24},
        'extend_attrs': {'inner_defense': 19, 'outer_defense': 18}
    },
    {
        'id': 10105005,
        'name': '培元甲胄·灵',
        'quality': 1,
        'position': EquipPart.ARMOR,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 24, 'outer_defense': 23},
        'extend_attrs': {'inner_defense': 18, 'outer_defense': 19}
    },
    {
        'id': 10105100,
        'name': '筑基·青龙甲胄',
        'quality': 1,
        'position': EquipPart.ARMOR,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 26, 'outer_defense': 26},
        'extend_attrs': {'inner_defense': 20, 'outer_defense': 20, 'hp': 192}
    },
    {
        'id': 10105101,
        'name': '筑基·白虎甲胄',
        'quality': 1,
        'position': EquipPart.ARMOR,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 26, 'outer_defense': 26},
        'extend_attrs': {'inner_defense': 20, 'outer_defense': 20, 'hp': 192}
    },
    {
        'id': 10105102,
        'name': '筑基·朱雀甲胄',
        'quality': 1,
        'position': EquipPart.ARMOR,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 26, 'outer_defense': 26},
        'extend_attrs': {'inner_defense': 20, 'outer_defense': 20, 'hp': 192}
    },
    {
        'id': 10106000,
        'name': '筑基腰带',
        'quality': 1,
        'position': EquipPart.BELT,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'dodge': 25},
        'extend_attrs': {'crit_defense': 19}
    },
    {
        'id': 10106001,
        'name': '固本腰带',
        'quality': 1,
        'position': EquipPart.BELT,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'dodge': 23},
        'extend_attrs': {'crit_defense': 19}
    },
    {
        'id': 10106002,
        'name': '培元腰带',
        'quality': 1,
        'position': EquipPart.BELT,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'dodge': 24},
        'extend_attrs': {'crit_defense': 18}
    },
    {
        'id': 10106003,
        'name': '筑基腰带·改',
        'quality': 1,
        'position': EquipPart.BELT,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'dodge': 23},
        'extend_attrs': {'crit_defense': 18}
    },
    {
        'id': 10106004,
        'name': '固本腰带·真',
        'quality': 1,
        'position': EquipPart.BELT,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'dodge': 24},
        'extend_attrs': {'crit_defense': 19}
    },
    {
        'id': 10106005,
        'name': '培元腰带·灵',
        'quality': 1,
        'position': EquipPart.BELT,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'dodge': 24},
        'extend_attrs': {'crit_defense': 19}
    },
    {
        'id': 10106100,
        'name': '筑基·青龙腰带',
        'quality': 1,
        'position': EquipPart.BELT,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'dodge': 26},
        'extend_attrs': {'crit_defense': 20, 'hp': 192}
    },
    {
        'id': 10106101,
        'name': '筑基·白虎腰带',
        'quality': 1,
        'position': EquipPart.BELT,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'dodge': 26},
        'extend_attrs': {'crit_defense': 20, 'hp': 192}
    },
    {
        'id': 10106102,
        'name': '筑基·朱雀腰带',
        'quality': 1,
        'position': EquipPart.BELT,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'dodge': 26},
        'extend_attrs': {'crit_defense': 20, 'hp': 192}
    },
    {
        'id': 10107000,
        'name': '筑基护肩',
        'quality': 1,
        'position': EquipPart.SHOULDER,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'dodge': 23},
        'extend_attrs': {'crit_defense': 19}
    },
    {
        'id': 10107001,
        'name': '固本护肩',
        'quality': 1,
        'position': EquipPart.SHOULDER,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'dodge': 24},
        'extend_attrs': {'crit_defense': 19}
    },
    {
        'id': 10107002,
        'name': '培元护肩',
        'quality': 1,
        'position': EquipPart.SHOULDER,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'dodge': 24},
        'extend_attrs': {'crit_defense': 18}
    },
    {
        'id': 10107003,
        'name': '筑基护肩·改',
        'quality': 1,
        'position': EquipPart.SHOULDER,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'dodge': 25},
        'extend_attrs': {'crit_defense': 18}
    },
    {
        'id': 10107004,
        'name': '固本护肩·真',
        'quality': 1,
        'position': EquipPart.SHOULDER,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'dodge': 23},
        'extend_attrs': {'crit_defense': 18}
    },
    {
        'id': 10107005,
        'name': '培元护肩·灵',
        'quality': 1,
        'position': EquipPart.SHOULDER,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'dodge': 22},
        'extend_attrs': {'crit_defense': 19}
    },
    {
        'id': 10107100,
        'name': '筑基·青龙护肩',
        'quality': 1,
        'position': EquipPart.SHOULDER,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'dodge': 26},
        'extend_attrs': {'crit_defense': 20, 'hp': 192}
    },
    {
        'id': 10107101,
        'name': '筑基·白虎护肩',
        'quality': 1,
        'position': EquipPart.SHOULDER,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'dodge': 26},
        'extend_attrs': {'crit_defense': 20, 'hp': 192}
    },
    {
        'id': 10107102,
        'name': '筑基·朱雀护肩',
        'quality': 1,
        'position': EquipPart.SHOULDER,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'dodge': 26},
        'extend_attrs': {'crit_defense': 20, 'hp': 192}
    },
    {
        'id': 10108000,
        'name': '筑基鞋履',
        'quality': 1,
        'position': EquipPart.BOOTS,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 24},
        'extend_attrs': {'dodge': 18}
    },
    {
        'id': 10108001,
        'name': '固本鞋履',
        'quality': 1,
        'position': EquipPart.BOOTS,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 24},
        'extend_attrs': {'dodge': 19}
    },
    {
        'id': 10108002,
        'name': '培元鞋履',
        'quality': 1,
        'position': EquipPart.BOOTS,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 25},
        'extend_attrs': {'dodge': 19}
    },
    {
        'id': 10108003,
        'name': '筑基鞋履·改',
        'quality': 1,
        'position': EquipPart.BOOTS,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 22},
        'extend_attrs': {'dodge': 19}
    },
    {
        'id': 10108004,
        'name': '固本鞋履·真',
        'quality': 1,
        'position': EquipPart.BOOTS,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 22},
        'extend_attrs': {'dodge': 18}
    },
    {
        'id': 10108005,
        'name': '培元鞋履·灵',
        'quality': 1,
        'position': EquipPart.BOOTS,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 23},
        'extend_attrs': {'dodge': 18}
    },
    {
        'id': 10108100,
        'name': '筑基·青龙鞋履',
        'quality': 1,
        'position': EquipPart.BOOTS,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 26},
        'extend_attrs': {'dodge': 20, 'hp': 192}
    },
    {
        'id': 10108101,
        'name': '筑基·白虎鞋履',
        'quality': 1,
        'position': EquipPart.BOOTS,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 26},
        'extend_attrs': {'dodge': 20, 'hp': 192}
    },
    {
        'id': 10108102,
        'name': '筑基·朱雀鞋履',
        'quality': 1,
        'position': EquipPart.BOOTS,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 26},
        'extend_attrs': {'dodge': 20, 'hp': 192}
    },
    {
        'id': 10109000,
        'name': '筑基手套',
        'quality': 1,
        'position': EquipPart.GLOVES,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'outer_defense': 23},
        'extend_attrs': {'dodge': 18}
    },
    {
        'id': 10109001,
        'name': '固本手套',
        'quality': 1,
        'position': EquipPart.GLOVES,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'outer_defense': 24},
        'extend_attrs': {'dodge': 19}
    },
    {
        'id': 10109002,
        'name': '培元手套',
        'quality': 1,
        'position': EquipPart.GLOVES,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'outer_defense': 24},
        'extend_attrs': {'dodge': 19}
    },
    {
        'id': 10109003,
        'name': '筑基手套·改',
        'quality': 1,
        'position': EquipPart.GLOVES,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'outer_defense': 24},
        'extend_attrs': {'dodge': 18}
    },
    {
        'id': 10109004,
        'name': '固本手套·真',
        'quality': 1,
        'position': EquipPart.GLOVES,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'outer_defense': 25},
        'extend_attrs': {'dodge': 18}
    },
    {
        'id': 10109005,
        'name': '培元手套·灵',
        'quality': 1,
        'position': EquipPart.GLOVES,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'outer_defense': 24},
        'extend_attrs': {'dodge': 18}
    },
    {
        'id': 10109100,
        'name': '筑基·青龙手套',
        'quality': 1,
        'position': EquipPart.GLOVES,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'outer_defense': 26},
        'extend_attrs': {'dodge': 20, 'hp': 192}
    },
    {
        'id': 10109101,
        'name': '筑基·白虎手套',
        'quality': 1,
        'position': EquipPart.GLOVES,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'outer_defense': 26},
        'extend_attrs': {'dodge': 20, 'hp': 192}
    },
    {
        'id': 10109102,
        'name': '筑基·朱雀手套',
        'quality': 1,
        'position': EquipPart.GLOVES,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'outer_defense': 26},
        'extend_attrs': {'dodge': 20, 'hp': 192}
    },
    {
        'id': 10110000,
        'name': '筑基项链',
        'quality': 1,
        'position': EquipPart.NECKLACE,
        'type': EquipmentType.HYBRID,
        'base_attrs': {'inner_attack': 47, 'outer_attack': 48},
        'extend_attrs': {'hp': 197, 'inner_defense': 19, 'outer_defense': 19}
    },
    {
        'id': 10110001,
        'name': '固本项链',
        'quality': 1,
        'position': EquipPart.NECKLACE,
        'type': EquipmentType.HYBRID,
        'base_attrs': {'inner_attack': 48, 'outer_attack': 47},
        'extend_attrs': {'hp': 183, 'inner_defense': 19, 'outer_defense': 18}
    },
    {
        'id': 10110002,
        'name': '培元项链',
        'quality': 1,
        'position': EquipPart.NECKLACE,
        'type': EquipmentType.HYBRID,
        'base_attrs': {'inner_attack': 47, 'outer_attack': 49},
        'extend_attrs': {'hp': 199, 'inner_defense': 19, 'outer_defense': 18}
    },
    {
        'id': 10110003,
        'name': '筑基项链·改',
        'quality': 1,
        'position': EquipPart.NECKLACE,
        'type': EquipmentType.HYBRID,
        'base_attrs': {'inner_attack': 48, 'outer_attack': 45},
        'extend_attrs': {'hp': 186, 'inner_defense': 19, 'outer_defense': 19}
    },
    {
        'id': 10110004,
        'name': '固本项链·真',
        'quality': 1,
        'position': EquipPart.NECKLACE,
        'type': EquipmentType.HYBRID,
        'base_attrs': {'inner_attack': 49, 'outer_attack': 46},
        'extend_attrs': {'hp': 195, 'inner_defense': 19, 'outer_defense': 18}
    },
    {
        'id': 10110005,
        'name': '培元项链·灵',
        'quality': 1,
        'position': EquipPart.NECKLACE,
        'type': EquipmentType.HYBRID,
        'base_attrs': {'inner_attack': 49, 'outer_attack': 46},
        'extend_attrs': {'hp': 188, 'inner_defense': 19, 'outer_defense': 18}
    },
    {
        'id': 10110100,
        'name': '筑基·青龙项链',
        'quality': 1,
        'position': EquipPart.NECKLACE,
        'type': EquipmentType.HYBRID,
        'base_attrs': {'inner_attack': 52, 'outer_attack': 52},
        'extend_attrs': {'hp': 403, 'inner_defense': 20, 'outer_defense': 20}
    },
    {
        'id': 10110101,
        'name': '筑基·白虎项链',
        'quality': 1,
        'position': EquipPart.NECKLACE,
        'type': EquipmentType.HYBRID,
        'base_attrs': {'inner_attack': 52, 'outer_attack': 52},
        'extend_attrs': {'hp': 403, 'inner_defense': 20, 'outer_defense': 20}
    },
    {
        'id': 10110102,
        'name': '筑基·朱雀项链',
        'quality': 1,
        'position': EquipPart.NECKLACE,
        'type': EquipmentType.HYBRID,
        'base_attrs': {'inner_attack': 52, 'outer_attack': 52},
        'extend_attrs': {'hp': 403, 'inner_defense': 20, 'outer_defense': 20}
    },
    {
        'id': 10111000,
        'name': '筑基法宝',
        'quality': 1,
        'position': EquipPart.ARTIFACT,
        'type': EquipmentType.HYBRID,
        'base_attrs': {'hit': 24, 'crit': 24},
        'extend_attrs': {'outer_attack': 37, 'inner_attack': 36}
    },
    {
        'id': 10111001,
        'name': '固本法宝',
        'quality': 1,
        'position': EquipPart.ARTIFACT,
        'type': EquipmentType.HYBRID,
        'base_attrs': {'hit': 23, 'crit': 23},
        'extend_attrs': {'outer_attack': 39, 'inner_attack': 39}
    },
    {
        'id': 10111002,
        'name': '培元法宝',
        'quality': 1,
        'position': EquipPart.ARTIFACT,
        'type': EquipmentType.HYBRID,
        'base_attrs': {'hit': 24, 'crit': 23},
        'extend_attrs': {'outer_attack': 39, 'inner_attack': 39}
    },
    {
        'id': 10111003,
        'name': '筑基法宝·改',
        'quality': 1,
        'position': EquipPart.ARTIFACT,
        'type': EquipmentType.HYBRID,
        'base_attrs': {'hit': 23, 'crit': 22},
        'extend_attrs': {'outer_attack': 39, 'inner_attack': 37}
    },
    {
        'id': 10111004,
        'name': '固本法宝·真',
        'quality': 1,
        'position': EquipPart.ARTIFACT,
        'type': EquipmentType.HYBRID,
        'base_attrs': {'hit': 23, 'crit': 23},
        'extend_attrs': {'outer_attack': 38, 'inner_attack': 36}
    },
    {
        'id': 10111005,
        'name': '培元法宝·灵',
        'quality': 1,
        'position': EquipPart.ARTIFACT,
        'type': EquipmentType.HYBRID,
        'base_attrs': {'hit': 24, 'crit': 24},
        'extend_attrs': {'outer_attack': 38, 'inner_attack': 37}
    },
    {
        'id': 10111100,
        'name': '筑基·青龙法宝',
        'quality': 1,
        'position': EquipPart.ARTIFACT,
        'type': EquipmentType.HYBRID,
        'base_attrs': {'hit': 26, 'crit': 26},
        'extend_attrs': {'outer_attack': 41, 'inner_attack': 41, 'hp': 192}
    },
    {
        'id': 10111101,
        'name': '筑基·白虎法宝',
        'quality': 1,
        'position': EquipPart.ARTIFACT,
        'type': EquipmentType.HYBRID,
        'base_attrs': {'hit': 26, 'crit': 26},
        'extend_attrs': {'outer_attack': 41, 'inner_attack': 41, 'hp': 192}
    },
    {
        'id': 10111102,
        'name': '筑基·朱雀法宝',
        'quality': 1,
        'position': EquipPart.ARTIFACT,
        'type': EquipmentType.HYBRID,
        'base_attrs': {'hit': 26, 'crit': 26},
        'extend_attrs': {'outer_attack': 41, 'inner_attack': 41, 'hp': 192}
    },
    {
        'id': 10200000,
        'name': '结丹剑',
        'quality': 2,
        'position': EquipPart.WEAPON,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'inner_attack': 70, 'outer_attack': 75},
        'extend_attrs': {'hp': 299, 'hit': 27, 'crit': 28}
    },
    {
        'id': 10200001,
        'name': '金丹刀',
        'quality': 2,
        'position': EquipPart.WEAPON,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'inner_attack': 73, 'outer_attack': 69},
        'extend_attrs': {'hp': 297, 'hit': 27, 'crit': 28}
    },
    {
        'id': 10200002,
        'name': '开光弓',
        'quality': 2,
        'position': EquipPart.WEAPON,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'inner_attack': 73, 'outer_attack': 71},
        'extend_attrs': {'hp': 279, 'hit': 28, 'crit': 29}
    },
    {
        'id': 10200003,
        'name': '结丹弩',
        'quality': 2,
        'position': EquipPart.WEAPON,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'inner_attack': 72, 'outer_attack': 72},
        'extend_attrs': {'hp': 289, 'hit': 28, 'crit': 27}
    },
    {
        'id': 10200004,
        'name': '金丹枪',
        'quality': 2,
        'position': EquipPart.WEAPON,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'inner_attack': 74, 'outer_attack': 70},
        'extend_attrs': {'hp': 289, 'hit': 29, 'crit': 27}
    },
    {
        'id': 10200005,
        'name': '开光棍',
        'quality': 2,
        'position': EquipPart.WEAPON,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'inner_attack': 70, 'outer_attack': 71},
        'extend_attrs': {'hp': 292, 'hit': 27, 'crit': 27}
    },
    {
        'id': 10200100,
        'name': '结丹·青龙剑',
        'quality': 2,
        'position': EquipPart.WEAPON,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'inner_attack': 79, 'outer_attack': 79},
        'extend_attrs': {'hp': 604, 'hit': 30, 'crit': 30}
    },
    {
        'id': 10200101,
        'name': '结丹·白虎刀',
        'quality': 2,
        'position': EquipPart.WEAPON,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'inner_attack': 79, 'outer_attack': 79},
        'extend_attrs': {'hp': 604, 'hit': 30, 'crit': 30}
    },
    {
        'id': 10200102,
        'name': '结丹·朱雀弓',
        'quality': 2,
        'position': EquipPart.WEAPON,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'inner_attack': 79, 'outer_attack': 79},
        'extend_attrs': {'hp': 604, 'hit': 30, 'crit': 30}
    },
    {
        'id': 10201000,
        'name': '结丹护腕',
        'quality': 2,
        'position': EquipPart.BRACER,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'hit': 36},
        'extend_attrs': {'outer_attack': 59, 'inner_attack': 54}
    },
    {
        'id': 10201001,
        'name': '金丹护腕',
        'quality': 2,
        'position': EquipPart.BRACER,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'hit': 36},
        'extend_attrs': {'outer_attack': 56, 'inner_attack': 59}
    },
    {
        'id': 10201002,
        'name': '开光护腕',
        'quality': 2,
        'position': EquipPart.BRACER,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'hit': 34},
        'extend_attrs': {'outer_attack': 59, 'inner_attack': 59}
    },
    {
        'id': 10201003,
        'name': '结丹护腕·改',
        'quality': 2,
        'position': EquipPart.BRACER,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'hit': 36},
        'extend_attrs': {'outer_attack': 56, 'inner_attack': 55}
    },
    {
        'id': 10201004,
        'name': '金丹护腕·真',
        'quality': 2,
        'position': EquipPart.BRACER,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'hit': 35},
        'extend_attrs': {'outer_attack': 55, 'inner_attack': 55}
    },
    {
        'id': 10201005,
        'name': '开光护腕·灵',
        'quality': 2,
        'position': EquipPart.BRACER,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'hit': 36},
        'extend_attrs': {'outer_attack': 58, 'inner_attack': 57}
    },
    {
        'id': 10201100,
        'name': '结丹·青龙护腕',
        'quality': 2,
        'position': EquipPart.BRACER,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'hit': 39},
        'extend_attrs': {'outer_attack': 62, 'inner_attack': 62, 'hp': 288}
    },
    {
        'id': 10201101,
        'name': '结丹·白虎护腕',
        'quality': 2,
        'position': EquipPart.BRACER,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'hit': 39},
        'extend_attrs': {'outer_attack': 62, 'inner_attack': 62, 'hp': 288}
    },
    {
        'id': 10201102,
        'name': '结丹·朱雀护腕',
        'quality': 2,
        'position': EquipPart.BRACER,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'hit': 39},
        'extend_attrs': {'outer_attack': 62, 'inner_attack': 62, 'hp': 288}
    },
    {
        'id': 10202000,
        'name': '结丹戒指',
        'quality': 2,
        'position': EquipPart.RING,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'inner_attack': 69},
        'extend_attrs': {'hit': 29, 'crit': 27}
    },
    {
        'id': 10202001,
        'name': '金丹戒指',
        'quality': 2,
        'position': EquipPart.RING,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'inner_attack': 69},
        'extend_attrs': {'hit': 26, 'crit': 28}
    },
    {
        'id': 10202002,
        'name': '开光戒指',
        'quality': 2,
        'position': EquipPart.RING,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'inner_attack': 70},
        'extend_attrs': {'hit': 27, 'crit': 29}
    },
    {
        'id': 10202003,
        'name': '结丹戒指·改',
        'quality': 2,
        'position': EquipPart.RING,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'inner_attack': 68},
        'extend_attrs': {'hit': 27, 'crit': 28}
    },
    {
        'id': 10202004,
        'name': '金丹戒指·真',
        'quality': 2,
        'position': EquipPart.RING,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'inner_attack': 73},
        'extend_attrs': {'hit': 26, 'crit': 27}
    },
    {
        'id': 10202005,
        'name': '开光戒指·灵',
        'quality': 2,
        'position': EquipPart.RING,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'inner_attack': 72},
        'extend_attrs': {'hit': 28, 'crit': 29}
    },
    {
        'id': 10202100,
        'name': '结丹·青龙戒指',
        'quality': 2,
        'position': EquipPart.RING,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'inner_attack': 79},
        'extend_attrs': {'hit': 30, 'crit': 30, 'hp': 288}
    },
    {
        'id': 10202101,
        'name': '结丹·白虎戒指',
        'quality': 2,
        'position': EquipPart.RING,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'inner_attack': 79},
        'extend_attrs': {'hit': 30, 'crit': 30, 'hp': 288}
    },
    {
        'id': 10202102,
        'name': '结丹·朱雀戒指',
        'quality': 2,
        'position': EquipPart.RING,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'inner_attack': 79},
        'extend_attrs': {'hit': 30, 'crit': 30, 'hp': 288}
    },
    {
        'id': 10203000,
        'name': '结丹护符',
        'quality': 2,
        'position': EquipPart.AMULET,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'outer_attack': 74},
        'extend_attrs': {'hit': 28, 'crit': 29}
    },
    {
        'id': 10203001,
        'name': '金丹护符',
        'quality': 2,
        'position': EquipPart.AMULET,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'outer_attack': 69},
        'extend_attrs': {'hit': 27, 'crit': 27}
    },
    {
        'id': 10203002,
        'name': '开光护符',
        'quality': 2,
        'position': EquipPart.AMULET,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'outer_attack': 73},
        'extend_attrs': {'hit': 27, 'crit': 27}
    },
    {
        'id': 10203003,
        'name': '结丹护符·改',
        'quality': 2,
        'position': EquipPart.AMULET,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'outer_attack': 70},
        'extend_attrs': {'hit': 26, 'crit': 28}
    },
    {
        'id': 10203004,
        'name': '金丹护符·真',
        'quality': 2,
        'position': EquipPart.AMULET,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'outer_attack': 69},
        'extend_attrs': {'hit': 28, 'crit': 28}
    },
    {
        'id': 10203005,
        'name': '开光护符·灵',
        'quality': 2,
        'position': EquipPart.AMULET,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'outer_attack': 75},
        'extend_attrs': {'hit': 29, 'crit': 26}
    },
    {
        'id': 10203100,
        'name': '结丹·青龙护符',
        'quality': 2,
        'position': EquipPart.AMULET,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'outer_attack': 79},
        'extend_attrs': {'hit': 30, 'crit': 30, 'hp': 288}
    },
    {
        'id': 10203101,
        'name': '结丹·白虎护符',
        'quality': 2,
        'position': EquipPart.AMULET,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'outer_attack': 79},
        'extend_attrs': {'hit': 30, 'crit': 30, 'hp': 288}
    },
    {
        'id': 10203102,
        'name': '结丹·朱雀护符',
        'quality': 2,
        'position': EquipPart.AMULET,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'outer_attack': 79},
        'extend_attrs': {'hit': 30, 'crit': 30, 'hp': 288}
    },
    {
        'id': 10204000,
        'name': '结丹头盔',
        'quality': 2,
        'position': EquipPart.HELMET,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 37, 'outer_defense': 36},
        'extend_attrs': {'inner_defense': 27, 'outer_defense': 28}
    },
    {
        'id': 10204001,
        'name': '金丹头盔',
        'quality': 2,
        'position': EquipPart.HELMET,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 36, 'outer_defense': 37},
        'extend_attrs': {'inner_defense': 29, 'outer_defense': 29}
    },
    {
        'id': 10204002,
        'name': '开光头盔',
        'quality': 2,
        'position': EquipPart.HELMET,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 36, 'outer_defense': 37},
        'extend_attrs': {'inner_defense': 28, 'outer_defense': 29}
    },
    {
        'id': 10204003,
        'name': '结丹头盔·改',
        'quality': 2,
        'position': EquipPart.HELMET,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 36, 'outer_defense': 35},
        'extend_attrs': {'inner_defense': 27, 'outer_defense': 28}
    },
    {
        'id': 10204004,
        'name': '金丹头盔·真',
        'quality': 2,
        'position': EquipPart.HELMET,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 36, 'outer_defense': 37},
        'extend_attrs': {'inner_defense': 28, 'outer_defense': 26}
    },
    {
        'id': 10204005,
        'name': '开光头盔·灵',
        'quality': 2,
        'position': EquipPart.HELMET,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 35, 'outer_defense': 35},
        'extend_attrs': {'inner_defense': 29, 'outer_defense': 27}
    },
    {
        'id': 10204100,
        'name': '结丹·青龙头盔',
        'quality': 2,
        'position': EquipPart.HELMET,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 39, 'outer_defense': 39},
        'extend_attrs': {'inner_defense': 30, 'outer_defense': 30, 'hp': 288}
    },
    {
        'id': 10204101,
        'name': '结丹·白虎头盔',
        'quality': 2,
        'position': EquipPart.HELMET,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 39, 'outer_defense': 39},
        'extend_attrs': {'inner_defense': 30, 'outer_defense': 30, 'hp': 288}
    },
    {
        'id': 10204102,
        'name': '结丹·朱雀头盔',
        'quality': 2,
        'position': EquipPart.HELMET,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 39, 'outer_defense': 39},
        'extend_attrs': {'inner_defense': 30, 'outer_defense': 30, 'hp': 288}
    },
    {
        'id': 10205000,
        'name': '结丹甲胄',
        'quality': 2,
        'position': EquipPart.ARMOR,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 36, 'outer_defense': 36},
        'extend_attrs': {'inner_defense': 29, 'outer_defense': 27}
    },
    {
        'id': 10205001,
        'name': '金丹甲胄',
        'quality': 2,
        'position': EquipPart.ARMOR,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 36, 'outer_defense': 37},
        'extend_attrs': {'inner_defense': 29, 'outer_defense': 28}
    },
    {
        'id': 10205002,
        'name': '开光甲胄',
        'quality': 2,
        'position': EquipPart.ARMOR,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 35, 'outer_defense': 35},
        'extend_attrs': {'inner_defense': 28, 'outer_defense': 28}
    },
    {
        'id': 10205003,
        'name': '结丹甲胄·改',
        'quality': 2,
        'position': EquipPart.ARMOR,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 34, 'outer_defense': 37},
        'extend_attrs': {'inner_defense': 28, 'outer_defense': 27}
    },
    {
        'id': 10205004,
        'name': '金丹甲胄·真',
        'quality': 2,
        'position': EquipPart.ARMOR,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 37, 'outer_defense': 34},
        'extend_attrs': {'inner_defense': 28, 'outer_defense': 27}
    },
    {
        'id': 10205005,
        'name': '开光甲胄·灵',
        'quality': 2,
        'position': EquipPart.ARMOR,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 35, 'outer_defense': 34},
        'extend_attrs': {'inner_defense': 26, 'outer_defense': 28}
    },
    {
        'id': 10205100,
        'name': '结丹·青龙甲胄',
        'quality': 2,
        'position': EquipPart.ARMOR,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 39, 'outer_defense': 39},
        'extend_attrs': {'inner_defense': 30, 'outer_defense': 30, 'hp': 288}
    },
    {
        'id': 10205101,
        'name': '结丹·白虎甲胄',
        'quality': 2,
        'position': EquipPart.ARMOR,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 39, 'outer_defense': 39},
        'extend_attrs': {'inner_defense': 30, 'outer_defense': 30, 'hp': 288}
    },
    {
        'id': 10205102,
        'name': '结丹·朱雀甲胄',
        'quality': 2,
        'position': EquipPart.ARMOR,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 39, 'outer_defense': 39},
        'extend_attrs': {'inner_defense': 30, 'outer_defense': 30, 'hp': 288}
    },
    {
        'id': 10206000,
        'name': '结丹腰带',
        'quality': 2,
        'position': EquipPart.BELT,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'dodge': 36},
        'extend_attrs': {'crit_defense': 27}
    },
    {
        'id': 10206001,
        'name': '金丹腰带',
        'quality': 2,
        'position': EquipPart.BELT,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'dodge': 34},
        'extend_attrs': {'crit_defense': 29}
    },
    {
        'id': 10206002,
        'name': '开光腰带',
        'quality': 2,
        'position': EquipPart.BELT,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'dodge': 35},
        'extend_attrs': {'crit_defense': 26}
    },
    {
        'id': 10206003,
        'name': '结丹腰带·改',
        'quality': 2,
        'position': EquipPart.BELT,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'dodge': 36},
        'extend_attrs': {'crit_defense': 26}
    },
    {
        'id': 10206004,
        'name': '金丹腰带·真',
        'quality': 2,
        'position': EquipPart.BELT,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'dodge': 35},
        'extend_attrs': {'crit_defense': 27}
    },
    {
        'id': 10206005,
        'name': '开光腰带·灵',
        'quality': 2,
        'position': EquipPart.BELT,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'dodge': 35},
        'extend_attrs': {'crit_defense': 27}
    },
    {
        'id': 10206100,
        'name': '结丹·青龙腰带',
        'quality': 2,
        'position': EquipPart.BELT,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'dodge': 39},
        'extend_attrs': {'crit_defense': 30, 'hp': 288}
    },
    {
        'id': 10206101,
        'name': '结丹·白虎腰带',
        'quality': 2,
        'position': EquipPart.BELT,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'dodge': 39},
        'extend_attrs': {'crit_defense': 30, 'hp': 288}
    },
    {
        'id': 10206102,
        'name': '结丹·朱雀腰带',
        'quality': 2,
        'position': EquipPart.BELT,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'dodge': 39},
        'extend_attrs': {'crit_defense': 30, 'hp': 288}
    },
    {
        'id': 10207000,
        'name': '结丹护肩',
        'quality': 2,
        'position': EquipPart.SHOULDER,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'dodge': 34},
        'extend_attrs': {'crit_defense': 28}
    },
    {
        'id': 10207001,
        'name': '金丹护肩',
        'quality': 2,
        'position': EquipPart.SHOULDER,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'dodge': 34},
        'extend_attrs': {'crit_defense': 29}
    },
    {
        'id': 10207002,
        'name': '开光护肩',
        'quality': 2,
        'position': EquipPart.SHOULDER,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'dodge': 34},
        'extend_attrs': {'crit_defense': 28}
    },
    {
        'id': 10207003,
        'name': '结丹护肩·改',
        'quality': 2,
        'position': EquipPart.SHOULDER,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'dodge': 36},
        'extend_attrs': {'crit_defense': 26}
    },
    {
        'id': 10207004,
        'name': '金丹护肩·真',
        'quality': 2,
        'position': EquipPart.SHOULDER,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'dodge': 34},
        'extend_attrs': {'crit_defense': 27}
    },
    {
        'id': 10207005,
        'name': '开光护肩·灵',
        'quality': 2,
        'position': EquipPart.SHOULDER,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'dodge': 35},
        'extend_attrs': {'crit_defense': 29}
    },
    {
        'id': 10207100,
        'name': '结丹·青龙护肩',
        'quality': 2,
        'position': EquipPart.SHOULDER,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'dodge': 39},
        'extend_attrs': {'crit_defense': 30, 'hp': 288}
    },
    {
        'id': 10207101,
        'name': '结丹·白虎护肩',
        'quality': 2,
        'position': EquipPart.SHOULDER,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'dodge': 39},
        'extend_attrs': {'crit_defense': 30, 'hp': 288}
    },
    {
        'id': 10207102,
        'name': '结丹·朱雀护肩',
        'quality': 2,
        'position': EquipPart.SHOULDER,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'dodge': 39},
        'extend_attrs': {'crit_defense': 30, 'hp': 288}
    },
    {
        'id': 10208000,
        'name': '结丹鞋履',
        'quality': 2,
        'position': EquipPart.BOOTS,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 36},
        'extend_attrs': {'dodge': 26}
    },
    {
        'id': 10208001,
        'name': '金丹鞋履',
        'quality': 2,
        'position': EquipPart.BOOTS,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 36},
        'extend_attrs': {'dodge': 28}
    },
    {
        'id': 10208002,
        'name': '开光鞋履',
        'quality': 2,
        'position': EquipPart.BOOTS,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 36},
        'extend_attrs': {'dodge': 26}
    },
    {
        'id': 10208003,
        'name': '结丹鞋履·改',
        'quality': 2,
        'position': EquipPart.BOOTS,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 36},
        'extend_attrs': {'dodge': 27}
    },
    {
        'id': 10208004,
        'name': '金丹鞋履·真',
        'quality': 2,
        'position': EquipPart.BOOTS,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 36},
        'extend_attrs': {'dodge': 27}
    },
    {
        'id': 10208005,
        'name': '开光鞋履·灵',
        'quality': 2,
        'position': EquipPart.BOOTS,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 36},
        'extend_attrs': {'dodge': 29}
    },
    {
        'id': 10208100,
        'name': '结丹·青龙鞋履',
        'quality': 2,
        'position': EquipPart.BOOTS,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 39},
        'extend_attrs': {'dodge': 30, 'hp': 288}
    },
    {
        'id': 10208101,
        'name': '结丹·白虎鞋履',
        'quality': 2,
        'position': EquipPart.BOOTS,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 39},
        'extend_attrs': {'dodge': 30, 'hp': 288}
    },
    {
        'id': 10208102,
        'name': '结丹·朱雀鞋履',
        'quality': 2,
        'position': EquipPart.BOOTS,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 39},
        'extend_attrs': {'dodge': 30, 'hp': 288}
    },
    {
        'id': 10209000,
        'name': '结丹手套',
        'quality': 2,
        'position': EquipPart.GLOVES,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'outer_defense': 36},
        'extend_attrs': {'dodge': 27}
    },
    {
        'id': 10209001,
        'name': '金丹手套',
        'quality': 2,
        'position': EquipPart.GLOVES,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'outer_defense': 37},
        'extend_attrs': {'dodge': 28}
    },
    {
        'id': 10209002,
        'name': '开光手套',
        'quality': 2,
        'position': EquipPart.GLOVES,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'outer_defense': 36},
        'extend_attrs': {'dodge': 29}
    },
    {
        'id': 10209003,
        'name': '结丹手套·改',
        'quality': 2,
        'position': EquipPart.GLOVES,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'outer_defense': 35},
        'extend_attrs': {'dodge': 28}
    },
    {
        'id': 10209004,
        'name': '金丹手套·真',
        'quality': 2,
        'position': EquipPart.GLOVES,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'outer_defense': 35},
        'extend_attrs': {'dodge': 27}
    },
    {
        'id': 10209005,
        'name': '开光手套·灵',
        'quality': 2,
        'position': EquipPart.GLOVES,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'outer_defense': 34},
        'extend_attrs': {'dodge': 28}
    },
    {
        'id': 10209100,
        'name': '结丹·青龙手套',
        'quality': 2,
        'position': EquipPart.GLOVES,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'outer_defense': 39},
        'extend_attrs': {'dodge': 30, 'hp': 288}
    },
    {
        'id': 10209101,
        'name': '结丹·白虎手套',
        'quality': 2,
        'position': EquipPart.GLOVES,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'outer_defense': 39},
        'extend_attrs': {'dodge': 30, 'hp': 288}
    },
    {
        'id': 10209102,
        'name': '结丹·朱雀手套',
        'quality': 2,
        'position': EquipPart.GLOVES,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'outer_defense': 39},
        'extend_attrs': {'dodge': 30, 'hp': 288}
    },
    {
        'id': 10210000,
        'name': '结丹项链',
        'quality': 2,
        'position': EquipPart.NECKLACE,
        'type': EquipmentType.HYBRID,
        'base_attrs': {'inner_attack': 71, 'outer_attack': 68},
        'extend_attrs': {'hp': 283, 'inner_defense': 28, 'outer_defense': 26}
    },
    {
        'id': 10210001,
        'name': '金丹项链',
        'quality': 2,
        'position': EquipPart.NECKLACE,
        'type': EquipmentType.HYBRID,
        'base_attrs': {'inner_attack': 70, 'outer_attack': 73},
        'extend_attrs': {'hp': 293, 'inner_defense': 28, 'outer_defense': 29}
    },
    {
        'id': 10210002,
        'name': '开光项链',
        'quality': 2,
        'position': EquipPart.NECKLACE,
        'type': EquipmentType.HYBRID,
        'base_attrs': {'inner_attack': 75, 'outer_attack': 69},
        'extend_attrs': {'hp': 283, 'inner_defense': 26, 'outer_defense': 28}
    },
    {
        'id': 10210003,
        'name': '结丹项链·改',
        'quality': 2,
        'position': EquipPart.NECKLACE,
        'type': EquipmentType.HYBRID,
        'base_attrs': {'inner_attack': 73, 'outer_attack': 74},
        'extend_attrs': {'hp': 284, 'inner_defense': 29, 'outer_defense': 26}
    },
    {
        'id': 10210004,
        'name': '金丹项链·真',
        'quality': 2,
        'position': EquipPart.NECKLACE,
        'type': EquipmentType.HYBRID,
        'base_attrs': {'inner_attack': 73, 'outer_attack': 71},
        'extend_attrs': {'hp': 288, 'inner_defense': 27, 'outer_defense': 27}
    },
    {
        'id': 10210005,
        'name': '开光项链·灵',
        'quality': 2,
        'position': EquipPart.NECKLACE,
        'type': EquipmentType.HYBRID,
        'base_attrs': {'inner_attack': 74, 'outer_attack': 71},
        'extend_attrs': {'hp': 301, 'inner_defense': 29, 'outer_defense': 28}
    },
    {
        'id': 10210100,
        'name': '结丹·青龙项链',
        'quality': 2,
        'position': EquipPart.NECKLACE,
        'type': EquipmentType.HYBRID,
        'base_attrs': {'inner_attack': 79, 'outer_attack': 79},
        'extend_attrs': {'hp': 604, 'inner_defense': 30, 'outer_defense': 30}
    },
    {
        'id': 10210101,
        'name': '结丹·白虎项链',
        'quality': 2,
        'position': EquipPart.NECKLACE,
        'type': EquipmentType.HYBRID,
        'base_attrs': {'inner_attack': 79, 'outer_attack': 79},
        'extend_attrs': {'hp': 604, 'inner_defense': 30, 'outer_defense': 30}
    },
    {
        'id': 10210102,
        'name': '结丹·朱雀项链',
        'quality': 2,
        'position': EquipPart.NECKLACE,
        'type': EquipmentType.HYBRID,
        'base_attrs': {'inner_attack': 79, 'outer_attack': 79},
        'extend_attrs': {'hp': 604, 'inner_defense': 30, 'outer_defense': 30}
    },
    {
        'id': 10211000,
        'name': '结丹法宝',
        'quality': 2,
        'position': EquipPart.ARTIFACT,
        'type': EquipmentType.HYBRID,
        'base_attrs': {'hit': 34, 'crit': 36},
        'extend_attrs': {'outer_attack': 59, 'inner_attack': 58}
    },
    {
        'id': 10211001,
        'name': '金丹法宝',
        'quality': 2,
        'position': EquipPart.ARTIFACT,
        'type': EquipmentType.HYBRID,
        'base_attrs': {'hit': 36, 'crit': 35},
        'extend_attrs': {'outer_attack': 57, 'inner_attack': 56}
    },
    {
        'id': 10211002,
        'name': '开光法宝',
        'quality': 2,
        'position': EquipPart.ARTIFACT,
        'type': EquipmentType.HYBRID,
        'base_attrs': {'hit': 34, 'crit': 35},
        'extend_attrs': {'outer_attack': 54, 'inner_attack': 55}
    },
    {
        'id': 10211003,
        'name': '结丹法宝·改',
        'quality': 2,
        'position': EquipPart.ARTIFACT,
        'type': EquipmentType.HYBRID,
        'base_attrs': {'hit': 34, 'crit': 34},
        'extend_attrs': {'outer_attack': 56, 'inner_attack': 54}
    },
    {
        'id': 10211004,
        'name': '金丹法宝·真',
        'quality': 2,
        'position': EquipPart.ARTIFACT,
        'type': EquipmentType.HYBRID,
        'base_attrs': {'hit': 37, 'crit': 35},
        'extend_attrs': {'outer_attack': 59, 'inner_attack': 57}
    },
    {
        'id': 10211005,
        'name': '开光法宝·灵',
        'quality': 2,
        'position': EquipPart.ARTIFACT,
        'type': EquipmentType.HYBRID,
        'base_attrs': {'hit': 35, 'crit': 35},
        'extend_attrs': {'outer_attack': 57, 'inner_attack': 55}
    },
    {
        'id': 10211100,
        'name': '结丹·青龙法宝',
        'quality': 2,
        'position': EquipPart.ARTIFACT,
        'type': EquipmentType.HYBRID,
        'base_attrs': {'hit': 39, 'crit': 39},
        'extend_attrs': {'outer_attack': 62, 'inner_attack': 62, 'hp': 288}
    },
    {
        'id': 10211101,
        'name': '结丹·白虎法宝',
        'quality': 2,
        'position': EquipPart.ARTIFACT,
        'type': EquipmentType.HYBRID,
        'base_attrs': {'hit': 39, 'crit': 39},
        'extend_attrs': {'outer_attack': 62, 'inner_attack': 62, 'hp': 288}
    },
    {
        'id': 10211102,
        'name': '结丹·朱雀法宝',
        'quality': 2,
        'position': EquipPart.ARTIFACT,
        'type': EquipmentType.HYBRID,
        'base_attrs': {'hit': 39, 'crit': 39},
        'extend_attrs': {'outer_attack': 62, 'inner_attack': 62, 'hp': 288}
    },
    {
        'id': 10300000,
        'name': '元婴剑',
        'quality': 3,
        'position': EquipPart.WEAPON,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'inner_attack': 97, 'outer_attack': 99},
        'extend_attrs': {'hp': 366, 'hit': 37, 'crit': 38}
    },
    {
        'id': 10300001,
        'name': '化灵刀',
        'quality': 3,
        'position': EquipPart.WEAPON,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'inner_attack': 93, 'outer_attack': 92},
        'extend_attrs': {'hp': 385, 'hit': 38, 'crit': 37}
    },
    {
        'id': 10300002,
        'name': '凝神弓',
        'quality': 3,
        'position': EquipPart.WEAPON,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'inner_attack': 94, 'outer_attack': 95},
        'extend_attrs': {'hp': 382, 'hit': 39, 'crit': 38}
    },
    {
        'id': 10300003,
        'name': '元婴弩',
        'quality': 3,
        'position': EquipPart.WEAPON,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'inner_attack': 94, 'outer_attack': 92},
        'extend_attrs': {'hp': 390, 'hit': 37, 'crit': 39}
    },
    {
        'id': 10300004,
        'name': '化灵枪',
        'quality': 3,
        'position': EquipPart.WEAPON,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'inner_attack': 97, 'outer_attack': 97},
        'extend_attrs': {'hp': 395, 'hit': 37, 'crit': 38}
    },
    {
        'id': 10300005,
        'name': '凝神棍',
        'quality': 3,
        'position': EquipPart.WEAPON,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'inner_attack': 91, 'outer_attack': 97},
        'extend_attrs': {'hp': 394, 'hit': 39, 'crit': 39}
    },
    {
        'id': 10300100,
        'name': '元婴·青龙剑',
        'quality': 3,
        'position': EquipPart.WEAPON,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'inner_attack': 105, 'outer_attack': 105},
        'extend_attrs': {'hp': 806, 'hit': 41, 'crit': 41}
    },
    {
        'id': 10300101,
        'name': '元婴·白虎刀',
        'quality': 3,
        'position': EquipPart.WEAPON,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'inner_attack': 105, 'outer_attack': 105},
        'extend_attrs': {'hp': 806, 'hit': 41, 'crit': 41}
    },
    {
        'id': 10300102,
        'name': '元婴·朱雀弓',
        'quality': 3,
        'position': EquipPart.WEAPON,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'inner_attack': 105, 'outer_attack': 105},
        'extend_attrs': {'hp': 806, 'hit': 41, 'crit': 41}
    },
    {
        'id': 10301000,
        'name': '元婴护腕',
        'quality': 3,
        'position': EquipPart.BRACER,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'hit': 49},
        'extend_attrs': {'outer_attack': 78, 'inner_attack': 75}
    },
    {
        'id': 10301001,
        'name': '化灵护腕',
        'quality': 3,
        'position': EquipPart.BRACER,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'hit': 46},
        'extend_attrs': {'outer_attack': 74, 'inner_attack': 73}
    },
    {
        'id': 10301002,
        'name': '凝神护腕',
        'quality': 3,
        'position': EquipPart.BRACER,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'hit': 49},
        'extend_attrs': {'outer_attack': 74, 'inner_attack': 79}
    },
    {
        'id': 10301003,
        'name': '元婴护腕·改',
        'quality': 3,
        'position': EquipPart.BRACER,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'hit': 50},
        'extend_attrs': {'outer_attack': 77, 'inner_attack': 77}
    },
    {
        'id': 10301004,
        'name': '化灵护腕·真',
        'quality': 3,
        'position': EquipPart.BRACER,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'hit': 48},
        'extend_attrs': {'outer_attack': 77, 'inner_attack': 77}
    },
    {
        'id': 10301005,
        'name': '凝神护腕·灵',
        'quality': 3,
        'position': EquipPart.BRACER,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'hit': 46},
        'extend_attrs': {'outer_attack': 76, 'inner_attack': 72}
    },
    {
        'id': 10301100,
        'name': '元婴·青龙护腕',
        'quality': 3,
        'position': EquipPart.BRACER,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'hit': 52},
        'extend_attrs': {'outer_attack': 83, 'inner_attack': 83, 'hp': 384}
    },
    {
        'id': 10301101,
        'name': '元婴·白虎护腕',
        'quality': 3,
        'position': EquipPart.BRACER,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'hit': 52},
        'extend_attrs': {'outer_attack': 83, 'inner_attack': 83, 'hp': 384}
    },
    {
        'id': 10301102,
        'name': '元婴·朱雀护腕',
        'quality': 3,
        'position': EquipPart.BRACER,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'hit': 52},
        'extend_attrs': {'outer_attack': 83, 'inner_attack': 83, 'hp': 384}
    },
    {
        'id': 10302000,
        'name': '元婴戒指',
        'quality': 3,
        'position': EquipPart.RING,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'inner_attack': 97},
        'extend_attrs': {'hit': 36, 'crit': 37}
    },
    {
        'id': 10302001,
        'name': '化灵戒指',
        'quality': 3,
        'position': EquipPart.RING,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'inner_attack': 100},
        'extend_attrs': {'hit': 36, 'crit': 36}
    },
    {
        'id': 10302002,
        'name': '凝神戒指',
        'quality': 3,
        'position': EquipPart.RING,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'inner_attack': 99},
        'extend_attrs': {'hit': 38, 'crit': 37}
    },
    {
        'id': 10302003,
        'name': '元婴戒指·改',
        'quality': 3,
        'position': EquipPart.RING,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'inner_attack': 91},
        'extend_attrs': {'hit': 36, 'crit': 37}
    },
    {
        'id': 10302004,
        'name': '化灵戒指·真',
        'quality': 3,
        'position': EquipPart.RING,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'inner_attack': 100},
        'extend_attrs': {'hit': 36, 'crit': 37}
    },
    {
        'id': 10302005,
        'name': '凝神戒指·灵',
        'quality': 3,
        'position': EquipPart.RING,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'inner_attack': 95},
        'extend_attrs': {'hit': 36, 'crit': 39}
    },
    {
        'id': 10302100,
        'name': '元婴·青龙戒指',
        'quality': 3,
        'position': EquipPart.RING,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'inner_attack': 105},
        'extend_attrs': {'hit': 41, 'crit': 41, 'hp': 384}
    },
    {
        'id': 10302101,
        'name': '元婴·白虎戒指',
        'quality': 3,
        'position': EquipPart.RING,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'inner_attack': 105},
        'extend_attrs': {'hit': 41, 'crit': 41, 'hp': 384}
    },
    {
        'id': 10302102,
        'name': '元婴·朱雀戒指',
        'quality': 3,
        'position': EquipPart.RING,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'inner_attack': 105},
        'extend_attrs': {'hit': 41, 'crit': 41, 'hp': 384}
    },
    {
        'id': 10303000,
        'name': '元婴护符',
        'quality': 3,
        'position': EquipPart.AMULET,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'outer_attack': 91},
        'extend_attrs': {'hit': 38, 'crit': 39}
    },
    {
        'id': 10303001,
        'name': '化灵护符',
        'quality': 3,
        'position': EquipPart.AMULET,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'outer_attack': 98},
        'extend_attrs': {'hit': 36, 'crit': 39}
    },
    {
        'id': 10303002,
        'name': '凝神护符',
        'quality': 3,
        'position': EquipPart.AMULET,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'outer_attack': 92},
        'extend_attrs': {'hit': 38, 'crit': 38}
    },
    {
        'id': 10303003,
        'name': '元婴护符·改',
        'quality': 3,
        'position': EquipPart.AMULET,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'outer_attack': 93},
        'extend_attrs': {'hit': 36, 'crit': 36}
    },
    {
        'id': 10303004,
        'name': '化灵护符·真',
        'quality': 3,
        'position': EquipPart.AMULET,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'outer_attack': 98},
        'extend_attrs': {'hit': 38, 'crit': 37}
    },
    {
        'id': 10303005,
        'name': '凝神护符·灵',
        'quality': 3,
        'position': EquipPart.AMULET,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'outer_attack': 96},
        'extend_attrs': {'hit': 36, 'crit': 37}
    },
    {
        'id': 10303100,
        'name': '元婴·青龙护符',
        'quality': 3,
        'position': EquipPart.AMULET,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'outer_attack': 105},
        'extend_attrs': {'hit': 41, 'crit': 41, 'hp': 384}
    },
    {
        'id': 10303101,
        'name': '元婴·白虎护符',
        'quality': 3,
        'position': EquipPart.AMULET,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'outer_attack': 105},
        'extend_attrs': {'hit': 41, 'crit': 41, 'hp': 384}
    },
    {
        'id': 10303102,
        'name': '元婴·朱雀护符',
        'quality': 3,
        'position': EquipPart.AMULET,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'outer_attack': 105},
        'extend_attrs': {'hit': 41, 'crit': 41, 'hp': 384}
    },
    {
        'id': 10304000,
        'name': '元婴头盔',
        'quality': 3,
        'position': EquipPart.HELMET,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 46, 'outer_defense': 46},
        'extend_attrs': {'inner_defense': 39, 'outer_defense': 38}
    },
    {
        'id': 10304001,
        'name': '化灵头盔',
        'quality': 3,
        'position': EquipPart.HELMET,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 47, 'outer_defense': 46},
        'extend_attrs': {'inner_defense': 37, 'outer_defense': 38}
    },
    {
        'id': 10304002,
        'name': '凝神头盔',
        'quality': 3,
        'position': EquipPart.HELMET,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 47, 'outer_defense': 47},
        'extend_attrs': {'inner_defense': 39, 'outer_defense': 39}
    },
    {
        'id': 10304003,
        'name': '元婴头盔·改',
        'quality': 3,
        'position': EquipPart.HELMET,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 48, 'outer_defense': 46},
        'extend_attrs': {'inner_defense': 36, 'outer_defense': 39}
    },
    {
        'id': 10304004,
        'name': '化灵头盔·真',
        'quality': 3,
        'position': EquipPart.HELMET,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 46, 'outer_defense': 46},
        'extend_attrs': {'inner_defense': 36, 'outer_defense': 39}
    },
    {
        'id': 10304005,
        'name': '凝神头盔·灵',
        'quality': 3,
        'position': EquipPart.HELMET,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 46, 'outer_defense': 49},
        'extend_attrs': {'inner_defense': 38, 'outer_defense': 38}
    },
    {
        'id': 10304100,
        'name': '元婴·青龙头盔',
        'quality': 3,
        'position': EquipPart.HELMET,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 52, 'outer_defense': 52},
        'extend_attrs': {'inner_defense': 41, 'outer_defense': 41, 'hp': 384}
    },
    {
        'id': 10304101,
        'name': '元婴·白虎头盔',
        'quality': 3,
        'position': EquipPart.HELMET,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 52, 'outer_defense': 52},
        'extend_attrs': {'inner_defense': 41, 'outer_defense': 41, 'hp': 384}
    },
    {
        'id': 10304102,
        'name': '元婴·朱雀头盔',
        'quality': 3,
        'position': EquipPart.HELMET,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 52, 'outer_defense': 52},
        'extend_attrs': {'inner_defense': 41, 'outer_defense': 41, 'hp': 384}
    },
    {
        'id': 10305000,
        'name': '元婴甲胄',
        'quality': 3,
        'position': EquipPart.ARMOR,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 48, 'outer_defense': 50},
        'extend_attrs': {'inner_defense': 39, 'outer_defense': 38}
    },
    {
        'id': 10305001,
        'name': '化灵甲胄',
        'quality': 3,
        'position': EquipPart.ARMOR,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 46, 'outer_defense': 46},
        'extend_attrs': {'inner_defense': 38, 'outer_defense': 38}
    },
    {
        'id': 10305002,
        'name': '凝神甲胄',
        'quality': 3,
        'position': EquipPart.ARMOR,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 46, 'outer_defense': 46},
        'extend_attrs': {'inner_defense': 39, 'outer_defense': 38}
    },
    {
        'id': 10305003,
        'name': '元婴甲胄·改',
        'quality': 3,
        'position': EquipPart.ARMOR,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 47, 'outer_defense': 48},
        'extend_attrs': {'inner_defense': 38, 'outer_defense': 38}
    },
    {
        'id': 10305004,
        'name': '化灵甲胄·真',
        'quality': 3,
        'position': EquipPart.ARMOR,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 46, 'outer_defense': 46},
        'extend_attrs': {'inner_defense': 37, 'outer_defense': 39}
    },
    {
        'id': 10305005,
        'name': '凝神甲胄·灵',
        'quality': 3,
        'position': EquipPart.ARMOR,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 48, 'outer_defense': 46},
        'extend_attrs': {'inner_defense': 38, 'outer_defense': 38}
    },
    {
        'id': 10305100,
        'name': '元婴·青龙甲胄',
        'quality': 3,
        'position': EquipPart.ARMOR,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 52, 'outer_defense': 52},
        'extend_attrs': {'inner_defense': 41, 'outer_defense': 41, 'hp': 384}
    },
    {
        'id': 10305101,
        'name': '元婴·白虎甲胄',
        'quality': 3,
        'position': EquipPart.ARMOR,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 52, 'outer_defense': 52},
        'extend_attrs': {'inner_defense': 41, 'outer_defense': 41, 'hp': 384}
    },
    {
        'id': 10305102,
        'name': '元婴·朱雀甲胄',
        'quality': 3,
        'position': EquipPart.ARMOR,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 52, 'outer_defense': 52},
        'extend_attrs': {'inner_defense': 41, 'outer_defense': 41, 'hp': 384}
    },
    {
        'id': 10306000,
        'name': '元婴腰带',
        'quality': 3,
        'position': EquipPart.BELT,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'dodge': 49},
        'extend_attrs': {'crit_defense': 36}
    },
    {
        'id': 10306001,
        'name': '化灵腰带',
        'quality': 3,
        'position': EquipPart.BELT,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'dodge': 48},
        'extend_attrs': {'crit_defense': 36}
    },
    {
        'id': 10306002,
        'name': '凝神腰带',
        'quality': 3,
        'position': EquipPart.BELT,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'dodge': 49},
        'extend_attrs': {'crit_defense': 39}
    },
    {
        'id': 10306003,
        'name': '元婴腰带·改',
        'quality': 3,
        'position': EquipPart.BELT,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'dodge': 48},
        'extend_attrs': {'crit_defense': 37}
    },
    {
        'id': 10306004,
        'name': '化灵腰带·真',
        'quality': 3,
        'position': EquipPart.BELT,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'dodge': 49},
        'extend_attrs': {'crit_defense': 38}
    },
    {
        'id': 10306005,
        'name': '凝神腰带·灵',
        'quality': 3,
        'position': EquipPart.BELT,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'dodge': 49},
        'extend_attrs': {'crit_defense': 36}
    },
    {
        'id': 10306100,
        'name': '元婴·青龙腰带',
        'quality': 3,
        'position': EquipPart.BELT,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'dodge': 52},
        'extend_attrs': {'crit_defense': 41, 'hp': 384}
    },
    {
        'id': 10306101,
        'name': '元婴·白虎腰带',
        'quality': 3,
        'position': EquipPart.BELT,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'dodge': 52},
        'extend_attrs': {'crit_defense': 41, 'hp': 384}
    },
    {
        'id': 10306102,
        'name': '元婴·朱雀腰带',
        'quality': 3,
        'position': EquipPart.BELT,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'dodge': 52},
        'extend_attrs': {'crit_defense': 41, 'hp': 384}
    },
    {
        'id': 10307000,
        'name': '元婴护肩',
        'quality': 3,
        'position': EquipPart.SHOULDER,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'dodge': 47},
        'extend_attrs': {'crit_defense': 36}
    },
    {
        'id': 10307001,
        'name': '化灵护肩',
        'quality': 3,
        'position': EquipPart.SHOULDER,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'dodge': 46},
        'extend_attrs': {'crit_defense': 36}
    },
    {
        'id': 10307002,
        'name': '凝神护肩',
        'quality': 3,
        'position': EquipPart.SHOULDER,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'dodge': 50},
        'extend_attrs': {'crit_defense': 37}
    },
    {
        'id': 10307003,
        'name': '元婴护肩·改',
        'quality': 3,
        'position': EquipPart.SHOULDER,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'dodge': 50},
        'extend_attrs': {'crit_defense': 38}
    },
    {
        'id': 10307004,
        'name': '化灵护肩·真',
        'quality': 3,
        'position': EquipPart.SHOULDER,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'dodge': 48},
        'extend_attrs': {'crit_defense': 36}
    },
    {
        'id': 10307005,
        'name': '凝神护肩·灵',
        'quality': 3,
        'position': EquipPart.SHOULDER,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'dodge': 46},
        'extend_attrs': {'crit_defense': 39}
    },
    {
        'id': 10307100,
        'name': '元婴·青龙护肩',
        'quality': 3,
        'position': EquipPart.SHOULDER,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'dodge': 52},
        'extend_attrs': {'crit_defense': 41, 'hp': 384}
    },
    {
        'id': 10307101,
        'name': '元婴·白虎护肩',
        'quality': 3,
        'position': EquipPart.SHOULDER,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'dodge': 52},
        'extend_attrs': {'crit_defense': 41, 'hp': 384}
    },
    {
        'id': 10307102,
        'name': '元婴·朱雀护肩',
        'quality': 3,
        'position': EquipPart.SHOULDER,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'dodge': 52},
        'extend_attrs': {'crit_defense': 41, 'hp': 384}
    },
    {
        'id': 10308000,
        'name': '元婴鞋履',
        'quality': 3,
        'position': EquipPart.BOOTS,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 49},
        'extend_attrs': {'dodge': 36}
    },
    {
        'id': 10308001,
        'name': '化灵鞋履',
        'quality': 3,
        'position': EquipPart.BOOTS,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 46},
        'extend_attrs': {'dodge': 39}
    },
    {
        'id': 10308002,
        'name': '凝神鞋履',
        'quality': 3,
        'position': EquipPart.BOOTS,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 47},
        'extend_attrs': {'dodge': 37}
    },
    {
        'id': 10308003,
        'name': '元婴鞋履·改',
        'quality': 3,
        'position': EquipPart.BOOTS,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 48},
        'extend_attrs': {'dodge': 39}
    },
    {
        'id': 10308004,
        'name': '化灵鞋履·真',
        'quality': 3,
        'position': EquipPart.BOOTS,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 49},
        'extend_attrs': {'dodge': 38}
    },
    {
        'id': 10308005,
        'name': '凝神鞋履·灵',
        'quality': 3,
        'position': EquipPart.BOOTS,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 49},
        'extend_attrs': {'dodge': 38}
    },
    {
        'id': 10308100,
        'name': '元婴·青龙鞋履',
        'quality': 3,
        'position': EquipPart.BOOTS,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 52},
        'extend_attrs': {'dodge': 41, 'hp': 384}
    },
    {
        'id': 10308101,
        'name': '元婴·白虎鞋履',
        'quality': 3,
        'position': EquipPart.BOOTS,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 52},
        'extend_attrs': {'dodge': 41, 'hp': 384}
    },
    {
        'id': 10308102,
        'name': '元婴·朱雀鞋履',
        'quality': 3,
        'position': EquipPart.BOOTS,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 52},
        'extend_attrs': {'dodge': 41, 'hp': 384}
    },
    {
        'id': 10309000,
        'name': '元婴手套',
        'quality': 3,
        'position': EquipPart.GLOVES,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'outer_defense': 46},
        'extend_attrs': {'dodge': 37}
    },
    {
        'id': 10309001,
        'name': '化灵手套',
        'quality': 3,
        'position': EquipPart.GLOVES,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'outer_defense': 47},
        'extend_attrs': {'dodge': 39}
    },
    {
        'id': 10309002,
        'name': '凝神手套',
        'quality': 3,
        'position': EquipPart.GLOVES,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'outer_defense': 48},
        'extend_attrs': {'dodge': 38}
    },
    {
        'id': 10309003,
        'name': '元婴手套·改',
        'quality': 3,
        'position': EquipPart.GLOVES,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'outer_defense': 46},
        'extend_attrs': {'dodge': 37}
    },
    {
        'id': 10309004,
        'name': '化灵手套·真',
        'quality': 3,
        'position': EquipPart.GLOVES,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'outer_defense': 47},
        'extend_attrs': {'dodge': 37}
    },
    {
        'id': 10309005,
        'name': '凝神手套·灵',
        'quality': 3,
        'position': EquipPart.GLOVES,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'outer_defense': 47},
        'extend_attrs': {'dodge': 36}
    },
    {
        'id': 10309100,
        'name': '元婴·青龙手套',
        'quality': 3,
        'position': EquipPart.GLOVES,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'outer_defense': 52},
        'extend_attrs': {'dodge': 41, 'hp': 384}
    },
    {
        'id': 10309101,
        'name': '元婴·白虎手套',
        'quality': 3,
        'position': EquipPart.GLOVES,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'outer_defense': 52},
        'extend_attrs': {'dodge': 41, 'hp': 384}
    },
    {
        'id': 10309102,
        'name': '元婴·朱雀手套',
        'quality': 3,
        'position': EquipPart.GLOVES,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'outer_defense': 52},
        'extend_attrs': {'dodge': 41, 'hp': 384}
    },
    {
        'id': 10310000,
        'name': '元婴项链',
        'quality': 3,
        'position': EquipPart.NECKLACE,
        'type': EquipmentType.HYBRID,
        'base_attrs': {'inner_attack': 98, 'outer_attack': 99},
        'extend_attrs': {'hp': 370, 'inner_defense': 38, 'outer_defense': 39}
    },
    {
        'id': 10310001,
        'name': '化灵项链',
        'quality': 3,
        'position': EquipPart.NECKLACE,
        'type': EquipmentType.HYBRID,
        'base_attrs': {'inner_attack': 95, 'outer_attack': 94},
        'extend_attrs': {'hp': 369, 'inner_defense': 38, 'outer_defense': 36}
    },
    {
        'id': 10310002,
        'name': '凝神项链',
        'quality': 3,
        'position': EquipPart.NECKLACE,
        'type': EquipmentType.HYBRID,
        'base_attrs': {'inner_attack': 93, 'outer_attack': 97},
        'extend_attrs': {'hp': 364, 'inner_defense': 38, 'outer_defense': 39}
    },
    {
        'id': 10310003,
        'name': '元婴项链·改',
        'quality': 3,
        'position': EquipPart.NECKLACE,
        'type': EquipmentType.HYBRID,
        'base_attrs': {'inner_attack': 96, 'outer_attack': 93},
        'extend_attrs': {'hp': 401, 'inner_defense': 36, 'outer_defense': 36}
    },
    {
        'id': 10310004,
        'name': '化灵项链·真',
        'quality': 3,
        'position': EquipPart.NECKLACE,
        'type': EquipmentType.HYBRID,
        'base_attrs': {'inner_attack': 100, 'outer_attack': 92},
        'extend_attrs': {'hp': 395, 'inner_defense': 38, 'outer_defense': 36}
    },
    {
        'id': 10310005,
        'name': '凝神项链·灵',
        'quality': 3,
        'position': EquipPart.NECKLACE,
        'type': EquipmentType.HYBRID,
        'base_attrs': {'inner_attack': 100, 'outer_attack': 91},
        'extend_attrs': {'hp': 371, 'inner_defense': 38, 'outer_defense': 38}
    },
    {
        'id': 10310100,
        'name': '元婴·青龙项链',
        'quality': 3,
        'position': EquipPart.NECKLACE,
        'type': EquipmentType.HYBRID,
        'base_attrs': {'inner_attack': 105, 'outer_attack': 105},
        'extend_attrs': {'hp': 806, 'inner_defense': 41, 'outer_defense': 41}
    },
    {
        'id': 10310101,
        'name': '元婴·白虎项链',
        'quality': 3,
        'position': EquipPart.NECKLACE,
        'type': EquipmentType.HYBRID,
        'base_attrs': {'inner_attack': 105, 'outer_attack': 105},
        'extend_attrs': {'hp': 806, 'inner_defense': 41, 'outer_defense': 41}
    },
    {
        'id': 10310102,
        'name': '元婴·朱雀项链',
        'quality': 3,
        'position': EquipPart.NECKLACE,
        'type': EquipmentType.HYBRID,
        'base_attrs': {'inner_attack': 105, 'outer_attack': 105},
        'extend_attrs': {'hp': 806, 'inner_defense': 41, 'outer_defense': 41}
    },
    {
        'id': 10311000,
        'name': '元婴法宝',
        'quality': 3,
        'position': EquipPart.ARTIFACT,
        'type': EquipmentType.HYBRID,
        'base_attrs': {'hit': 47, 'crit': 48},
        'extend_attrs': {'outer_attack': 79, 'inner_attack': 75}
    },
    {
        'id': 10311001,
        'name': '化灵法宝',
        'quality': 3,
        'position': EquipPart.ARTIFACT,
        'type': EquipmentType.HYBRID,
        'base_attrs': {'hit': 50, 'crit': 48},
        'extend_attrs': {'outer_attack': 76, 'inner_attack': 72}
    },
    {
        'id': 10311002,
        'name': '凝神法宝',
        'quality': 3,
        'position': EquipPart.ARTIFACT,
        'type': EquipmentType.HYBRID,
        'base_attrs': {'hit': 48, 'crit': 48},
        'extend_attrs': {'outer_attack': 78, 'inner_attack': 78}
    },
    {
        'id': 10311003,
        'name': '元婴法宝·改',
        'quality': 3,
        'position': EquipPart.ARTIFACT,
        'type': EquipmentType.HYBRID,
        'base_attrs': {'hit': 46, 'crit': 46},
        'extend_attrs': {'outer_attack': 76, 'inner_attack': 79}
    },
    {
        'id': 10311004,
        'name': '化灵法宝·真',
        'quality': 3,
        'position': EquipPart.ARTIFACT,
        'type': EquipmentType.HYBRID,
        'base_attrs': {'hit': 47, 'crit': 48},
        'extend_attrs': {'outer_attack': 76, 'inner_attack': 78}
    },
    {
        'id': 10311005,
        'name': '凝神法宝·灵',
        'quality': 3,
        'position': EquipPart.ARTIFACT,
        'type': EquipmentType.HYBRID,
        'base_attrs': {'hit': 47, 'crit': 50},
        'extend_attrs': {'outer_attack': 78, 'inner_attack': 77}
    },
    {
        'id': 10311100,
        'name': '元婴·青龙法宝',
        'quality': 3,
        'position': EquipPart.ARTIFACT,
        'type': EquipmentType.HYBRID,
        'base_attrs': {'hit': 52, 'crit': 52},
        'extend_attrs': {'outer_attack': 83, 'inner_attack': 83, 'hp': 384}
    },
    {
        'id': 10311101,
        'name': '元婴·白虎法宝',
        'quality': 3,
        'position': EquipPart.ARTIFACT,
        'type': EquipmentType.HYBRID,
        'base_attrs': {'hit': 52, 'crit': 52},
        'extend_attrs': {'outer_attack': 83, 'inner_attack': 83, 'hp': 384}
    },
    {
        'id': 10311102,
        'name': '元婴·朱雀法宝',
        'quality': 3,
        'position': EquipPart.ARTIFACT,
        'type': EquipmentType.HYBRID,
        'base_attrs': {'hit': 52, 'crit': 52},
        'extend_attrs': {'outer_attack': 83, 'inner_attack': 83, 'hp': 384}
    },
    {
        'id': 10400000,
        'name': '化神剑',
        'quality': 4,
        'position': EquipPart.WEAPON,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'inner_attack': 124, 'outer_attack': 124},
        'extend_attrs': {'hp': 463, 'hit': 47, 'crit': 47}
    },
    {
        'id': 10400001,
        'name': '分神刀',
        'quality': 4,
        'position': EquipPart.WEAPON,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'inner_attack': 124, 'outer_attack': 124},
        'extend_attrs': {'hp': 482, 'hit': 49, 'crit': 49}
    },
    {
        'id': 10400002,
        'name': '元神弓',
        'quality': 4,
        'position': EquipPart.WEAPON,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'inner_attack': 121, 'outer_attack': 125},
        'extend_attrs': {'hp': 456, 'hit': 49, 'crit': 49}
    },
    {
        'id': 10400003,
        'name': '化神弩',
        'quality': 4,
        'position': EquipPart.WEAPON,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'inner_attack': 116, 'outer_attack': 121},
        'extend_attrs': {'hp': 496, 'hit': 45, 'crit': 50}
    },
    {
        'id': 10400004,
        'name': '分神枪',
        'quality': 4,
        'position': EquipPart.WEAPON,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'inner_attack': 116, 'outer_attack': 116},
        'extend_attrs': {'hp': 460, 'hit': 47, 'crit': 46}
    },
    {
        'id': 10400005,
        'name': '元神棍',
        'quality': 4,
        'position': EquipPart.WEAPON,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'inner_attack': 118, 'outer_attack': 115},
        'extend_attrs': {'hp': 469, 'hit': 48, 'crit': 46}
    },
    {
        'id': 10400100,
        'name': '化神·青龙剑',
        'quality': 4,
        'position': EquipPart.WEAPON,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'inner_attack': 132, 'outer_attack': 132},
        'extend_attrs': {'hp': 1008, 'hit': 52, 'crit': 52}
    },
    {
        'id': 10400101,
        'name': '化神·白虎刀',
        'quality': 4,
        'position': EquipPart.WEAPON,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'inner_attack': 132, 'outer_attack': 132},
        'extend_attrs': {'hp': 1008, 'hit': 52, 'crit': 52}
    },
    {
        'id': 10400102,
        'name': '化神·朱雀弓',
        'quality': 4,
        'position': EquipPart.WEAPON,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'inner_attack': 132, 'outer_attack': 132},
        'extend_attrs': {'hp': 1008, 'hit': 52, 'crit': 52}
    },
    {
        'id': 10401000,
        'name': '化神护腕',
        'quality': 4,
        'position': EquipPart.BRACER,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'hit': 58},
        'extend_attrs': {'outer_attack': 92, 'inner_attack': 99}
    },
    {
        'id': 10401001,
        'name': '分神护腕',
        'quality': 4,
        'position': EquipPart.BRACER,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'hit': 62},
        'extend_attrs': {'outer_attack': 98, 'inner_attack': 93}
    },
    {
        'id': 10401002,
        'name': '元神护腕',
        'quality': 4,
        'position': EquipPart.BRACER,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'hit': 59},
        'extend_attrs': {'outer_attack': 99, 'inner_attack': 100}
    },
    {
        'id': 10401003,
        'name': '化神护腕·改',
        'quality': 4,
        'position': EquipPart.BRACER,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'hit': 58},
        'extend_attrs': {'outer_attack': 97, 'inner_attack': 99}
    },
    {
        'id': 10401004,
        'name': '分神护腕·真',
        'quality': 4,
        'position': EquipPart.BRACER,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'hit': 58},
        'extend_attrs': {'outer_attack': 96, 'inner_attack': 91}
    },
    {
        'id': 10401005,
        'name': '元神护腕·灵',
        'quality': 4,
        'position': EquipPart.BRACER,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'hit': 58},
        'extend_attrs': {'outer_attack': 93, 'inner_attack': 92}
    },
    {
        'id': 10401100,
        'name': '化神·青龙护腕',
        'quality': 4,
        'position': EquipPart.BRACER,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'hit': 66},
        'extend_attrs': {'outer_attack': 105, 'inner_attack': 105, 'hp': 480}
    },
    {
        'id': 10401101,
        'name': '化神·白虎护腕',
        'quality': 4,
        'position': EquipPart.BRACER,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'hit': 66},
        'extend_attrs': {'outer_attack': 105, 'inner_attack': 105, 'hp': 480}
    },
    {
        'id': 10401102,
        'name': '化神·朱雀护腕',
        'quality': 4,
        'position': EquipPart.BRACER,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'hit': 66},
        'extend_attrs': {'outer_attack': 105, 'inner_attack': 105, 'hp': 480}
    },
    {
        'id': 10402000,
        'name': '化神戒指',
        'quality': 4,
        'position': EquipPart.RING,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'inner_attack': 114},
        'extend_attrs': {'hit': 46, 'crit': 48}
    },
    {
        'id': 10402001,
        'name': '分神戒指',
        'quality': 4,
        'position': EquipPart.RING,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'inner_attack': 117},
        'extend_attrs': {'hit': 47, 'crit': 46}
    },
    {
        'id': 10402002,
        'name': '元神戒指',
        'quality': 4,
        'position': EquipPart.RING,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'inner_attack': 120},
        'extend_attrs': {'hit': 46, 'crit': 46}
    },
    {
        'id': 10402003,
        'name': '化神戒指·改',
        'quality': 4,
        'position': EquipPart.RING,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'inner_attack': 120},
        'extend_attrs': {'hit': 47, 'crit': 47}
    },
    {
        'id': 10402004,
        'name': '分神戒指·真',
        'quality': 4,
        'position': EquipPart.RING,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'inner_attack': 120},
        'extend_attrs': {'hit': 46, 'crit': 47}
    },
    {
        'id': 10402005,
        'name': '元神戒指·灵',
        'quality': 4,
        'position': EquipPart.RING,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'inner_attack': 122},
        'extend_attrs': {'hit': 46, 'crit': 48}
    },
    {
        'id': 10402100,
        'name': '化神·青龙戒指',
        'quality': 4,
        'position': EquipPart.RING,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'inner_attack': 132},
        'extend_attrs': {'hit': 52, 'crit': 52, 'hp': 480}
    },
    {
        'id': 10402101,
        'name': '化神·白虎戒指',
        'quality': 4,
        'position': EquipPart.RING,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'inner_attack': 132},
        'extend_attrs': {'hit': 52, 'crit': 52, 'hp': 480}
    },
    {
        'id': 10402102,
        'name': '化神·朱雀戒指',
        'quality': 4,
        'position': EquipPart.RING,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'inner_attack': 132},
        'extend_attrs': {'hit': 52, 'crit': 52, 'hp': 480}
    },
    {
        'id': 10403000,
        'name': '化神护符',
        'quality': 4,
        'position': EquipPart.AMULET,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'outer_attack': 117},
        'extend_attrs': {'hit': 49, 'crit': 46}
    },
    {
        'id': 10403001,
        'name': '分神护符',
        'quality': 4,
        'position': EquipPart.AMULET,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'outer_attack': 120},
        'extend_attrs': {'hit': 48, 'crit': 48}
    },
    {
        'id': 10403002,
        'name': '元神护符',
        'quality': 4,
        'position': EquipPart.AMULET,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'outer_attack': 122},
        'extend_attrs': {'hit': 45, 'crit': 45}
    },
    {
        'id': 10403003,
        'name': '化神护符·改',
        'quality': 4,
        'position': EquipPart.AMULET,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'outer_attack': 117},
        'extend_attrs': {'hit': 46, 'crit': 45}
    },
    {
        'id': 10403004,
        'name': '分神护符·真',
        'quality': 4,
        'position': EquipPart.AMULET,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'outer_attack': 116},
        'extend_attrs': {'hit': 49, 'crit': 47}
    },
    {
        'id': 10403005,
        'name': '元神护符·灵',
        'quality': 4,
        'position': EquipPart.AMULET,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'outer_attack': 117},
        'extend_attrs': {'hit': 46, 'crit': 49}
    },
    {
        'id': 10403100,
        'name': '化神·青龙护符',
        'quality': 4,
        'position': EquipPart.AMULET,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'outer_attack': 132},
        'extend_attrs': {'hit': 52, 'crit': 52, 'hp': 480}
    },
    {
        'id': 10403101,
        'name': '化神·白虎护符',
        'quality': 4,
        'position': EquipPart.AMULET,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'outer_attack': 132},
        'extend_attrs': {'hit': 52, 'crit': 52, 'hp': 480}
    },
    {
        'id': 10403102,
        'name': '化神·朱雀护符',
        'quality': 4,
        'position': EquipPart.AMULET,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'outer_attack': 132},
        'extend_attrs': {'hit': 52, 'crit': 52, 'hp': 480}
    },
    {
        'id': 10404000,
        'name': '化神头盔',
        'quality': 4,
        'position': EquipPart.HELMET,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 61, 'outer_defense': 58},
        'extend_attrs': {'inner_defense': 45, 'outer_defense': 49}
    },
    {
        'id': 10404001,
        'name': '分神头盔',
        'quality': 4,
        'position': EquipPart.HELMET,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 62, 'outer_defense': 57},
        'extend_attrs': {'inner_defense': 46, 'outer_defense': 47}
    },
    {
        'id': 10404002,
        'name': '元神头盔',
        'quality': 4,
        'position': EquipPart.HELMET,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 59, 'outer_defense': 57},
        'extend_attrs': {'inner_defense': 46, 'outer_defense': 50}
    },
    {
        'id': 10404003,
        'name': '化神头盔·改',
        'quality': 4,
        'position': EquipPart.HELMET,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 60, 'outer_defense': 59},
        'extend_attrs': {'inner_defense': 48, 'outer_defense': 46}
    },
    {
        'id': 10404004,
        'name': '分神头盔·真',
        'quality': 4,
        'position': EquipPart.HELMET,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 60, 'outer_defense': 58},
        'extend_attrs': {'inner_defense': 49, 'outer_defense': 46}
    },
    {
        'id': 10404005,
        'name': '元神头盔·灵',
        'quality': 4,
        'position': EquipPart.HELMET,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 57, 'outer_defense': 57},
        'extend_attrs': {'inner_defense': 47, 'outer_defense': 46}
    },
    {
        'id': 10404100,
        'name': '化神·青龙头盔',
        'quality': 4,
        'position': EquipPart.HELMET,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 66, 'outer_defense': 66},
        'extend_attrs': {'inner_defense': 52, 'outer_defense': 52, 'hp': 480}
    },
    {
        'id': 10404101,
        'name': '化神·白虎头盔',
        'quality': 4,
        'position': EquipPart.HELMET,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 66, 'outer_defense': 66},
        'extend_attrs': {'inner_defense': 52, 'outer_defense': 52, 'hp': 480}
    },
    {
        'id': 10404102,
        'name': '化神·朱雀头盔',
        'quality': 4,
        'position': EquipPart.HELMET,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 66, 'outer_defense': 66},
        'extend_attrs': {'inner_defense': 52, 'outer_defense': 52, 'hp': 480}
    },
    {
        'id': 10405000,
        'name': '化神甲胄',
        'quality': 4,
        'position': EquipPart.ARMOR,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 60, 'outer_defense': 57},
        'extend_attrs': {'inner_defense': 49, 'outer_defense': 49}
    },
    {
        'id': 10405001,
        'name': '分神甲胄',
        'quality': 4,
        'position': EquipPart.ARMOR,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 59, 'outer_defense': 59},
        'extend_attrs': {'inner_defense': 50, 'outer_defense': 48}
    },
    {
        'id': 10405002,
        'name': '元神甲胄',
        'quality': 4,
        'position': EquipPart.ARMOR,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 61, 'outer_defense': 61},
        'extend_attrs': {'inner_defense': 48, 'outer_defense': 46}
    },
    {
        'id': 10405003,
        'name': '化神甲胄·改',
        'quality': 4,
        'position': EquipPart.ARMOR,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 59, 'outer_defense': 59},
        'extend_attrs': {'inner_defense': 47, 'outer_defense': 50}
    },
    {
        'id': 10405004,
        'name': '分神甲胄·真',
        'quality': 4,
        'position': EquipPart.ARMOR,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 59, 'outer_defense': 58},
        'extend_attrs': {'inner_defense': 50, 'outer_defense': 47}
    },
    {
        'id': 10405005,
        'name': '元神甲胄·灵',
        'quality': 4,
        'position': EquipPart.ARMOR,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 58, 'outer_defense': 60},
        'extend_attrs': {'inner_defense': 45, 'outer_defense': 46}
    },
    {
        'id': 10405100,
        'name': '化神·青龙甲胄',
        'quality': 4,
        'position': EquipPart.ARMOR,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 66, 'outer_defense': 66},
        'extend_attrs': {'inner_defense': 52, 'outer_defense': 52, 'hp': 480}
    },
    {
        'id': 10405101,
        'name': '化神·白虎甲胄',
        'quality': 4,
        'position': EquipPart.ARMOR,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 66, 'outer_defense': 66},
        'extend_attrs': {'inner_defense': 52, 'outer_defense': 52, 'hp': 480}
    },
    {
        'id': 10405102,
        'name': '化神·朱雀甲胄',
        'quality': 4,
        'position': EquipPart.ARMOR,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 66, 'outer_defense': 66},
        'extend_attrs': {'inner_defense': 52, 'outer_defense': 52, 'hp': 480}
    },
    {
        'id': 10406000,
        'name': '化神腰带',
        'quality': 4,
        'position': EquipPart.BELT,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'dodge': 61},
        'extend_attrs': {'crit_defense': 45}
    },
    {
        'id': 10406001,
        'name': '分神腰带',
        'quality': 4,
        'position': EquipPart.BELT,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'dodge': 59},
        'extend_attrs': {'crit_defense': 49}
    },
    {
        'id': 10406002,
        'name': '元神腰带',
        'quality': 4,
        'position': EquipPart.BELT,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'dodge': 59},
        'extend_attrs': {'crit_defense': 49}
    },
    {
        'id': 10406003,
        'name': '化神腰带·改',
        'quality': 4,
        'position': EquipPart.BELT,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'dodge': 59},
        'extend_attrs': {'crit_defense': 48}
    },
    {
        'id': 10406004,
        'name': '分神腰带·真',
        'quality': 4,
        'position': EquipPart.BELT,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'dodge': 58},
        'extend_attrs': {'crit_defense': 49}
    },
    {
        'id': 10406005,
        'name': '元神腰带·灵',
        'quality': 4,
        'position': EquipPart.BELT,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'dodge': 57},
        'extend_attrs': {'crit_defense': 46}
    },
    {
        'id': 10406100,
        'name': '化神·青龙腰带',
        'quality': 4,
        'position': EquipPart.BELT,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'dodge': 66},
        'extend_attrs': {'crit_defense': 52, 'hp': 480}
    },
    {
        'id': 10406101,
        'name': '化神·白虎腰带',
        'quality': 4,
        'position': EquipPart.BELT,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'dodge': 66},
        'extend_attrs': {'crit_defense': 52, 'hp': 480}
    },
    {
        'id': 10406102,
        'name': '化神·朱雀腰带',
        'quality': 4,
        'position': EquipPart.BELT,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'dodge': 66},
        'extend_attrs': {'crit_defense': 52, 'hp': 480}
    },
    {
        'id': 10407000,
        'name': '化神护肩',
        'quality': 4,
        'position': EquipPart.SHOULDER,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'dodge': 57},
        'extend_attrs': {'crit_defense': 48}
    },
    {
        'id': 10407001,
        'name': '分神护肩',
        'quality': 4,
        'position': EquipPart.SHOULDER,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'dodge': 58},
        'extend_attrs': {'crit_defense': 50}
    },
    {
        'id': 10407002,
        'name': '元神护肩',
        'quality': 4,
        'position': EquipPart.SHOULDER,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'dodge': 62},
        'extend_attrs': {'crit_defense': 46}
    },
    {
        'id': 10407003,
        'name': '化神护肩·改',
        'quality': 4,
        'position': EquipPart.SHOULDER,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'dodge': 57},
        'extend_attrs': {'crit_defense': 49}
    },
    {
        'id': 10407004,
        'name': '分神护肩·真',
        'quality': 4,
        'position': EquipPart.SHOULDER,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'dodge': 61},
        'extend_attrs': {'crit_defense': 48}
    },
    {
        'id': 10407005,
        'name': '元神护肩·灵',
        'quality': 4,
        'position': EquipPart.SHOULDER,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'dodge': 62},
        'extend_attrs': {'crit_defense': 48}
    },
    {
        'id': 10407100,
        'name': '化神·青龙护肩',
        'quality': 4,
        'position': EquipPart.SHOULDER,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'dodge': 66},
        'extend_attrs': {'crit_defense': 52, 'hp': 480}
    },
    {
        'id': 10407101,
        'name': '化神·白虎护肩',
        'quality': 4,
        'position': EquipPart.SHOULDER,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'dodge': 66},
        'extend_attrs': {'crit_defense': 52, 'hp': 480}
    },
    {
        'id': 10407102,
        'name': '化神·朱雀护肩',
        'quality': 4,
        'position': EquipPart.SHOULDER,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'dodge': 66},
        'extend_attrs': {'crit_defense': 52, 'hp': 480}
    },
    {
        'id': 10408000,
        'name': '化神鞋履',
        'quality': 4,
        'position': EquipPart.BOOTS,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 60},
        'extend_attrs': {'dodge': 50}
    },
    {
        'id': 10408001,
        'name': '分神鞋履',
        'quality': 4,
        'position': EquipPart.BOOTS,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 60},
        'extend_attrs': {'dodge': 49}
    },
    {
        'id': 10408002,
        'name': '元神鞋履',
        'quality': 4,
        'position': EquipPart.BOOTS,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 61},
        'extend_attrs': {'dodge': 48}
    },
    {
        'id': 10408003,
        'name': '化神鞋履·改',
        'quality': 4,
        'position': EquipPart.BOOTS,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 61},
        'extend_attrs': {'dodge': 48}
    },
    {
        'id': 10408004,
        'name': '分神鞋履·真',
        'quality': 4,
        'position': EquipPart.BOOTS,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 61},
        'extend_attrs': {'dodge': 49}
    },
    {
        'id': 10408005,
        'name': '元神鞋履·灵',
        'quality': 4,
        'position': EquipPart.BOOTS,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 59},
        'extend_attrs': {'dodge': 46}
    },
    {
        'id': 10408100,
        'name': '化神·青龙鞋履',
        'quality': 4,
        'position': EquipPart.BOOTS,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 66},
        'extend_attrs': {'dodge': 52, 'hp': 480}
    },
    {
        'id': 10408101,
        'name': '化神·白虎鞋履',
        'quality': 4,
        'position': EquipPart.BOOTS,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 66},
        'extend_attrs': {'dodge': 52, 'hp': 480}
    },
    {
        'id': 10408102,
        'name': '化神·朱雀鞋履',
        'quality': 4,
        'position': EquipPart.BOOTS,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 66},
        'extend_attrs': {'dodge': 52, 'hp': 480}
    },
    {
        'id': 10409000,
        'name': '化神手套',
        'quality': 4,
        'position': EquipPart.GLOVES,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'outer_defense': 60},
        'extend_attrs': {'dodge': 49}
    },
    {
        'id': 10409001,
        'name': '分神手套',
        'quality': 4,
        'position': EquipPart.GLOVES,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'outer_defense': 60},
        'extend_attrs': {'dodge': 47}
    },
    {
        'id': 10409002,
        'name': '元神手套',
        'quality': 4,
        'position': EquipPart.GLOVES,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'outer_defense': 61},
        'extend_attrs': {'dodge': 46}
    },
    {
        'id': 10409003,
        'name': '化神手套·改',
        'quality': 4,
        'position': EquipPart.GLOVES,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'outer_defense': 61},
        'extend_attrs': {'dodge': 46}
    },
    {
        'id': 10409004,
        'name': '分神手套·真',
        'quality': 4,
        'position': EquipPart.GLOVES,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'outer_defense': 57},
        'extend_attrs': {'dodge': 47}
    },
    {
        'id': 10409005,
        'name': '元神手套·灵',
        'quality': 4,
        'position': EquipPart.GLOVES,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'outer_defense': 62},
        'extend_attrs': {'dodge': 47}
    },
    {
        'id': 10409100,
        'name': '化神·青龙手套',
        'quality': 4,
        'position': EquipPart.GLOVES,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'outer_defense': 66},
        'extend_attrs': {'dodge': 52, 'hp': 480}
    },
    {
        'id': 10409101,
        'name': '化神·白虎手套',
        'quality': 4,
        'position': EquipPart.GLOVES,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'outer_defense': 66},
        'extend_attrs': {'dodge': 52, 'hp': 480}
    },
    {
        'id': 10409102,
        'name': '化神·朱雀手套',
        'quality': 4,
        'position': EquipPart.GLOVES,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'outer_defense': 66},
        'extend_attrs': {'dodge': 52, 'hp': 480}
    },
    {
        'id': 10410000,
        'name': '化神项链',
        'quality': 4,
        'position': EquipPart.NECKLACE,
        'type': EquipmentType.HYBRID,
        'base_attrs': {'inner_attack': 124, 'outer_attack': 121},
        'extend_attrs': {'hp': 491, 'inner_defense': 48, 'outer_defense': 46}
    },
    {
        'id': 10410001,
        'name': '分神项链',
        'quality': 4,
        'position': EquipPart.NECKLACE,
        'type': EquipmentType.HYBRID,
        'base_attrs': {'inner_attack': 119, 'outer_attack': 118},
        'extend_attrs': {'hp': 460, 'inner_defense': 49, 'outer_defense': 47}
    },
    {
        'id': 10410002,
        'name': '元神项链',
        'quality': 4,
        'position': EquipPart.NECKLACE,
        'type': EquipmentType.HYBRID,
        'base_attrs': {'inner_attack': 121, 'outer_attack': 118},
        'extend_attrs': {'hp': 475, 'inner_defense': 49, 'outer_defense': 49}
    },
    {
        'id': 10410003,
        'name': '化神项链·改',
        'quality': 4,
        'position': EquipPart.NECKLACE,
        'type': EquipmentType.HYBRID,
        'base_attrs': {'inner_attack': 119, 'outer_attack': 118},
        'extend_attrs': {'hp': 460, 'inner_defense': 46, 'outer_defense': 48}
    },
    {
        'id': 10410004,
        'name': '分神项链·真',
        'quality': 4,
        'position': EquipPart.NECKLACE,
        'type': EquipmentType.HYBRID,
        'base_attrs': {'inner_attack': 119, 'outer_attack': 117},
        'extend_attrs': {'hp': 471, 'inner_defense': 49, 'outer_defense': 48}
    },
    {
        'id': 10410005,
        'name': '元神项链·灵',
        'quality': 4,
        'position': EquipPart.NECKLACE,
        'type': EquipmentType.HYBRID,
        'base_attrs': {'inner_attack': 119, 'outer_attack': 121},
        'extend_attrs': {'hp': 463, 'inner_defense': 47, 'outer_defense': 46}
    },
    {
        'id': 10410100,
        'name': '化神·青龙项链',
        'quality': 4,
        'position': EquipPart.NECKLACE,
        'type': EquipmentType.HYBRID,
        'base_attrs': {'inner_attack': 132, 'outer_attack': 132},
        'extend_attrs': {'hp': 1008, 'inner_defense': 52, 'outer_defense': 52}
    },
    {
        'id': 10410101,
        'name': '化神·白虎项链',
        'quality': 4,
        'position': EquipPart.NECKLACE,
        'type': EquipmentType.HYBRID,
        'base_attrs': {'inner_attack': 132, 'outer_attack': 132},
        'extend_attrs': {'hp': 1008, 'inner_defense': 52, 'outer_defense': 52}
    },
    {
        'id': 10410102,
        'name': '化神·朱雀项链',
        'quality': 4,
        'position': EquipPart.NECKLACE,
        'type': EquipmentType.HYBRID,
        'base_attrs': {'inner_attack': 132, 'outer_attack': 132},
        'extend_attrs': {'hp': 1008, 'inner_defense': 52, 'outer_defense': 52}
    },
    {
        'id': 10411000,
        'name': '化神法宝',
        'quality': 4,
        'position': EquipPart.ARTIFACT,
        'type': EquipmentType.HYBRID,
        'base_attrs': {'hit': 59, 'crit': 58},
        'extend_attrs': {'outer_attack': 96, 'inner_attack': 99}
    },
    {
        'id': 10411001,
        'name': '分神法宝',
        'quality': 4,
        'position': EquipPart.ARTIFACT,
        'type': EquipmentType.HYBRID,
        'base_attrs': {'hit': 59, 'crit': 61},
        'extend_attrs': {'outer_attack': 99, 'inner_attack': 95}
    },
    {
        'id': 10411002,
        'name': '元神法宝',
        'quality': 4,
        'position': EquipPart.ARTIFACT,
        'type': EquipmentType.HYBRID,
        'base_attrs': {'hit': 62, 'crit': 61},
        'extend_attrs': {'outer_attack': 99, 'inner_attack': 93}
    },
    {
        'id': 10411003,
        'name': '化神法宝·改',
        'quality': 4,
        'position': EquipPart.ARTIFACT,
        'type': EquipmentType.HYBRID,
        'base_attrs': {'hit': 57, 'crit': 59},
        'extend_attrs': {'outer_attack': 96, 'inner_attack': 96}
    },
    {
        'id': 10411004,
        'name': '分神法宝·真',
        'quality': 4,
        'position': EquipPart.ARTIFACT,
        'type': EquipmentType.HYBRID,
        'base_attrs': {'hit': 61, 'crit': 60},
        'extend_attrs': {'outer_attack': 94, 'inner_attack': 93}
    },
    {
        'id': 10411005,
        'name': '元神法宝·灵',
        'quality': 4,
        'position': EquipPart.ARTIFACT,
        'type': EquipmentType.HYBRID,
        'base_attrs': {'hit': 58, 'crit': 60},
        'extend_attrs': {'outer_attack': 97, 'inner_attack': 96}
    },
    {
        'id': 10411100,
        'name': '化神·青龙法宝',
        'quality': 4,
        'position': EquipPart.ARTIFACT,
        'type': EquipmentType.HYBRID,
        'base_attrs': {'hit': 66, 'crit': 66},
        'extend_attrs': {'outer_attack': 105, 'inner_attack': 105, 'hp': 480}
    },
    {
        'id': 10411101,
        'name': '化神·白虎法宝',
        'quality': 4,
        'position': EquipPart.ARTIFACT,
        'type': EquipmentType.HYBRID,
        'base_attrs': {'hit': 66, 'crit': 66},
        'extend_attrs': {'outer_attack': 105, 'inner_attack': 105, 'hp': 480}
    },
    {
        'id': 10411102,
        'name': '化神·朱雀法宝',
        'quality': 4,
        'position': EquipPart.ARTIFACT,
        'type': EquipmentType.HYBRID,
        'base_attrs': {'hit': 66, 'crit': 66},
        'extend_attrs': {'outer_attack': 105, 'inner_attack': 105, 'hp': 480}
    },
    {
        'id': 10500000,
        'name': '炼虚剑',
        'quality': 5,
        'position': EquipPart.WEAPON,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'inner_attack': 145, 'outer_attack': 141},
        'extend_attrs': {'hp': 562, 'hit': 57, 'crit': 55}
    },
    {
        'id': 10500001,
        'name': '虚灵刀',
        'quality': 5,
        'position': EquipPart.WEAPON,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'inner_attack': 144, 'outer_attack': 137},
        'extend_attrs': {'hp': 561, 'hit': 58, 'crit': 57}
    },
    {
        'id': 10500002,
        'name': '破虚弓',
        'quality': 5,
        'position': EquipPart.WEAPON,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'inner_attack': 144, 'outer_attack': 146},
        'extend_attrs': {'hp': 584, 'hit': 55, 'crit': 56}
    },
    {
        'id': 10500003,
        'name': '炼虚弩',
        'quality': 5,
        'position': EquipPart.WEAPON,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'inner_attack': 143, 'outer_attack': 138},
        'extend_attrs': {'hp': 590, 'hit': 54, 'crit': 59}
    },
    {
        'id': 10500004,
        'name': '虚灵枪',
        'quality': 5,
        'position': EquipPart.WEAPON,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'inner_attack': 139, 'outer_attack': 150},
        'extend_attrs': {'hp': 579, 'hit': 59, 'crit': 56}
    },
    {
        'id': 10500005,
        'name': '破虚棍',
        'quality': 5,
        'position': EquipPart.WEAPON,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'inner_attack': 144, 'outer_attack': 149},
        'extend_attrs': {'hp': 575, 'hit': 57, 'crit': 57}
    },
    {
        'id': 10500100,
        'name': '炼虚·青龙剑',
        'quality': 5,
        'position': EquipPart.WEAPON,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'inner_attack': 158, 'outer_attack': 158},
        'extend_attrs': {'hp': 1209, 'hit': 62, 'crit': 62}
    },
    {
        'id': 10500101,
        'name': '炼虚·白虎刀',
        'quality': 5,
        'position': EquipPart.WEAPON,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'inner_attack': 158, 'outer_attack': 158},
        'extend_attrs': {'hp': 1209, 'hit': 62, 'crit': 62}
    },
    {
        'id': 10500102,
        'name': '炼虚·朱雀弓',
        'quality': 5,
        'position': EquipPart.WEAPON,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'inner_attack': 158, 'outer_attack': 158},
        'extend_attrs': {'hp': 1209, 'hit': 62, 'crit': 62}
    },
    {
        'id': 10501000,
        'name': '炼虚护腕',
        'quality': 5,
        'position': EquipPart.BRACER,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'hit': 74},
        'extend_attrs': {'outer_attack': 117, 'inner_attack': 118}
    },
    {
        'id': 10501001,
        'name': '虚灵护腕',
        'quality': 5,
        'position': EquipPart.BRACER,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'hit': 73},
        'extend_attrs': {'outer_attack': 116, 'inner_attack': 109}
    },
    {
        'id': 10501002,
        'name': '破虚护腕',
        'quality': 5,
        'position': EquipPart.BRACER,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'hit': 75},
        'extend_attrs': {'outer_attack': 115, 'inner_attack': 113}
    },
    {
        'id': 10501003,
        'name': '炼虚护腕·改',
        'quality': 5,
        'position': EquipPart.BRACER,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'hit': 68},
        'extend_attrs': {'outer_attack': 120, 'inner_attack': 113}
    },
    {
        'id': 10501004,
        'name': '虚灵护腕·真',
        'quality': 5,
        'position': EquipPart.BRACER,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'hit': 71},
        'extend_attrs': {'outer_attack': 119, 'inner_attack': 112}
    },
    {
        'id': 10501005,
        'name': '破虚护腕·灵',
        'quality': 5,
        'position': EquipPart.BRACER,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'hit': 70},
        'extend_attrs': {'outer_attack': 118, 'inner_attack': 109}
    },
    {
        'id': 10501100,
        'name': '炼虚·青龙护腕',
        'quality': 5,
        'position': EquipPart.BRACER,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'hit': 79},
        'extend_attrs': {'outer_attack': 126, 'inner_attack': 126, 'hp': 576}
    },
    {
        'id': 10501101,
        'name': '炼虚·白虎护腕',
        'quality': 5,
        'position': EquipPart.BRACER,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'hit': 79},
        'extend_attrs': {'outer_attack': 126, 'inner_attack': 126, 'hp': 576}
    },
    {
        'id': 10501102,
        'name': '炼虚·朱雀护腕',
        'quality': 5,
        'position': EquipPart.BRACER,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'hit': 79},
        'extend_attrs': {'outer_attack': 126, 'inner_attack': 126, 'hp': 576}
    },
    {
        'id': 10502000,
        'name': '炼虚戒指',
        'quality': 5,
        'position': EquipPart.RING,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'inner_attack': 139},
        'extend_attrs': {'hit': 56, 'crit': 57}
    },
    {
        'id': 10502001,
        'name': '虚灵戒指',
        'quality': 5,
        'position': EquipPart.RING,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'inner_attack': 140},
        'extend_attrs': {'hit': 55, 'crit': 58}
    },
    {
        'id': 10502002,
        'name': '破虚戒指',
        'quality': 5,
        'position': EquipPart.RING,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'inner_attack': 147},
        'extend_attrs': {'hit': 58, 'crit': 54}
    },
    {
        'id': 10502003,
        'name': '炼虚戒指·改',
        'quality': 5,
        'position': EquipPart.RING,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'inner_attack': 137},
        'extend_attrs': {'hit': 58, 'crit': 58}
    },
    {
        'id': 10502004,
        'name': '虚灵戒指·真',
        'quality': 5,
        'position': EquipPart.RING,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'inner_attack': 137},
        'extend_attrs': {'hit': 54, 'crit': 57}
    },
    {
        'id': 10502005,
        'name': '破虚戒指·灵',
        'quality': 5,
        'position': EquipPart.RING,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'inner_attack': 150},
        'extend_attrs': {'hit': 56, 'crit': 55}
    },
    {
        'id': 10502100,
        'name': '炼虚·青龙戒指',
        'quality': 5,
        'position': EquipPart.RING,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'inner_attack': 158},
        'extend_attrs': {'hit': 62, 'crit': 62, 'hp': 576}
    },
    {
        'id': 10502101,
        'name': '炼虚·白虎戒指',
        'quality': 5,
        'position': EquipPart.RING,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'inner_attack': 158},
        'extend_attrs': {'hit': 62, 'crit': 62, 'hp': 576}
    },
    {
        'id': 10502102,
        'name': '炼虚·朱雀戒指',
        'quality': 5,
        'position': EquipPart.RING,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'inner_attack': 158},
        'extend_attrs': {'hit': 62, 'crit': 62, 'hp': 576}
    },
    {
        'id': 10503000,
        'name': '炼虚护符',
        'quality': 5,
        'position': EquipPart.AMULET,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'outer_attack': 149},
        'extend_attrs': {'hit': 57, 'crit': 55}
    },
    {
        'id': 10503001,
        'name': '虚灵护符',
        'quality': 5,
        'position': EquipPart.AMULET,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'outer_attack': 141},
        'extend_attrs': {'hit': 58, 'crit': 55}
    },
    {
        'id': 10503002,
        'name': '破虚护符',
        'quality': 5,
        'position': EquipPart.AMULET,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'outer_attack': 149},
        'extend_attrs': {'hit': 57, 'crit': 57}
    },
    {
        'id': 10503003,
        'name': '炼虚护符·改',
        'quality': 5,
        'position': EquipPart.AMULET,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'outer_attack': 144},
        'extend_attrs': {'hit': 55, 'crit': 57}
    },
    {
        'id': 10503004,
        'name': '虚灵护符·真',
        'quality': 5,
        'position': EquipPart.AMULET,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'outer_attack': 139},
        'extend_attrs': {'hit': 56, 'crit': 57}
    },
    {
        'id': 10503005,
        'name': '破虚护符·灵',
        'quality': 5,
        'position': EquipPart.AMULET,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'outer_attack': 150},
        'extend_attrs': {'hit': 56, 'crit': 59}
    },
    {
        'id': 10503100,
        'name': '炼虚·青龙护符',
        'quality': 5,
        'position': EquipPart.AMULET,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'outer_attack': 158},
        'extend_attrs': {'hit': 62, 'crit': 62, 'hp': 576}
    },
    {
        'id': 10503101,
        'name': '炼虚·白虎护符',
        'quality': 5,
        'position': EquipPart.AMULET,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'outer_attack': 158},
        'extend_attrs': {'hit': 62, 'crit': 62, 'hp': 576}
    },
    {
        'id': 10503102,
        'name': '炼虚·朱雀护符',
        'quality': 5,
        'position': EquipPart.AMULET,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'outer_attack': 158},
        'extend_attrs': {'hit': 62, 'crit': 62, 'hp': 576}
    },
    {
        'id': 10504000,
        'name': '炼虚头盔',
        'quality': 5,
        'position': EquipPart.HELMET,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 69, 'outer_defense': 75},
        'extend_attrs': {'inner_defense': 56, 'outer_defense': 58}
    },
    {
        'id': 10504001,
        'name': '虚灵头盔',
        'quality': 5,
        'position': EquipPart.HELMET,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 72, 'outer_defense': 73},
        'extend_attrs': {'inner_defense': 58, 'outer_defense': 59}
    },
    {
        'id': 10504002,
        'name': '破虚头盔',
        'quality': 5,
        'position': EquipPart.HELMET,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 71, 'outer_defense': 70},
        'extend_attrs': {'inner_defense': 57, 'outer_defense': 59}
    },
    {
        'id': 10504003,
        'name': '炼虚头盔·改',
        'quality': 5,
        'position': EquipPart.HELMET,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 68, 'outer_defense': 71},
        'extend_attrs': {'inner_defense': 57, 'outer_defense': 57}
    },
    {
        'id': 10504004,
        'name': '虚灵头盔·真',
        'quality': 5,
        'position': EquipPart.HELMET,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 70, 'outer_defense': 71},
        'extend_attrs': {'inner_defense': 54, 'outer_defense': 54}
    },
    {
        'id': 10504005,
        'name': '破虚头盔·灵',
        'quality': 5,
        'position': EquipPart.HELMET,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 73, 'outer_defense': 70},
        'extend_attrs': {'inner_defense': 55, 'outer_defense': 56}
    },
    {
        'id': 10504100,
        'name': '炼虚·青龙头盔',
        'quality': 5,
        'position': EquipPart.HELMET,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 79, 'outer_defense': 79},
        'extend_attrs': {'inner_defense': 62, 'outer_defense': 62, 'hp': 576}
    },
    {
        'id': 10504101,
        'name': '炼虚·白虎头盔',
        'quality': 5,
        'position': EquipPart.HELMET,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 79, 'outer_defense': 79},
        'extend_attrs': {'inner_defense': 62, 'outer_defense': 62, 'hp': 576}
    },
    {
        'id': 10504102,
        'name': '炼虚·朱雀头盔',
        'quality': 5,
        'position': EquipPart.HELMET,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 79, 'outer_defense': 79},
        'extend_attrs': {'inner_defense': 62, 'outer_defense': 62, 'hp': 576}
    },
    {
        'id': 10505000,
        'name': '炼虚甲胄',
        'quality': 5,
        'position': EquipPart.ARMOR,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 73, 'outer_defense': 75},
        'extend_attrs': {'inner_defense': 59, 'outer_defense': 57}
    },
    {
        'id': 10505001,
        'name': '虚灵甲胄',
        'quality': 5,
        'position': EquipPart.ARMOR,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 70, 'outer_defense': 74},
        'extend_attrs': {'inner_defense': 59, 'outer_defense': 58}
    },
    {
        'id': 10505002,
        'name': '破虚甲胄',
        'quality': 5,
        'position': EquipPart.ARMOR,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 68, 'outer_defense': 70},
        'extend_attrs': {'inner_defense': 57, 'outer_defense': 58}
    },
    {
        'id': 10505003,
        'name': '炼虚甲胄·改',
        'quality': 5,
        'position': EquipPart.ARMOR,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 71, 'outer_defense': 69},
        'extend_attrs': {'inner_defense': 56, 'outer_defense': 57}
    },
    {
        'id': 10505004,
        'name': '虚灵甲胄·真',
        'quality': 5,
        'position': EquipPart.ARMOR,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 68, 'outer_defense': 70},
        'extend_attrs': {'inner_defense': 58, 'outer_defense': 57}
    },
    {
        'id': 10505005,
        'name': '破虚甲胄·灵',
        'quality': 5,
        'position': EquipPart.ARMOR,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 69, 'outer_defense': 75},
        'extend_attrs': {'inner_defense': 54, 'outer_defense': 54}
    },
    {
        'id': 10505100,
        'name': '炼虚·青龙甲胄',
        'quality': 5,
        'position': EquipPart.ARMOR,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 79, 'outer_defense': 79},
        'extend_attrs': {'inner_defense': 62, 'outer_defense': 62, 'hp': 576}
    },
    {
        'id': 10505101,
        'name': '炼虚·白虎甲胄',
        'quality': 5,
        'position': EquipPart.ARMOR,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 79, 'outer_defense': 79},
        'extend_attrs': {'inner_defense': 62, 'outer_defense': 62, 'hp': 576}
    },
    {
        'id': 10505102,
        'name': '炼虚·朱雀甲胄',
        'quality': 5,
        'position': EquipPart.ARMOR,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 79, 'outer_defense': 79},
        'extend_attrs': {'inner_defense': 62, 'outer_defense': 62, 'hp': 576}
    },
    {
        'id': 10506000,
        'name': '炼虚腰带',
        'quality': 5,
        'position': EquipPart.BELT,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'dodge': 74},
        'extend_attrs': {'crit_defense': 57}
    },
    {
        'id': 10506001,
        'name': '虚灵腰带',
        'quality': 5,
        'position': EquipPart.BELT,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'dodge': 73},
        'extend_attrs': {'crit_defense': 57}
    },
    {
        'id': 10506002,
        'name': '破虚腰带',
        'quality': 5,
        'position': EquipPart.BELT,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'dodge': 73},
        'extend_attrs': {'crit_defense': 59}
    },
    {
        'id': 10506003,
        'name': '炼虚腰带·改',
        'quality': 5,
        'position': EquipPart.BELT,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'dodge': 71},
        'extend_attrs': {'crit_defense': 56}
    },
    {
        'id': 10506004,
        'name': '虚灵腰带·真',
        'quality': 5,
        'position': EquipPart.BELT,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'dodge': 70},
        'extend_attrs': {'crit_defense': 59}
    },
    {
        'id': 10506005,
        'name': '破虚腰带·灵',
        'quality': 5,
        'position': EquipPart.BELT,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'dodge': 75},
        'extend_attrs': {'crit_defense': 56}
    },
    {
        'id': 10506100,
        'name': '炼虚·青龙腰带',
        'quality': 5,
        'position': EquipPart.BELT,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'dodge': 79},
        'extend_attrs': {'crit_defense': 62, 'hp': 576}
    },
    {
        'id': 10506101,
        'name': '炼虚·白虎腰带',
        'quality': 5,
        'position': EquipPart.BELT,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'dodge': 79},
        'extend_attrs': {'crit_defense': 62, 'hp': 576}
    },
    {
        'id': 10506102,
        'name': '炼虚·朱雀腰带',
        'quality': 5,
        'position': EquipPart.BELT,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'dodge': 79},
        'extend_attrs': {'crit_defense': 62, 'hp': 576}
    },
    {
        'id': 10507000,
        'name': '炼虚护肩',
        'quality': 5,
        'position': EquipPart.SHOULDER,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'dodge': 74},
        'extend_attrs': {'crit_defense': 55}
    },
    {
        'id': 10507001,
        'name': '虚灵护肩',
        'quality': 5,
        'position': EquipPart.SHOULDER,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'dodge': 69},
        'extend_attrs': {'crit_defense': 55}
    },
    {
        'id': 10507002,
        'name': '破虚护肩',
        'quality': 5,
        'position': EquipPart.SHOULDER,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'dodge': 68},
        'extend_attrs': {'crit_defense': 58}
    },
    {
        'id': 10507003,
        'name': '炼虚护肩·改',
        'quality': 5,
        'position': EquipPart.SHOULDER,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'dodge': 70},
        'extend_attrs': {'crit_defense': 55}
    },
    {
        'id': 10507004,
        'name': '虚灵护肩·真',
        'quality': 5,
        'position': EquipPart.SHOULDER,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'dodge': 74},
        'extend_attrs': {'crit_defense': 56}
    },
    {
        'id': 10507005,
        'name': '破虚护肩·灵',
        'quality': 5,
        'position': EquipPart.SHOULDER,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'dodge': 68},
        'extend_attrs': {'crit_defense': 54}
    },
    {
        'id': 10507100,
        'name': '炼虚·青龙护肩',
        'quality': 5,
        'position': EquipPart.SHOULDER,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'dodge': 79},
        'extend_attrs': {'crit_defense': 62, 'hp': 576}
    },
    {
        'id': 10507101,
        'name': '炼虚·白虎护肩',
        'quality': 5,
        'position': EquipPart.SHOULDER,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'dodge': 79},
        'extend_attrs': {'crit_defense': 62, 'hp': 576}
    },
    {
        'id': 10507102,
        'name': '炼虚·朱雀护肩',
        'quality': 5,
        'position': EquipPart.SHOULDER,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'dodge': 79},
        'extend_attrs': {'crit_defense': 62, 'hp': 576}
    },
    {
        'id': 10508000,
        'name': '炼虚鞋履',
        'quality': 5,
        'position': EquipPart.BOOTS,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 72},
        'extend_attrs': {'dodge': 58}
    },
    {
        'id': 10508001,
        'name': '虚灵鞋履',
        'quality': 5,
        'position': EquipPart.BOOTS,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 72},
        'extend_attrs': {'dodge': 55}
    },
    {
        'id': 10508002,
        'name': '破虚鞋履',
        'quality': 5,
        'position': EquipPart.BOOTS,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 69},
        'extend_attrs': {'dodge': 58}
    },
    {
        'id': 10508003,
        'name': '炼虚鞋履·改',
        'quality': 5,
        'position': EquipPart.BOOTS,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 72},
        'extend_attrs': {'dodge': 58}
    },
    {
        'id': 10508004,
        'name': '虚灵鞋履·真',
        'quality': 5,
        'position': EquipPart.BOOTS,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 71},
        'extend_attrs': {'dodge': 55}
    },
    {
        'id': 10508005,
        'name': '破虚鞋履·灵',
        'quality': 5,
        'position': EquipPart.BOOTS,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 70},
        'extend_attrs': {'dodge': 58}
    },
    {
        'id': 10508100,
        'name': '炼虚·青龙鞋履',
        'quality': 5,
        'position': EquipPart.BOOTS,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 79},
        'extend_attrs': {'dodge': 62, 'hp': 576}
    },
    {
        'id': 10508101,
        'name': '炼虚·白虎鞋履',
        'quality': 5,
        'position': EquipPart.BOOTS,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 79},
        'extend_attrs': {'dodge': 62, 'hp': 576}
    },
    {
        'id': 10508102,
        'name': '炼虚·朱雀鞋履',
        'quality': 5,
        'position': EquipPart.BOOTS,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 79},
        'extend_attrs': {'dodge': 62, 'hp': 576}
    },
    {
        'id': 10509000,
        'name': '炼虚手套',
        'quality': 5,
        'position': EquipPart.GLOVES,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'outer_defense': 70},
        'extend_attrs': {'dodge': 57}
    },
    {
        'id': 10509001,
        'name': '虚灵手套',
        'quality': 5,
        'position': EquipPart.GLOVES,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'outer_defense': 74},
        'extend_attrs': {'dodge': 58}
    },
    {
        'id': 10509002,
        'name': '破虚手套',
        'quality': 5,
        'position': EquipPart.GLOVES,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'outer_defense': 71},
        'extend_attrs': {'dodge': 56}
    },
    {
        'id': 10509003,
        'name': '炼虚手套·改',
        'quality': 5,
        'position': EquipPart.GLOVES,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'outer_defense': 71},
        'extend_attrs': {'dodge': 56}
    },
    {
        'id': 10509004,
        'name': '虚灵手套·真',
        'quality': 5,
        'position': EquipPart.GLOVES,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'outer_defense': 70},
        'extend_attrs': {'dodge': 56}
    },
    {
        'id': 10509005,
        'name': '破虚手套·灵',
        'quality': 5,
        'position': EquipPart.GLOVES,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'outer_defense': 71},
        'extend_attrs': {'dodge': 56}
    },
    {
        'id': 10509100,
        'name': '炼虚·青龙手套',
        'quality': 5,
        'position': EquipPart.GLOVES,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'outer_defense': 79},
        'extend_attrs': {'dodge': 62, 'hp': 576}
    },
    {
        'id': 10509101,
        'name': '炼虚·白虎手套',
        'quality': 5,
        'position': EquipPart.GLOVES,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'outer_defense': 79},
        'extend_attrs': {'dodge': 62, 'hp': 576}
    },
    {
        'id': 10509102,
        'name': '炼虚·朱雀手套',
        'quality': 5,
        'position': EquipPart.GLOVES,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'outer_defense': 79},
        'extend_attrs': {'dodge': 62, 'hp': 576}
    },
    {
        'id': 10510000,
        'name': '炼虚项链',
        'quality': 5,
        'position': EquipPart.NECKLACE,
        'type': EquipmentType.HYBRID,
        'base_attrs': {'inner_attack': 139, 'outer_attack': 140},
        'extend_attrs': {'hp': 584, 'inner_defense': 54, 'outer_defense': 55}
    },
    {
        'id': 10510001,
        'name': '虚灵项链',
        'quality': 5,
        'position': EquipPart.NECKLACE,
        'type': EquipmentType.HYBRID,
        'base_attrs': {'inner_attack': 145, 'outer_attack': 143},
        'extend_attrs': {'hp': 594, 'inner_defense': 59, 'outer_defense': 54}
    },
    {
        'id': 10510002,
        'name': '破虚项链',
        'quality': 5,
        'position': EquipPart.NECKLACE,
        'type': EquipmentType.HYBRID,
        'base_attrs': {'inner_attack': 150, 'outer_attack': 143},
        'extend_attrs': {'hp': 591, 'inner_defense': 54, 'outer_defense': 54}
    },
    {
        'id': 10510003,
        'name': '炼虚项链·改',
        'quality': 5,
        'position': EquipPart.NECKLACE,
        'type': EquipmentType.HYBRID,
        'base_attrs': {'inner_attack': 139, 'outer_attack': 148},
        'extend_attrs': {'hp': 571, 'inner_defense': 56, 'outer_defense': 59}
    },
    {
        'id': 10510004,
        'name': '虚灵项链·真',
        'quality': 5,
        'position': EquipPart.NECKLACE,
        'type': EquipmentType.HYBRID,
        'base_attrs': {'inner_attack': 144, 'outer_attack': 147},
        'extend_attrs': {'hp': 574, 'inner_defense': 55, 'outer_defense': 55}
    },
    {
        'id': 10510005,
        'name': '破虚项链·灵',
        'quality': 5,
        'position': EquipPart.NECKLACE,
        'type': EquipmentType.HYBRID,
        'base_attrs': {'inner_attack': 148, 'outer_attack': 149},
        'extend_attrs': {'hp': 556, 'inner_defense': 56, 'outer_defense': 56}
    },
    {
        'id': 10510100,
        'name': '炼虚·青龙项链',
        'quality': 5,
        'position': EquipPart.NECKLACE,
        'type': EquipmentType.HYBRID,
        'base_attrs': {'inner_attack': 158, 'outer_attack': 158},
        'extend_attrs': {'hp': 1209, 'inner_defense': 62, 'outer_defense': 62}
    },
    {
        'id': 10510101,
        'name': '炼虚·白虎项链',
        'quality': 5,
        'position': EquipPart.NECKLACE,
        'type': EquipmentType.HYBRID,
        'base_attrs': {'inner_attack': 158, 'outer_attack': 158},
        'extend_attrs': {'hp': 1209, 'inner_defense': 62, 'outer_defense': 62}
    },
    {
        'id': 10510102,
        'name': '炼虚·朱雀项链',
        'quality': 5,
        'position': EquipPart.NECKLACE,
        'type': EquipmentType.HYBRID,
        'base_attrs': {'inner_attack': 158, 'outer_attack': 158},
        'extend_attrs': {'hp': 1209, 'inner_defense': 62, 'outer_defense': 62}
    },
    {
        'id': 10511000,
        'name': '炼虚法宝',
        'quality': 5,
        'position': EquipPart.ARTIFACT,
        'type': EquipmentType.HYBRID,
        'base_attrs': {'hit': 75, 'crit': 75},
        'extend_attrs': {'outer_attack': 112, 'inner_attack': 116}
    },
    {
        'id': 10511001,
        'name': '虚灵法宝',
        'quality': 5,
        'position': EquipPart.ARTIFACT,
        'type': EquipmentType.HYBRID,
        'base_attrs': {'hit': 68, 'crit': 75},
        'extend_attrs': {'outer_attack': 119, 'inner_attack': 120}
    },
    {
        'id': 10511002,
        'name': '破虚法宝',
        'quality': 5,
        'position': EquipPart.ARTIFACT,
        'type': EquipmentType.HYBRID,
        'base_attrs': {'hit': 70, 'crit': 73},
        'extend_attrs': {'outer_attack': 110, 'inner_attack': 111}
    },
    {
        'id': 10511003,
        'name': '炼虚法宝·改',
        'quality': 5,
        'position': EquipPart.ARTIFACT,
        'type': EquipmentType.HYBRID,
        'base_attrs': {'hit': 72, 'crit': 72},
        'extend_attrs': {'outer_attack': 120, 'inner_attack': 119}
    },
    {
        'id': 10511004,
        'name': '虚灵法宝·真',
        'quality': 5,
        'position': EquipPart.ARTIFACT,
        'type': EquipmentType.HYBRID,
        'base_attrs': {'hit': 73, 'crit': 73},
        'extend_attrs': {'outer_attack': 110, 'inner_attack': 119}
    },
    {
        'id': 10511005,
        'name': '破虚法宝·灵',
        'quality': 5,
        'position': EquipPart.ARTIFACT,
        'type': EquipmentType.HYBRID,
        'base_attrs': {'hit': 68, 'crit': 71},
        'extend_attrs': {'outer_attack': 113, 'inner_attack': 112}
    },
    {
        'id': 10511100,
        'name': '炼虚·青龙法宝',
        'quality': 5,
        'position': EquipPart.ARTIFACT,
        'type': EquipmentType.HYBRID,
        'base_attrs': {'hit': 79, 'crit': 79},
        'extend_attrs': {'outer_attack': 126, 'inner_attack': 126, 'hp': 576}
    },
    {
        'id': 10511101,
        'name': '炼虚·白虎法宝',
        'quality': 5,
        'position': EquipPart.ARTIFACT,
        'type': EquipmentType.HYBRID,
        'base_attrs': {'hit': 79, 'crit': 79},
        'extend_attrs': {'outer_attack': 126, 'inner_attack': 126, 'hp': 576}
    },
    {
        'id': 10511102,
        'name': '炼虚·朱雀法宝',
        'quality': 5,
        'position': EquipPart.ARTIFACT,
        'type': EquipmentType.HYBRID,
        'base_attrs': {'hit': 79, 'crit': 79},
        'extend_attrs': {'outer_attack': 126, 'inner_attack': 126, 'hp': 576}
    },
    {
        'id': 10600000,
        'name': '合体剑',
        'quality': 6,
        'position': EquipPart.WEAPON,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'inner_attack': 171, 'outer_attack': 174},
        'extend_attrs': {'hp': 638, 'hit': 64, 'crit': 69}
    },
    {
        'id': 10600001,
        'name': '融合刀',
        'quality': 6,
        'position': EquipPart.WEAPON,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'inner_attack': 164, 'outer_attack': 160},
        'extend_attrs': {'hp': 649, 'hit': 65, 'crit': 68}
    },
    {
        'id': 10600002,
        'name': '归一弓',
        'quality': 6,
        'position': EquipPart.WEAPON,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'inner_attack': 171, 'outer_attack': 175},
        'extend_attrs': {'hp': 668, 'hit': 70, 'crit': 69}
    },
    {
        'id': 10600003,
        'name': '合体弩',
        'quality': 6,
        'position': EquipPart.WEAPON,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'inner_attack': 165, 'outer_attack': 171},
        'extend_attrs': {'hp': 689, 'hit': 68, 'crit': 70}
    },
    {
        'id': 10600004,
        'name': '融合枪',
        'quality': 6,
        'position': EquipPart.WEAPON,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'inner_attack': 172, 'outer_attack': 168},
        'extend_attrs': {'hp': 694, 'hit': 69, 'crit': 69}
    },
    {
        'id': 10600005,
        'name': '归一棍',
        'quality': 6,
        'position': EquipPart.WEAPON,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'inner_attack': 175, 'outer_attack': 172},
        'extend_attrs': {'hp': 702, 'hit': 68, 'crit': 68}
    },
    {
        'id': 10600100,
        'name': '合体·青龙剑',
        'quality': 6,
        'position': EquipPart.WEAPON,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'inner_attack': 184, 'outer_attack': 184},
        'extend_attrs': {'hp': 1411, 'hit': 73, 'crit': 73}
    },
    {
        'id': 10600101,
        'name': '合体·白虎刀',
        'quality': 6,
        'position': EquipPart.WEAPON,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'inner_attack': 184, 'outer_attack': 184},
        'extend_attrs': {'hp': 1411, 'hit': 73, 'crit': 73}
    },
    {
        'id': 10600102,
        'name': '合体·朱雀弓',
        'quality': 6,
        'position': EquipPart.WEAPON,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'inner_attack': 184, 'outer_attack': 184},
        'extend_attrs': {'hp': 1411, 'hit': 73, 'crit': 73}
    },
    {
        'id': 10601000,
        'name': '合体护腕',
        'quality': 6,
        'position': EquipPart.BRACER,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'hit': 86},
        'extend_attrs': {'outer_attack': 136, 'inner_attack': 138}
    },
    {
        'id': 10601001,
        'name': '融合护腕',
        'quality': 6,
        'position': EquipPart.BRACER,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'hit': 81},
        'extend_attrs': {'outer_attack': 129, 'inner_attack': 134}
    },
    {
        'id': 10601002,
        'name': '归一护腕',
        'quality': 6,
        'position': EquipPart.BRACER,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'hit': 82},
        'extend_attrs': {'outer_attack': 128, 'inner_attack': 140}
    },
    {
        'id': 10601003,
        'name': '合体护腕·改',
        'quality': 6,
        'position': EquipPart.BRACER,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'hit': 87},
        'extend_attrs': {'outer_attack': 137, 'inner_attack': 134}
    },
    {
        'id': 10601004,
        'name': '融合护腕·真',
        'quality': 6,
        'position': EquipPart.BRACER,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'hit': 83},
        'extend_attrs': {'outer_attack': 134, 'inner_attack': 134}
    },
    {
        'id': 10601005,
        'name': '归一护腕·灵',
        'quality': 6,
        'position': EquipPart.BRACER,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'hit': 85},
        'extend_attrs': {'outer_attack': 131, 'inner_attack': 138}
    },
    {
        'id': 10601100,
        'name': '合体·青龙护腕',
        'quality': 6,
        'position': EquipPart.BRACER,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'hit': 92},
        'extend_attrs': {'outer_attack': 147, 'inner_attack': 147, 'hp': 672}
    },
    {
        'id': 10601101,
        'name': '合体·白虎护腕',
        'quality': 6,
        'position': EquipPart.BRACER,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'hit': 92},
        'extend_attrs': {'outer_attack': 147, 'inner_attack': 147, 'hp': 672}
    },
    {
        'id': 10601102,
        'name': '合体·朱雀护腕',
        'quality': 6,
        'position': EquipPart.BRACER,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'hit': 92},
        'extend_attrs': {'outer_attack': 147, 'inner_attack': 147, 'hp': 672}
    },
    {
        'id': 10602000,
        'name': '合体戒指',
        'quality': 6,
        'position': EquipPart.RING,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'inner_attack': 163},
        'extend_attrs': {'hit': 65, 'crit': 66}
    },
    {
        'id': 10602001,
        'name': '融合戒指',
        'quality': 6,
        'position': EquipPart.RING,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'inner_attack': 165},
        'extend_attrs': {'hit': 65, 'crit': 67}
    },
    {
        'id': 10602002,
        'name': '归一戒指',
        'quality': 6,
        'position': EquipPart.RING,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'inner_attack': 172},
        'extend_attrs': {'hit': 68, 'crit': 68}
    },
    {
        'id': 10602003,
        'name': '合体戒指·改',
        'quality': 6,
        'position': EquipPart.RING,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'inner_attack': 164},
        'extend_attrs': {'hit': 67, 'crit': 66}
    },
    {
        'id': 10602004,
        'name': '融合戒指·真',
        'quality': 6,
        'position': EquipPart.RING,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'inner_attack': 162},
        'extend_attrs': {'hit': 67, 'crit': 69}
    },
    {
        'id': 10602005,
        'name': '归一戒指·灵',
        'quality': 6,
        'position': EquipPart.RING,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'inner_attack': 166},
        'extend_attrs': {'hit': 65, 'crit': 63}
    },
    {
        'id': 10602100,
        'name': '合体·青龙戒指',
        'quality': 6,
        'position': EquipPart.RING,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'inner_attack': 184},
        'extend_attrs': {'hit': 73, 'crit': 73, 'hp': 672}
    },
    {
        'id': 10602101,
        'name': '合体·白虎戒指',
        'quality': 6,
        'position': EquipPart.RING,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'inner_attack': 184},
        'extend_attrs': {'hit': 73, 'crit': 73, 'hp': 672}
    },
    {
        'id': 10602102,
        'name': '合体·朱雀戒指',
        'quality': 6,
        'position': EquipPart.RING,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'inner_attack': 184},
        'extend_attrs': {'hit': 73, 'crit': 73, 'hp': 672}
    },
    {
        'id': 10603000,
        'name': '合体护符',
        'quality': 6,
        'position': EquipPart.AMULET,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'outer_attack': 173},
        'extend_attrs': {'hit': 63, 'crit': 65}
    },
    {
        'id': 10603001,
        'name': '融合护符',
        'quality': 6,
        'position': EquipPart.AMULET,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'outer_attack': 175},
        'extend_attrs': {'hit': 65, 'crit': 66}
    },
    {
        'id': 10603002,
        'name': '归一护符',
        'quality': 6,
        'position': EquipPart.AMULET,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'outer_attack': 163},
        'extend_attrs': {'hit': 67, 'crit': 66}
    },
    {
        'id': 10603003,
        'name': '合体护符·改',
        'quality': 6,
        'position': EquipPart.AMULET,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'outer_attack': 164},
        'extend_attrs': {'hit': 67, 'crit': 68}
    },
    {
        'id': 10603004,
        'name': '融合护符·真',
        'quality': 6,
        'position': EquipPart.AMULET,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'outer_attack': 159},
        'extend_attrs': {'hit': 67, 'crit': 69}
    },
    {
        'id': 10603005,
        'name': '归一护符·灵',
        'quality': 6,
        'position': EquipPart.AMULET,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'outer_attack': 172},
        'extend_attrs': {'hit': 63, 'crit': 66}
    },
    {
        'id': 10603100,
        'name': '合体·青龙护符',
        'quality': 6,
        'position': EquipPart.AMULET,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'outer_attack': 184},
        'extend_attrs': {'hit': 73, 'crit': 73, 'hp': 672}
    },
    {
        'id': 10603101,
        'name': '合体·白虎护符',
        'quality': 6,
        'position': EquipPart.AMULET,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'outer_attack': 184},
        'extend_attrs': {'hit': 73, 'crit': 73, 'hp': 672}
    },
    {
        'id': 10603102,
        'name': '合体·朱雀护符',
        'quality': 6,
        'position': EquipPart.AMULET,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'outer_attack': 184},
        'extend_attrs': {'hit': 73, 'crit': 73, 'hp': 672}
    },
    {
        'id': 10604000,
        'name': '合体头盔',
        'quality': 6,
        'position': EquipPart.HELMET,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 80, 'outer_defense': 84},
        'extend_attrs': {'inner_defense': 70, 'outer_defense': 69}
    },
    {
        'id': 10604001,
        'name': '融合头盔',
        'quality': 6,
        'position': EquipPart.HELMET,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 87, 'outer_defense': 86},
        'extend_attrs': {'inner_defense': 63, 'outer_defense': 68}
    },
    {
        'id': 10604002,
        'name': '归一头盔',
        'quality': 6,
        'position': EquipPart.HELMET,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 86, 'outer_defense': 80},
        'extend_attrs': {'inner_defense': 70, 'outer_defense': 69}
    },
    {
        'id': 10604003,
        'name': '合体头盔·改',
        'quality': 6,
        'position': EquipPart.HELMET,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 80, 'outer_defense': 81},
        'extend_attrs': {'inner_defense': 68, 'outer_defense': 65}
    },
    {
        'id': 10604004,
        'name': '融合头盔·真',
        'quality': 6,
        'position': EquipPart.HELMET,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 84, 'outer_defense': 83},
        'extend_attrs': {'inner_defense': 65, 'outer_defense': 65}
    },
    {
        'id': 10604005,
        'name': '归一头盔·灵',
        'quality': 6,
        'position': EquipPart.HELMET,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 82, 'outer_defense': 85},
        'extend_attrs': {'inner_defense': 68, 'outer_defense': 66}
    },
    {
        'id': 10604100,
        'name': '合体·青龙头盔',
        'quality': 6,
        'position': EquipPart.HELMET,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 92, 'outer_defense': 92},
        'extend_attrs': {'inner_defense': 73, 'outer_defense': 73, 'hp': 672}
    },
    {
        'id': 10604101,
        'name': '合体·白虎头盔',
        'quality': 6,
        'position': EquipPart.HELMET,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 92, 'outer_defense': 92},
        'extend_attrs': {'inner_defense': 73, 'outer_defense': 73, 'hp': 672}
    },
    {
        'id': 10604102,
        'name': '合体·朱雀头盔',
        'quality': 6,
        'position': EquipPart.HELMET,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 92, 'outer_defense': 92},
        'extend_attrs': {'inner_defense': 73, 'outer_defense': 73, 'hp': 672}
    },
    {
        'id': 10605000,
        'name': '合体甲胄',
        'quality': 6,
        'position': EquipPart.ARMOR,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 86, 'outer_defense': 80},
        'extend_attrs': {'inner_defense': 69, 'outer_defense': 64}
    },
    {
        'id': 10605001,
        'name': '融合甲胄',
        'quality': 6,
        'position': EquipPart.ARMOR,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 85, 'outer_defense': 81},
        'extend_attrs': {'inner_defense': 69, 'outer_defense': 65}
    },
    {
        'id': 10605002,
        'name': '归一甲胄',
        'quality': 6,
        'position': EquipPart.ARMOR,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 80, 'outer_defense': 83},
        'extend_attrs': {'inner_defense': 66, 'outer_defense': 64}
    },
    {
        'id': 10605003,
        'name': '合体甲胄·改',
        'quality': 6,
        'position': EquipPart.ARMOR,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 86, 'outer_defense': 85},
        'extend_attrs': {'inner_defense': 70, 'outer_defense': 65}
    },
    {
        'id': 10605004,
        'name': '融合甲胄·真',
        'quality': 6,
        'position': EquipPart.ARMOR,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 83, 'outer_defense': 81},
        'extend_attrs': {'inner_defense': 66, 'outer_defense': 68}
    },
    {
        'id': 10605005,
        'name': '归一甲胄·灵',
        'quality': 6,
        'position': EquipPart.ARMOR,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 87, 'outer_defense': 85},
        'extend_attrs': {'inner_defense': 66, 'outer_defense': 66}
    },
    {
        'id': 10605100,
        'name': '合体·青龙甲胄',
        'quality': 6,
        'position': EquipPart.ARMOR,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 92, 'outer_defense': 92},
        'extend_attrs': {'inner_defense': 73, 'outer_defense': 73, 'hp': 672}
    },
    {
        'id': 10605101,
        'name': '合体·白虎甲胄',
        'quality': 6,
        'position': EquipPart.ARMOR,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 92, 'outer_defense': 92},
        'extend_attrs': {'inner_defense': 73, 'outer_defense': 73, 'hp': 672}
    },
    {
        'id': 10605102,
        'name': '合体·朱雀甲胄',
        'quality': 6,
        'position': EquipPart.ARMOR,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 92, 'outer_defense': 92},
        'extend_attrs': {'inner_defense': 73, 'outer_defense': 73, 'hp': 672}
    },
    {
        'id': 10606000,
        'name': '合体腰带',
        'quality': 6,
        'position': EquipPart.BELT,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'dodge': 83},
        'extend_attrs': {'crit_defense': 69}
    },
    {
        'id': 10606001,
        'name': '融合腰带',
        'quality': 6,
        'position': EquipPart.BELT,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'dodge': 87},
        'extend_attrs': {'crit_defense': 68}
    },
    {
        'id': 10606002,
        'name': '归一腰带',
        'quality': 6,
        'position': EquipPart.BELT,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'dodge': 85},
        'extend_attrs': {'crit_defense': 66}
    },
    {
        'id': 10606003,
        'name': '合体腰带·改',
        'quality': 6,
        'position': EquipPart.BELT,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'dodge': 84},
        'extend_attrs': {'crit_defense': 69}
    },
    {
        'id': 10606004,
        'name': '融合腰带·真',
        'quality': 6,
        'position': EquipPart.BELT,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'dodge': 87},
        'extend_attrs': {'crit_defense': 70}
    },
    {
        'id': 10606005,
        'name': '归一腰带·灵',
        'quality': 6,
        'position': EquipPart.BELT,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'dodge': 81},
        'extend_attrs': {'crit_defense': 67}
    },
    {
        'id': 10606100,
        'name': '合体·青龙腰带',
        'quality': 6,
        'position': EquipPart.BELT,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'dodge': 92},
        'extend_attrs': {'crit_defense': 73, 'hp': 672}
    },
    {
        'id': 10606101,
        'name': '合体·白虎腰带',
        'quality': 6,
        'position': EquipPart.BELT,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'dodge': 92},
        'extend_attrs': {'crit_defense': 73, 'hp': 672}
    },
    {
        'id': 10606102,
        'name': '合体·朱雀腰带',
        'quality': 6,
        'position': EquipPart.BELT,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'dodge': 92},
        'extend_attrs': {'crit_defense': 73, 'hp': 672}
    },
    {
        'id': 10607000,
        'name': '合体护肩',
        'quality': 6,
        'position': EquipPart.SHOULDER,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'dodge': 82},
        'extend_attrs': {'crit_defense': 66}
    },
    {
        'id': 10607001,
        'name': '融合护肩',
        'quality': 6,
        'position': EquipPart.SHOULDER,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'dodge': 86},
        'extend_attrs': {'crit_defense': 64}
    },
    {
        'id': 10607002,
        'name': '归一护肩',
        'quality': 6,
        'position': EquipPart.SHOULDER,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'dodge': 81},
        'extend_attrs': {'crit_defense': 67}
    },
    {
        'id': 10607003,
        'name': '合体护肩·改',
        'quality': 6,
        'position': EquipPart.SHOULDER,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'dodge': 80},
        'extend_attrs': {'crit_defense': 68}
    },
    {
        'id': 10607004,
        'name': '融合护肩·真',
        'quality': 6,
        'position': EquipPart.SHOULDER,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'dodge': 84},
        'extend_attrs': {'crit_defense': 66}
    },
    {
        'id': 10607005,
        'name': '归一护肩·灵',
        'quality': 6,
        'position': EquipPart.SHOULDER,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'dodge': 85},
        'extend_attrs': {'crit_defense': 65}
    },
    {
        'id': 10607100,
        'name': '合体·青龙护肩',
        'quality': 6,
        'position': EquipPart.SHOULDER,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'dodge': 92},
        'extend_attrs': {'crit_defense': 73, 'hp': 672}
    },
    {
        'id': 10607101,
        'name': '合体·白虎护肩',
        'quality': 6,
        'position': EquipPart.SHOULDER,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'dodge': 92},
        'extend_attrs': {'crit_defense': 73, 'hp': 672}
    },
    {
        'id': 10607102,
        'name': '合体·朱雀护肩',
        'quality': 6,
        'position': EquipPart.SHOULDER,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'dodge': 92},
        'extend_attrs': {'crit_defense': 73, 'hp': 672}
    },
    {
        'id': 10608000,
        'name': '合体鞋履',
        'quality': 6,
        'position': EquipPart.BOOTS,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 81},
        'extend_attrs': {'dodge': 66}
    },
    {
        'id': 10608001,
        'name': '融合鞋履',
        'quality': 6,
        'position': EquipPart.BOOTS,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 82},
        'extend_attrs': {'dodge': 70}
    },
    {
        'id': 10608002,
        'name': '归一鞋履',
        'quality': 6,
        'position': EquipPart.BOOTS,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 81},
        'extend_attrs': {'dodge': 68}
    },
    {
        'id': 10608003,
        'name': '合体鞋履·改',
        'quality': 6,
        'position': EquipPart.BOOTS,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 83},
        'extend_attrs': {'dodge': 64}
    },
    {
        'id': 10608004,
        'name': '融合鞋履·真',
        'quality': 6,
        'position': EquipPart.BOOTS,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 81},
        'extend_attrs': {'dodge': 67}
    },
    {
        'id': 10608005,
        'name': '归一鞋履·灵',
        'quality': 6,
        'position': EquipPart.BOOTS,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 82},
        'extend_attrs': {'dodge': 69}
    },
    {
        'id': 10608100,
        'name': '合体·青龙鞋履',
        'quality': 6,
        'position': EquipPart.BOOTS,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 92},
        'extend_attrs': {'dodge': 73, 'hp': 672}
    },
    {
        'id': 10608101,
        'name': '合体·白虎鞋履',
        'quality': 6,
        'position': EquipPart.BOOTS,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 92},
        'extend_attrs': {'dodge': 73, 'hp': 672}
    },
    {
        'id': 10608102,
        'name': '合体·朱雀鞋履',
        'quality': 6,
        'position': EquipPart.BOOTS,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 92},
        'extend_attrs': {'dodge': 73, 'hp': 672}
    },
    {
        'id': 10609000,
        'name': '合体手套',
        'quality': 6,
        'position': EquipPart.GLOVES,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'outer_defense': 87},
        'extend_attrs': {'dodge': 63}
    },
    {
        'id': 10609001,
        'name': '融合手套',
        'quality': 6,
        'position': EquipPart.GLOVES,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'outer_defense': 81},
        'extend_attrs': {'dodge': 69}
    },
    {
        'id': 10609002,
        'name': '归一手套',
        'quality': 6,
        'position': EquipPart.GLOVES,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'outer_defense': 79},
        'extend_attrs': {'dodge': 66}
    },
    {
        'id': 10609003,
        'name': '合体手套·改',
        'quality': 6,
        'position': EquipPart.GLOVES,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'outer_defense': 85},
        'extend_attrs': {'dodge': 69}
    },
    {
        'id': 10609004,
        'name': '融合手套·真',
        'quality': 6,
        'position': EquipPart.GLOVES,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'outer_defense': 83},
        'extend_attrs': {'dodge': 70}
    },
    {
        'id': 10609005,
        'name': '归一手套·灵',
        'quality': 6,
        'position': EquipPart.GLOVES,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'outer_defense': 81},
        'extend_attrs': {'dodge': 65}
    },
    {
        'id': 10609100,
        'name': '合体·青龙手套',
        'quality': 6,
        'position': EquipPart.GLOVES,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'outer_defense': 92},
        'extend_attrs': {'dodge': 73, 'hp': 672}
    },
    {
        'id': 10609101,
        'name': '合体·白虎手套',
        'quality': 6,
        'position': EquipPart.GLOVES,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'outer_defense': 92},
        'extend_attrs': {'dodge': 73, 'hp': 672}
    },
    {
        'id': 10609102,
        'name': '合体·朱雀手套',
        'quality': 6,
        'position': EquipPart.GLOVES,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'outer_defense': 92},
        'extend_attrs': {'dodge': 73, 'hp': 672}
    },
    {
        'id': 10610000,
        'name': '合体项链',
        'quality': 6,
        'position': EquipPart.NECKLACE,
        'type': EquipmentType.HYBRID,
        'base_attrs': {'inner_attack': 175, 'outer_attack': 168},
        'extend_attrs': {'hp': 649, 'inner_defense': 64, 'outer_defense': 64}
    },
    {
        'id': 10610001,
        'name': '融合项链',
        'quality': 6,
        'position': EquipPart.NECKLACE,
        'type': EquipmentType.HYBRID,
        'base_attrs': {'inner_attack': 163, 'outer_attack': 176},
        'extend_attrs': {'hp': 679, 'inner_defense': 64, 'outer_defense': 63}
    },
    {
        'id': 10610002,
        'name': '归一项链',
        'quality': 6,
        'position': EquipPart.NECKLACE,
        'type': EquipmentType.HYBRID,
        'base_attrs': {'inner_attack': 170, 'outer_attack': 175},
        'extend_attrs': {'hp': 660, 'inner_defense': 66, 'outer_defense': 64}
    },
    {
        'id': 10610003,
        'name': '合体项链·改',
        'quality': 6,
        'position': EquipPart.NECKLACE,
        'type': EquipmentType.HYBRID,
        'base_attrs': {'inner_attack': 173, 'outer_attack': 171},
        'extend_attrs': {'hp': 693, 'inner_defense': 66, 'outer_defense': 69}
    },
    {
        'id': 10610004,
        'name': '融合项链·真',
        'quality': 6,
        'position': EquipPart.NECKLACE,
        'type': EquipmentType.HYBRID,
        'base_attrs': {'inner_attack': 175, 'outer_attack': 162},
        'extend_attrs': {'hp': 685, 'inner_defense': 69, 'outer_defense': 67}
    },
    {
        'id': 10610005,
        'name': '归一项链·灵',
        'quality': 6,
        'position': EquipPart.NECKLACE,
        'type': EquipmentType.HYBRID,
        'base_attrs': {'inner_attack': 173, 'outer_attack': 167},
        'extend_attrs': {'hp': 679, 'inner_defense': 66, 'outer_defense': 67}
    },
    {
        'id': 10610100,
        'name': '合体·青龙项链',
        'quality': 6,
        'position': EquipPart.NECKLACE,
        'type': EquipmentType.HYBRID,
        'base_attrs': {'inner_attack': 184, 'outer_attack': 184},
        'extend_attrs': {'hp': 1411, 'inner_defense': 73, 'outer_defense': 73}
    },
    {
        'id': 10610101,
        'name': '合体·白虎项链',
        'quality': 6,
        'position': EquipPart.NECKLACE,
        'type': EquipmentType.HYBRID,
        'base_attrs': {'inner_attack': 184, 'outer_attack': 184},
        'extend_attrs': {'hp': 1411, 'inner_defense': 73, 'outer_defense': 73}
    },
    {
        'id': 10610102,
        'name': '合体·朱雀项链',
        'quality': 6,
        'position': EquipPart.NECKLACE,
        'type': EquipmentType.HYBRID,
        'base_attrs': {'inner_attack': 184, 'outer_attack': 184},
        'extend_attrs': {'hp': 1411, 'inner_defense': 73, 'outer_defense': 73}
    },
    {
        'id': 10611000,
        'name': '合体法宝',
        'quality': 6,
        'position': EquipPart.ARTIFACT,
        'type': EquipmentType.HYBRID,
        'base_attrs': {'hit': 81, 'crit': 84},
        'extend_attrs': {'outer_attack': 134, 'inner_attack': 138}
    },
    {
        'id': 10611001,
        'name': '融合法宝',
        'quality': 6,
        'position': EquipPart.ARTIFACT,
        'type': EquipmentType.HYBRID,
        'base_attrs': {'hit': 83, 'crit': 86},
        'extend_attrs': {'outer_attack': 129, 'inner_attack': 129}
    },
    {
        'id': 10611002,
        'name': '归一法宝',
        'quality': 6,
        'position': EquipPart.ARTIFACT,
        'type': EquipmentType.HYBRID,
        'base_attrs': {'hit': 85, 'crit': 81},
        'extend_attrs': {'outer_attack': 136, 'inner_attack': 138}
    },
    {
        'id': 10611003,
        'name': '合体法宝·改',
        'quality': 6,
        'position': EquipPart.ARTIFACT,
        'type': EquipmentType.HYBRID,
        'base_attrs': {'hit': 83, 'crit': 83},
        'extend_attrs': {'outer_attack': 132, 'inner_attack': 132}
    },
    {
        'id': 10611004,
        'name': '融合法宝·真',
        'quality': 6,
        'position': EquipPart.ARTIFACT,
        'type': EquipmentType.HYBRID,
        'base_attrs': {'hit': 85, 'crit': 81},
        'extend_attrs': {'outer_attack': 136, 'inner_attack': 138}
    },
    {
        'id': 10611005,
        'name': '归一法宝·灵',
        'quality': 6,
        'position': EquipPart.ARTIFACT,
        'type': EquipmentType.HYBRID,
        'base_attrs': {'hit': 83, 'crit': 81},
        'extend_attrs': {'outer_attack': 128, 'inner_attack': 129}
    },
    {
        'id': 10611100,
        'name': '合体·青龙法宝',
        'quality': 6,
        'position': EquipPart.ARTIFACT,
        'type': EquipmentType.HYBRID,
        'base_attrs': {'hit': 92, 'crit': 92},
        'extend_attrs': {'outer_attack': 147, 'inner_attack': 147, 'hp': 672}
    },
    {
        'id': 10611101,
        'name': '合体·白虎法宝',
        'quality': 6,
        'position': EquipPart.ARTIFACT,
        'type': EquipmentType.HYBRID,
        'base_attrs': {'hit': 92, 'crit': 92},
        'extend_attrs': {'outer_attack': 147, 'inner_attack': 147, 'hp': 672}
    },
    {
        'id': 10611102,
        'name': '合体·朱雀法宝',
        'quality': 6,
        'position': EquipPart.ARTIFACT,
        'type': EquipmentType.HYBRID,
        'base_attrs': {'hit': 92, 'crit': 92},
        'extend_attrs': {'outer_attack': 147, 'inner_attack': 147, 'hp': 672}
    },
    {
        'id': 10700000,
        'name': '大乘剑',
        'quality': 7,
        'position': EquipPart.WEAPON,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'inner_attack': 190, 'outer_attack': 197},
        'extend_attrs': {'hp': 752, 'hit': 77, 'crit': 73}
    },
    {
        'id': 10700001,
        'name': '圆满刀',
        'quality': 7,
        'position': EquipPart.WEAPON,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'inner_attack': 196, 'outer_attack': 195},
        'extend_attrs': {'hp': 766, 'hit': 76, 'crit': 72}
    },
    {
        'id': 10700002,
        'name': '通天弓',
        'quality': 7,
        'position': EquipPart.WEAPON,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'inner_attack': 192, 'outer_attack': 184},
        'extend_attrs': {'hp': 794, 'hit': 76, 'crit': 74}
    },
    {
        'id': 10700003,
        'name': '大乘弩',
        'quality': 7,
        'position': EquipPart.WEAPON,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'inner_attack': 197, 'outer_attack': 193},
        'extend_attrs': {'hp': 734, 'hit': 76, 'crit': 73}
    },
    {
        'id': 10700004,
        'name': '圆满枪',
        'quality': 7,
        'position': EquipPart.WEAPON,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'inner_attack': 189, 'outer_attack': 185},
        'extend_attrs': {'hp': 764, 'hit': 79, 'crit': 73}
    },
    {
        'id': 10700005,
        'name': '通天棍',
        'quality': 7,
        'position': EquipPart.WEAPON,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'inner_attack': 200, 'outer_attack': 186},
        'extend_attrs': {'hp': 803, 'hit': 79, 'crit': 74}
    },
    {
        'id': 10700100,
        'name': '大乘·青龙剑',
        'quality': 7,
        'position': EquipPart.WEAPON,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'inner_attack': 211, 'outer_attack': 211},
        'extend_attrs': {'hp': 1612, 'hit': 83, 'crit': 83}
    },
    {
        'id': 10700101,
        'name': '大乘·白虎刀',
        'quality': 7,
        'position': EquipPart.WEAPON,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'inner_attack': 211, 'outer_attack': 211},
        'extend_attrs': {'hp': 1612, 'hit': 83, 'crit': 83}
    },
    {
        'id': 10700102,
        'name': '大乘·朱雀弓',
        'quality': 7,
        'position': EquipPart.WEAPON,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'inner_attack': 211, 'outer_attack': 211},
        'extend_attrs': {'hp': 1612, 'hit': 83, 'crit': 83}
    },
    {
        'id': 10701000,
        'name': '大乘护腕',
        'quality': 7,
        'position': EquipPart.BRACER,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'hit': 99},
        'extend_attrs': {'outer_attack': 158, 'inner_attack': 154}
    },
    {
        'id': 10701001,
        'name': '圆满护腕',
        'quality': 7,
        'position': EquipPart.BRACER,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'hit': 100},
        'extend_attrs': {'outer_attack': 158, 'inner_attack': 155}
    },
    {
        'id': 10701002,
        'name': '通天护腕',
        'quality': 7,
        'position': EquipPart.BRACER,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'hit': 96},
        'extend_attrs': {'outer_attack': 151, 'inner_attack': 147}
    },
    {
        'id': 10701003,
        'name': '大乘护腕·改',
        'quality': 7,
        'position': EquipPart.BRACER,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'hit': 95},
        'extend_attrs': {'outer_attack': 153, 'inner_attack': 155}
    },
    {
        'id': 10701004,
        'name': '圆满护腕·真',
        'quality': 7,
        'position': EquipPart.BRACER,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'hit': 94},
        'extend_attrs': {'outer_attack': 158, 'inner_attack': 145}
    },
    {
        'id': 10701005,
        'name': '通天护腕·灵',
        'quality': 7,
        'position': EquipPart.BRACER,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'hit': 93},
        'extend_attrs': {'outer_attack': 152, 'inner_attack': 147}
    },
    {
        'id': 10701100,
        'name': '大乘·青龙护腕',
        'quality': 7,
        'position': EquipPart.BRACER,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'hit': 105},
        'extend_attrs': {'outer_attack': 168, 'inner_attack': 168, 'hp': 768}
    },
    {
        'id': 10701101,
        'name': '大乘·白虎护腕',
        'quality': 7,
        'position': EquipPart.BRACER,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'hit': 105},
        'extend_attrs': {'outer_attack': 168, 'inner_attack': 168, 'hp': 768}
    },
    {
        'id': 10701102,
        'name': '大乘·朱雀护腕',
        'quality': 7,
        'position': EquipPart.BRACER,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'hit': 105},
        'extend_attrs': {'outer_attack': 168, 'inner_attack': 168, 'hp': 768}
    },
    {
        'id': 10702000,
        'name': '大乘戒指',
        'quality': 7,
        'position': EquipPart.RING,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'inner_attack': 191},
        'extend_attrs': {'hit': 73, 'crit': 77}
    },
    {
        'id': 10702001,
        'name': '圆满戒指',
        'quality': 7,
        'position': EquipPart.RING,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'inner_attack': 194},
        'extend_attrs': {'hit': 76, 'crit': 74}
    },
    {
        'id': 10702002,
        'name': '通天戒指',
        'quality': 7,
        'position': EquipPart.RING,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'inner_attack': 194},
        'extend_attrs': {'hit': 73, 'crit': 79}
    },
    {
        'id': 10702003,
        'name': '大乘戒指·改',
        'quality': 7,
        'position': EquipPart.RING,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'inner_attack': 194},
        'extend_attrs': {'hit': 72, 'crit': 79}
    },
    {
        'id': 10702004,
        'name': '圆满戒指·真',
        'quality': 7,
        'position': EquipPart.RING,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'inner_attack': 193},
        'extend_attrs': {'hit': 78, 'crit': 78}
    },
    {
        'id': 10702005,
        'name': '通天戒指·灵',
        'quality': 7,
        'position': EquipPart.RING,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'inner_attack': 192},
        'extend_attrs': {'hit': 72, 'crit': 78}
    },
    {
        'id': 10702100,
        'name': '大乘·青龙戒指',
        'quality': 7,
        'position': EquipPart.RING,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'inner_attack': 211},
        'extend_attrs': {'hit': 83, 'crit': 83, 'hp': 768}
    },
    {
        'id': 10702101,
        'name': '大乘·白虎戒指',
        'quality': 7,
        'position': EquipPart.RING,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'inner_attack': 211},
        'extend_attrs': {'hit': 83, 'crit': 83, 'hp': 768}
    },
    {
        'id': 10702102,
        'name': '大乘·朱雀戒指',
        'quality': 7,
        'position': EquipPart.RING,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'inner_attack': 211},
        'extend_attrs': {'hit': 83, 'crit': 83, 'hp': 768}
    },
    {
        'id': 10703000,
        'name': '大乘护符',
        'quality': 7,
        'position': EquipPart.AMULET,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'outer_attack': 192},
        'extend_attrs': {'hit': 78, 'crit': 72}
    },
    {
        'id': 10703001,
        'name': '圆满护符',
        'quality': 7,
        'position': EquipPart.AMULET,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'outer_attack': 187},
        'extend_attrs': {'hit': 76, 'crit': 75}
    },
    {
        'id': 10703002,
        'name': '通天护符',
        'quality': 7,
        'position': EquipPart.AMULET,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'outer_attack': 188},
        'extend_attrs': {'hit': 73, 'crit': 78}
    },
    {
        'id': 10703003,
        'name': '大乘护符·改',
        'quality': 7,
        'position': EquipPart.AMULET,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'outer_attack': 189},
        'extend_attrs': {'hit': 79, 'crit': 75}
    },
    {
        'id': 10703004,
        'name': '圆满护符·真',
        'quality': 7,
        'position': EquipPart.AMULET,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'outer_attack': 185},
        'extend_attrs': {'hit': 79, 'crit': 73}
    },
    {
        'id': 10703005,
        'name': '通天护符·灵',
        'quality': 7,
        'position': EquipPart.AMULET,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'outer_attack': 187},
        'extend_attrs': {'hit': 78, 'crit': 73}
    },
    {
        'id': 10703100,
        'name': '大乘·青龙护符',
        'quality': 7,
        'position': EquipPart.AMULET,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'outer_attack': 211},
        'extend_attrs': {'hit': 83, 'crit': 83, 'hp': 768}
    },
    {
        'id': 10703101,
        'name': '大乘·白虎护符',
        'quality': 7,
        'position': EquipPart.AMULET,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'outer_attack': 211},
        'extend_attrs': {'hit': 83, 'crit': 83, 'hp': 768}
    },
    {
        'id': 10703102,
        'name': '大乘·朱雀护符',
        'quality': 7,
        'position': EquipPart.AMULET,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'outer_attack': 211},
        'extend_attrs': {'hit': 83, 'crit': 83, 'hp': 768}
    },
    {
        'id': 10704000,
        'name': '大乘头盔',
        'quality': 7,
        'position': EquipPart.HELMET,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 99, 'outer_defense': 99},
        'extend_attrs': {'inner_defense': 77, 'outer_defense': 75}
    },
    {
        'id': 10704001,
        'name': '圆满头盔',
        'quality': 7,
        'position': EquipPart.HELMET,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 93, 'outer_defense': 98},
        'extend_attrs': {'inner_defense': 76, 'outer_defense': 74}
    },
    {
        'id': 10704002,
        'name': '通天头盔',
        'quality': 7,
        'position': EquipPart.HELMET,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 98, 'outer_defense': 96},
        'extend_attrs': {'inner_defense': 75, 'outer_defense': 78}
    },
    {
        'id': 10704003,
        'name': '大乘头盔·改',
        'quality': 7,
        'position': EquipPart.HELMET,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 91, 'outer_defense': 92},
        'extend_attrs': {'inner_defense': 72, 'outer_defense': 73}
    },
    {
        'id': 10704004,
        'name': '圆满头盔·真',
        'quality': 7,
        'position': EquipPart.HELMET,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 97, 'outer_defense': 98},
        'extend_attrs': {'inner_defense': 74, 'outer_defense': 79}
    },
    {
        'id': 10704005,
        'name': '通天头盔·灵',
        'quality': 7,
        'position': EquipPart.HELMET,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 93, 'outer_defense': 99},
        'extend_attrs': {'inner_defense': 79, 'outer_defense': 77}
    },
    {
        'id': 10704100,
        'name': '大乘·青龙头盔',
        'quality': 7,
        'position': EquipPart.HELMET,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 105, 'outer_defense': 105},
        'extend_attrs': {'inner_defense': 83, 'outer_defense': 83, 'hp': 768}
    },
    {
        'id': 10704101,
        'name': '大乘·白虎头盔',
        'quality': 7,
        'position': EquipPart.HELMET,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 105, 'outer_defense': 105},
        'extend_attrs': {'inner_defense': 83, 'outer_defense': 83, 'hp': 768}
    },
    {
        'id': 10704102,
        'name': '大乘·朱雀头盔',
        'quality': 7,
        'position': EquipPart.HELMET,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 105, 'outer_defense': 105},
        'extend_attrs': {'inner_defense': 83, 'outer_defense': 83, 'hp': 768}
    },
    {
        'id': 10705000,
        'name': '大乘甲胄',
        'quality': 7,
        'position': EquipPart.ARMOR,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 94, 'outer_defense': 98},
        'extend_attrs': {'inner_defense': 76, 'outer_defense': 77}
    },
    {
        'id': 10705001,
        'name': '圆满甲胄',
        'quality': 7,
        'position': EquipPart.ARMOR,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 95, 'outer_defense': 96},
        'extend_attrs': {'inner_defense': 73, 'outer_defense': 74}
    },
    {
        'id': 10705002,
        'name': '通天甲胄',
        'quality': 7,
        'position': EquipPart.ARMOR,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 99, 'outer_defense': 97},
        'extend_attrs': {'inner_defense': 76, 'outer_defense': 78}
    },
    {
        'id': 10705003,
        'name': '大乘甲胄·改',
        'quality': 7,
        'position': EquipPart.ARMOR,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 100, 'outer_defense': 93},
        'extend_attrs': {'inner_defense': 72, 'outer_defense': 79}
    },
    {
        'id': 10705004,
        'name': '圆满甲胄·真',
        'quality': 7,
        'position': EquipPart.ARMOR,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 96, 'outer_defense': 98},
        'extend_attrs': {'inner_defense': 74, 'outer_defense': 79}
    },
    {
        'id': 10705005,
        'name': '通天甲胄·灵',
        'quality': 7,
        'position': EquipPart.ARMOR,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 94, 'outer_defense': 94},
        'extend_attrs': {'inner_defense': 76, 'outer_defense': 74}
    },
    {
        'id': 10705100,
        'name': '大乘·青龙甲胄',
        'quality': 7,
        'position': EquipPart.ARMOR,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 105, 'outer_defense': 105},
        'extend_attrs': {'inner_defense': 83, 'outer_defense': 83, 'hp': 768}
    },
    {
        'id': 10705101,
        'name': '大乘·白虎甲胄',
        'quality': 7,
        'position': EquipPart.ARMOR,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 105, 'outer_defense': 105},
        'extend_attrs': {'inner_defense': 83, 'outer_defense': 83, 'hp': 768}
    },
    {
        'id': 10705102,
        'name': '大乘·朱雀甲胄',
        'quality': 7,
        'position': EquipPart.ARMOR,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 105, 'outer_defense': 105},
        'extend_attrs': {'inner_defense': 83, 'outer_defense': 83, 'hp': 768}
    },
    {
        'id': 10706000,
        'name': '大乘腰带',
        'quality': 7,
        'position': EquipPart.BELT,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'dodge': 93},
        'extend_attrs': {'crit_defense': 73}
    },
    {
        'id': 10706001,
        'name': '圆满腰带',
        'quality': 7,
        'position': EquipPart.BELT,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'dodge': 91},
        'extend_attrs': {'crit_defense': 72}
    },
    {
        'id': 10706002,
        'name': '通天腰带',
        'quality': 7,
        'position': EquipPart.BELT,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'dodge': 91},
        'extend_attrs': {'crit_defense': 78}
    },
    {
        'id': 10706003,
        'name': '大乘腰带·改',
        'quality': 7,
        'position': EquipPart.BELT,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'dodge': 100},
        'extend_attrs': {'crit_defense': 76}
    },
    {
        'id': 10706004,
        'name': '圆满腰带·真',
        'quality': 7,
        'position': EquipPart.BELT,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'dodge': 91},
        'extend_attrs': {'crit_defense': 78}
    },
    {
        'id': 10706005,
        'name': '通天腰带·灵',
        'quality': 7,
        'position': EquipPart.BELT,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'dodge': 95},
        'extend_attrs': {'crit_defense': 76}
    },
    {
        'id': 10706100,
        'name': '大乘·青龙腰带',
        'quality': 7,
        'position': EquipPart.BELT,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'dodge': 105},
        'extend_attrs': {'crit_defense': 83, 'hp': 768}
    },
    {
        'id': 10706101,
        'name': '大乘·白虎腰带',
        'quality': 7,
        'position': EquipPart.BELT,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'dodge': 105},
        'extend_attrs': {'crit_defense': 83, 'hp': 768}
    },
    {
        'id': 10706102,
        'name': '大乘·朱雀腰带',
        'quality': 7,
        'position': EquipPart.BELT,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'dodge': 105},
        'extend_attrs': {'crit_defense': 83, 'hp': 768}
    },
    {
        'id': 10707000,
        'name': '大乘护肩',
        'quality': 7,
        'position': EquipPart.SHOULDER,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'dodge': 93},
        'extend_attrs': {'crit_defense': 77}
    },
    {
        'id': 10707001,
        'name': '圆满护肩',
        'quality': 7,
        'position': EquipPart.SHOULDER,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'dodge': 96},
        'extend_attrs': {'crit_defense': 74}
    },
    {
        'id': 10707002,
        'name': '通天护肩',
        'quality': 7,
        'position': EquipPart.SHOULDER,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'dodge': 99},
        'extend_attrs': {'crit_defense': 78}
    },
    {
        'id': 10707003,
        'name': '大乘护肩·改',
        'quality': 7,
        'position': EquipPart.SHOULDER,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'dodge': 97},
        'extend_attrs': {'crit_defense': 76}
    },
    {
        'id': 10707004,
        'name': '圆满护肩·真',
        'quality': 7,
        'position': EquipPart.SHOULDER,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'dodge': 91},
        'extend_attrs': {'crit_defense': 77}
    },
    {
        'id': 10707005,
        'name': '通天护肩·灵',
        'quality': 7,
        'position': EquipPart.SHOULDER,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'dodge': 91},
        'extend_attrs': {'crit_defense': 75}
    },
    {
        'id': 10707100,
        'name': '大乘·青龙护肩',
        'quality': 7,
        'position': EquipPart.SHOULDER,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'dodge': 105},
        'extend_attrs': {'crit_defense': 83, 'hp': 768}
    },
    {
        'id': 10707101,
        'name': '大乘·白虎护肩',
        'quality': 7,
        'position': EquipPart.SHOULDER,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'dodge': 105},
        'extend_attrs': {'crit_defense': 83, 'hp': 768}
    },
    {
        'id': 10707102,
        'name': '大乘·朱雀护肩',
        'quality': 7,
        'position': EquipPart.SHOULDER,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'dodge': 105},
        'extend_attrs': {'crit_defense': 83, 'hp': 768}
    },
    {
        'id': 10708000,
        'name': '大乘鞋履',
        'quality': 7,
        'position': EquipPart.BOOTS,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 93},
        'extend_attrs': {'dodge': 75}
    },
    {
        'id': 10708001,
        'name': '圆满鞋履',
        'quality': 7,
        'position': EquipPart.BOOTS,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 98},
        'extend_attrs': {'dodge': 73}
    },
    {
        'id': 10708002,
        'name': '通天鞋履',
        'quality': 7,
        'position': EquipPart.BOOTS,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 98},
        'extend_attrs': {'dodge': 78}
    },
    {
        'id': 10708003,
        'name': '大乘鞋履·改',
        'quality': 7,
        'position': EquipPart.BOOTS,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 96},
        'extend_attrs': {'dodge': 74}
    },
    {
        'id': 10708004,
        'name': '圆满鞋履·真',
        'quality': 7,
        'position': EquipPart.BOOTS,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 100},
        'extend_attrs': {'dodge': 77}
    },
    {
        'id': 10708005,
        'name': '通天鞋履·灵',
        'quality': 7,
        'position': EquipPart.BOOTS,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 97},
        'extend_attrs': {'dodge': 73}
    },
    {
        'id': 10708100,
        'name': '大乘·青龙鞋履',
        'quality': 7,
        'position': EquipPart.BOOTS,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 105},
        'extend_attrs': {'dodge': 83, 'hp': 768}
    },
    {
        'id': 10708101,
        'name': '大乘·白虎鞋履',
        'quality': 7,
        'position': EquipPart.BOOTS,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 105},
        'extend_attrs': {'dodge': 83, 'hp': 768}
    },
    {
        'id': 10708102,
        'name': '大乘·朱雀鞋履',
        'quality': 7,
        'position': EquipPart.BOOTS,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 105},
        'extend_attrs': {'dodge': 83, 'hp': 768}
    },
    {
        'id': 10709000,
        'name': '大乘手套',
        'quality': 7,
        'position': EquipPart.GLOVES,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'outer_defense': 94},
        'extend_attrs': {'dodge': 77}
    },
    {
        'id': 10709001,
        'name': '圆满手套',
        'quality': 7,
        'position': EquipPart.GLOVES,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'outer_defense': 94},
        'extend_attrs': {'dodge': 78}
    },
    {
        'id': 10709002,
        'name': '通天手套',
        'quality': 7,
        'position': EquipPart.GLOVES,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'outer_defense': 98},
        'extend_attrs': {'dodge': 74}
    },
    {
        'id': 10709003,
        'name': '大乘手套·改',
        'quality': 7,
        'position': EquipPart.GLOVES,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'outer_defense': 96},
        'extend_attrs': {'dodge': 74}
    },
    {
        'id': 10709004,
        'name': '圆满手套·真',
        'quality': 7,
        'position': EquipPart.GLOVES,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'outer_defense': 94},
        'extend_attrs': {'dodge': 77}
    },
    {
        'id': 10709005,
        'name': '通天手套·灵',
        'quality': 7,
        'position': EquipPart.GLOVES,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'outer_defense': 96},
        'extend_attrs': {'dodge': 76}
    },
    {
        'id': 10709100,
        'name': '大乘·青龙手套',
        'quality': 7,
        'position': EquipPart.GLOVES,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'outer_defense': 105},
        'extend_attrs': {'dodge': 83, 'hp': 768}
    },
    {
        'id': 10709101,
        'name': '大乘·白虎手套',
        'quality': 7,
        'position': EquipPart.GLOVES,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'outer_defense': 105},
        'extend_attrs': {'dodge': 83, 'hp': 768}
    },
    {
        'id': 10709102,
        'name': '大乘·朱雀手套',
        'quality': 7,
        'position': EquipPart.GLOVES,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'outer_defense': 105},
        'extend_attrs': {'dodge': 83, 'hp': 768}
    },
    {
        'id': 10710000,
        'name': '大乘项链',
        'quality': 7,
        'position': EquipPart.NECKLACE,
        'type': EquipmentType.HYBRID,
        'base_attrs': {'inner_attack': 187, 'outer_attack': 194},
        'extend_attrs': {'hp': 740, 'inner_defense': 77, 'outer_defense': 75}
    },
    {
        'id': 10710001,
        'name': '圆满项链',
        'quality': 7,
        'position': EquipPart.NECKLACE,
        'type': EquipmentType.HYBRID,
        'base_attrs': {'inner_attack': 195, 'outer_attack': 201},
        'extend_attrs': {'hp': 776, 'inner_defense': 79, 'outer_defense': 77}
    },
    {
        'id': 10710002,
        'name': '通天项链',
        'quality': 7,
        'position': EquipPart.NECKLACE,
        'type': EquipmentType.HYBRID,
        'base_attrs': {'inner_attack': 192, 'outer_attack': 199},
        'extend_attrs': {'hp': 786, 'inner_defense': 78, 'outer_defense': 73}
    },
    {
        'id': 10710003,
        'name': '大乘项链·改',
        'quality': 7,
        'position': EquipPart.NECKLACE,
        'type': EquipmentType.HYBRID,
        'base_attrs': {'inner_attack': 184, 'outer_attack': 200},
        'extend_attrs': {'hp': 758, 'inner_defense': 76, 'outer_defense': 76}
    },
    {
        'id': 10710004,
        'name': '圆满项链·真',
        'quality': 7,
        'position': EquipPart.NECKLACE,
        'type': EquipmentType.HYBRID,
        'base_attrs': {'inner_attack': 195, 'outer_attack': 184},
        'extend_attrs': {'hp': 730, 'inner_defense': 75, 'outer_defense': 78}
    },
    {
        'id': 10710005,
        'name': '通天项链·灵',
        'quality': 7,
        'position': EquipPart.NECKLACE,
        'type': EquipmentType.HYBRID,
        'base_attrs': {'inner_attack': 200, 'outer_attack': 182},
        'extend_attrs': {'hp': 733, 'inner_defense': 75, 'outer_defense': 77}
    },
    {
        'id': 10710100,
        'name': '大乘·青龙项链',
        'quality': 7,
        'position': EquipPart.NECKLACE,
        'type': EquipmentType.HYBRID,
        'base_attrs': {'inner_attack': 211, 'outer_attack': 211},
        'extend_attrs': {'hp': 1612, 'inner_defense': 83, 'outer_defense': 83}
    },
    {
        'id': 10710101,
        'name': '大乘·白虎项链',
        'quality': 7,
        'position': EquipPart.NECKLACE,
        'type': EquipmentType.HYBRID,
        'base_attrs': {'inner_attack': 211, 'outer_attack': 211},
        'extend_attrs': {'hp': 1612, 'inner_defense': 83, 'outer_defense': 83}
    },
    {
        'id': 10710102,
        'name': '大乘·朱雀项链',
        'quality': 7,
        'position': EquipPart.NECKLACE,
        'type': EquipmentType.HYBRID,
        'base_attrs': {'inner_attack': 211, 'outer_attack': 211},
        'extend_attrs': {'hp': 1612, 'inner_defense': 83, 'outer_defense': 83}
    },
    {
        'id': 10711000,
        'name': '大乘法宝',
        'quality': 7,
        'position': EquipPart.ARTIFACT,
        'type': EquipmentType.HYBRID,
        'base_attrs': {'hit': 93, 'crit': 95},
        'extend_attrs': {'outer_attack': 157, 'inner_attack': 152}
    },
    {
        'id': 10711001,
        'name': '圆满法宝',
        'quality': 7,
        'position': EquipPart.ARTIFACT,
        'type': EquipmentType.HYBRID,
        'base_attrs': {'hit': 97, 'crit': 97},
        'extend_attrs': {'outer_attack': 147, 'inner_attack': 154}
    },
    {
        'id': 10711002,
        'name': '通天法宝',
        'quality': 7,
        'position': EquipPart.ARTIFACT,
        'type': EquipmentType.HYBRID,
        'base_attrs': {'hit': 94, 'crit': 99},
        'extend_attrs': {'outer_attack': 149, 'inner_attack': 160}
    },
    {
        'id': 10711003,
        'name': '大乘法宝·改',
        'quality': 7,
        'position': EquipPart.ARTIFACT,
        'type': EquipmentType.HYBRID,
        'base_attrs': {'hit': 95, 'crit': 95},
        'extend_attrs': {'outer_attack': 146, 'inner_attack': 146}
    },
    {
        'id': 10711004,
        'name': '圆满法宝·真',
        'quality': 7,
        'position': EquipPart.ARTIFACT,
        'type': EquipmentType.HYBRID,
        'base_attrs': {'hit': 92, 'crit': 96},
        'extend_attrs': {'outer_attack': 152, 'inner_attack': 158}
    },
    {
        'id': 10711005,
        'name': '通天法宝·灵',
        'quality': 7,
        'position': EquipPart.ARTIFACT,
        'type': EquipmentType.HYBRID,
        'base_attrs': {'hit': 97, 'crit': 93},
        'extend_attrs': {'outer_attack': 149, 'inner_attack': 156}
    },
    {
        'id': 10711100,
        'name': '大乘·青龙法宝',
        'quality': 7,
        'position': EquipPart.ARTIFACT,
        'type': EquipmentType.HYBRID,
        'base_attrs': {'hit': 105, 'crit': 105},
        'extend_attrs': {'outer_attack': 168, 'inner_attack': 168, 'hp': 768}
    },
    {
        'id': 10711101,
        'name': '大乘·白虎法宝',
        'quality': 7,
        'position': EquipPart.ARTIFACT,
        'type': EquipmentType.HYBRID,
        'base_attrs': {'hit': 105, 'crit': 105},
        'extend_attrs': {'outer_attack': 168, 'inner_attack': 168, 'hp': 768}
    },
    {
        'id': 10711102,
        'name': '大乘·朱雀法宝',
        'quality': 7,
        'position': EquipPart.ARTIFACT,
        'type': EquipmentType.HYBRID,
        'base_attrs': {'hit': 105, 'crit': 105},
        'extend_attrs': {'outer_attack': 168, 'inner_attack': 168, 'hp': 768}
    },
    {
        'id': 10800000,
        'name': '渡劫剑',
        'quality': 8,
        'position': EquipPart.WEAPON,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'inner_attack': 209, 'outer_attack': 214},
        'extend_attrs': {'hp': 885, 'hit': 85, 'crit': 83}
    },
    {
        'id': 10800001,
        'name': '天劫刀',
        'quality': 8,
        'position': EquipPart.WEAPON,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'inner_attack': 215, 'outer_attack': 223},
        'extend_attrs': {'hp': 829, 'hit': 88, 'crit': 84}
    },
    {
        'id': 10800002,
        'name': '雷劫弓',
        'quality': 8,
        'position': EquipPart.WEAPON,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'inner_attack': 219, 'outer_attack': 207},
        'extend_attrs': {'hp': 889, 'hit': 89, 'crit': 84}
    },
    {
        'id': 10800003,
        'name': '渡劫弩',
        'quality': 8,
        'position': EquipPart.WEAPON,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'inner_attack': 224, 'outer_attack': 208},
        'extend_attrs': {'hp': 865, 'hit': 83, 'crit': 84}
    },
    {
        'id': 10800004,
        'name': '天劫枪',
        'quality': 8,
        'position': EquipPart.WEAPON,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'inner_attack': 205, 'outer_attack': 216},
        'extend_attrs': {'hp': 826, 'hit': 81, 'crit': 89}
    },
    {
        'id': 10800005,
        'name': '雷劫棍',
        'quality': 8,
        'position': EquipPart.WEAPON,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'inner_attack': 216, 'outer_attack': 213},
        'extend_attrs': {'hp': 868, 'hit': 86, 'crit': 82}
    },
    {
        'id': 10800100,
        'name': '渡劫·青龙剑',
        'quality': 8,
        'position': EquipPart.WEAPON,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'inner_attack': 237, 'outer_attack': 237},
        'extend_attrs': {'hp': 1814, 'hit': 94, 'crit': 94}
    },
    {
        'id': 10800101,
        'name': '渡劫·白虎刀',
        'quality': 8,
        'position': EquipPart.WEAPON,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'inner_attack': 237, 'outer_attack': 237},
        'extend_attrs': {'hp': 1814, 'hit': 94, 'crit': 94}
    },
    {
        'id': 10800102,
        'name': '渡劫·朱雀弓',
        'quality': 8,
        'position': EquipPart.WEAPON,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'inner_attack': 237, 'outer_attack': 237},
        'extend_attrs': {'hp': 1814, 'hit': 94, 'crit': 94}
    },
    {
        'id': 10801000,
        'name': '渡劫护腕',
        'quality': 8,
        'position': EquipPart.BRACER,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'hit': 110},
        'extend_attrs': {'outer_attack': 164, 'inner_attack': 178}
    },
    {
        'id': 10801001,
        'name': '天劫护腕',
        'quality': 8,
        'position': EquipPart.BRACER,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'hit': 112},
        'extend_attrs': {'outer_attack': 175, 'inner_attack': 179}
    },
    {
        'id': 10801002,
        'name': '雷劫护腕',
        'quality': 8,
        'position': EquipPart.BRACER,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'hit': 112},
        'extend_attrs': {'outer_attack': 176, 'inner_attack': 168}
    },
    {
        'id': 10801003,
        'name': '渡劫护腕·改',
        'quality': 8,
        'position': EquipPart.BRACER,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'hit': 109},
        'extend_attrs': {'outer_attack': 175, 'inner_attack': 164}
    },
    {
        'id': 10801004,
        'name': '天劫护腕·真',
        'quality': 8,
        'position': EquipPart.BRACER,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'hit': 109},
        'extend_attrs': {'outer_attack': 176, 'inner_attack': 164}
    },
    {
        'id': 10801005,
        'name': '雷劫护腕·灵',
        'quality': 8,
        'position': EquipPart.BRACER,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'hit': 106},
        'extend_attrs': {'outer_attack': 178, 'inner_attack': 172}
    },
    {
        'id': 10801100,
        'name': '渡劫·青龙护腕',
        'quality': 8,
        'position': EquipPart.BRACER,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'hit': 118},
        'extend_attrs': {'outer_attack': 189, 'inner_attack': 189, 'hp': 864}
    },
    {
        'id': 10801101,
        'name': '渡劫·白虎护腕',
        'quality': 8,
        'position': EquipPart.BRACER,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'hit': 118},
        'extend_attrs': {'outer_attack': 189, 'inner_attack': 189, 'hp': 864}
    },
    {
        'id': 10801102,
        'name': '渡劫·朱雀护腕',
        'quality': 8,
        'position': EquipPart.BRACER,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'hit': 118},
        'extend_attrs': {'outer_attack': 189, 'inner_attack': 189, 'hp': 864}
    },
    {
        'id': 10802000,
        'name': '渡劫戒指',
        'quality': 8,
        'position': EquipPart.RING,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'inner_attack': 214},
        'extend_attrs': {'hit': 84, 'crit': 89}
    },
    {
        'id': 10802001,
        'name': '天劫戒指',
        'quality': 8,
        'position': EquipPart.RING,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'inner_attack': 216},
        'extend_attrs': {'hit': 82, 'crit': 85}
    },
    {
        'id': 10802002,
        'name': '雷劫戒指',
        'quality': 8,
        'position': EquipPart.RING,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'inner_attack': 225},
        'extend_attrs': {'hit': 88, 'crit': 83}
    },
    {
        'id': 10802003,
        'name': '渡劫戒指·改',
        'quality': 8,
        'position': EquipPart.RING,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'inner_attack': 217},
        'extend_attrs': {'hit': 86, 'crit': 86}
    },
    {
        'id': 10802004,
        'name': '天劫戒指·真',
        'quality': 8,
        'position': EquipPart.RING,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'inner_attack': 218},
        'extend_attrs': {'hit': 89, 'crit': 83}
    },
    {
        'id': 10802005,
        'name': '雷劫戒指·灵',
        'quality': 8,
        'position': EquipPart.RING,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'inner_attack': 219},
        'extend_attrs': {'hit': 87, 'crit': 84}
    },
    {
        'id': 10802100,
        'name': '渡劫·青龙戒指',
        'quality': 8,
        'position': EquipPart.RING,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'inner_attack': 237},
        'extend_attrs': {'hit': 94, 'crit': 94, 'hp': 864}
    },
    {
        'id': 10802101,
        'name': '渡劫·白虎戒指',
        'quality': 8,
        'position': EquipPart.RING,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'inner_attack': 237},
        'extend_attrs': {'hit': 94, 'crit': 94, 'hp': 864}
    },
    {
        'id': 10802102,
        'name': '渡劫·朱雀戒指',
        'quality': 8,
        'position': EquipPart.RING,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'inner_attack': 237},
        'extend_attrs': {'hit': 94, 'crit': 94, 'hp': 864}
    },
    {
        'id': 10803000,
        'name': '渡劫护符',
        'quality': 8,
        'position': EquipPart.AMULET,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'outer_attack': 214},
        'extend_attrs': {'hit': 84, 'crit': 88}
    },
    {
        'id': 10803001,
        'name': '天劫护符',
        'quality': 8,
        'position': EquipPart.AMULET,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'outer_attack': 217},
        'extend_attrs': {'hit': 88, 'crit': 89}
    },
    {
        'id': 10803002,
        'name': '雷劫护符',
        'quality': 8,
        'position': EquipPart.AMULET,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'outer_attack': 217},
        'extend_attrs': {'hit': 88, 'crit': 86}
    },
    {
        'id': 10803003,
        'name': '渡劫护符·改',
        'quality': 8,
        'position': EquipPart.AMULET,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'outer_attack': 219},
        'extend_attrs': {'hit': 90, 'crit': 84}
    },
    {
        'id': 10803004,
        'name': '天劫护符·真',
        'quality': 8,
        'position': EquipPart.AMULET,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'outer_attack': 209},
        'extend_attrs': {'hit': 87, 'crit': 82}
    },
    {
        'id': 10803005,
        'name': '雷劫护符·灵',
        'quality': 8,
        'position': EquipPart.AMULET,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'outer_attack': 212},
        'extend_attrs': {'hit': 86, 'crit': 89}
    },
    {
        'id': 10803100,
        'name': '渡劫·青龙护符',
        'quality': 8,
        'position': EquipPart.AMULET,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'outer_attack': 237},
        'extend_attrs': {'hit': 94, 'crit': 94, 'hp': 864}
    },
    {
        'id': 10803101,
        'name': '渡劫·白虎护符',
        'quality': 8,
        'position': EquipPart.AMULET,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'outer_attack': 237},
        'extend_attrs': {'hit': 94, 'crit': 94, 'hp': 864}
    },
    {
        'id': 10803102,
        'name': '渡劫·朱雀护符',
        'quality': 8,
        'position': EquipPart.AMULET,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'outer_attack': 237},
        'extend_attrs': {'hit': 94, 'crit': 94, 'hp': 864}
    },
    {
        'id': 10804000,
        'name': '渡劫头盔',
        'quality': 8,
        'position': EquipPart.HELMET,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 108, 'outer_defense': 103},
        'extend_attrs': {'inner_defense': 85, 'outer_defense': 90}
    },
    {
        'id': 10804001,
        'name': '天劫头盔',
        'quality': 8,
        'position': EquipPart.HELMET,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 110, 'outer_defense': 103},
        'extend_attrs': {'inner_defense': 89, 'outer_defense': 88}
    },
    {
        'id': 10804002,
        'name': '雷劫头盔',
        'quality': 8,
        'position': EquipPart.HELMET,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 106, 'outer_defense': 104},
        'extend_attrs': {'inner_defense': 83, 'outer_defense': 88}
    },
    {
        'id': 10804003,
        'name': '渡劫头盔·改',
        'quality': 8,
        'position': EquipPart.HELMET,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 104, 'outer_defense': 103},
        'extend_attrs': {'inner_defense': 87, 'outer_defense': 86}
    },
    {
        'id': 10804004,
        'name': '天劫头盔·真',
        'quality': 8,
        'position': EquipPart.HELMET,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 110, 'outer_defense': 103},
        'extend_attrs': {'inner_defense': 87, 'outer_defense': 89}
    },
    {
        'id': 10804005,
        'name': '雷劫头盔·灵',
        'quality': 8,
        'position': EquipPart.HELMET,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 109, 'outer_defense': 109},
        'extend_attrs': {'inner_defense': 82, 'outer_defense': 88}
    },
    {
        'id': 10804100,
        'name': '渡劫·青龙头盔',
        'quality': 8,
        'position': EquipPart.HELMET,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 118, 'outer_defense': 118},
        'extend_attrs': {'inner_defense': 94, 'outer_defense': 94, 'hp': 864}
    },
    {
        'id': 10804101,
        'name': '渡劫·白虎头盔',
        'quality': 8,
        'position': EquipPart.HELMET,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 118, 'outer_defense': 118},
        'extend_attrs': {'inner_defense': 94, 'outer_defense': 94, 'hp': 864}
    },
    {
        'id': 10804102,
        'name': '渡劫·朱雀头盔',
        'quality': 8,
        'position': EquipPart.HELMET,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 118, 'outer_defense': 118},
        'extend_attrs': {'inner_defense': 94, 'outer_defense': 94, 'hp': 864}
    },
    {
        'id': 10805000,
        'name': '渡劫甲胄',
        'quality': 8,
        'position': EquipPart.ARMOR,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 104, 'outer_defense': 110},
        'extend_attrs': {'inner_defense': 85, 'outer_defense': 86}
    },
    {
        'id': 10805001,
        'name': '天劫甲胄',
        'quality': 8,
        'position': EquipPart.ARMOR,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 109, 'outer_defense': 110},
        'extend_attrs': {'inner_defense': 86, 'outer_defense': 89}
    },
    {
        'id': 10805002,
        'name': '雷劫甲胄',
        'quality': 8,
        'position': EquipPart.ARMOR,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 102, 'outer_defense': 106},
        'extend_attrs': {'inner_defense': 89, 'outer_defense': 83}
    },
    {
        'id': 10805003,
        'name': '渡劫甲胄·改',
        'quality': 8,
        'position': EquipPart.ARMOR,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 110, 'outer_defense': 109},
        'extend_attrs': {'inner_defense': 85, 'outer_defense': 82}
    },
    {
        'id': 10805004,
        'name': '天劫甲胄·真',
        'quality': 8,
        'position': EquipPart.ARMOR,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 111, 'outer_defense': 106},
        'extend_attrs': {'inner_defense': 86, 'outer_defense': 82}
    },
    {
        'id': 10805005,
        'name': '雷劫甲胄·灵',
        'quality': 8,
        'position': EquipPart.ARMOR,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 104, 'outer_defense': 104},
        'extend_attrs': {'inner_defense': 89, 'outer_defense': 81}
    },
    {
        'id': 10805100,
        'name': '渡劫·青龙甲胄',
        'quality': 8,
        'position': EquipPart.ARMOR,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 118, 'outer_defense': 118},
        'extend_attrs': {'inner_defense': 94, 'outer_defense': 94, 'hp': 864}
    },
    {
        'id': 10805101,
        'name': '渡劫·白虎甲胄',
        'quality': 8,
        'position': EquipPart.ARMOR,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 118, 'outer_defense': 118},
        'extend_attrs': {'inner_defense': 94, 'outer_defense': 94, 'hp': 864}
    },
    {
        'id': 10805102,
        'name': '渡劫·朱雀甲胄',
        'quality': 8,
        'position': EquipPart.ARMOR,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 118, 'outer_defense': 118},
        'extend_attrs': {'inner_defense': 94, 'outer_defense': 94, 'hp': 864}
    },
    {
        'id': 10806000,
        'name': '渡劫腰带',
        'quality': 8,
        'position': EquipPart.BELT,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'dodge': 104},
        'extend_attrs': {'crit_defense': 83}
    },
    {
        'id': 10806001,
        'name': '天劫腰带',
        'quality': 8,
        'position': EquipPart.BELT,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'dodge': 102},
        'extend_attrs': {'crit_defense': 86}
    },
    {
        'id': 10806002,
        'name': '雷劫腰带',
        'quality': 8,
        'position': EquipPart.BELT,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'dodge': 103},
        'extend_attrs': {'crit_defense': 83}
    },
    {
        'id': 10806003,
        'name': '渡劫腰带·改',
        'quality': 8,
        'position': EquipPart.BELT,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'dodge': 109},
        'extend_attrs': {'crit_defense': 83}
    },
    {
        'id': 10806004,
        'name': '天劫腰带·真',
        'quality': 8,
        'position': EquipPart.BELT,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'dodge': 112},
        'extend_attrs': {'crit_defense': 81}
    },
    {
        'id': 10806005,
        'name': '雷劫腰带·灵',
        'quality': 8,
        'position': EquipPart.BELT,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'dodge': 109},
        'extend_attrs': {'crit_defense': 83}
    },
    {
        'id': 10806100,
        'name': '渡劫·青龙腰带',
        'quality': 8,
        'position': EquipPart.BELT,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'dodge': 118},
        'extend_attrs': {'crit_defense': 94, 'hp': 864}
    },
    {
        'id': 10806101,
        'name': '渡劫·白虎腰带',
        'quality': 8,
        'position': EquipPart.BELT,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'dodge': 118},
        'extend_attrs': {'crit_defense': 94, 'hp': 864}
    },
    {
        'id': 10806102,
        'name': '渡劫·朱雀腰带',
        'quality': 8,
        'position': EquipPart.BELT,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'dodge': 118},
        'extend_attrs': {'crit_defense': 94, 'hp': 864}
    },
    {
        'id': 10807000,
        'name': '渡劫护肩',
        'quality': 8,
        'position': EquipPart.SHOULDER,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'dodge': 108},
        'extend_attrs': {'crit_defense': 86}
    },
    {
        'id': 10807001,
        'name': '天劫护肩',
        'quality': 8,
        'position': EquipPart.SHOULDER,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'dodge': 107},
        'extend_attrs': {'crit_defense': 86}
    },
    {
        'id': 10807002,
        'name': '雷劫护肩',
        'quality': 8,
        'position': EquipPart.SHOULDER,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'dodge': 105},
        'extend_attrs': {'crit_defense': 87}
    },
    {
        'id': 10807003,
        'name': '渡劫护肩·改',
        'quality': 8,
        'position': EquipPart.SHOULDER,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'dodge': 111},
        'extend_attrs': {'crit_defense': 88}
    },
    {
        'id': 10807004,
        'name': '天劫护肩·真',
        'quality': 8,
        'position': EquipPart.SHOULDER,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'dodge': 103},
        'extend_attrs': {'crit_defense': 88}
    },
    {
        'id': 10807005,
        'name': '雷劫护肩·灵',
        'quality': 8,
        'position': EquipPart.SHOULDER,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'dodge': 106},
        'extend_attrs': {'crit_defense': 88}
    },
    {
        'id': 10807100,
        'name': '渡劫·青龙护肩',
        'quality': 8,
        'position': EquipPart.SHOULDER,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'dodge': 118},
        'extend_attrs': {'crit_defense': 94, 'hp': 864}
    },
    {
        'id': 10807101,
        'name': '渡劫·白虎护肩',
        'quality': 8,
        'position': EquipPart.SHOULDER,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'dodge': 118},
        'extend_attrs': {'crit_defense': 94, 'hp': 864}
    },
    {
        'id': 10807102,
        'name': '渡劫·朱雀护肩',
        'quality': 8,
        'position': EquipPart.SHOULDER,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'dodge': 118},
        'extend_attrs': {'crit_defense': 94, 'hp': 864}
    },
    {
        'id': 10808000,
        'name': '渡劫鞋履',
        'quality': 8,
        'position': EquipPart.BOOTS,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 109},
        'extend_attrs': {'dodge': 86}
    },
    {
        'id': 10808001,
        'name': '天劫鞋履',
        'quality': 8,
        'position': EquipPart.BOOTS,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 108},
        'extend_attrs': {'dodge': 82}
    },
    {
        'id': 10808002,
        'name': '雷劫鞋履',
        'quality': 8,
        'position': EquipPart.BOOTS,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 112},
        'extend_attrs': {'dodge': 82}
    },
    {
        'id': 10808003,
        'name': '渡劫鞋履·改',
        'quality': 8,
        'position': EquipPart.BOOTS,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 105},
        'extend_attrs': {'dodge': 86}
    },
    {
        'id': 10808004,
        'name': '天劫鞋履·真',
        'quality': 8,
        'position': EquipPart.BOOTS,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 102},
        'extend_attrs': {'dodge': 89}
    },
    {
        'id': 10808005,
        'name': '雷劫鞋履·灵',
        'quality': 8,
        'position': EquipPart.BOOTS,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 107},
        'extend_attrs': {'dodge': 81}
    },
    {
        'id': 10808100,
        'name': '渡劫·青龙鞋履',
        'quality': 8,
        'position': EquipPart.BOOTS,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 118},
        'extend_attrs': {'dodge': 94, 'hp': 864}
    },
    {
        'id': 10808101,
        'name': '渡劫·白虎鞋履',
        'quality': 8,
        'position': EquipPart.BOOTS,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 118},
        'extend_attrs': {'dodge': 94, 'hp': 864}
    },
    {
        'id': 10808102,
        'name': '渡劫·朱雀鞋履',
        'quality': 8,
        'position': EquipPart.BOOTS,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 118},
        'extend_attrs': {'dodge': 94, 'hp': 864}
    },
    {
        'id': 10809000,
        'name': '渡劫手套',
        'quality': 8,
        'position': EquipPart.GLOVES,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'outer_defense': 106},
        'extend_attrs': {'dodge': 84}
    },
    {
        'id': 10809001,
        'name': '天劫手套',
        'quality': 8,
        'position': EquipPart.GLOVES,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'outer_defense': 104},
        'extend_attrs': {'dodge': 84}
    },
    {
        'id': 10809002,
        'name': '雷劫手套',
        'quality': 8,
        'position': EquipPart.GLOVES,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'outer_defense': 112},
        'extend_attrs': {'dodge': 84}
    },
    {
        'id': 10809003,
        'name': '渡劫手套·改',
        'quality': 8,
        'position': EquipPart.GLOVES,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'outer_defense': 103},
        'extend_attrs': {'dodge': 85}
    },
    {
        'id': 10809004,
        'name': '天劫手套·真',
        'quality': 8,
        'position': EquipPart.GLOVES,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'outer_defense': 105},
        'extend_attrs': {'dodge': 82}
    },
    {
        'id': 10809005,
        'name': '雷劫手套·灵',
        'quality': 8,
        'position': EquipPart.GLOVES,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'outer_defense': 112},
        'extend_attrs': {'dodge': 89}
    },
    {
        'id': 10809100,
        'name': '渡劫·青龙手套',
        'quality': 8,
        'position': EquipPart.GLOVES,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'outer_defense': 118},
        'extend_attrs': {'dodge': 94, 'hp': 864}
    },
    {
        'id': 10809101,
        'name': '渡劫·白虎手套',
        'quality': 8,
        'position': EquipPart.GLOVES,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'outer_defense': 118},
        'extend_attrs': {'dodge': 94, 'hp': 864}
    },
    {
        'id': 10809102,
        'name': '渡劫·朱雀手套',
        'quality': 8,
        'position': EquipPart.GLOVES,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'outer_defense': 118},
        'extend_attrs': {'dodge': 94, 'hp': 864}
    },
    {
        'id': 10810000,
        'name': '渡劫项链',
        'quality': 8,
        'position': EquipPart.NECKLACE,
        'type': EquipmentType.HYBRID,
        'base_attrs': {'inner_attack': 218, 'outer_attack': 214},
        'extend_attrs': {'hp': 834, 'inner_defense': 82, 'outer_defense': 89}
    },
    {
        'id': 10810001,
        'name': '天劫项链',
        'quality': 8,
        'position': EquipPart.NECKLACE,
        'type': EquipmentType.HYBRID,
        'base_attrs': {'inner_attack': 213, 'outer_attack': 212},
        'extend_attrs': {'hp': 863, 'inner_defense': 85, 'outer_defense': 88}
    },
    {
        'id': 10810002,
        'name': '雷劫项链',
        'quality': 8,
        'position': EquipPart.NECKLACE,
        'type': EquipmentType.HYBRID,
        'base_attrs': {'inner_attack': 219, 'outer_attack': 211},
        'extend_attrs': {'hp': 892, 'inner_defense': 87, 'outer_defense': 87}
    },
    {
        'id': 10810003,
        'name': '渡劫项链·改',
        'quality': 8,
        'position': EquipPart.NECKLACE,
        'type': EquipmentType.HYBRID,
        'base_attrs': {'inner_attack': 214, 'outer_attack': 207},
        'extend_attrs': {'hp': 898, 'inner_defense': 81, 'outer_defense': 86}
    },
    {
        'id': 10810004,
        'name': '天劫项链·真',
        'quality': 8,
        'position': EquipPart.NECKLACE,
        'type': EquipmentType.HYBRID,
        'base_attrs': {'inner_attack': 214, 'outer_attack': 210},
        'extend_attrs': {'hp': 888, 'inner_defense': 85, 'outer_defense': 85}
    },
    {
        'id': 10810005,
        'name': '雷劫项链·灵',
        'quality': 8,
        'position': EquipPart.NECKLACE,
        'type': EquipmentType.HYBRID,
        'base_attrs': {'inner_attack': 220, 'outer_attack': 209},
        'extend_attrs': {'hp': 859, 'inner_defense': 82, 'outer_defense': 84}
    },
    {
        'id': 10810100,
        'name': '渡劫·青龙项链',
        'quality': 8,
        'position': EquipPart.NECKLACE,
        'type': EquipmentType.HYBRID,
        'base_attrs': {'inner_attack': 237, 'outer_attack': 237},
        'extend_attrs': {'hp': 1814, 'inner_defense': 94, 'outer_defense': 94}
    },
    {
        'id': 10810101,
        'name': '渡劫·白虎项链',
        'quality': 8,
        'position': EquipPart.NECKLACE,
        'type': EquipmentType.HYBRID,
        'base_attrs': {'inner_attack': 237, 'outer_attack': 237},
        'extend_attrs': {'hp': 1814, 'inner_defense': 94, 'outer_defense': 94}
    },
    {
        'id': 10810102,
        'name': '渡劫·朱雀项链',
        'quality': 8,
        'position': EquipPart.NECKLACE,
        'type': EquipmentType.HYBRID,
        'base_attrs': {'inner_attack': 237, 'outer_attack': 237},
        'extend_attrs': {'hp': 1814, 'inner_defense': 94, 'outer_defense': 94}
    },
    {
        'id': 10811000,
        'name': '渡劫法宝',
        'quality': 8,
        'position': EquipPart.ARTIFACT,
        'type': EquipmentType.HYBRID,
        'base_attrs': {'hit': 105, 'crit': 110},
        'extend_attrs': {'outer_attack': 178, 'inner_attack': 178}
    },
    {
        'id': 10811001,
        'name': '天劫法宝',
        'quality': 8,
        'position': EquipPart.ARTIFACT,
        'type': EquipmentType.HYBRID,
        'base_attrs': {'hit': 111, 'crit': 109},
        'extend_attrs': {'outer_attack': 171, 'inner_attack': 168}
    },
    {
        'id': 10811002,
        'name': '雷劫法宝',
        'quality': 8,
        'position': EquipPart.ARTIFACT,
        'type': EquipmentType.HYBRID,
        'base_attrs': {'hit': 107, 'crit': 108},
        'extend_attrs': {'outer_attack': 175, 'inner_attack': 169}
    },
    {
        'id': 10811003,
        'name': '渡劫法宝·改',
        'quality': 8,
        'position': EquipPart.ARTIFACT,
        'type': EquipmentType.HYBRID,
        'base_attrs': {'hit': 112, 'crit': 109},
        'extend_attrs': {'outer_attack': 172, 'inner_attack': 168}
    },
    {
        'id': 10811004,
        'name': '天劫法宝·真',
        'quality': 8,
        'position': EquipPart.ARTIFACT,
        'type': EquipmentType.HYBRID,
        'base_attrs': {'hit': 110, 'crit': 109},
        'extend_attrs': {'outer_attack': 171, 'inner_attack': 175}
    },
    {
        'id': 10811005,
        'name': '雷劫法宝·灵',
        'quality': 8,
        'position': EquipPart.ARTIFACT,
        'type': EquipmentType.HYBRID,
        'base_attrs': {'hit': 102, 'crit': 105},
        'extend_attrs': {'outer_attack': 174, 'inner_attack': 164}
    },
    {
        'id': 10811100,
        'name': '渡劫·青龙法宝',
        'quality': 8,
        'position': EquipPart.ARTIFACT,
        'type': EquipmentType.HYBRID,
        'base_attrs': {'hit': 118, 'crit': 118},
        'extend_attrs': {'outer_attack': 189, 'inner_attack': 189, 'hp': 864}
    },
    {
        'id': 10811101,
        'name': '渡劫·白虎法宝',
        'quality': 8,
        'position': EquipPart.ARTIFACT,
        'type': EquipmentType.HYBRID,
        'base_attrs': {'hit': 118, 'crit': 118},
        'extend_attrs': {'outer_attack': 189, 'inner_attack': 189, 'hp': 864}
    },
    {
        'id': 10811102,
        'name': '渡劫·朱雀法宝',
        'quality': 8,
        'position': EquipPart.ARTIFACT,
        'type': EquipmentType.HYBRID,
        'base_attrs': {'hit': 118, 'crit': 118},
        'extend_attrs': {'outer_attack': 189, 'inner_attack': 189, 'hp': 864}
    },
    {
        'id': 10900000,
        'name': '金仙剑',
        'quality': 9,
        'position': EquipPart.WEAPON,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'inner_attack': 240, 'outer_attack': 246},
        'extend_attrs': {'hp': 975, 'hit': 94, 'crit': 92}
    },
    {
        'id': 10900001,
        'name': '真仙刀',
        'quality': 9,
        'position': EquipPart.WEAPON,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'inner_attack': 249, 'outer_attack': 240},
        'extend_attrs': {'hp': 1002, 'hit': 99, 'crit': 97}
    },
    {
        'id': 10900002,
        'name': '天仙弓',
        'quality': 9,
        'position': EquipPart.WEAPON,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'inner_attack': 236, 'outer_attack': 235},
        'extend_attrs': {'hp': 997, 'hit': 98, 'crit': 98}
    },
    {
        'id': 10900003,
        'name': '金仙弩',
        'quality': 9,
        'position': EquipPart.WEAPON,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'inner_attack': 232, 'outer_attack': 239},
        'extend_attrs': {'hp': 982, 'hit': 96, 'crit': 92}
    },
    {
        'id': 10900004,
        'name': '真仙枪',
        'quality': 9,
        'position': EquipPart.WEAPON,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'inner_attack': 242, 'outer_attack': 233},
        'extend_attrs': {'hp': 913, 'hit': 94, 'crit': 98}
    },
    {
        'id': 10900005,
        'name': '天仙棍',
        'quality': 9,
        'position': EquipPart.WEAPON,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'inner_attack': 240, 'outer_attack': 241},
        'extend_attrs': {'hp': 1000, 'hit': 93, 'crit': 99}
    },
    {
        'id': 10900100,
        'name': '金仙·青龙剑',
        'quality': 9,
        'position': EquipPart.WEAPON,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'inner_attack': 264, 'outer_attack': 264},
        'extend_attrs': {'hp': 2016, 'hit': 105, 'crit': 105}
    },
    {
        'id': 10900101,
        'name': '金仙·白虎刀',
        'quality': 9,
        'position': EquipPart.WEAPON,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'inner_attack': 264, 'outer_attack': 264},
        'extend_attrs': {'hp': 2016, 'hit': 105, 'crit': 105}
    },
    {
        'id': 10900102,
        'name': '金仙·朱雀弓',
        'quality': 9,
        'position': EquipPart.WEAPON,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'inner_attack': 264, 'outer_attack': 264},
        'extend_attrs': {'hp': 2016, 'hit': 105, 'crit': 105}
    },
    {
        'id': 10901000,
        'name': '金仙护腕',
        'quality': 9,
        'position': EquipPart.BRACER,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'hit': 116},
        'extend_attrs': {'outer_attack': 197, 'inner_attack': 187}
    },
    {
        'id': 10901001,
        'name': '真仙护腕',
        'quality': 9,
        'position': EquipPart.BRACER,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'hit': 124},
        'extend_attrs': {'outer_attack': 195, 'inner_attack': 190}
    },
    {
        'id': 10901002,
        'name': '天仙护腕',
        'quality': 9,
        'position': EquipPart.BRACER,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'hit': 125},
        'extend_attrs': {'outer_attack': 188, 'inner_attack': 183}
    },
    {
        'id': 10901003,
        'name': '金仙护腕·改',
        'quality': 9,
        'position': EquipPart.BRACER,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'hit': 117},
        'extend_attrs': {'outer_attack': 200, 'inner_attack': 182}
    },
    {
        'id': 10901004,
        'name': '真仙护腕·真',
        'quality': 9,
        'position': EquipPart.BRACER,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'hit': 114},
        'extend_attrs': {'outer_attack': 194, 'inner_attack': 194}
    },
    {
        'id': 10901005,
        'name': '天仙护腕·灵',
        'quality': 9,
        'position': EquipPart.BRACER,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'hit': 120},
        'extend_attrs': {'outer_attack': 193, 'inner_attack': 190}
    },
    {
        'id': 10901100,
        'name': '金仙·青龙护腕',
        'quality': 9,
        'position': EquipPart.BRACER,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'hit': 132},
        'extend_attrs': {'outer_attack': 211, 'inner_attack': 211, 'hp': 960}
    },
    {
        'id': 10901101,
        'name': '金仙·白虎护腕',
        'quality': 9,
        'position': EquipPart.BRACER,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'hit': 132},
        'extend_attrs': {'outer_attack': 211, 'inner_attack': 211, 'hp': 960}
    },
    {
        'id': 10901102,
        'name': '金仙·朱雀护腕',
        'quality': 9,
        'position': EquipPart.BRACER,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'hit': 132},
        'extend_attrs': {'outer_attack': 211, 'inner_attack': 211, 'hp': 960}
    },
    {
        'id': 10902000,
        'name': '金仙戒指',
        'quality': 9,
        'position': EquipPart.RING,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'inner_attack': 232},
        'extend_attrs': {'hit': 98, 'crit': 94}
    },
    {
        'id': 10902001,
        'name': '真仙戒指',
        'quality': 9,
        'position': EquipPart.RING,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'inner_attack': 231},
        'extend_attrs': {'hit': 99, 'crit': 94}
    },
    {
        'id': 10902002,
        'name': '天仙戒指',
        'quality': 9,
        'position': EquipPart.RING,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'inner_attack': 249},
        'extend_attrs': {'hit': 97, 'crit': 93}
    },
    {
        'id': 10902003,
        'name': '金仙戒指·改',
        'quality': 9,
        'position': EquipPart.RING,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'inner_attack': 238},
        'extend_attrs': {'hit': 91, 'crit': 98}
    },
    {
        'id': 10902004,
        'name': '真仙戒指·真',
        'quality': 9,
        'position': EquipPart.RING,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'inner_attack': 241},
        'extend_attrs': {'hit': 93, 'crit': 95}
    },
    {
        'id': 10902005,
        'name': '天仙戒指·灵',
        'quality': 9,
        'position': EquipPart.RING,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'inner_attack': 244},
        'extend_attrs': {'hit': 99, 'crit': 97}
    },
    {
        'id': 10902100,
        'name': '金仙·青龙戒指',
        'quality': 9,
        'position': EquipPart.RING,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'inner_attack': 264},
        'extend_attrs': {'hit': 105, 'crit': 105, 'hp': 960}
    },
    {
        'id': 10902101,
        'name': '金仙·白虎戒指',
        'quality': 9,
        'position': EquipPart.RING,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'inner_attack': 264},
        'extend_attrs': {'hit': 105, 'crit': 105, 'hp': 960}
    },
    {
        'id': 10902102,
        'name': '金仙·朱雀戒指',
        'quality': 9,
        'position': EquipPart.RING,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'inner_attack': 264},
        'extend_attrs': {'hit': 105, 'crit': 105, 'hp': 960}
    },
    {
        'id': 10903000,
        'name': '金仙护符',
        'quality': 9,
        'position': EquipPart.AMULET,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'outer_attack': 240},
        'extend_attrs': {'hit': 92, 'crit': 93}
    },
    {
        'id': 10903001,
        'name': '真仙护符',
        'quality': 9,
        'position': EquipPart.AMULET,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'outer_attack': 248},
        'extend_attrs': {'hit': 96, 'crit': 92}
    },
    {
        'id': 10903002,
        'name': '天仙护符',
        'quality': 9,
        'position': EquipPart.AMULET,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'outer_attack': 250},
        'extend_attrs': {'hit': 99, 'crit': 93}
    },
    {
        'id': 10903003,
        'name': '金仙护符·改',
        'quality': 9,
        'position': EquipPart.AMULET,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'outer_attack': 245},
        'extend_attrs': {'hit': 91, 'crit': 99}
    },
    {
        'id': 10903004,
        'name': '真仙护符·真',
        'quality': 9,
        'position': EquipPart.AMULET,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'outer_attack': 233},
        'extend_attrs': {'hit': 91, 'crit': 98}
    },
    {
        'id': 10903005,
        'name': '天仙护符·灵',
        'quality': 9,
        'position': EquipPart.AMULET,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'outer_attack': 242},
        'extend_attrs': {'hit': 95, 'crit': 92}
    },
    {
        'id': 10903100,
        'name': '金仙·青龙护符',
        'quality': 9,
        'position': EquipPart.AMULET,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'outer_attack': 264},
        'extend_attrs': {'hit': 105, 'crit': 105, 'hp': 960}
    },
    {
        'id': 10903101,
        'name': '金仙·白虎护符',
        'quality': 9,
        'position': EquipPart.AMULET,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'outer_attack': 264},
        'extend_attrs': {'hit': 105, 'crit': 105, 'hp': 960}
    },
    {
        'id': 10903102,
        'name': '金仙·朱雀护符',
        'quality': 9,
        'position': EquipPart.AMULET,
        'type': EquipmentType.OFFENSIVE,
        'base_attrs': {'outer_attack': 264},
        'extend_attrs': {'hit': 105, 'crit': 105, 'hp': 960}
    },
    {
        'id': 10904000,
        'name': '金仙头盔',
        'quality': 9,
        'position': EquipPart.HELMET,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 122, 'outer_defense': 120},
        'extend_attrs': {'inner_defense': 92, 'outer_defense': 100}
    },
    {
        'id': 10904001,
        'name': '真仙头盔',
        'quality': 9,
        'position': EquipPart.HELMET,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 118, 'outer_defense': 117},
        'extend_attrs': {'inner_defense': 94, 'outer_defense': 99}
    },
    {
        'id': 10904002,
        'name': '天仙头盔',
        'quality': 9,
        'position': EquipPart.HELMET,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 117, 'outer_defense': 122},
        'extend_attrs': {'inner_defense': 97, 'outer_defense': 96}
    },
    {
        'id': 10904003,
        'name': '金仙头盔·改',
        'quality': 9,
        'position': EquipPart.HELMET,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 124, 'outer_defense': 124},
        'extend_attrs': {'inner_defense': 94, 'outer_defense': 95}
    },
    {
        'id': 10904004,
        'name': '真仙头盔·真',
        'quality': 9,
        'position': EquipPart.HELMET,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 119, 'outer_defense': 124},
        'extend_attrs': {'inner_defense': 95, 'outer_defense': 98}
    },
    {
        'id': 10904005,
        'name': '天仙头盔·灵',
        'quality': 9,
        'position': EquipPart.HELMET,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 125, 'outer_defense': 125},
        'extend_attrs': {'inner_defense': 94, 'outer_defense': 98}
    },
    {
        'id': 10904100,
        'name': '金仙·青龙头盔',
        'quality': 9,
        'position': EquipPart.HELMET,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 132, 'outer_defense': 132},
        'extend_attrs': {'inner_defense': 105, 'outer_defense': 105, 'hp': 960}
    },
    {
        'id': 10904101,
        'name': '金仙·白虎头盔',
        'quality': 9,
        'position': EquipPart.HELMET,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 132, 'outer_defense': 132},
        'extend_attrs': {'inner_defense': 105, 'outer_defense': 105, 'hp': 960}
    },
    {
        'id': 10904102,
        'name': '金仙·朱雀头盔',
        'quality': 9,
        'position': EquipPart.HELMET,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 132, 'outer_defense': 132},
        'extend_attrs': {'inner_defense': 105, 'outer_defense': 105, 'hp': 960}
    },
    {
        'id': 10905000,
        'name': '金仙甲胄',
        'quality': 9,
        'position': EquipPart.ARMOR,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 119, 'outer_defense': 121},
        'extend_attrs': {'inner_defense': 100, 'outer_defense': 93}
    },
    {
        'id': 10905001,
        'name': '真仙甲胄',
        'quality': 9,
        'position': EquipPart.ARMOR,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 115, 'outer_defense': 120},
        'extend_attrs': {'inner_defense': 93, 'outer_defense': 97}
    },
    {
        'id': 10905002,
        'name': '天仙甲胄',
        'quality': 9,
        'position': EquipPart.ARMOR,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 114, 'outer_defense': 120},
        'extend_attrs': {'inner_defense': 96, 'outer_defense': 95}
    },
    {
        'id': 10905003,
        'name': '金仙甲胄·改',
        'quality': 9,
        'position': EquipPart.ARMOR,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 123, 'outer_defense': 119},
        'extend_attrs': {'inner_defense': 93, 'outer_defense': 97}
    },
    {
        'id': 10905004,
        'name': '真仙甲胄·真',
        'quality': 9,
        'position': EquipPart.ARMOR,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 124, 'outer_defense': 116},
        'extend_attrs': {'inner_defense': 95, 'outer_defense': 92}
    },
    {
        'id': 10905005,
        'name': '天仙甲胄·灵',
        'quality': 9,
        'position': EquipPart.ARMOR,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 119, 'outer_defense': 124},
        'extend_attrs': {'inner_defense': 94, 'outer_defense': 92}
    },
    {
        'id': 10905100,
        'name': '金仙·青龙甲胄',
        'quality': 9,
        'position': EquipPart.ARMOR,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 132, 'outer_defense': 132},
        'extend_attrs': {'inner_defense': 105, 'outer_defense': 105, 'hp': 960}
    },
    {
        'id': 10905101,
        'name': '金仙·白虎甲胄',
        'quality': 9,
        'position': EquipPart.ARMOR,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 132, 'outer_defense': 132},
        'extend_attrs': {'inner_defense': 105, 'outer_defense': 105, 'hp': 960}
    },
    {
        'id': 10905102,
        'name': '金仙·朱雀甲胄',
        'quality': 9,
        'position': EquipPart.ARMOR,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 132, 'outer_defense': 132},
        'extend_attrs': {'inner_defense': 105, 'outer_defense': 105, 'hp': 960}
    },
    {
        'id': 10906000,
        'name': '金仙腰带',
        'quality': 9,
        'position': EquipPart.BELT,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'dodge': 122},
        'extend_attrs': {'crit_defense': 92}
    },
    {
        'id': 10906001,
        'name': '真仙腰带',
        'quality': 9,
        'position': EquipPart.BELT,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'dodge': 124},
        'extend_attrs': {'crit_defense': 97}
    },
    {
        'id': 10906002,
        'name': '天仙腰带',
        'quality': 9,
        'position': EquipPart.BELT,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'dodge': 125},
        'extend_attrs': {'crit_defense': 98}
    },
    {
        'id': 10906003,
        'name': '金仙腰带·改',
        'quality': 9,
        'position': EquipPart.BELT,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'dodge': 114},
        'extend_attrs': {'crit_defense': 91}
    },
    {
        'id': 10906004,
        'name': '真仙腰带·真',
        'quality': 9,
        'position': EquipPart.BELT,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'dodge': 120},
        'extend_attrs': {'crit_defense': 93}
    },
    {
        'id': 10906005,
        'name': '天仙腰带·灵',
        'quality': 9,
        'position': EquipPart.BELT,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'dodge': 124},
        'extend_attrs': {'crit_defense': 98}
    },
    {
        'id': 10906100,
        'name': '金仙·青龙腰带',
        'quality': 9,
        'position': EquipPart.BELT,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'dodge': 132},
        'extend_attrs': {'crit_defense': 105, 'hp': 960}
    },
    {
        'id': 10906101,
        'name': '金仙·白虎腰带',
        'quality': 9,
        'position': EquipPart.BELT,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'dodge': 132},
        'extend_attrs': {'crit_defense': 105, 'hp': 960}
    },
    {
        'id': 10906102,
        'name': '金仙·朱雀腰带',
        'quality': 9,
        'position': EquipPart.BELT,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'dodge': 132},
        'extend_attrs': {'crit_defense': 105, 'hp': 960}
    },
    {
        'id': 10907000,
        'name': '金仙护肩',
        'quality': 9,
        'position': EquipPart.SHOULDER,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'dodge': 115},
        'extend_attrs': {'crit_defense': 99}
    },
    {
        'id': 10907001,
        'name': '真仙护肩',
        'quality': 9,
        'position': EquipPart.SHOULDER,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'dodge': 115},
        'extend_attrs': {'crit_defense': 92}
    },
    {
        'id': 10907002,
        'name': '天仙护肩',
        'quality': 9,
        'position': EquipPart.SHOULDER,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'dodge': 121},
        'extend_attrs': {'crit_defense': 99}
    },
    {
        'id': 10907003,
        'name': '金仙护肩·改',
        'quality': 9,
        'position': EquipPart.SHOULDER,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'dodge': 120},
        'extend_attrs': {'crit_defense': 98}
    },
    {
        'id': 10907004,
        'name': '真仙护肩·真',
        'quality': 9,
        'position': EquipPart.SHOULDER,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'dodge': 116},
        'extend_attrs': {'crit_defense': 100}
    },
    {
        'id': 10907005,
        'name': '天仙护肩·灵',
        'quality': 9,
        'position': EquipPart.SHOULDER,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'dodge': 114},
        'extend_attrs': {'crit_defense': 99}
    },
    {
        'id': 10907100,
        'name': '金仙·青龙护肩',
        'quality': 9,
        'position': EquipPart.SHOULDER,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'dodge': 132},
        'extend_attrs': {'crit_defense': 105, 'hp': 960}
    },
    {
        'id': 10907101,
        'name': '金仙·白虎护肩',
        'quality': 9,
        'position': EquipPart.SHOULDER,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'dodge': 132},
        'extend_attrs': {'crit_defense': 105, 'hp': 960}
    },
    {
        'id': 10907102,
        'name': '金仙·朱雀护肩',
        'quality': 9,
        'position': EquipPart.SHOULDER,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'dodge': 132},
        'extend_attrs': {'crit_defense': 105, 'hp': 960}
    },
    {
        'id': 10908000,
        'name': '金仙鞋履',
        'quality': 9,
        'position': EquipPart.BOOTS,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 115},
        'extend_attrs': {'dodge': 94}
    },
    {
        'id': 10908001,
        'name': '真仙鞋履',
        'quality': 9,
        'position': EquipPart.BOOTS,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 125},
        'extend_attrs': {'dodge': 93}
    },
    {
        'id': 10908002,
        'name': '天仙鞋履',
        'quality': 9,
        'position': EquipPart.BOOTS,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 122},
        'extend_attrs': {'dodge': 97}
    },
    {
        'id': 10908003,
        'name': '金仙鞋履·改',
        'quality': 9,
        'position': EquipPart.BOOTS,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 119},
        'extend_attrs': {'dodge': 100}
    },
    {
        'id': 10908004,
        'name': '真仙鞋履·真',
        'quality': 9,
        'position': EquipPart.BOOTS,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 115},
        'extend_attrs': {'dodge': 96}
    },
    {
        'id': 10908005,
        'name': '天仙鞋履·灵',
        'quality': 9,
        'position': EquipPart.BOOTS,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 122},
        'extend_attrs': {'dodge': 98}
    },
    {
        'id': 10908100,
        'name': '金仙·青龙鞋履',
        'quality': 9,
        'position': EquipPart.BOOTS,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 132},
        'extend_attrs': {'dodge': 105, 'hp': 960}
    },
    {
        'id': 10908101,
        'name': '金仙·白虎鞋履',
        'quality': 9,
        'position': EquipPart.BOOTS,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 132},
        'extend_attrs': {'dodge': 105, 'hp': 960}
    },
    {
        'id': 10908102,
        'name': '金仙·朱雀鞋履',
        'quality': 9,
        'position': EquipPart.BOOTS,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'inner_defense': 132},
        'extend_attrs': {'dodge': 105, 'hp': 960}
    },
    {
        'id': 10909000,
        'name': '金仙手套',
        'quality': 9,
        'position': EquipPart.GLOVES,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'outer_defense': 123},
        'extend_attrs': {'dodge': 99}
    },
    {
        'id': 10909001,
        'name': '真仙手套',
        'quality': 9,
        'position': EquipPart.GLOVES,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'outer_defense': 122},
        'extend_attrs': {'dodge': 97}
    },
    {
        'id': 10909002,
        'name': '天仙手套',
        'quality': 9,
        'position': EquipPart.GLOVES,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'outer_defense': 116},
        'extend_attrs': {'dodge': 91}
    },
    {
        'id': 10909003,
        'name': '金仙手套·改',
        'quality': 9,
        'position': EquipPart.GLOVES,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'outer_defense': 120},
        'extend_attrs': {'dodge': 92}
    },
    {
        'id': 10909004,
        'name': '真仙手套·真',
        'quality': 9,
        'position': EquipPart.GLOVES,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'outer_defense': 122},
        'extend_attrs': {'dodge': 91}
    },
    {
        'id': 10909005,
        'name': '天仙手套·灵',
        'quality': 9,
        'position': EquipPart.GLOVES,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'outer_defense': 114},
        'extend_attrs': {'dodge': 97}
    },
    {
        'id': 10909100,
        'name': '金仙·青龙手套',
        'quality': 9,
        'position': EquipPart.GLOVES,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'outer_defense': 132},
        'extend_attrs': {'dodge': 105, 'hp': 960}
    },
    {
        'id': 10909101,
        'name': '金仙·白虎手套',
        'quality': 9,
        'position': EquipPart.GLOVES,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'outer_defense': 132},
        'extend_attrs': {'dodge': 105, 'hp': 960}
    },
    {
        'id': 10909102,
        'name': '金仙·朱雀手套',
        'quality': 9,
        'position': EquipPart.GLOVES,
        'type': EquipmentType.DEFENSIVE,
        'base_attrs': {'outer_defense': 132},
        'extend_attrs': {'dodge': 105, 'hp': 960}
    },
    {
        'id': 10910000,
        'name': '金仙项链',
        'quality': 9,
        'position': EquipPart.NECKLACE,
        'type': EquipmentType.HYBRID,
        'base_attrs': {'inner_attack': 248, 'outer_attack': 251},
        'extend_attrs': {'hp': 1001, 'inner_defense': 98, 'outer_defense': 96}
    },
    {
        'id': 10910001,
        'name': '真仙项链',
        'quality': 9,
        'position': EquipPart.NECKLACE,
        'type': EquipmentType.HYBRID,
        'base_attrs': {'inner_attack': 246, 'outer_attack': 239},
        'extend_attrs': {'hp': 937, 'inner_defense': 91, 'outer_defense': 100}
    },
    {
        'id': 10910002,
        'name': '天仙项链',
        'quality': 9,
        'position': EquipPart.NECKLACE,
        'type': EquipmentType.HYBRID,
        'base_attrs': {'inner_attack': 246, 'outer_attack': 233},
        'extend_attrs': {'hp': 925, 'inner_defense': 98, 'outer_defense': 97}
    },
    {
        'id': 10910003,
        'name': '金仙项链·改',
        'quality': 9,
        'position': EquipPart.NECKLACE,
        'type': EquipmentType.HYBRID,
        'base_attrs': {'inner_attack': 240, 'outer_attack': 239},
        'extend_attrs': {'hp': 965, 'inner_defense': 92, 'outer_defense': 93}
    },
    {
        'id': 10910004,
        'name': '真仙项链·真',
        'quality': 9,
        'position': EquipPart.NECKLACE,
        'type': EquipmentType.HYBRID,
        'base_attrs': {'inner_attack': 236, 'outer_attack': 242},
        'extend_attrs': {'hp': 984, 'inner_defense': 92, 'outer_defense': 99}
    },
    {
        'id': 10910005,
        'name': '天仙项链·灵',
        'quality': 9,
        'position': EquipPart.NECKLACE,
        'type': EquipmentType.HYBRID,
        'base_attrs': {'inner_attack': 232, 'outer_attack': 236},
        'extend_attrs': {'hp': 962, 'inner_defense': 98, 'outer_defense': 93}
    },
    {
        'id': 10910100,
        'name': '金仙·青龙项链',
        'quality': 9,
        'position': EquipPart.NECKLACE,
        'type': EquipmentType.HYBRID,
        'base_attrs': {'inner_attack': 264, 'outer_attack': 264},
        'extend_attrs': {'hp': 2016, 'inner_defense': 105, 'outer_defense': 105}
    },
    {
        'id': 10910101,
        'name': '金仙·白虎项链',
        'quality': 9,
        'position': EquipPart.NECKLACE,
        'type': EquipmentType.HYBRID,
        'base_attrs': {'inner_attack': 264, 'outer_attack': 264},
        'extend_attrs': {'hp': 2016, 'inner_defense': 105, 'outer_defense': 105}
    },
    {
        'id': 10910102,
        'name': '金仙·朱雀项链',
        'quality': 9,
        'position': EquipPart.NECKLACE,
        'type': EquipmentType.HYBRID,
        'base_attrs': {'inner_attack': 264, 'outer_attack': 264},
        'extend_attrs': {'hp': 2016, 'inner_defense': 105, 'outer_defense': 105}
    },
    {
        'id': 10911000,
        'name': '金仙法宝',
        'quality': 9,
        'position': EquipPart.ARTIFACT,
        'type': EquipmentType.HYBRID,
        'base_attrs': {'hit': 115, 'crit': 122},
        'extend_attrs': {'outer_attack': 185, 'inner_attack': 198}
    },
    {
        'id': 10911001,
        'name': '真仙法宝',
        'quality': 9,
        'position': EquipPart.ARTIFACT,
        'type': EquipmentType.HYBRID,
        'base_attrs': {'hit': 124, 'crit': 114},
        'extend_attrs': {'outer_attack': 192, 'inner_attack': 196}
    },
    {
        'id': 10911002,
        'name': '天仙法宝',
        'quality': 9,
        'position': EquipPart.ARTIFACT,
        'type': EquipmentType.HYBRID,
        'base_attrs': {'hit': 123, 'crit': 119},
        'extend_attrs': {'outer_attack': 185, 'inner_attack': 195}
    },
    {
        'id': 10911003,
        'name': '金仙法宝·改',
        'quality': 9,
        'position': EquipPart.ARTIFACT,
        'type': EquipmentType.HYBRID,
        'base_attrs': {'hit': 117, 'crit': 123},
        'extend_attrs': {'outer_attack': 191, 'inner_attack': 185}
    },
    {
        'id': 10911004,
        'name': '真仙法宝·真',
        'quality': 9,
        'position': EquipPart.ARTIFACT,
        'type': EquipmentType.HYBRID,
        'base_attrs': {'hit': 116, 'crit': 125},
        'extend_attrs': {'outer_attack': 186, 'inner_attack': 197}
    },
    {
        'id': 10911005,
        'name': '天仙法宝·灵',
        'quality': 9,
        'position': EquipPart.ARTIFACT,
        'type': EquipmentType.HYBRID,
        'base_attrs': {'hit': 117, 'crit': 114},
        'extend_attrs': {'outer_attack': 183, 'inner_attack': 196}
    },
    {
        'id': 10911100,
        'name': '金仙·青龙法宝',
        'quality': 9,
        'position': EquipPart.ARTIFACT,
        'type': EquipmentType.HYBRID,
        'base_attrs': {'hit': 132, 'crit': 132},
        'extend_attrs': {'outer_attack': 211, 'inner_attack': 211, 'hp': 960}
    },
    {
        'id': 10911101,
        'name': '金仙·白虎法宝',
        'quality': 9,
        'position': EquipPart.ARTIFACT,
        'type': EquipmentType.HYBRID,
        'base_attrs': {'hit': 132, 'crit': 132},
        'extend_attrs': {'outer_attack': 211, 'inner_attack': 211, 'hp': 960}
    },
    {
        'id': 10911102,
        'name': '金仙·朱雀法宝',
        'quality': 9,
        'position': EquipPart.ARTIFACT,
        'type': EquipmentType.HYBRID,
        'base_attrs': {'hit': 132, 'crit': 132},
        'extend_attrs': {'outer_attack': 211, 'inner_attack': 211, 'hp': 960}
    },
]