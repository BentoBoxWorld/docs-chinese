# BentoBox 物品解析器

没有一个好办法从配置文件中定义物品堆栈。
因为每个物品都有不同的元数据可以分配。
所以 BentoBox 使用一种非常奇怪的格式，这种格式来自 ASkyBlock 时代。

## 快速示例

### 通用 Minecraft 物品翻译

从 BentoBox 2.0.0 开始，你可以像 give 指令一样使用 minecraft 物品翻译：

    - minecraft:diamond_sword{display:{Lore:["\"一把传奇武器\""]}} 
    - minecraft:stone
    - diamond_chestplate{Enchantments:[{id:mending,lvl:1},{id:protection,lvl:4},{id:unbreaking,lvl:3}]}

### 通用翻译

默认情况下，所有物品都按以下格式翻译：

    - [TYPE]<:QUANTITY>

数量不是必需的，但是，如果你提供了数量，则需要在前面添加 `:`。

你可以在这里找到所有类型：[Material](https://hub.spigotmc.org/javadocs/bukkit/org/bukkit/Material.html)

但是，有一些例外情况，它们有一些更多的自定义选项可用。你可以在下面查看它们。

### 可损坏物品

你还可以按照以下格式定义可损坏物品：

    - [TYPE]:<DAMAGE_AMOUNT>:<QUANTITY>

损坏量和数量是可选的。

### 药水和药水箭

药水、喷溅药水、滞留药水和药水箭遵循相同的模式：

    - [TYPE]:<POTION_TYPE>:QUANTITY

[TYPE] 可以替换为 POTION、SPLASH_POTION、LINGERING_POTION 或 TIPPED_ARROW。
你可以通过以下链接找到所有药水类型：[PotionTypes](https://hub.spigotmc.org/javadocs/spigot/org/bukkit/potion/PotionType.html)

示例：

    - POTION:STRENGTH:1 - 将创建一个力量 1 的延长药水。
    - SPLASH_POTION:INSTANT_DAMAGE:2 - 将创建 2 个瞬间伤害 2 的喷溅药水
    - LINGERING_POTION:STRONG_LEAPING:1 - 将创建一个跳跃 2 的滞留药水。
    - TIPPED_ARROW:WEAKNESS:1 - 将创建一个虚弱 1 的药水箭。

### 旗帜

旗帜有自定义解析选项，遵循以下方案：

    - [color]_BANNER:QUANTITY<:PatternType:DyeColor>

你可以指定任意多个图案，但它们必须遵循给定的顺序，先是图案类型，然后是染料颜色。

你可以在这里找到所有图案类型：[PatternType](https://hub.spigotmc.org/javadocs/spigot/org/bukkit/block/banner/PatternType.html)

你可以在这里找到所有染料颜色：[DyeColor](https://hub.spigotmc.org/javadocs/spigot/org/bukkit/DyeColor.html)

### 玩家头颅

玩家头颅有自定义解析选项。它遵循以下方案：

 - PLAYER_HEAD:<Name|Trimmed UUID|UUID|Texture>:<QUANTITY>

PLAYER_HEAD - 表示该物品将是玩家头颅。
在下一部分中，你可以指定：

    - 玩家名称
    - 玩家精简 UUID（不带 -）
    - 玩家 UUID（带 -）
    - 材质链接

在最后，你可以指定堆栈中玩家头颅的数量。
例如：`PLAYER_HEAD:BONNe1704` - 将给予 1 个带有 BONNe1704 皮肤的玩家头颅。

### 自定义模型数据

自定义模型数据可以添加到任何可解析的物品堆栈中。自定义模型数据文本可以添加到可解析字符串的任何部分。自定义模型数据的方案：

- `CMD-[number]`

示例：

- IRON_INGOT:2:CMD-12345678 => 创建一个包含 2 个铁锭和自定义模型数据 `12345678` 的物品堆栈
- GOLD_INGOT:CMD-12345678 => 创建一个包含金锭和自定义模型数据 `12345678` 的物品堆栈
- PLAYER_HEAD:BONNe1704:CMD-12345678 => 创建一个包含 BONNe1704 玩家头颅和自定义模型数据 `12345678` 的物品堆栈
