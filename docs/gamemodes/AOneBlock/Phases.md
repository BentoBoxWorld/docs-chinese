# 自定义 AOneBlock 阶段

玩家从魔法方块中开采出来的一切都来自**阶段文件**。本页面解释了这些文件的工作原理、其中每个数字的含义，以及如何构建你自己的阶段。

!!! tip "简短答案"
    材料或生物后面的数字 — `COBBLESTONE: 900` — 是**权重**，不是计数也不是百分比。一个阶段把它所有的权重加起来，然后按照权重的比例随机选择一个条目。`blocks:`、`mobs:` 和 `custom-blocks:` 都从同一个单一池中抽取。

## 文件位置

插件第一次运行后，文件位于：

```
plugins/BentoBox/addons/AOneBlock/
├── config.yml
├── phases_index.yml          ← 哪些阶段加载、按什么顺序加载、各自有多长
└── phases/
    ├── 0_plains.yml          ← 阶段的方块、怪物、全息图和设置
    ├── 0_plains_chests.yml   ← 该阶段的战利品表
    ├── 700_underground.yml
    ├── 700_underground_chests.yml
    └── ...
```

每个阶段都是一对文件：`<name>.yml` 和 `<name>_chests.yml`。宝箱文件按文件名配对，所以如果你重命名一个，必须也重命名另一个。

!!! info "`0_plains.yml` 是参考文件"
    发行的 `0_plains.yml` 包含了大量注释，文档化了所有选项。如果你只想读一个文件，就读这个。本页面用实际例子覆盖相同的内容。

编辑完这些文件后，重新加载插件（`/bbox reload`）或重启服务器。

---

## 三种数字类型

这是容易绊住人的地方。阶段文件包含三种完全不同的数字类型，区分它们完全取决于**它所在的章节**。

| 位置 | 数字的含义 |
|---|---|
| `blocks:`、`mobs:`、`custom-blocks:` | 一个**权重** — 该条目在随机池中的份额。 |
| `fixedBlocks` 和 `holograms:` 中的键 | 一个**位置** — 该阶段中的第几个方块，从 0 开始计数。 |
| 文件的顶层键（`'0':`、`'2500':`） | 阶段的**章节名称**，历史上是起始方块数。阶段顺序和长度现在来自 `phases_index.yml`。 |

---

## 权重 — `blocks:` 和 `mobs:` 章节

### 掷骰如何工作

玩家每次破坏魔法方块时，AOneBlock 会：

1. 加总**所有**当前阶段的权重 — `blocks:` 中的全部、`mobs:` 中的全部，以及 `custom-blocks:` 中的全部。
2. 在该范围内挑选一个随机数，返回它落在的条目。

所以：

```
条目的机会 = 它的权重 ÷ 阶段中所有权重的总和
```

权重不是数量。`STONE: 1000` 不是说在该阶段会生成一千个石头 — 它是说石头在抽签中获得 1000 张票，而且每次破坏都重新抽一次。

### 实际例子

```yaml
'2500':
  name: Winter
  firstBlock: SNOW_BLOCK
  biome: SNOWY_TAIGA
  blocks:
    COBBLESTONE: 900
    SAND: 100
    DIRT: 200
    STONE: 1000
    SPRUCE_LEAVES: 500
```

权重总和为 `900 + 100 + 200 + 1000 + 500 = 2700`，所以：

| 方块 | 权重 | 每次破坏的机会 |
|---|---:|---:|
| `STONE` | 1000 | 1000 / 2700 = **37.0%** |
| `COBBLESTONE` | 900 | 900 / 2700 = **33.3%** |
| `SPRUCE_LEAVES` | 500 | 500 / 2700 = **18.5%** |
| `DIRT` | 200 | 200 / 2700 = **7.4%** |
| `SAND` | 100 | 100 / 2700 = **3.7%** |

在 1000 方块阶段中，你会**预期**大约 370 块石头，但每次破坏都是独立抽取，所以实际数字会在这个数字周围波动。

### 只有比例重要

```yaml
blocks:
  STONE: 1000
  DIRT: 200
```

的行为**完全相同**于

```yaml
blocks:
  STONE: 10
  DIRT: 2
```

发行的文件故意使用大数字：当总数在几千范围内时，你可以在权重 `5` 处添加稀有条目，而不必重新缩放其他所有内容来保持百分比合理。

### 方块和怪物共享一个池

!!! warning "怪物权重计入与方块权重相同的总数"
    `mobs:` 不是单独的抽取。怪物条目只是同一抽签中的另一张票，所以 `CHICKEN: 200` 恰好与权重 200 的方块一样可能 — 而加入怪物会让每个方块稍微少见一些。

