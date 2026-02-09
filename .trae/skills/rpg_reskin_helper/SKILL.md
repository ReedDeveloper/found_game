---
name: "rpg_reskin_helper"
description: "辅助进行RPG游戏的换皮与迭代，包括根据新题材生成装备/怪物/掉落配置、调整UI布局常量及重构描述文本。当用户需要修改游戏题材、数值或布局以制作新游戏时调用。"
---

# RPG Reskin Helper

此 Skill 旨在帮助开发者基于当前的 RPG 框架快速迭代出新的换皮游戏。它专注于配置修改、题材适配和 UI 调整。

## 能力范围

1.  **题材重构 (Theme Reskinning)**
    *   根据给定的新题材（如：科幻、西幻、末日等），自动重写装备名称、描述、怪物名称和掉落物品。
    *   **目标文件**: `src/equip_cfg.py`, `src/monster_cfg.py`, `src/item_cfg.py`, `src/drop_cfg.py`

2.  **数值调整 (Numerical Tuning)**
    *   调整战力公式权重、升级曲线、掉落概率和强化成功率。
    *   **目标文件**: `src/const.py` (POWER_WEIGHTS), `src/level.py` (exp curve), `src/equipment.py` (enhance logic)

3.  **UI 布局适配 (Layout Adaptation)**
    *   根据新的美术资源尺寸，快速调整 UI 组件的坐标和大小。
    *   **目标文件**: `src/const.py` (UI_*)

## 使用流程

当用户要求“制作一款[新题材]游戏”或“调整数值以适应[新节奏]”时：

### 第一步：理解当前配置
首先读取核心配置文件，了解数据结构：
```python
# 读取所有配置表
read_files(['src/const.py', 'src/equip_cfg.py', 'src/monster_cfg.py', 'src/item_cfg.py'])
```

### 第二步：生成新配置
根据用户的新题材，保持原有数据结构（Dict Keys 不变），仅修改 Values（Name, Desc, ImagePath）。

**示例：修仙 -> 赛博朋克**
*   `陨铁` -> `钛合金芯片`
*   `炼气` -> `黑客入门`
*   `妖兽` -> `安保机器人`

### 第三步：更新资源引用
如果用户提供了新图片目录，使用 `ls` 检查目录结构，并批量更新配置文件中的 `image` 路径。

### 第四步：调整常量
如果界面布局需要调整（例如从竖版变横版，或侧边栏位置改变），修改 `src/const.py` 中的布局常量。

## 常用指令模板

**1. 生成新题材配置**
> "读取当前的 monster_cfg.py，将所有怪物名称和描述修改为【克苏鲁风格】，战力数值保持不变。"

**2. 调整掉落率**
> "修改 drop_cfg.py，大幅提高稀有物品的掉落率，让玩家在前期能更快获得神装。"

**3. UI 重新布局**
> "修改 const.py，将侧边栏从右侧移动到左侧，并调整所有相关面板的坐标。"

## 注意事项
*   修改配置时，**严禁**删除原有的 Key，否则会导致代码逻辑报错。
*   涉及图片路径修改时，确保新路径在文件系统中存在，或提示用户补充资源。
