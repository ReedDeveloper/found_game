---
name: "rpg_equip_gen"
description: "生成完整的RPG装备系统，包含枚举定义、随机属性逻辑、套装系统及配置导出。当涉及装备创建、属性查询、品阶计算或装备展示时调用。"
---

# RPG装备生成器 (RPG Equipment Generator)

本Skill用于设计和生成复杂的RPG游戏装备系统，专注于程序化生成具有不同品阶、部位、类型和属性的物品数据。

## 核心能力 (Capabilities)

1.  **架构定义 (Schema Definition)**
    *   定义装备核心常量：部位 (头、身、武器...)、品阶 (1-10阶)、属性类型 (攻击、防御...)、装备类型 (攻击/防御/攻防兼备) 以及品质颜色规范。
2.  **程序化生成 (Procedural Generation)**
    *   **多维组合**：通过 `品阶 x 部位 x 变种` 的方式生成海量唯一物品。
    *   **命名系统**：结合品阶前缀、部位名称、武器子类型 (刀/剑/弓...) 以及变种后缀生成丰富多样的装备名称。
    *   **数值成长**：基于基础数值、品阶系数和随机浮动生成属性值。
    *   **套装逻辑**：支持生成具有独立命名和属性加成的套装组件。
3.  **数据导出 (Data Export)**
    *   将生成的内存对象序列化为结构化的配置文件 (`equip_cfg.py` 或 JSON)，供游戏逻辑直接加载使用。

## 设计理念与规范 (Design Philosophy)

### 1. 枚举与常量 (`const.py`)
*   **EquipPart**: 12个部位（武器、护腕、戒指、护符、头盔、甲胄、腰带、护肩、鞋履、手套、项链、法宝）。
*   **Rank**: 10个修仙品阶（炼气 -> 金仙），每个品阶对应一组特定的前缀词库（如"聚气"、"纳灵"）。
*   **WeaponType**: 7种武器子类型（剑、刀、弓、弩、枪、棍、戟）。
*   **QualityColor**: 严格的 RGB 颜色规范，从灰阶到金阶一一对应。

### 2. 生成规则 (`equip_table.py`)
*   **ID 规则**: `1xxyyzzz`
    *   `xx`: 品阶 (00-09)
    *   `yy`: 部位 (00-11)
    *   `zzz`: 变种序号 (000-099 为散件, 100+ 为套装)
*   **属性计算**:
    *   `基础值 = 预设基数 * (品阶 + 1) * 1.2`
    *   `最终值 = 基础值 * 随机浮动(0.95~1.05)`
    *   套装拥有 1.1 倍属性加成及额外词条。

## 使用模式 (Implementation Pattern)

当需要创建或更新装备库时，请遵循以下流程：

### 第一步：定义常量
在 `src/const.py` 中定义所有枚举类和配置表 (`BASE_STATS_CONFIG`, `EXT_STATS_CONFIG`)。

### 第二步：实现生成器
编写 `src/equip_table.py`，包含 `EquipItem` 类和 `generate_equip_table()` 函数。实现具体的遍历循环（品阶->部位->变种）和属性计算逻辑。

### 第三步：导出配置
运行生成器脚本，将生成的装备列表写入 `src/equip_cfg.py`，确保输出格式为合法的 Python 列表或字典，以便 `import` 使用。

## 示例代码结构

```python
# const.py
class Rank(Enum):
    LIAN_QI = 0
    ZHU_JI = 1
    ...

# equip_table.py
def generate():
    equip_list = []
    for rank in Rank:
        for part in EquipPart:
            # 生成6种普通散件
            for i in range(6):
                create_item(...)
            # 生成3种套装
            for s in range(3):
                create_set_item(...)
    return equip_list
```