发行的平原阶段具体说明了这一点。它的 `blocks:` 权重总计 11450，`mobs:` 权重总计 665，阶段总计 **12115**：

| 条目 | 权重 | 每次破坏的机会 |
|---|---:|---:|
| `GRASS_BLOCK` | 2000 | 16.5% |
| `OAK_LOG` | 2000 | 16.5% |
| `CHEST` | 200 | 1.7% |
| `CHICKEN` *(怪物)* | 200 | 1.7% |
| `COW` *(怪物)* | 150 | 1.2% |
| `DIAMOND_ORE` | 30 | 0.25% |
| `VILLAGER` *(怪物)* | 15 | 0.12% |
| `EMERALD_ORE` | 10 | 0.08% |

### 调优秘诀

| 你想要… | 这样做 |
|---|---|
| 使某物的出现频率翻倍 | 加倍其权重 |
| 移除某物 | 删除该行（或注释掉） |
| 添加一个大约 *X*% 的方块 | 权重 ≈ `X/100 × 当前总数 ÷ (1 − X/100)` — 或者直接取当前总数，对于约 1% 添加一个权重约为总数 / 100 的条目 |
| 重新平衡整个阶段 | 一次改变一个权重 — 每次改变都会改变其他所有百分比，因为总数在移动 |
| 使怪物更少见而不改动方块 | 降低 `mobs:` 权重；方块百分比自动上升 |

### 规则和陷阱

