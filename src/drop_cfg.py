
# Drop Configuration
# Format: {monster_id: {'drop_p': [weight1, weight2, ...], 'drop_items': [item_id1, item_id2, ...]}}
# 0 in drop_items means no drop

# Items:
# 60000: 陨铁 (Quality 3)
# 60100: 秘银 (Quality 3)
# 60200: 灵槐 (Quality 3)
# 60300: 灵魄 (Quality 4)

DROP_CFG = {
    # 炼气 (20000)
    20000: {
        'drop_p': [10, 80, 10], # 10% Material, 80% Nothing, 10% Material2
        'drop_items': [60000, 0, 60000] 
    },
    # 筑基 (20001)
    20001: {
        'drop_p': [15, 75, 10], 
        'drop_items': [60000, 0, 60100]
    },
    # 结丹 (20002)
    20002: {
        'drop_p': [20, 70, 10], 
        'drop_items': [60000, 0, 60100]
    },
    # 元婴 (20003)
    20003: {
        'drop_p': [15, 70, 15], 
        'drop_items': [60100, 0, 60200]
    },
    # 化神 (20004)
    20004: {
        'drop_p': [20, 60, 20], 
        'drop_items': [60100, 0, 60200]
    },
    # 炼虚 (20005) - User Example
    20005: {
        'drop_p': [10, 80, 10], 
        'drop_items': [60100, 0, 60200]
    },
    # 合体 (20006)
    20006: {
        'drop_p': [20, 50, 30], 
        'drop_items': [60200, 0, 60300]
    },
    # 大乘 (20007)
    20007: {
        'drop_p': [30, 40, 30], 
        'drop_items': [60200, 0, 60300]
    },
    # 渡劫 (20008)
    20008: {
        'drop_p': [40, 30, 30], 
        'drop_items': [60300, 0, 60300]
    },
    # 金仙 (20009)
    20009: {
        'drop_p': [50, 20, 30], 
        'drop_items': [60300, 0, 60300]
    },
    # BOSS: 妖王 (20010)
    20010: {
        'drop_p': [80, 0, 20], 
        'drop_items': [60300, 0, 60200]
    },
    # BOSS: 妖皇 (20011)
    20011: {
        'drop_p': [90, 0, 10], 
        'drop_items': [60300, 0, 60300]
    },
    # BOSS: 魔神 (20012)
    20012: {
        'drop_p': [100, 0, 0], 
        'drop_items': [60300, 0, 0]
    }
}
