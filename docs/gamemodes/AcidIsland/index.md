# AcidIsland

**AcidIsland** 是一种生存游戏模式，玩家必须在一个被酸海包围的岛屿上生存。

由 [tastybento](https://github.com/tastybento) 创建并维护。

{{ addon_description("AcidIsland") }}

## 故事
你在一个岛上，周围是酸海！如果你喜欢 Skyblock，尝试 AcidIsland，迎接新的挑战吧！

这是 SkyBlock 的一个变种。扩展你的岛屿时，你必须应对酸水，而不是掉落，玩家可以乘船前往彼此的岛屿。

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

## 权限

权限可以在 [这里](Permissions) 找到。

## 命令

命令可以在 [这里](Commands) 找到。

## 占位符

占位符可以在 [这里](Placeholders) 找到。

## 更新日志

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