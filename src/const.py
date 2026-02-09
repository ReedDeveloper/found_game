from enum import Enum

class EquipmentType(Enum):
    OFFENSIVE = 0   # 攻击类
    DEFENSIVE = 1   # 防御类
    HYBRID = 2      # 攻防兼备类

class EquipPart(Enum):
    WEAPON = 0      # 武器
    BRACER = 1      # 护腕
    RING = 2        # 戒指
    AMULET = 3      # 护符
    HELMET = 4      # 头盔
    ARMOR = 5       # 甲胄
    BELT = 6        # 腰带
    SHOULDER = 7    # 护肩
    BOOTS = 8       # 鞋履
    GLOVES = 9      # 手套
    NECKLACE = 10   # 项链
    ARTIFACT = 11   # 法宝

    @classmethod
    def get_name(cls, part):
        names = {
            cls.WEAPON: "武器",
            cls.BRACER: "护腕",
            cls.RING: "戒指",
            cls.AMULET: "护符",
            cls.HELMET: "头盔",
            cls.ARMOR: "甲胄",
            cls.BELT: "腰带",
            cls.SHOULDER: "护肩",
            cls.BOOTS: "鞋履",
            cls.GLOVES: "手套",
            cls.NECKLACE: "项链",
            cls.ARTIFACT: "法宝"
        }
        return names.get(part, "未知")

class WeaponType(Enum):
    SWORD = 0   # 剑
    BLADE = 1   # 刀
    BOW = 2     # 弓
    CROSSBOW = 3 # 弩
    SPEAR = 4   # 枪
    STAFF = 5   # 棍
    HALBERD = 6 # 戟

    @classmethod
    def get_name(cls, w_type):
        names = {
            cls.SWORD: "剑",
            cls.BLADE: "刀",
            cls.BOW: "弓",
            cls.CROSSBOW: "弩",
            cls.SPEAR: "枪",
            cls.STAFF: "棍",
            cls.HALBERD: "戟"
        }
        return names.get(w_type, "")

# 装备部位类型映射
EQUIP_TYPE_MAP = {
    EquipPart.WEAPON: EquipmentType.OFFENSIVE,
    EquipPart.BRACER: EquipmentType.OFFENSIVE,
    EquipPart.RING: EquipmentType.OFFENSIVE,
    EquipPart.AMULET: EquipmentType.OFFENSIVE,
    EquipPart.HELMET: EquipmentType.DEFENSIVE,
    EquipPart.ARMOR: EquipmentType.DEFENSIVE,
    EquipPart.BELT: EquipmentType.DEFENSIVE,
    EquipPart.SHOULDER: EquipmentType.DEFENSIVE,
    EquipPart.BOOTS: EquipmentType.DEFENSIVE,
    EquipPart.GLOVES: EquipmentType.DEFENSIVE,
    EquipPart.NECKLACE: EquipmentType.HYBRID,
    EquipPart.ARTIFACT: EquipmentType.HYBRID
}

class AttributeType(Enum):
    OUTER_ATK = "外功攻击"
    INNER_ATK = "内功攻击"
    HIT = "命中"
    CRIT = "暴击"
    OUTER_DEF = "外功防御"
    INNER_DEF = "内功防御"
    DODGE = "闪避"
    CRIT_DEF = "暴防"
    MAX_HP = "血上限"

    @property
    def key(self):
        """返回属性对应的英文Key"""
        keys = {
            "外功攻击": "outer_attack",
            "内功攻击": "inner_attack",
            "命中": "hit",
            "暴击": "crit",
            "外功防御": "outer_defense",
            "内功防御": "inner_defense",
            "闪避": "dodge",
            "暴防": "crit_defense",
            "血上限": "hp"
        }
        return keys.get(self.value, "unknown")

class Rank(Enum):
    LIAN_QI = 0     # 炼气
    ZHU_JI = 1      # 筑基
    JIE_DAN = 2     # 结丹
    YUAN_YING = 3   # 元婴
    HUA_SHEN = 4    # 化神
    LIAN_XU = 5     # 炼虚
    HE_TI = 6       # 合体
    DA_CHENG = 7    # 大乘
    DU_JIE = 8      # 渡劫
    JIN_XIAN = 9    # 金仙

    @classmethod
    def get_name(cls, rank):
        names = [
            "炼气", "筑基", "结丹", "元婴", "化神",
            "炼虚", "合体", "大乘", "渡劫", "金仙"
        ]
        if 0 <= rank.value < len(names):
            return names[rank.value]
        return ""
    
    @classmethod
    def get_prefix(cls, rank):
        # 丰富的前缀命名，用于增加装备多样性
        prefixes = [
            ["炼气", "聚气", "纳灵"],         # 0
            ["筑基", "固本", "培元"],         # 1
            ["结丹", "金丹", "开光"],         # 2
            ["元婴", "化灵", "凝神"],         # 3
            ["化神", "分神", "元神"],         # 4
            ["炼虚", "虚灵", "破虚"],         # 5
            ["合体", "融合", "归一"],         # 6
            ["大乘", "圆满", "通天"],         # 7
            ["渡劫", "天劫", "雷劫"],         # 8
            ["金仙", "真仙", "天仙"]          # 9
        ]
        if 0 <= rank.value < len(prefixes):
            return prefixes[rank.value]
        return ["未知"]

