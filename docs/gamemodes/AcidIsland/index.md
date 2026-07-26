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

!!! warning "这些是世界生成设置"
    下面三个选项都会在区块生成时固化。BentoBox 不支持在游戏过程中更改它们——已生成的区块会保持原样，因此除非你新开一个世界，否则在旧区块边界处会看到明显的接缝。

??? note "world.default-biome"
    主世界的默认生物群系。`SULFUR_CAVES`（Minecraft 26.2+）会带来酸绿色的水和与之相配的绿色雾气。在更旧的服务端上该生物群系不存在，将改用 `WARM_OCEAN`。

    默认值:`SULFUR_CAVES`（2.0.0 之前为 `WARM_OCEAN`）

??? note "world.sulfur-vent-chance"
    每个区块在海面下方生成硫磺喷口的几率（0–100）。喷口由强效硫磺覆盖在岩浆块之上构成，会冒泡、放气并喷发成间歇泉。它们有四种自然形态——烟囱状、丘状、双生状和尖刺峭壁状——并带有随机变化。需要 Minecraft 26.2 或更高版本；在更旧的服务端上会被忽略。

    默认值:`10`

??? note "world.make-structures"
    在世界中生成原版结构。试炼密室等地下结构会埋在海底之下生成，给玩家一个向下挖掘的理由，也让初始装备中的试炼钥匙有了用武之地。

    默认值:`true`（2.0.0 之前为 `false`）

## 权限

权限可以在 [这里](Permissions) 找到。

## 命令

命令可以在 [这里](Commands) 找到。

## 占位符

占位符可以在 [这里](Placeholders) 找到。

## 更新日志

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