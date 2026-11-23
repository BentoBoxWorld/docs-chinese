# 温室

温室是一个为你的岛屿世界增添力量的BentoBox插件！它使玩家能够建造他们自己的生态区温室，包括天气、友好的生物生成、独特的植物生长，甚至还有方块侵蚀！

温室是由玻璃制成的，并且必须包含生物区配方中的方块才算有效。有一个配方GUI。一旦建造完成，温室可以用来用骨粉促进植物生长，它可能会生成特定生物区的生物。如果你在里面放了一个含有水的漏斗，下雨时温室内会形成雪。如果你在漏斗里放骨粉，会生长特定生物区的植物。一些方块也会因为“侵蚀”而随时间转化。

由[tastybento](https://github.com/tastybento)创建和维护。

{{ addon_description("Greenhouses") }}

## 特性

* 在岛屿上（或你喜欢的其他地方）制造你自己的独立生态区温室
* 温室可以生长通常无法生长的植物，如向日葵
* 如果温室设计得当，友好的生物可以生成 - 需要史莱姆？建一个沼泽温室吧！
* 生物区内的方块会随时间改变 - 例如，沙漠中的泥土变成沙子，河流中的泥土变成粘土
* 温室可以在多个世界运行
* 易于使用的GUI显示温室配方（例如 **/is greenhouses**）
* 管理员可以完全自定义生物区和配方

## 如何建造一个温室

以下示例适用于BSkyBlock世界。对于AcidIsland，只需使用/ai代替/island。

1. 制作玻璃块并建造一个带有平顶的矩形墙。
2. 在墙壁或屋顶放置一个漏斗。
3. 在墙上放置一扇门，以便你可以进出。
4. 输入 **/island greenhouses** 并阅读你想要的温室的规则。
5. 退出GUI并放置方块、水、岩浆和冰，以便你制造出你想要的生物区。
6. 再次输入 **/island greenhouses** 并点击生物区以创建它。
7. 输入 **/island greenhouses help** 查看其他选项。

### 一旦建成：

* 在温室内的草方块上使用骨粉可以立即生长小植物。
* 或者将骨粉放入漏斗中，让温室自动撒播骨粉。回来后看看长出了什么！
* 将一个（或多个）水桶放入漏斗中，可以在寒冷生物区内下雪。当世界下雨时，雪会下落。每次下雪会消耗一个水桶。
* 友好的特定生物区生物可能会在你的温室中生成 - 通常的规则适用（距离超过24格）。

## 常见问题

* 我可以使用着色玻璃吗？可以，这很漂亮。
* 我可以将我的温室充满水吗？可以。那是一个海洋。
* 那里会生成鱿鱼吗？也许...好吧，如果它是足够大的海洋，它会生成。
* 如果墙全是玻璃，我如何在墙上高处放置门？把它放在漏斗上。
* 我如何在漏斗上放置门？蹲下然后放置。
* 我可以使用金属门吗？可以。
* 我可以使用活板门吗？可以。
* 我可以用这个生长沼泽花吗？可以。制作一个沼泽生物区并使用骨粉。
* 生长植物使用多少骨粉？每成功生长一个植物使用一个。
* 我需要在漏斗中放多少水来让它下雪？每次下雨时使用一个水桶（只有水）。这只在寒冷生物区发生。
* 我可以建造一个下界温室吗？试试看...(实际上，你可能需要权限)
* 我可以在下界建造温室吗？可以。你可以用它们在下界建立殖民地。
* 哪种生物会在生物区中生成？这是你所期待的，冷亚带针叶林中有狼，在平原上有马等等。
* 管理员如何更新下界温室使其有机会生成凋零骷髅？在 `biomes.yml` 中的 `NETHER` 配方中添加该生物——详见下文的[自定义生物生成](#自定义生物生成示例凋零骷髅)。

## 需要的插件

这个版本的温室是BentoBox的一个插件，不能单独运行！

1. BentoBox - 确保你使用的是最新版本！Greenhouses 1.11.0 需要 BentoBox 3.24.0 或更高版本、Paper 1.21.11 至 26.3 以及 Java 25。

## 安装和配置

1. 如果你还没有安装BentoBox，下载并安装BentoBox
2. 下载插件
3. 放入BentoBox插件的addons文件夹中
4. 重启你的服务器
5. 插件将创建一个名为greenhouses的数据文件夹。打开那个文件夹。
6. 检查**config.yml**并根据你的需求进行编辑，注意世界名称列表。
7. 如果你愿意，配置**biomes.yml**（高级）。
8. 在游戏中输入 **/bsbadmin greenhouses reload** 重新加载配置或重启服务器。
9. 完成！

Greenhouses 1.11.0 新增了一个 `config.yml` 选项：

??? note "sample-ticks"
    在 Greenhouses 1.11.0 中添加。每隔多少服务器 tick（20 = 1 秒）在每个温室中随机挑选一些位置，用于生物生成和方块转化。数值越低，工作负载分布得越均匀。它不会改变整体速率——整体速率由 `mobtick` 和 `blocktick` 设定：平均而言，每个位置在每个 `mobtick` 或 `blocktick` 周期内仍有一次机会，因此生物会陆续出现，而不是一下子全部出现。

    默认值：`20`

要制作你的第一个温室，建造一个玻璃盒子并输入 **/is greenhouses make** 看看你会得到什么类型的温室。输入 **/is greenhouses** 查看配方。

## 升级

阅读文件发布说明以了解更改和如何升级的说明。

## 玩家指令

添加到/island, /ai。指令标签为 `greenhouse`，别名为 `gh` 和 `greenhouses`。

* **greenhouses** - 打开配方 GUI；点击一个配方会尝试制作该类型的温室
* **greenhouses help** - 列出这些指令
* **greenhouses make [recipe]**: 尝试制作一个温室，可以自动寻找第一个有效的配方，也可以使用指定名称的配方
* **greenhouses remove**: 如果你是所有者，移除你站立处的温室

!!! warning "`list` 和 `recipe` 已在 1.10.0 中移除"
    这两个玩家指令虽然被写进了文档，但从未真正注册过——它们是无法访问的空壳，调用它们只会得到"未知指令"的错误。它们已在 1.10.0 中删除。不带参数的 `/is greenhouses` 会打开配方 GUI，这正是它们本应做的事。

## 管理员指令

!!! new "Greenhouses 1.10.0 新增"
    在 1.10.0 之前，本插件根本没有管理员指令树。一旦某条温室记录出了问题，唯一的办法就是停服并手动编辑数据库。

注册在你的游戏模式管理员指令之下，例如 `/bsbadmin greenhouses` 或 `/acid greenhouses`。指令标签为 `greenhouses`，别名为 `greenhouse` 和 `gh`。

| 指令 | 作用 |
|---|---|
| `list [player] [page]` | 分页列出温室，也可以只列出某个玩家的。加载失败的记录**始终**会一并列出，并附上原因。 |
| `info [id]` | 显示配方、所有者、世界、位置、边界框、面积、原始生物群系、漏斗、损坏状态以及缺失的方块。不带 ID 时，使用你当前所在的温室。 |
| `delete <id>` | 删除一条记录——无论是否加载成功——删除前会要求你确认。 |
| `tp <id>` | 把你传送到温室地面的中心。别名：`teleport`。 |
| `verify [id]` | 按配方重新检查某一个或全部温室，并报告缺少什么。别名：`check`。 |
| `reload` | 重新读取 `biomes.yml`，然后从数据库重新加载温室。 |
| `edit [recipe]` | 打开[配方编辑器](#in-game-recipe-editor)，或某个配方的编辑器。自 1.11.0 起可用。 |
| `build <recipe> [x y z] [WxDxH] [keep\|clear]` | 以你所在位置或指定的地面中心为中心，为某个配方建造一个[测试温室](#test-greenhouse-builder)。自 1.11.0 起可用。 |

- ID 来自 `list`，可以缩短为**只匹配一个**温室的任意前缀。有歧义的前缀会被当作没有匹配，而不是去猜——因为删错温室是无法撤销的。
- 除 `tp`、`edit` 和 `build` 之外的所有指令都可以在服务器控制台中使用。
- 无法加载的温室记录——重叠、配方未知、世界缺失、没有位置——会连同原因一起保留在内存中，而不是被悄悄丢弃。正因如此，它们才能被列出和删除。
- 记录永远不会被自动删除。未经询问就移除玩家的温室，比反复出现的警告更糟糕。

!!! tip "重叠的温室"
    如果两个已持久化的温室互相重叠，启动时会跳过其中一个，并在日志中列出它和与之重叠的记录。用 `/bsbadmin greenhouses list` 查看被跳过的记录及其原因，再用 `/bsbadmin greenhouses delete <id>` 删除你不想保留的那个。无需编辑数据库，也无需重启。

### 管理中心 { #admin-hub }

*在 Greenhouses 1.11.0 中添加。*

不带参数运行 `/bsbadmin greenhouses` 会打开一个 GUI，可从中使用所有管理工具。在控制台中运行该指令仍会显示帮助。管理中心有以下按钮：

- **配方** 打开配方编辑器。
- **温室** 打开温室浏览器。
- **建造测试温室** 在你所站的位置建造一个测试温室。
- **检查所有温室** 重新检查每个温室。
- **重新加载** 在你确认后重新加载。

只有当你拥有对应子指令的权限时，按钮才会出现；按钮运行的就是你手动输入的同一条指令，因此权限检查和提示消息也完全相同。

浏览器会列出所有温室（包括加载失败的温室），并可按所有者筛选。在浏览器中：

| 点击方式 | 作用 |
|---|---|
| 左键点击 | 传送到该温室 |
| 右键点击 | 检查该温室 |
| Shift+点击 | 显示其详细信息 |
| ++q++ | 弹出确认对话框后删除该温室 |

### 游戏内配方编辑器 { #in-game-recipe-editor }

*在 Greenhouses 1.11.0 中添加。*

`/bsbadmin greenhouses edit [recipe]`（权限 `[gamemode].greenhouses.admin.edit`）无需改动 `biomes.yml` 或重启服务器，即可创建、编辑、复制和删除生物区配方。配方的每个部分都可以修改：

- 图标、名称和描述；
- 生物群系、优先级和权限；
- 水、岩浆和冰的覆盖范围；
- [按栖息环境的生物上限](#mob-limits-per-habitat)；
- 必需的方块、植物、生物（包括变体）和方块转化。

方块可以从可搜索的列表中选择，也可以点击你物品栏中的物品来选择。

保存时：

- 先检查配方。
- `biomes.yml` 会备份到 `backups/`，并保留最近 10 个备份。
- 只重写你修改过的配方，注释会保留。
- 温室会立即使用新规则，无需重启。

每位管理员未保存的更改会一直保留，直到其保存或放弃。如果在你编辑期间另一位管理员保存了同一个配方，你可以覆盖对方的版本，或基于对方的版本重新开始。删除配方永远不会删除温室：使用该配方的温室会改为显示为未加载。

### 测试温室建造器 { #test-greenhouse-builder }

*在 Greenhouses 1.11.0 中添加。*

`/bsbadmin greenhouses build <recipe> [x y z] [WxDxH] [keep|clear]`（权限 `[gamemode].greenhouses.admin.build`）为某个配方建造一个可正常运作的温室并将其注册：

- 玻璃墙；
- 在你面朝的一侧放置一扇与该生物群系风格相称的门；
- 一个装满骨粉的屋顶漏斗；
- 配方所需的方块、水和岩浆（海洋温室会被灌满水，下界温室会放入岩浆）。

`keep` 会围绕已有的东西（例如一棵树）建造。`clear` 会在你确认后先清空该空间。支持 `~ ~ ~` 坐标。

## 自定义生物生成（示例：凋零骷髅） { #自定义生物生成示例凋零骷髅 }

温室能生成的每种生物都在 `plugins/BentoBox/addons/Greenhouses/biomes.yml` 中按配方定义，所以添加一种新生物就只是编辑配置。配方的 `mobs:` 部分中的每个条目有这样的格式：

```
ENTITY_TYPE: chance:BLOCK_TO_SPAWN_ON
```

例如，要给下界温室添加凋零骷髅生成机会，找到 `NETHER:` 配方并在其 `mobs:` 部分添加一行：

```yaml
NETHER:
  # ...
  mobs:
    ZOMBIFIED_PIGLIN: 10:NETHERRACK
    PIGLIN: 10:NETHERRACK
    STRIDER: 10:LAVA
    ENDERMAN: 5:NETHERRACK
    WITHER_SKELETON: 5:NETHERRACK
```

这给了凋零骷髅 5% 的概率在每次生成尝试中出现在温室内的地狱岩上。生成所在的方块可以是温室内的任何方块——为了更像堡垒的氛围你可以改用 `WITHER_SKELETON: 10:NETHER_BRICKS`，但这样玩家就需要在温室内放置下界砖才能触发。

使用 **/bsbadmin greenhouses reload**（或你的游戏模式等效指令，如 **/acid greenhouses reload**）或重启服务器来应用改动。现有温室无需重建即可获得新的生物生成。

需要记住的事项：

* **一个配方中所有的生成概率加起来必须是 100 或更少。** 如果新条目使总数超过 100，该生物会被跳过且会在加载时记录错误（`Mob chances add up to > 100% in NETHER biome recipe! Skipping ...`）。在 1.11.0 之前，舍入误差可能导致总和恰好为 100 的概率被拒绝。
* 生成还受限于配方的 `moblimit` 和 `maxmobs` 值，以及 `config.yml` 中的生物 tick 间隔——所以一个低的百分比在实际操作中可能感觉很罕见。
* `ENTITY_TYPE` 必须是有效的 [Bukkit EntityType](https://jd.papermc.io/paper/1.21.5/org/bukkit/entity/EntityType.html) 名称；未知的名称会被跳过并记录警告。
* 在 Minecraft 26.x 上，哞菇的名称是 `MOOSHROOM`，而不是 `MUSHROOM_COW`。请将 `biomes.yml` 中所有 `MUSHROOM_COW` 条目改名。
* 自 1.11.0 起，也可以在游戏内用[配方编辑器](#in-game-recipe-editor)进行同样的修改。

### 按栖息环境的生物上限 { #mob-limits-per-habitat }

*在 Greenhouses 1.11.0 中添加。*

`moblimit` 是每只生物所需的地面方块数，对深海、岩浆湖或飞行生物来说，这并不是合适的衡量标准。配方可以在 `biomes.yml` 中另外设置三个可选键。每个键分别统计各自的生物，其值都是每只生物所需的方块数：

| 键 | 统计的生物 | 衡量所依据的空间 |
|---|---|---|
| `moblimit-water` | 在水上生成的生物 | 水方块 |
| `moblimit-lava` | 在岩浆上生成的生物 | 岩浆方块 |
| `moblimit-air` | 飞行生物：悦灵、蝙蝠、蜜蜂、恶魂、鹦鹉、幻翼和恼鬼 | 温室的内部体积 |

地面生物仍使用 `moblimit`，`maxmobs` 仍限制总数。如果没有设置某项上限，相应的生物会与地面生物共用 `moblimit`，因此没有这些新键的配方行为与以前相同。内置的 `biomes.yml` 设置了：

- `moblimit-water`：海滩、积雪海滩和海洋（9），以及河流（1）；
- `moblimit-lava`：下界和诡异森林（9）；
- `moblimit-air`：丛林和溶洞（27），以及灵魂沙峡谷（64）。

自 1.11.0 起，`moblimit` 的计算是精确的：81 个方块、每只生物 9 个方块，得到 9 只生物，而不是 10 只。同样自 1.11.0 起，温室内的自然（原版）生成也会被取消，因此只会出现配方自己的生物。

## 权限 { #permissions }

权限的完整列表在[这里](Permissions)。

在biomes.yml中可以添加使用特定生物区的权限。

例如，下界生物区的权限是 **greenhouses.biome.nether** 并在这里设置：

 NETHER:

    permission: greenhouses.biome.nether

权限可以是你喜欢的任何内容，例如，一个等级权限，**myserver.VIP**。

### 通用权限是：

  greenhouses.player:

     description: 授予玩家指令的访问权限
     default: true

  greenhouses.admin:

     description: 授予管理员指令的访问权限
     default: op

自 1.10.0 起，每个管理员子指令还各有自己的权限节点——`greenhouses.admin.list`、`.info`、`.delete`、`.tp`、`.verify` 和 `.reload`——全部默认为 `op`。1.11.0 添加了 `.edit` 和 `.build`。管理员无需做任何事，但如果你是通过权限插件来授予管理员权限的，就需要把它们加上。在该版本之前，这些节点在 `addon.yml` 中完全缺失，这也正是除了 OP 之外什么都用不了的原因。

## 翻译

{{ translations("Greenhouses") }}

!!! warning "v1.11.0 新内容 — 管理中心和配方编辑器；需要 BentoBox 3.24.0"
    **发布于：** 2026-11-22

    兼容性：BentoBox API 3.24.0 或更高版本 · Paper 1.21.11 至 26.3 · Java 25。

    - 🔡 **管理中心。** `/[admin_command] greenhouses` 现在会打开一个 GUI，可从中使用所有管理工具：编辑配方、浏览温室、建造测试温室、检查全部温室以及重新加载。详见[管理中心](#admin-hub)。
    - 🔡 **游戏内配方编辑器。** `/[admin_command] greenhouses edit [recipe]` 无需改动 `biomes.yml` 或重启，即可创建、编辑、复制和删除生物区配方。详见[游戏内配方编辑器](#in-game-recipe-editor)。
    - 🔡 **测试温室建造器。** `/[admin_command] greenhouses build <recipe>` 可在你所站的位置为任意配方建造一个可正常运作的温室。详见[测试温室建造器](#test-greenhouse-builder)。
    - ⚙️ **更平滑的生物生成和方块转化。** 两者过去都会在同一个 tick 内扫描每个温室的每个方块，因此温室会一下子被生物填到上限。现在它们每隔 `sample-ticks` 个 tick（新设置，默认 `20`）对随机抽取的位置运行。平均速率不变，并且生物数量按每个温室自身的区域统计，而不是在整个世界范围内统计。
    - **水、岩浆和空中生物分别设上限。** 新的可选配方键 `moblimit-water`、`moblimit-lava` 和 `moblimit-air`。详见[按栖息环境的生物上限](#mob-limits-per-habitat)。
    - 🐛 **阻止温室内的自然生成。** 之前的生成防护只识别墙壁和屋顶方块，导致针叶林温室里满是狼，下界温室里满是恶魂、岩浆怪和僵尸猪灵。
    - 🐛 `moblimit` 会多允许一只生物；植物现在只会放在能存活的地方；总和恰好为 100% 的概率不再被拒绝。
    - 🔡 配方面板中新增**配方描述和 MiniMessage 颜色**，并已翻译成全部 22 种语言。
    - 新增权限 `[gamemode].greenhouses.admin.edit` 和 `[gamemode].greenhouses.admin.build`，均默认为 `op`。

    🔺 **需要 BentoBox 3.24.0 和 Paper 1.21.11+。** 配方编辑器和管理中心使用 BentoBox 的新对话框和分页面板 API，因此旧版 BentoBox 会拒绝加载此附属。请先更新 BentoBox。

    🔺 **`biomes.yml` 不会被替换。** 内置的文件已有改动：配方增加了描述和 MiniMessage 名称，设置了按栖息环境的生物上限，`MUSHROOM_COW` 改为 `MOOSHROOM`。你现有的文件会原样保留。要使用新的默认值，请自行合并这些改动，或将你的文件改名以生成一个新文件。无论哪种方式，都要把所有 `MUSHROOM_COW` 条目改名为 `MOOSHROOM`，因为旧名称在 26.x 上无效。

    🔡 **语言文件。** 要获得全部文本修正，请在启动服务器前删除 `plugins/BentoBox/locales/Greenhouses/`。BentoBox 会把新的语言键添加到现有文件中，但不会更新已更改的键。

    [发布 v1.11.0](https://github.com/BentoBoxWorld/Greenhouses/releases/tag/1.11.0)

??? warning "v1.10.2 新内容 — 修复 Paper 26.2 上的崩溃"
    **发布于：** 2026-09-06

    兼容性：BentoBox API 2.7.1 · Minecraft 1.21.5+ · Java 21。无配置或本地化改动。

    - 🐛 **植物生长不再在漏斗骨粉耗尽时崩溃。** 当屋顶漏斗只剩一个骨粉且至少一株植物生长时，Greenhouses 会将剩余部分写回为零数量物品。较旧的服务器会无声地容忍这一点；Paper 26.2 在每个植物 tick 时从 `EcoSystemManager.setBoneMeal` 抛出 `IllegalArgumentException: amount must be greater than 0` 异常并中止该温室的生长过程。最后一个骨粉现在只是被简单移除。

    🔺 **如果你在使用 Paper 26.2 或更新版本，强烈建议更新此版本。** 每个漏斗耗尽的温室否则会在每个 tick 记录此错误并停止植物生长，直到再次添加骨粉。

    [发布 v1.10.2](https://github.com/BentoBoxWorld/Greenhouses/releases/tag/1.10.2)

??? warning "v1.10.1 新内容 — 如果运行 Limits 请重新计算"
    **发布于：** 2026-09-01

    兼容性：BentoBox API 2.7.1 · Minecraft 1.21.5+ · Java 21。无配置或本地化改动。

    - 🐛 **Greenhouses 不再让生物绕过 Limits 附属。** 当 Limits 在达到实体限制时取消了一次生成，Greenhouses 会继续处理这个从未生成的实体，运行其"这个生物是否能适应玻璃内？"检查，当它不适应时（幽灵有 4×4×4，常常不适应），调用其 `remove()`。Paper 会为这个操作触发 `EntityRemoveEvent`，尽管该生物从未进入世界，而 Limits 会把它算作真实移除，所以其计数器向下倒数，下一次生成被允许——报告的案例是幽灵在 4/3。已取消的生成现在会被完全忽略。Limits 1.30.1 包含了对应的加强。

    🔺 **如果你看到了这个，** 受影响岛屿的 Limits 计数器仍然是错误的，直到它被重建。在更新后让玩家运行一次 `/[player_command] limits recount`（或运行管理员命令 `/[admin_command] limits calc <玩家>`）。

    [发布 v1.10.1](https://github.com/BentoBoxWorld/Greenhouses/releases/tag/1.10.1)

??? note "v1.10.0 新内容 — 管理员指令"
    **发布于：** 2026-07-26

    Greenhouses 终于有了管理员指令树。兼容性：BentoBox API 2.7.1 · Minecraft 1.21.5+ · Java 21。

    - 🛠️ **管理员指令。** `list`、`info`、`delete`、`tp`、`verify` 和 `reload`，注册在你的游戏模式管理员指令之下（例如 `/bsbadmin greenhouses`）。详见上面的"管理员指令"章节。无法加载的温室记录——重叠、配方未知、世界缺失、没有位置——现在会连同原因一起保留在内存中，而不是被悄悄丢弃，正因如此它们才能被显示和删除。记录仍然永远不会被自动删除。
    - ⚙️ **新增权限。** 六个子指令各有自己的 `greenhouses.admin.*` 节点，全部默认为 `op`。在本版本之前，它们在 `addon.yml` 中完全缺失，这正是除了 OP 之外什么都用不了的原因。
    - 🐛 **检查配方已不存在的温室时不再抛出 NPE。** 当数据库记录指向一个不在 `biomes.yml` 中的配方时，检查现在会报告 `FAIL_UNKNOWN_RECIPE`。
    - 🐛 **`getFloorHeight` 在处理没有位置的记录时不再抛异常**——而这类记录恰恰最可能是坏掉的。它现在会回退到边界框。
    - 🔺 **降雪现在会汇报所有扫描过的列的成功情况，** 而不只是最后一列。`SnowTracker` 在每一列都会覆盖自己的结果，因此一个在九十列中都造出了雪、只有最后一列没造出雪的温室会被判定为失败——而这个值决定了是否从漏斗中消耗水。
    - 🧹 解决了全部 68 个未处理的 SonarCloud 问题，将五个方法重构到认知复杂度阈值以下，移除了死代码，测试套件从 177 个增加到 224 个。

    🔡 **征集翻译。** 管理员指令新增了 `greenhouses.commands.admin.*` 下的消息，目前只有英文。其余 24 个本地化文件在翻译完成前会回退显示键名。

    🔺 **删除了三个玩家指令——但它们本来就都不能用。** `InfoCommand`、`ListCommand` 和 `RecipeCommand` 都是未注册的空壳，方法体只有占位内容。`InfoCommand` 甚至把自己声明在 `make` 标签下，一旦有人真的启用它，就会和真正的 make 指令冲突。本页此前把 `greenhouses list` 和 `greenhouses recipe` 列为可用的玩家指令；它们并不可用，现已更正。不带参数的 `/is greenhouses` 仍然会打开配方 GUI。

    [发布 v1.10.0](https://github.com/BentoBoxWorld/Greenhouses/releases/tag/1.10.0)

??? warning "v1.9.6 新内容 — 重叠的温室现在可以诊断了"
    **发布于：** 2026-07-25

    - 🐛 **重叠的温室现在可以诊断了。** 如果两个已持久化的温室互相重叠，启动时会跳过其中一个——但过去的日志只会写一句 `Greenhouse overlaps with another greenhouse. Skipping...`，让你无从下手，而且每次重启都会重复出现。现在这条警告会列出**两条**记录的 `uniqueId`、配方、所有者、世界、位置和边界框，并告诉你该如何修复。汇总行会显示 `Loaded 63 greenhouses out of 65 in the database.`，并在末尾统计跳过了多少条。
    - 🔺 **温室的加载顺序现在是确定的。** 过去温室按数据库返回的任意顺序加载，因此两条重叠记录中谁胜出并不确定，而且可能在重启之间来回变化。现在它们会先按 `uniqueId` 排序再加载，因此在你移除其中一条记录之前，结果是稳定的。
    - ⚙️ **移除了 `biomes.yml` 中 `OCEAN` 配方里重复的 `SQUID` 条目。** 它被列了两次，会在较新的服务端版本上触发 SnakeYAML 的重复键警告。YAML 保留最后一次出现的值，因此实际生效的值（`20:WATER`）不变，怪物生成也不受影响。

    ⚙️ **`biomes.yml` 的这项修复不会自动应用。** 你的服务器磁盘上已有自己的 `biomes.yml`，插件不会覆盖它。如果你看到关于 `SQUID` 的 SnakeYAML 重复键警告，请打开 `plugins/BentoBox/addons/Greenhouses/biomes.yml`，找到 `OCEAN` 小节，删除两行 `SQUID:` 中的第一行。全新安装会自动得到修正后的文件。

    🔺 **本版本只报告重叠的温室，并不会移除它们。** 被跳过的记录会被有意保留在数据库中——悄悄删除玩家的温室比反复出现的警告更糟糕。在 1.9.6 中，你需要根据日志中打印的 `uniqueId` 自行移除过期记录；1.10.0 新增的管理员指令可以在游戏内完成这件事。

    [发布 v1.9.6](https://github.com/BentoBoxWorld/Greenhouses/releases/tag/1.9.6)

??? note "v1.9.5 更新内容"
    **发布日期：** 2026-06-03

    这是一个专注于植物生长和配方 GUI 的错误修复版本。完整说明见 [Release v1.9.5](https://github.com/BentoBoxWorld/Greenhouses/releases/tag/1.9.5)。

    - 🔡 修复了 GUI 颜色渗漏问题：下界配方条目的红色颜色代码未被重置，导致配方面板其余文本变红。高大/双格植物（向日葵、丁香、玫瑰丛等）现在能正确放置其上半部分。
    - 发光地衣现在可以在陆地方块上生长（例如 `GLOW_LICHEN: 10:STONE`），而不再被视为仅限水下。
    - `maxmobs` 限制现在在每次生成时都会强制执行，因此温室不会再超过配置的生物上限。