class QualityColor:
    GRAY = (180, 180, 180)
    BLUE = (59, 133, 197)
    PURPLE = (121, 69, 146)
    RED = (197, 71, 56)
    DARK_RED = (89, 37, 38)
    WU_JIN = (130, 121, 91)
    DARK_BLUE = (35, 78, 152)
    PINK = (217, 183, 198)
    ORANGE = (234, 136, 60)
    GOLD = (238, 219, 145)

    @classmethod
    def get_color_by_rank(cls, rank_val):
        colors = [
            cls.GRAY, cls.BLUE, cls.PURPLE, cls.RED, cls.DARK_RED,
            cls.WU_JIN, cls.DARK_BLUE, cls.PINK, cls.ORANGE, cls.GOLD
        ]
        if 0 <= rank_val < len(colors):
            return colors[rank_val]
        return cls.GRAY

# 基础属性配置
BASE_STATS_CONFIG = {
    EquipPart.WEAPON: [AttributeType.INNER_ATK, AttributeType.OUTER_ATK],
    EquipPart.BRACER: [AttributeType.HIT],
    EquipPart.RING: [AttributeType.INNER_ATK],
    EquipPart.AMULET: [AttributeType.OUTER_ATK],
    EquipPart.HELMET: [AttributeType.INNER_DEF, AttributeType.OUTER_DEF],
    EquipPart.ARMOR: [AttributeType.INNER_DEF, AttributeType.OUTER_DEF],
    EquipPart.BELT: [AttributeType.DODGE],
    EquipPart.SHOULDER: [AttributeType.DODGE],
    EquipPart.BOOTS: [AttributeType.INNER_DEF],
    EquipPart.GLOVES: [AttributeType.OUTER_DEF],
    EquipPart.NECKLACE: [AttributeType.INNER_ATK, AttributeType.OUTER_ATK],
    EquipPart.ARTIFACT: [AttributeType.HIT, AttributeType.CRIT]
}

# 扩展属性配置
EXT_STATS_CONFIG = {
    EquipPart.WEAPON: [AttributeType.MAX_HP, AttributeType.HIT, AttributeType.CRIT],
    EquipPart.BRACER: [AttributeType.OUTER_ATK, AttributeType.INNER_ATK],
    EquipPart.RING: [AttributeType.HIT, AttributeType.CRIT],
    EquipPart.AMULET: [AttributeType.HIT, AttributeType.CRIT],
    EquipPart.HELMET: [AttributeType.INNER_DEF, AttributeType.OUTER_DEF],
    EquipPart.ARMOR: [AttributeType.INNER_DEF, AttributeType.OUTER_DEF],
    EquipPart.BELT: [AttributeType.CRIT_DEF],
    EquipPart.SHOULDER: [AttributeType.CRIT_DEF],
    EquipPart.BOOTS: [AttributeType.DODGE],
    EquipPart.GLOVES: [AttributeType.DODGE],
    EquipPart.NECKLACE: [AttributeType.MAX_HP, AttributeType.INNER_DEF, AttributeType.OUTER_DEF],
    EquipPart.ARTIFACT: [AttributeType.OUTER_ATK, AttributeType.INNER_ATK] 
}

# 战力换算系数 (每个属性点对应的战力值)
POWER_WEIGHTS = {
    AttributeType.MAX_HP.key: 0.2,       # 血量权重较低
    AttributeType.OUTER_ATK.key: 1.0,    # 攻击权重高
    AttributeType.INNER_ATK.key: 1.0,
    AttributeType.OUTER_DEF.key: 0.8,    # 防御次之
    AttributeType.INNER_DEF.key: 0.8,
    AttributeType.HIT.key: 1.2,          # 命中暴击稀有，权重高
    AttributeType.DODGE.key: 1.2,
    AttributeType.CRIT.key: 1.5,
    AttributeType.CRIT_DEF.key: 1.5
}
# 等级战力系数
LEVEL_POWER_WEIGHT = 10 # 每级增加10点基础战力

# UI Coordinates & Layout Configuration
# Assuming 1440x810 Resolution
SCREEN_WIDTH = 1440
SCREEN_HEIGHT = 810

# Right Sidebar Layout
# The sidebar contains: Power, Exp, Equipment, Energy, Main Button
# It is aligned to the right edge with a margin.
UI_RIGHT_MARGIN = 50
UI_COL_WIDTH = 300
UI_SIDEBAR_X = SCREEN_WIDTH - UI_RIGHT_MARGIN - UI_COL_WIDTH # 1440 - 50 - 300 = 1090

# Sidebar Vertical Positions (Y)
UI_POWER_Y = 20 # Moved up from 50
UI_EXP_Y = 70   # Moved up from 110

UI_EQUIP_PANEL_Y = 110 # Moved up from 150
UI_EQUIP_PANEL_HEIGHT = 220 # Increased from implicit 150 to 220 to fit text

# Attribute Panel (Resident in Sidebar)
UI_ATTR_PANEL_GAP = 10
UI_ATTR_PANEL_Y = UI_EQUIP_PANEL_Y + UI_EQUIP_PANEL_HEIGHT + UI_ATTR_PANEL_GAP # 110 + 220 + 10 = 340
UI_ATTR_PANEL_HEIGHT = 220 # Reduced slightly from 250 if needed, but 250 fits: 340+250=590. Button at ~610. OK.

# Attribute Panel / Drop Tips Layout
# Tips are placed to the LEFT of the sidebar
UI_PANEL_WIDTH = 300
UI_PANEL_GAP = 20
UI_PANEL_X = UI_SIDEBAR_X - UI_PANEL_WIDTH - UI_PANEL_GAP # 1090 - 300 - 20 = 770
UI_PANEL_Y = UI_EQUIP_PANEL_Y # Align top with Equipment Panel

# Tips uses these coordinates (Left side)
TIPS_X = UI_PANEL_X
TIPS_Y = UI_PANEL_Y
