
# Item Configuration

# Item Types
class ItemType:
    MATERIAL = "material"
    CONSUMABLE = "consumable"

ITEM_CFG = {
    60000: {
        'id': 60000,
        'name': '陨铁',
        'image': 'pic/ui/item/yuntie.png',
        'desc': '来自天外的陨铁，坚硬无比，是打造神兵利器的上佳材料。',
        'type': ItemType.MATERIAL,
        'quality': 3 # Purple
    },
    60100: {
        'id': 60100,
        'name': '秘银',
        'image': 'pic/ui/item/miyin.png',
        'desc': '蕴含神秘力量的银矿，延展性极佳，常用于精细部件的制作。',
        'type': ItemType.MATERIAL,
        'quality': 3
    },
    60200: {
        'id': 60200,
        'name': '灵槐',
        'image': 'pic/ui/item/linghuai.png',
        'desc': '生长在灵气充裕之地的槐木，木质纹理中流动着淡淡的灵光。',
        'type': ItemType.MATERIAL,
        'quality': 3
    },
    60300: {
        'id': 60300,
        'name': '灵魄',
        'image': 'pic/ui/item/lingpo.png',
        'desc': '妖兽死后凝聚的灵力精华，是强化装备和炼制丹药的核心材料。',
        'type': ItemType.MATERIAL,
        'quality': 4 # Orange/Red?
    }
}
