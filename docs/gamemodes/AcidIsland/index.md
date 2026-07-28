# AcidIsland

这是 SkyBlock —— 但这片海洋想杀死你。

**AcidIsland** 把玩家放在一个被酸海包围的岛屿上。掉进去会受伤。这改变了一切：扩展你的岛屿变成了一个谨慎的、高风险的操作。在边缘建造是一场赌博。然而玩家仍然可以乘船访问彼此 —— 如果他们足够勇敢的话。

这是一个熟悉的设定，但有一个转折会让玩家始终保持警觉。

由 [tastybento](https://github.com/tastybento) 创建并维护。

{{ addon_description("AcidIsland") }}

## 安装

0. 安装 BentoBox 并至少运行一次以创建其数据文件夹。
1. 将此 jar 放入 BentoBox 插件的 addons 文件夹中。
2. 重启服务器。
3. 插件将创建世界和数据文件夹，在文件夹内将有一个 config.yml。
4. 停止服务器。
5. 按照您的意愿编辑 config.yml。
6. 如果您进行了会影响它们的更改，请删除默认创建的任何世界。
7. 重启服务器。

## 配置

最新的 `config.yml` 可在[此处](https://github.com/BentoBoxWorld/AcidIsland/blob/develop/src/main/resources/config.yml)查看。

### 净化水

!!! new "AcidIsland 1.22.0 新增"
    酸海依然危险,但现在你可以**净化**它了。喝下一瓶酸水会中毒;喝下一瓶净化水则会恢复生命值。所有水类物品都会带有彩色的附加说明,让你一眼看出手里拿的是什么。净化水的方法有四种 —— 用熔炉烧炼水瓶或水桶、在酿造台上用煤炭酿造水瓶、让钟乳石的水滴落入炼药锅 —— 挑一种你喜欢的就行。

??? note "acid.purified-water.enabled"
    净化水功能的总开关。设为 `false` 时,物品标记、熔炉/酿造拦截以及炼药锅跟踪都会停用。

    默认值:`true`

??? note "acid.purified-water.heal-amount"
    喝下一瓶净化水时恢复的生命值(以半颗心为单位)。`4.0` 即恢复两颗心。

    默认值:`4.0`

??? note "acid.purified-water.bucket-furnace-enabled"
    是否允许在熔炉里烧炼水桶以获得净化水桶。烧炼一桶需要 100 秒(是瓶装的 5 倍)。如果你觉得对服务器平衡来说太容易,可以设为 `false` 关闭此方式。

    默认值:`true`

??? note "acid.purified-water.nether-enabled"
    在本插件管理的下界世界(无论是岛屿型还是原版型)中启用净化水机制。

    默认值:`true`

??? note "acid.purified-water.end-enabled"
    在本插件管理的末地世界(无论是岛屿型还是原版型)中启用净化水机制。

    默认值:`true`

### 硫磺海洋

!!! new "AcidIsland 2.0.0 新增"
    在 Minecraft 26.2 及更高版本上，酸海变成了酸绿色的硫磺水，点缀着不断冒泡的硫磺喷口——它们会向水面释放使人反胃的气体，并周期性地喷发成间歇泉。海底是沙子、沙砾、砂岩和凝灰岩的加权混合，其间夹杂着冒泡的岩浆块；在 26.2+ 上还会散布硫磺和辰砂。同一个 jar 仍然可以在 Minecraft 1.21.x 服务器上运行，此时 26.2 的特性会自动停用，水也会回退为经典的温水海洋。

!!! warning "`default-biome` 和 `make-structures` 是世界生成设置"
    这两个选项会在区块生成时固化。BentoBox 不支持在游戏过程中更改它们——已生成的区块会保持原样，因此除非你新开一个世界，否则在旧区块边界处会看到明显的接缝。`sulfur-vent-chance` 则是例外：自 2.1.0 起它可以在服务器运行时更改，只是仅对此后新生成的区块生效。

??? note "world.default-biome"
    主世界的默认生物群系。`SULFUR_CAVES`（Minecraft 26.2+）会带来酸绿色的水和与之相配的绿色雾气。在更旧的服务端上该生物群系不存在，将改用 `WARM_OCEAN`。

    默认值:`SULFUR_CAVES`（2.0.0 之前为 `WARM_OCEAN`）

??? note "world.sulfur-vent-chance"
    每个区块在海面下方生成硫磺喷口的几率（0–100）。喷口由强效硫磺覆盖在岩浆块之上构成，会冒泡、放气并喷发成间歇泉。它们有四种自然形态——烟囱状、丘状、双生状和尖刺峭壁状——并带有随机变化。需要 Minecraft 26.2 或更高版本；在更旧的服务端上会被忽略。

    自 2.1.0 起，无需重置世界即可更改此项——新的数值仅对此后新生成的区块生效。

    默认值:`10`

??? note "world.make-structures"
    在世界中生成原版结构。试炼密室等地下结构会埋在海底之下生成，给玩家一个向下挖掘的理由，也让初始装备中的试炼钥匙有了用武之地。

    默认值:`true`（2.0.0 之前为 `false`）

### 间歇泉献祭

!!! new "AcidIsland 2.1.0 新增，2.1.1 完善"
    把物品扔进硫磺喷口周围的水里，间歇泉就会把它们当作献祭吞下。当喷口下一次喷发时，它会从水柱中把奖励喷回来——是嬗变过的，而不是原样奉还。你喂给它什么，就决定了产出什么：献祭矿石，它会偏向宝石；献祭木头，它会偏向有生命的东西。此机制需要 Minecraft 26.2 或更高版本（硫磺喷口在该版本才存在），在更旧的服务端上会自动停用。

    自 2.1.1 起，喷口是在**做交易，而不是赌博**：它会算出你的献祭值多少，然后返还价值大致相当的奖励——所以一颗钻石会以宝石的形式回来，而一组圆石则会换回圆石档次的杂物。漂浮在喷口附近的物品会被吸进它的水池，因此投掷不必很准；而且被喂食的喷口会在几秒后被激得提前喷发，让奖励在玩家还在场观看时就落地。

    只有玩家投掷的物品才算数——死亡掉落物、方块掉落物以及漂进水池的怪物掉落物都不会被理会。在喷口水池范围内被酸腐蚀掉的物品会被计为献祭，而不会白白损失；喷出的奖励也带有标记，永远不会被回收成新的献祭。挖掉一个喷口会让它待处理的献祭全部作废。

??? note "world.geyser-offerings.enabled"
    间歇泉献祭机制的总开关。

    默认值:`true`

??? note "world.geyser-offerings.max-rewards"
    单次喷发最多能喷出的奖励数量，无论献祭了多少物品。

    默认值:`12`

??? note "world.geyser-offerings.match-value"
    以价值大致相当的奖励来回应献祭，而不是每个物品随机产出一份奖励。喷口是嬗变而非销毁：喂它一颗钻石，它就欠你一颗钻石的价值；喂它圆石，它就欠你圆石。价值取自 `geyser-values.yml`，该文件可以回退到 Level 附属的方块价值。关闭此项可恢复 2.1.0 中「每个物品掷一次」的产出方式。

    默认值:`true`（2.1.1 新增）

??? note "world.geyser-offerings.exchange-rate"
    在按价值匹配时，喷口返还的献祭价值比例。`1.0` 为公平交易，低于 `1.0` 时喷口会抽成，高于 `1.0` 则献祭本身就有利可图——玩家一定会以此刷收益，因此调高时请谨慎。

    默认值:`1.0`（2.1.1 新增）

??? note "world.geyser-offerings.reward-ceiling"
    单份奖励价值的上限，以本次献祭中最贵物品价值的倍数表示。一组圆石就值一颗绿宝石，而刷石机是无限的，所以没有这个上限，喷口就会变成宝石打印机。在 `geyser-loot.yml` 中通过 `from:` 指定的奖励会忽略此上限——管理员亲自写下的嬗变规则永远被允许。设为 `0` 表示不限制。

    默认值:`8.0`（2.1.1 新增）

??? note "world.geyser-offerings.erupt-on-offering"
    在喷口被喂食后几秒就激它提前喷发，而不必等待原版的喷发周期，好让奖励紧随献祭出现、玩家还在场时就能看到。关闭此项则完全交由原版决定喷发时机——此时献祭会一直保留到喷口自行喷发为止。

    默认值:`true`（2.1.1 新增）

#### geyser-loot.yml

奖励在 `geyser-loot.yml` 中定义，该文件会在首次运行时复制到 `plugins/BentoBox/addons/AcidIsland/`。每个条目要么是一件物品，要么是一条控制台命令：

```yaml
loot:
  - {item: RAW_IRON, weight: 30, channel: mineral, amount: {min: 1, max: 3}}
  - {item: OBSIDIAN, weight: 10, channel: nether, from: [MAGMA_BLOCK, BASALT, LAVA_BUCKET]}
  - {item: MUSIC_DISC_13, weight: 1, from: [BONE, GUNPOWDER]}
  - {command: "give %player% cod 1", weight: 1, value: 4}
```

| 键 | 含义 |
| --- | --- |
| `item` / `command` | 奖励内容。命令以控制台身份执行，`%player%` 会被替换为玩家名。 |
| `weight` | 该条目被抽中的相对几率——数值越高越常见。 |
| `channel` | 可选。取值为 `gems`、`nether`、`mineral`、`forestry`、`husbandry` 之一。献祭会按各频道在本次献祭*价值*中所占的比重，把奖励表拉向对应频道。 |
| `from` | 可选，列出能嬗变成该奖励的材料。献祭其中任意一种，此条目被抽中的几率就会提高到八倍——并且它会忽略 `reward-ceiling`，因此这是让喷口返还远比投入贵重之物的唯一途径。 |
| `amount` | 可选的物品数量，可以是固定值，也可以是 `{min, max}` 区间。默认为 `1`。 |
| `value` | 可选，指定该奖励单份的价值，覆盖材料本身的价值。命令类奖励在未设置此项时价值为零，因此请给付费命令设定价值，否则它们会出现在每一次产出中。 |

!!! warning "从 2.1.0 升级"
    `geyser-loot.yml` 只在缺失时才会写入，因此从 2.1.0 遗留下来的文件不会获得 `from:` 嬗变和 `value:` 字段，所有具名嬗变都不会生效。请删除该文件让它重新生成，然后再把你的修改重新应用上去。

#### geyser-values.yml

`geyser-values.yml` 规定了各种材料对喷口而言值多少。这套数值是任意设定的——只有比例才有意义——它以铁锭 `6`、金锭 `12`、绿宝石 `15`、钻石 `45` 为基准，所以一颗钻石会换回三颗绿宝石，或者一颗绿宝石加两块金锭。

价值按以下顺序解析，命中即止：

1. 文件中的 `values:` 映射
2. 若已安装 Level 附属且 `use-level-addon: true`，则采用该世界下 **Level 附属**的方块价值——这样已经调好 Level 的服务器不必再调一遍。把某个条目从 `values:` 中删掉，即可让该材料交由 Level 处理。
3. `default:` 中的默认价值，用于其他途径都无法识别的材料

价值只按材料计算：附魔、自定义名称以及潜影盒中的内容都不计入，因此装备只值其基础材料的价值。

该文件会在首次运行时自动创建。

## 权限

权限可以在 [这里](Permissions) 找到。

## 命令

命令可以在 [这里](Commands) 找到。

## 占位符

占位符可以在 [这里](Placeholders) 找到。

## API

其他附属可以通过两个事件接入间歇泉献祭机制，二者都是 2.1.0 新增的：

- `GeyserSacrificeEvent` —— 当喷口吞下一份献祭时触发。可取消。
- `GeyserTransmuteEvent` —— 当喷口喷出一份奖励时触发。

## 更新日志

!!! warning "v2.1.1 新内容 — 喷口从赌博改为交易（请删除 `geyser-loot.yml`）"
    **发布于:** 2026-07-26

    2.1.0 带来了间歇泉献祭机制，却没有带来本该配套的经济体系：喷口对扔进去的每个物品只掷一次奖励，于是一组圆石和一颗钻石买到的是同样的机会，而且整个机制自始至终没对玩家说过一句话。2.1.1 把它补完了。兼容性:BentoBox API 3.14.0 · Minecraft 1.21.5 – 26.2（间歇泉相关特性需要 26.2+）· Java 21。

    - ⚙️ 🔺 **按价值匹配。** 新增的 `geyser-values.yml` 规定了各种材料对喷口而言值多少，以铁锭 6、金锭 12、绿宝石 15、钻石 45 为基准。喷口会把喂给它的东西累加起来，不断掷出它还负担得起的奖励，直到这份价值被花完为止。`world.geyser-offerings` 下新增了四个选项:`match-value`、`exchange-rate`、`reward-ceiling` 和 `erupt-on-offering`（详见上文「配置」）。在该文件未作规定之处，价值可以通过 `use-level-addon: true` 回退到 **Level 附属**的方块价值。
    - ⚙️ **具名嬗变。** `geyser-loot.yml` 中的战利品条目现在支持 `from:` 列表，用于指定哪些材料能嬗变成它——岩浆块变黑曜石、铁变金、骨头加火药变唱片。带 `from:` 的条目被抽中的几率是八倍，并且会忽略 `reward-ceiling`，因此正适合放那些原本需要刷怪塔才能拿到的奖励。
    - 🔡 **喷口终于开口说话了。** 新增的 `acidisland.geyser` 语言节添加了献祭、翻涌和产出的提示信息，以及五个奖励频道的显示名称，覆盖全部 24 种语言。它们默认以动作栏消息呈现——删掉 `[actionbar]` 标签即可改为在聊天栏发送。
    - **投掷不必再讲究准头。** 漂浮在喷口附近的物品会被吸进它的水池；被喂食的喷口还会被激得提前几秒喷发，让奖励在玩家还在场观看时就落地。
    - **频道偏向按价值计算。** 献祭仍会把奖励表拉向自己所属的频道，但这份拉力现在按价值而非物品数量加权——一颗钻石和与它等值的一组圆石，导向作用同样有力。

    🔺 **请删除 `geyser-loot.yml`**（位于 `plugins/BentoBox/addons/AcidIsland/`），如果你运行过 2.1.0 的话。该文件只在缺失时才会写入，因此遗留下来的文件不会获得 `from:` 嬗变和 `value:` 字段。请把你的修改重新应用到重新生成的文件上。

    ⚙️ `geyser-values.yml` 会在首次运行时自动创建；四个新增配置项会在启动时加入 `config.yml`，已有设置保持不变。🔡 请重新生成或更新你的语言文件，以获取 `acidisland.geyser` 相关文本。若更喜欢 2.1.0 的产出方式，可以设置 `match-value: false`，其余保持不变。

    [发布 v2.1.1](https://github.com/BentoBoxWorld/AcidIsland/releases/tag/2.1.1)

??? note "v2.1.0 新内容 — 间歇泉献祭"
    **发布于:** 2026-07-26

    AcidIsland 2.1.0 让硫磺喷口从布景变成了一套经济体系。把物品扔进喷口周围的水里，间歇泉就会把它们当作献祭吞下，然后在下一次喷发时回报你，从水柱中喷出嬗变后的奖励。兼容性:BentoBox API 3.14.0 · Minecraft 1.21.11 – 26.2（间歇泉献祭需要 26.2+）· Java 21。

    - ⚙️ **间歇泉献祭。** 漂浮在硫磺喷口周围水池中的物品会伴着「嘶」的一声被当作献祭吞下——水池范围内任何位置都算数，不需要精准投掷。当喷口下一次喷发时，会按献祭的物品数产出对应数量的奖励（有上限，可配置），从水柱中呈放射状喷洒出来。
    - **频道。** 献祭会被归入 **gems**（宝石）、**nether**（下界）、**mineral**（矿物）、**forestry**（林业）和 **husbandry**（畜牧）五个频道，并使奖励表偏向所献祭的那一类。
    - ⚙️ **新增 `geyser-loot.yml`**，首次运行时会复制到附属的数据文件夹：包含带数量区间的加权物品条目，以及支持 `%player%` 替换的控制台命令奖励。
    - ⚙️ **新增 `world.geyser-offerings` 配置节**:`enabled`（默认 `true`）与每次喷发的 `max-rewards`（默认 `12`）。
    - **新增 API 事件**供其他附属使用:`GeyserSacrificeEvent`（可取消）和 `GeyserTransmuteEvent`。
    - **与酸腐蚀物品机制兼容。** 在喷口水池范围内被酸溶解的物品会被计为献祭而不会白白损失，无论你的 `acid.damage.acid.item` 腐蚀时间设为多少——而且喷出的奖励带有标记，永远不会被回收成新的献祭。挖掉的喷口会让待处理的献祭作废；间歇泉不是储物箱。
    - ⚙️ **`world.sulfur-vent-chance` 不再需要重置世界**即可更改。它仅影响此后新生成的区块，因此管理员可以在服务器运行时调整喷口密度。

    **无需重置世界。** 献祭在任何已有的硫磺喷口上都能生效——本次更新不涉及任何世界生成变更。

    [发布 v2.1.0](https://github.com/BentoBoxWorld/AcidIsland/releases/tag/2.1.0)

!!! warning "v2.0.0 新内容 — 硫磺海洋（涉及世界生成变更）"
    **发布于:** 2026-07-20

    AcidIsland 采用 Minecraft 26.2 的硫磺池作为酸性海洋的标志性外观。兼容性:BentoBox API 3.14.0 · Minecraft 1.21.11 – 26.2（硫磺相关特性需要 26.2+）· Java 21。

    - ⚙️ **酸绿色的硫磺水。** 主世界的默认生物群系现在是 `SULFUR_CAVES`,所有水都变成酸绿色,并配有相应的绿色雾气。在低于 26.2 的服务端上该生物群系不存在,世界会回退为 `WARM_OCEAN`。
    - ⚙️ **硫磺喷口与间歇泉。** 强效硫磺喷口会在海面下方生成:冒泡、在水面形成一团使人反胃的气体,并周期性地喷发间歇泉,共有四种自然形态并带有随机变化。每个区块的生成几率由新增的 `world.sulfur-vent-chance` 选项设置(默认 10%);需要 Minecraft 26.2+。
    - **更丰富的海底。** 原本单调的沙质海底现在是沙子、沙砾、砂岩和凝灰岩的加权混合,其间夹杂冒泡的岩浆块,在 26.2+ 上还有硫磺和辰砂。更旧的服务端会用沙砾和凝灰岩代替 26.2 才有的方块。
    - **新增"硫磺泉庇护所"起始岛屿。** 一处坚韧的云杉突岩,配有落叶、眼眸花、凋灵玫瑰、灰化土,下方有一座凝灰岩圣所,还有一只山羊,初始装备与樱花林岛屿相同。完全使用 1.21 即可支持的方块搭建。
    - ⚙️ **结构默认开启。** `world.make-structures` 现在默认为 `true`,因此试炼密室等地下结构会埋在海底之下生成。

    🔺 **世界生成变更。** 新的水生物群系、喷口、海底和结构都在区块生成时固化。已有世界中已探索的区块会保持原样;若要体验完整的 2.0.0,请新开一个世界,否则请预期在旧区块边界处出现明显接缝。

    ⚙️ **现有配置不会被修改。** 你的 `config.yml` 会保留已保存的值。若想在现有安装上采用新默认值,请设置 `default-biome: SULFUR_CAVES` 和 `make-structures: true`,并添加 `sulfur-vent-chance: 10`,或者删除配置让它重新生成。

    🔺 **现有安装不会自动获得新蓝图。** BentoBox 只会在蓝图文件夹*缺失*时才解压内置蓝图。若要在现有安装上看到新的岛屿选项,请从 jar 中把 `sulfur-spring.blueprint` 和 `sulfur_spring.json` 复制到 `plugins/BentoBox/addons/AcidIsland/blueprints/`。

    [发布 v2.0.0](https://github.com/BentoBoxWorld/AcidIsland/releases/tag/2.0.0)

??? note "v1.22.1 新内容"
    **发布于:** 2026-06-28

    维护版本。无需任何配置或本地化更改。

    - 🐛 **修复了 `addon.yml` 中重复的权限键。** 有几个命令本来就共用同一个权限节点——`/ai ban`、`/ai unban` 和 `/ai banlist` 都使用 `acidisland.island.ban`——但它们被写成了键名相同的多个 YAML 条目。YAML 只保留重复键中的最后一个,因此靠前的权限描述被悄悄丢弃,服务器每次加载都会记录 `duplicate keys found`。现在每个共用节点合并为一个条目并附带综合描述,启动警告也随之消失。
    - 在发布的游戏版本列表中加入了 Minecraft 26.2(并补上了 26.1.2)。

    [发布 v1.22.1](https://github.com/BentoBoxWorld/AcidIsland/releases/tag/1.22.1)

??? note "v1.22.0 新内容 — 净化水机制"
    **发布于:** 2026-04-15

    酸水现在可以被净化,玩家终于可以安全地饮用、灌溉和装瓶了。所有水类物品都带有彩色说明 —— <span style="color:red">Acid Water</span> 或 <span style="color:green">Purified Water</span>,炼药锅也会在服务器重启后记住自己的水状态。

    - ⚙️ **新增净化水** — 四种净化方式:用熔炉烧炼水瓶(10 秒)、用煤炭在酿造台酿造水瓶、用熔炉烧炼水桶(100 秒,可开关)、以及让钟乳石的水滴落入炼药锅。
    - ⚙️ **饮用效果** — 酸水瓶施加原版中毒效果;净化水瓶恢复生命值(数值可通过 `acid.purified-water.heal-amount` 配置)。
    - ⚙️ 新增配置块 `acid.purified-water.*`(详见上方的配置章节)。包含总开关、恢复量、水桶熔炉烧炼开关以及下界/末地的分维度开关。
    - 🔡 在 `acidisland.purified-water.*` 下新增两个语言键,并已同步至全部 18 种语言。
    - **新增事件** — 新增 `ItemFillWithAcidEvent` 与 `PlayerDrinkPurifiedWaterEvent`,方便其他插件挂接。
    - 代码整理:使用模式匹配 `instanceof`、`Math.clamp`,降低 `onPlayerMove`、`getWorld`、`findEntities`、`makeNetherRoof` 的复杂度,并对测试代码做了现代化改写。

    [发布 v1.22.0](https://github.com/BentoBoxWorld/AcidIsland/releases/tag/1.22.0)

??? warning "v1.21.0 新内容 — 需要 BentoBox 3.14.0,语言文件迁移"
    **发布于:** 2026-04-12

    - **樱花林起始岛屿。** 为 Minecraft 1.21+ 服务器新增以樱花林生物群系为主题的起始岛屿蓝图。要激活它,请删除 `BentoBox/addons/AcidIsland/blueprints/`,以便在下次启动时重新生成蓝图。
    - 🔺 **现在需要 BentoBox API 3.14.0。** 安装此版本前请更新 BentoBox。
    - 🔡 **全部 24 个语言文件从 `&` 代码迁移至 MiniMessage。** 删除 `BentoBox/locales/AcidIsland/` 并重启以重新生成。自定义文件中任何剩余的 `&` 代码将显示为纯文本。
    - 错误修复:EssentialsX 启动时加载失败时,EssentialsX 上帝模式检查中的 NullPointerException。
    - 迁移过程中修复了几个预先存在的语言文件错误。

    [发布 v1.21.0](https://github.com/BentoBoxWorld/AcidIsland/releases/tag/1.21.0)

## 翻译

{{ translations("AcidIsland") }}