- 权重必须是**大于等于 1 的整数**。`0`、负数或小数会被拒绝并记录为 `Bad item weight for <phase>: <material>`。
- 材料必须是真实的 Bukkit [Material](https://hub.spigotmc.org/javadocs/bukkit/org/bukkit/Material.html)**且是方块**。像 `DIAMOND` 这样的物品会被记录为 `Bad block material`。
- 怪物必须是存活的、可生成的 [EntityType](https://hub.spigotmc.org/javadocs/bukkit/org/bukkit/entity/EntityType.html)。无效的名称在启动时记录完整的有效名称列表。
- 如果一个阶段根本没有有效的权重，它会记录 `has zero probability of generating blocks` 并回退到单个方块类型 — 检查章节名称的拼写。

### `CHEST` 是特殊情况

当 `CHEST` 从池中被抽到时，AOneBlock 会从该阶段的 `_chests.yml` 文件填充它。所以 `CHEST` 权重是得到**一个**宝箱的机会；你得到哪个宝箱是**第二个、单独的**稀有度随机抽取：

| 稀有度 | 机会 |
|---|---:|
| `COMMON` | 62% |
| `UNCOMMON` | 25% |
| `RARE` | 9% |
| `EPIC` | 4% |

这些稀有度机会在代码中是固定的，不可配置。如果一个稀有度对该阶段没有定义宝箱，会使用 `COMMON` 列表代替；如果根本没有宝箱，会放置一个空宝箱。

### 怪物

当一个怪物被抽到时，如果魔法方块是空的，它会变成 `STONE`，怪物在上面生成。设置了 `clear-blocks: true` 时，会清除挡道的方块，这样大型怪物才能放进去。

```yaml
mobs:
  COW: 150
  SPIDER: 75
  SHEEP: 75
  PIG: 150
  VILLAGER: 15
  CHICKEN: 200
```

---

## 位置 — `fixedBlocks` 和 `holograms`

这两个章节中的键是**阶段内的位置**，从 0 开始计数。位置 `0` 是阶段的第一个方块，`1` 是第二个，以此类推。它们**不是**玩家的总方块计数，大于阶段长度的位置根本不会到达。

### `fixedBlocks`

固定方块是有保障的 — 它们完全绕过加权池。用于脚本化时刻。

```yaml
fixedBlocks:
  0: GRASS_BLOCK
  1: GRASS_BLOCK
  2: GRASS_BLOCK
  3: OAK_LOG
  4: OAK_LOG
  5: OAK_LOG
  700: CHEST_WITH_WATER_BUCKET
```

- 在此处定义位置 `0` 替代 `firstBlock`，后者就不再需要了。
- `CHEST_WITH_<ITEM>` 是一种速写法，放置一个存放单个该材料物品的宝箱 — 用于在海洋阶段之前给玩家一个水桶很方便。
- 优先选择不需要支撑的方块。火把、铁轨或树苗作为魔法方块放置时只会直接掉落。
- 一个固定方块条目也可以是[自定义方块](#自定义方块)定义。

### `holograms`

编号相同，但值是要在魔法方块上方浮动的文字。`&` 颜色代码有效。

```yaml
holograms:
  0: "&aFirst block is grass!"
  1: "&aSecond block is grass!"
  3: "&aGood Luck!"
```

最开始的全息图 — 第一个阶段开始前显示的那个 — 位于插件的语言文件中，而不是这里。

---

## 阶段顺序和长度 — `phases_index.yml`

!!! new "自 AOneBlock 1.26.0 起"
    阶段顺序和长度**不再**从文件名或顶层键中获取。`phases_index.yml` 是唯一的真理来源。

```yaml
phases:
  - file: 0_plains
    section: '0'
    name: Plains
    length: 700
  - file: 700_underground
    section: '700'
    name: Underground
    length: 1300
gotoAtEnd: 0
```

| 字段 | 含义 |
|---|---|
| `file` | 阶段文件的基础名称，不含 `.yml`。宝箱文件是 `<file>_chests.yml`。 |
| `section` | 该阶段文件内部的顶层键。 |
| `name` | 显示名称，用于日志和 `/[admin_command] phases` 中。 |
| `length` | 该阶段持续的方块数。 |
| `enabled` | 可选，默认为 `true`。设为 `false` 可完全排除该阶段。 |
| `requiredMinecraftVersion` | 可选。该阶段在旧版服务器上被跳过，不占用任何方块。 |

起始方块是**计算**得出的：每个阶段从它上面所有已启用阶段长度的累加总和开始，从 0 开始。随意重新排序阶段；被禁用或跳过的阶段从进度中淡出。最后一个阶段后，方块计数跳转到 `gotoAtEnd`。

改变所有这些的最简单方法是在游戏中使用 `/[admin_command] phases`，它为你编辑索引。参见[阶段顺序编辑器](index.md#命令)说明。一旦你在那里编辑过长度，`adminLengths: true` 就会写入索引，你的长度永远不会被重新计算。

!!! tip "文件名中的数字只是提示"
    `0_plains`、`2500_winter` 等是历史遗留。一个自定义阶段可以是 `my_phase.yml`，带有 `my_phase:` 顶层键，数字都不需要。数字对全新文件仍然有用：它们告诉索引协调器该阶段在运行顺序中应该去哪里。

---

## 阶段文件的结构

```yaml
'0':                          # 章节名称（参见 phases_index.yml）
  name: Plains                # 显示名称
  icon: GRASS_BLOCK           # 阶段 GUI 中的图标（BentoBox ItemParser）
  firstBlock: GRASS_BLOCK     # 位置 0 的方块（可选）
  biome: PLAINS               # 魔法方块位置的生物群系
  requiredMinecraftVersion: '1.21.6'   # 可选版本门槛

  fixedBlocks: { ... }        # 位置处的有保障方块
  holograms: { ... }          # 位置处的文字

  blocks: { ... }             # 方块的加权池
  mobs: { ... }               # 怪物的加权池 — 同一池
  custom-blocks: [ ... ]      # 自定义条目的加权池 — 同一池

  start-commands: [ ... ]
  end-commands: [ ... ]
  end-commands-first-time: [ ... ]
  requirements: { ... }
```

=== "name"
    显示名称，显示在阶段 GUI、boss 血条、日志行和 `[phase]` 命令占位符中。

=== "icon"
    仅在阶段 GUI 中使用的图标。使用 [BentoBox ItemParser](../../BentoBox/ItemParser.md) 解析，所以自定义玩家头颅和任何可显示的物品都有效。没有图标的阶段回退到它的第一个方块。

=== "firstBlock"
    阶段位置 0 处放置的方块。可选 — 在 `fixedBlocks` 下定义 `0:` 做相同的事情并优先。

=== "biome"
    只改变**魔法方块位置**的生物群系，而不是整个岛屿。要在阶段改变时重新生物化整个岛屿，从 `start-commands` 条目调用生物群系插件。无效的生物群系名称在启动时记录完整的有效生物群系列表。

=== "requirements"
    限制进入阶段。在满足所有要求前，玩家被保持在前一个阶段的末尾。

    - `economy-balance` — 最低玩家余额（需要 Vault 和经济插件）
    - `bank-balance` — 最低岛屿银行余额（需要银行插件）
    - `level` — 最低岛屿等级（需要等级插件）
    - `permission` — 玩家必须拥有的权限字符串
    - `cooldown` — 自该阶段上次启动后必须经过的秒数

    ```yaml
    requirements:
      bank-balance: 10000
      level: 10
      permission: ready.for.battle
      cooldown: 60
    ```

---

## 阶段改变时的命令

命令作为**控制台**运行，除非带有 `[SUDO]` 前缀，此时它们作为触发它们的玩家运行。

| 章节 | 何时运行 |
|---|---|
| `start-commands` | 阶段开始时 |
| `end-commands` | 每次阶段完成时 |
| `end-commands-first-time` | 仅**第一次**该岛屿完成该阶段 |

代入命令字符串的占位符：

| 占位符 | 值 |
|---|---|
| `[island]` | 岛屿名称 |
| `[owner]` | 岛屿所有者的名称 |
| `[player]` | 破坏该方块的玩家的名称 |
| `[phase]` | 该阶段的名称 |
| `[blocks]` | 破坏的方块数量 |
| `[level]` | 岛屿等级（需要等级插件） |
| `[bank-balance]` | 岛屿银行余额（需要银行插件） |
| `[eco-balance]` | 玩家的经济余额（需要 Vault 和经济插件） |

```yaml
start-commands:
- 'give [player] WOODEN_AXE 1'
- 'broadcast [player] just started OneBlock!'
end-commands-first-time:
- 'broadcast &c&l[!] &b[player] &fhas completed the &d&n[phase]&f phase for the first time.'
```

---

## 宝箱

宝箱位于阶段的 `_chests.yml` 文件中，在同一个顶层章节名称下：

```yaml
'0':
  chests:
    '1':
      rarity: COMMON
      contents:
        0: ==: org.bukkit.inventory.ItemStack ...
    '2':
      rarity: EPIC
      contents:
        ...
```

- 键每个宝箱的数字（`'1'`、`'2'`）只是一个**唯一 ID** — 既不是权重也不是位置。当应该得到某个稀有度的宝箱时，该稀有度的宝箱中的一个以相等的概率被随机选中。
- `contents` 键是**物品栏槽位编号**。
- `rarity` 是 `COMMON`、`UNCOMMON`、`RARE` 或 `EPIC`。

!!! tip "在游戏中构建宝箱，不要手工做"
    用你想要的东西填满一个真实的宝箱，看着它，然后运行 `/[admin_command] setchest <phase> <rarity>`。宝箱被序列化直接进入阶段的宝箱文件，正确地，第一次。手工编辑序列化的物品 YAML 容易出错；之后使用 `/[admin_command] sanity [<phase>]` 检查你的战利品表。删除宝箱仍然意味着编辑文件并重新加载。

---

## 自定义方块

`custom-blocks:` 是不是普通材料的条目列表。每个条目都有一个 `probability:` 字段，尽管名称如此，它是一个**权重**，在与 `blocks:` 和 `mobs:` 完全相同的池中。`probability: 10` 与权重 10 的方块一样可能。

```yaml
custom-blocks:
  - type: block-data
    data: minecraft:chest[waterlogged=true]
    probability: 10
  - type: mob
    mob: ZOMBIE
    underlying-block: STONE
    probability: 5
  - type: itemsadder
    id: mypack:ruby_ore
    probability: 10
```

| `type` | 它做什么 | 需要 |
|---|---|---|
| `block` / `block-data` | 运行 `/setblock`，带完整的方块数据 — 方块状态、NBT 和可选的 `destroy`\|`keep`\|`replace` 模式。使用 NBT 时优先 `block`。 | — |
| `mob` | 使用生成实体 API 生成原版实体。 | `mob`；可选 `underlying-block`（默认 `STONE`） |
| `mob-data` | 运行 `/summon`，带原版 NBT/组件。方块在怪物的（缩放）边界框内会在生成后一刻被清除，这样它才能放进去。 | `data` |
| `mythic-mob` | 通过 BentoBox 的钩子生成一个 MythicMob。 | MythicMobs 插件 |
| `itemsadder` | 来自 [ItemsAdder](https://itemsadder.devs.beer/) 的方块。 | ItemsAdder 插件 |
| `nexo` | 来自 [Nexo](https://polymart.org/resource/nexo.6901) 的方块。 | Nexo 插件 |
| `craftengine` | 来自 [CraftEngine](https://github.com/Xiao-MoMi/craft-core) 的方块。 | CraftEngine 插件、BentoBox 3.15.0+ |

自定义方块也可以用在 `fixedBlocks` 中，作为对象而不是材料名称：

```yaml
fixedBlocks:
  0:
    type: block-data
    data: minecraft:chest[waterlogged=true]
  1: GRASS_BLOCK
```

!!! warning "引用你的数据字符串"
    自定义方块 `data` 字符串包含 `{`、`}`、`[`、`]` 和双引号。用**单**引号将整个值包裹起来，这样内部双引号就不会与 YAML 的字符串分隔符冲突。

    ```yaml
    - type: mob-data
      data: 'breeze{CustomName:[{text:"Breezy",color:"#f90606"}],Glowing:1b}'
      underlying-block: STONE
      probability: 10
    ```

!!! tip "生怪笼陷阱"
    放置没有计时字段的 `spawner` 在原版 1.21 中是无效的（`Delay:-1` 意味着"永不刻度"）。明确设置 `Delay`、`MinSpawnDelay`、`MaxSpawnDelay` 等，否则生怪笼出现但不做任何事。`Delay:0` 让第一次生成在下一刻就发生。

如果自定义方块的插件未安装，方块回退到 `STONE`，日志中写一行。

---

## 版本限制

一个阶段、单个方块或单个怪物可以声明它需要的最低 Minecraft 版本。服务器版本太旧而无法支持的任何内容都会跳过，只输出一行信息日志，而不是 `Tried to load invalid item` 错误。

**整个阶段** — 把 `requiredMinecraftVersion` 放在 `phases_index.yml` 中，这样文件在旧服务器上根本不会被解析。阶段则不占用任何方块，其后的阶段向上收起。

**单个方块或怪物** — 使用对象形式，用 `weight:` 字段交换裸权重：

```yaml
blocks:
  NETHERRACK: 300
  DRIED_GHAST:
    weight: 25
    requiredMinecraftVersion: '1.21.6'

mobs:
  ZOMBIFIED_PIGLIN: 100
  HAPPY_GHAST:
    weight: 5
    requiredMinecraftVersion: '1.21.6'
```

宝箱文件逐项读取，所以你的服务器版本不认识的物品在自己上被跳过，宝箱的其余部分仍加载。

---

## 构建新阶段

1. **复制一对现有文件**在 `phases` 文件夹中 — 比如 `4000_jungle.yml` 和 `4000_jungle_chests.yml` — 到 `volcano.yml` 和 `volcano_chests.yml`。
2. **改变两个文件中的顶层键**到某个独特的东西，比如 `volcano:`。它必须在两个文件中相匹配。
3. **设置 `name:` 和 `icon:`**，然后用你想要的权重编辑 `blocks:` 和 `mobs:`。记住百分比是相对于*阶段*总数的。
4. **重启或重新加载**。插件注意到新文件，以默认长度 500 添加它到 `phases_index.yml` 末尾，并记录：
   `Phase index: added Volcano from volcano.yml at the end of the phase order. Move it with the admin phases GUI.`
5. **用 `/[admin_command] phases` 定位它** — 左键点击将其拿起，点击它应该去的位置，shift-左键点击设置其长度。
6. **测试它**，使用 `/[admin_command] setcount <player> <number>` 直接跳到阶段的起始方块。

!!! tip "在临时岛屿上测试"
    破坏几百个方块，看看实际出现什么。权重在纸上读起来与它们实际运作的方式完全不同。`/[player_command] count` 显示你在阶段中的位置。

---

## 故障排除

| 症状 | 可能的原因 |
|---|---|
| `Bad block material in <phase>: X` | `X` 不是 Bukkit 材料，或是物品而不是方块 |
| `Bad item weight for <phase>: X. Must be positive number above 1` | 权重是 0、负数或不是整数 |
| `Bad entity type in <phase>: X` | 不是有效的 `EntityType`；日志列出有效的 |
| `<phase> has zero probability of generating blocks` | `blocks:` 章节缺失、空或在错误的章节键下 |
| `Phase name trying to be set to X but already set to Y. Duplicate phase file?` | 两个文件使用同一顶层章节键 |
| 阶段从不出现 | 它在 `phases_index.yml` 中是 `enabled: false`，或它的 `requiredMinecraftVersion` 比服务器更新 |
| 宝箱出现空的 | 宝箱文件的顶层键与阶段文件的不匹配，或其物品加载失败 — 运行 `/[admin_command] sanity` |
| 编辑不起作用 | 插件未被重新加载，或你编辑的是 jar 中 `src/main/resources` 中的文件而不是 `plugins/BentoBox/addons/AOneBlock/phases/` |

监视服务器日志在启动时。每个加载的阶段文件被记录，以及每个被拒绝的方块、怪物和物品，以及索引协调器做的每个改变（以 `Phase index:` 开头的行）。
