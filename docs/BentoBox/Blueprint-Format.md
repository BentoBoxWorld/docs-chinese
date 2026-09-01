# 蓝图文件格式

**规范版本 2**

此页面记录了 BentoBox 用于岛屿蓝图（`.blueprint` 文件）和蓝图包（包 `.json` 文件）的磁盘上 JSON 格式。它是随 BentoBox 存储库一起提供的机器可读 [JSON 模式](https://github.com/BentoBoxWorld/BentoBox/tree/develop/schemas) 的人类可读伴侣，可用于在编辑器或 CI 中验证文件。

如果你想要*制作*游戏中的蓝图，见 [蓝图页面](Blueprints.md)。此页面是针对直接生成、编辑或验证蓝图文件的开发人员和高级用户。

## 修订历史

| 版本 | 日期 | BentoBox 版本 | 描述 |
|------|------|------|------|
| 1 | 2019-06-09 | [1.5.0](https://github.com/BentoBoxWorld/BentoBox/releases/tag/1.5.0) | 初始版本，BentoBox Schem 格式的派生 |
| 1.1 | 2026 | 2.x | 存储从压缩二进制更改为纯 JSON；`.blueprint` 成为主要扩展 |
| 2 | 2026-08-14 | 3.22.x | 从源生成的完整字段级规范；发布了 JSON 模式 |

## 文件类型

| 扩展 | 格式 | 状态 |
|------|------|------|
| `.blueprint` | 包含单个 [蓝图](#蓝图) 对象的纯 UTF-8 JSON | 当前 |
| `.blu` | ZIP 存档包含同一 JSON 的单个条目 | 旧版——仍可加载，永不写入 |
| `<uniqueId>.json` | 包含单个 [蓝图包](#蓝图包) 对象的纯 UTF-8 JSON | 当前 |

两种类型的文件都在游戏模式附属的 `blueprints/` 文件夹中，例如 `plugins/BentoBox/addons/BSkyBlock/blueprints/`。一个包通过 `name` 引用其蓝图，被引用的 `.blueprint` 文件必须坐在同一文件夹中。

## 序列化规则

蓝图通过 Gson 写入。这些规则在整个应用，并解释你将在下方看到的形状：

- 只有此规范中列出的字段被发出；制作人必须不添加其他键。
- **向量** (`org.bukkit.util.Vector`) 是 3 元素 JSON 数组：`[x, y, z]`。块位置习惯上持有整数，但底层类型是双数。
- **由向量键控的地图** 使用 Gson 的复杂地图键形式：JSON *对数组*——`[[<vector>, <value>], ...]`——**不是** JSON 对象。这适用于 `blocks`、`attached` 和 `entities`。
- **由枚举键控的地图**（例如包的 `blueprints` 地图）是普通的 JSON 对象，枚举名称作为键。
- **由整数键控的地图**（库存槽 → 物品）是带字符串化整数键的 JSON 对象（`"0"`、`"13"`、…）。
- **物品栈** 序列化为 Bukkit YAML（通过 `ConfigurationSerializable`）并存储为 JSON *字符串*。将值视为可由 `YamlConfiguration#loadFromString` 解析的不透明 YAML 文档。
- **枚举** 通过其 Java `name()` 序列化。
- **颜色** (`org.bukkit.Color`) 序列化为 `{"ALPHA": int, "RED": int, "GREEN": int, "BLUE": int}`。
- 文件由作者漂亮打印；消费者必须不依赖空格。
- 所有字段名称都**区分大小写**。

## 蓝图

`.blueprint` 文件的顶级对象。它描述一个块卷、附加块和相对于锚点的实体（`bedrock`）。

| 字段 | 类型 | 描述 |
|------|------|------|
| `name` | 字符串 | 唯一标识符，用于从包中查找蓝图。按约定与文件名干匹配。 |
| `displayName` | 字符串 | 在 UI 中显示的人类可读名称。可能包含旧版 `§` 颜色代码或 MiniMessage 标签。 |
| `icon` | 字符串 | 图标材料：Bukkit `Material` 名称（`DIAMOND`）、虚拟键（`minecraft:diamond`）或资源包自定义模型键。默认 `PAPER`。 |
| `description` | 字符串[] | 在选择 UI 中的图标下显示的传说线。 |
| `bedrock` | 向量 | 锚点。粘贴时，蓝图 `(0,0,0)` 被翻译以使 `bedrock` 降落在粘贴目标上。如果省略，BentoBox 在加载时在 `(xSize/2, ySize/2, zSize/2)` 自动创建一个。 |
| `xSize`、`ySize`、`zSize` | 整数 | 边界框维度以块为单位。 |
| `sink` | 布尔 | 如果为真，蓝图在粘贴时下降直到它找到一个表面，而不是在锚点的确切 Y 粘贴。 |
| `blocks` | 向量键控地图 | 主块，按相对于蓝图源的位置键控（每个轴 `0..size-1`）。见 [蓝图块](#蓝图块)。 |
| `attached` | 向量键控地图 | 块粘贴**之后** `blocks`，因为它们附加到支撑：火焰、梯子、铁轨、床、门、标志等。相同坐标约定作为 `blocks`。 |
| `entities` | 向量键控列表地图 | 每块位置的实体来生成。多个实体可能共享一个键；块内的微调偏移在 [蓝图实体](#蓝图实体) 上。 |

一个最小的例子：

```json
{
  "name": "island",
  "displayName": "&aStarter island",
  "icon": "GRASS_BLOCK",
  "description": ["A tiny island"],
  "bedrock": [2.0, 1.0, 2.0],
  "xSize": 5, "ySize": 3, "zSize": 5,
  "blocks": [
    [[2.0, 1.0, 2.0], {"blockData": "minecraft:bedrock"}],
    [[2.0, 2.0, 2.0], {"blockData": "minecraft:grass_block[snowy=false]"}]
  ],
  "attached": [
    [[2.0, 3.0, 2.0], {"blockData": "minecraft:oak_sign[rotation=0,waterlogged=false]", "signLines": ["[spawn_here]", "", "", ""]}]
  ],
  "entities": [
    [[1.0, 2.0, 1.0], [{"type": "COW", "adult": true}]]
  ]
}
```

## 蓝图块

一个块单元格。仅 `blockData` 是必需的；每个其他字段仅在块类型支持它时应用。

| 字段 | 类型 | 描述 |
|------|------|------|
| `blockData` | 字符串 | **必需。** Bukkit `BlockData` 字符串，即 `BlockData#getAsString()` 的输出——例如 `minecraft:chest[facing=north,type=single,waterlogged=false]`。 |
| `signLines` | 字符串[]（≤4） | 前侧标志线。支持旧版 `§` 颜色代码。自 1.24.0 起弃用，支持侧特定字段，但仍然被写入和读取。 |
| `signLines2` | 字符串[]（≤4） | 后侧标志线（双面标志，在 1.24.0 中添加）。 |
| `glowingText` | 布尔 | 标志的前面有发光文本。 |
| `glowingText2` | 布尔 | 标志的后面有发光文本。 |
| `inventory` | 槽地图 | 容器内容（箱子、桶、漏斗、潜影箱、熔炉、酿造台……）。键是字符串化槽索引；值是 YAML 编码的物品栈。 |
| `bannerPatterns` | 对象[] | 标旗图案层，按顺序应用。每个条目有 `pattern`（旧版短代码，例如 `bri`）和 `color`（一个 `DyeColor` 名称）。 |
| `biome` | 字符串 | 此块单元格的生物群系覆盖（Bukkit `Biome` 名称）。 |
| `creatureSpawner` | 对象 | 仅当 `blockData` 是生成器时出现。见 [蓝图生物生成器](#蓝图生物生成器)。 |
| `trialSpawner` | 对象 | 仅当 `blockData` 是试验生成器时出现（1.21+，在 BentoBox 3.4.2 中添加）。与 `creatureSpawner` 互斥。见 [蓝图试验生成器](#蓝图试验生成器)。 |
| `itemsAdderBlock` | 字符串 | ItemsAdder 自定义块 ID（例如 `myserver:custom_ore`）。仅当 ItemsAdder 被安装时有意义；否则块回到 `blockData`。 |

### 蓝图生物生成器

虚拟（非试验）暴民生成器配置。

| 字段 | 类型 | 描述 |
|------|------|------|
| `spawnedType` | 字符串 | Bukkit `EntityType` 名称。 |
| `delay` | 整数 | 当前倒计时（刻度）直到下一个生成尝试。 |
| `maxNearbyEntities` | 整数 | 生成暂停当至少这多个生成的类型在跟踪范围内。 |
| `minSpawnDelay`、`maxSpawnDelay` | 整数 | 边界（刻度）的随机化延迟在每个生成后选择。 |
| `requiredPlayerRange` | 整数 | 最大玩家距离（块）让生成器活跃。 |
| `spawnRange` | 整数 | 半径（块）内可能生成暴民的。 |

### 蓝图试验生成器

试验生成器配置（Minecraft 1.21+）。使用 `spawnedType` **或** `potentialSpawns`，不两个。

| 字段 | 类型 | 描述 |
|------|------|------|
| `ominous` | 布尔 | 生成器是否在其不祥（诅咒）状态。 |
| `spawnedType` | 字符串 | 单个 `EntityType` 来生成。 |
| `potentialSpawns` | 对象[] | 加权生成候选。每个条目：`snapshot`（不透明 `EntitySnapshot#getAsString` 值）、`spawnrule`（Bukkit `SpawnRule` 对象；键因服务器版本而异）和必需 `spawnWeight`（整数 ≥ 1）。 |
| `delay` | 整数 | 生成延迟。 |
| `baseSimEnts` / `addSimulEnts` | 数字 | 基本同时实体保持活着 / 每额外玩家添加。 |
| `baseSpawnsB4Cool` / `addSpawnsB4Cool` | 数字 | 基本总生成在冷却前 / 每额外玩家添加。 |
| `spawnRange`、`requiredPlayerRange`、`playerRange` | 整数 | 范围以块为单位。 |
| `lootTableMap` | 对数组 | 候选奖励战利品表及相对权重：`[[{"nameSpace": "minecraft", "key": "chests/trial_chambers/reward"}, 1], ...]`。 |

## 蓝图实体

一个实体来生成。仅 `type` 是必需的。未设置的字段意味着"留下 Bukkit 默认独自"；每个字段仅当实体类支持它时应用。

**一般**

| 字段 | 类型 | 描述 |
|------|------|------|
| `type` | 字符串 | **必需。** Bukkit `EntityType` 名称（`VILLAGER`、`ARMOR_STAND`、`ITEM_FRAME`、…）。 |
| `customName` | 字符串 | 显示名称；支持旧版 `§` 颜色代码。 |
| `x`、`y`、`z` | 数字 | 在位置单元格内的微调偏移（通常 `0.0 ≤ v < 1.0`）。 |
| `glowing` | 布尔 | 发光效果。 |
| `gravity` | 布尔 | 重力是否适用。 |
| `visualFire` | 布尔 | 渲染火不管 `fireTicks`。 |
| `silent` | 布尔 | 抑制环境声音。 |
| `invulnerable` | 布尔 | 对所有伤害免疫。 |
| `fireTicks` | 整数 | 剩余火持续时间（刻度）。 |

**暴民**

| 字段 | 类型 | 描述 |
|------|------|------|
| `adult` | 布尔 | 年龄实体——`false` 生成一个婴儿。 |
| `color` | 字符串 | `DyeColor` 名称，对可着色实体（绵羊、潜影箱、狼项圈、…）。 |
| `tamed` | 布尔 | 可驯服实体；所有者没有被恢复。 |
| `chest` | 布尔 | 胸部携带马/羊驼。 |
| `domestication` | 整数（0–100） | 马驯化等级。 |
| `inventory` | 槽地图 | 马/羊驼库存。 |
| `style` | 字符串 | 马外套样式：`WHITE`、`WHITEFIELD`、`WHITE_DOTS`、`BLACK_DOTS`、`NONE`。 |
| `profession` | 字符串 | 村民职业（枚举名称或命名空间键）。 |
| `level` | 整数（1–5） | 村民等级。 |
| `experience` | 整数 | 村民经验。 |
| `villagerType` | 字符串 | 村民生物群系变体（枚举名称或命名空间键）。 |

**插件集成**（仅当插件被安装时有意义）

| 字段 | 类型 | 描述 |
|------|------|------|
| `npc` | 字符串 | Citizens NPC ID。 |
| `MMtype`、`MMLevel`、`MMpower`、`MMStance` | 字符串 / 数字 | MythicMobs 类型、等级、力量和姿态。 |

**显示实体和物品框**

| 字段 | 类型 | 描述 |
|------|------|------|
| `displayRec` | 对象 | 所有显示实体通用的属性——见 [显示记录](#显示记录)。 |
| `blockDisp` | 对象 | 块显示有效负载：显示的块，作为 [蓝图块](#蓝图块)。 |
| `itemDisp` | 对象 | 物品显示有效负载：`item`（YAML 编码的物品栈）和 `itemDispTrans`（一个 `ItemDisplayTransform` 名称：`NONE`、`HEAD`、`GUI`、`GROUND`、`FIXED`、`THIRDPERSON_LEFTHAND`、…）。 |
| `textDisp` | 对象 | 文本显示有效负载——见下面。 |
| `itemFrame` | 对象 | 物品框有效负载（自 3.2.6）：`item`（YAML 编码的物品栈）、`rotation`（Bukkit `Rotation` 名称）、`isFixed`、`isVisible`、`dropChance`（0.0–1.0）。 |

文本显示有效负载字段：`text`（支持旧版 `§` 代码）、`alignment`（`CENTER`/`LEFT`/`RIGHT`）、`bgColor`（颜色对象）、`face`（一个 `BlockFace` 名称）、`lWidth`（行环绕宽度以像素为单位）、`opacity`（有符号字节，−1 = 默认）、`isShadowed`、`isSeeThrough`、`isDefaultBg`。

### 显示记录

| 字段 | 类型 | 描述 |
|------|------|------|
| `billboard` | 字符串 | `FIXED`、`VERTICAL`、`HORIZONTAL` 或 `CENTER`——显示如何面对观看者。 |
| `brightness` | 对象 | Bukkit `Display.Brightness`，通常 `{"block": int, "sky": int}`。 |
| `width`、`height` | 数字 | 显示大小。 |
| `glowColorOverride` | 颜色 | 发光轮廓颜色。 |
| `interpolationDelay`、`interpolationDuration`、`teleportDuration` | 整数 | 动画时序。 |
| `shadowRadius`、`shadowStrength` | 数字 | 阴影渲染。 |
| `transformation` | 对象 | Bukkit `Transformation`（平移、旋转、缩放）。不透明。 |
| `range` | 数字 | 查看范围。 |

## 蓝图包

一个包将最多三个蓝图分组——每个世界环境一个——到岛屿创建 UI 中的单一选项，并控制该选项的成本、权限、GUI 槽、使用上限和创建后指令。持久化为游戏模式的 `blueprints/` 文件夹中的 `<uniqueId>.json`；文件名干**必须**等于 `uniqueId`。

| 字段 | 类型 | 描述 |
|------|------|------|
| `uniqueId` | 字符串 | **必需。** 唯一 ID；也是权限后缀当 `requirePermission` 是真。 |
| `displayName` | 字符串 | 选择 GUI 中显示的名称。 |
| `icon` | 字符串 | 图标材料，与蓝图图标相同形式。默认 `PAPER`。 |
| `description` | 字符串[] | 图标下的传说线。 |
| `blueprints` | 对象 | 环境地图（`NORMAL`、`NETHER`、`THE_END`、`CUSTOM`）到同一文件夹中的蓝图的 `name`。没有条目的环境没有生成。 |
| `requirePermission` | 布尔 | 如果真，玩家需要 `<gamemode>.island.create.<uniqueId>`。 |
| `slot` | 整数 | 优先 0 基础 GUI 槽；在运行时夹紧。 |
| `times` | 整数 | 单个玩家可能创建的最大岛屿具有此包；`0` = 无限。 |
| `cost` | 数字 | Vault 经济成本；`0` = 自由。需要经济插件。 |
| `commands` | 字符串[] | 当岛屿使用此包创建时运行的指令（在 2.6.0 中添加）。`[player]` 和 `[owner]` 被替换；以 `[SUDO]` 为前缀的条目作为玩家运行，其他作为控制台。 |

示例 `default.json`：

```json
{
  "uniqueId": "default",
  "displayName": "Default Island",
  "icon": "GRASS_BLOCK",
  "description": ["A standard island", "with grass and dirt"],
  "blueprints": {
    "NORMAL": "island",
    "NETHER": "nether",
    "THE_END": "end"
  },
  "requirePermission": false,
  "slot": 0,
  "times": 0,
  "cost": 0.0,
  "commands": ["[SUDO] me has arrived!"]
}
```

## 验证文件

BentoBox 存储库发布了两个 JSON 模式（草稿 2020-12）：

- [`schemas/blueprint.schema.json`](https://github.com/BentoBoxWorld/BentoBox/blob/develop/schemas/blueprint.schema.json)——验证一个 `.blueprint` 文件或包
- [`schemas/blueprint-bundle.schema.json`](https://github.com/BentoBoxWorld/BentoBox/blob/develop/schemas/blueprint-bundle.schema.json)——验证一个包文件自己

指向它们，例如与 [ajv](https://ajv.js.org/)：

```bash
ajv validate --spec=draft2020 -s blueprint.schema.json -d island.blueprint
```

注意 YAML 编码的物品栈字符串和一些 Bukkit `ConfigurationSerializable` 对象（转换、生成规则）对模式是不透明的——一个模式有效的文件如果那些嵌入的文档格式不好仍然可能加载失败。
