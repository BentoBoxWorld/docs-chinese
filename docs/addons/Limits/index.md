# 限制

**Limits** 允许你在 BSkyBlock 和 AcidIsland 等游戏模式中限制岛屿方块和实体。

此插件旨在帮助限制引起卡顿的实体或方块,例如漏斗。它可用于限制普通方块和实体,但不是所有都可以限制。

由 [tastybento](https://github.com/tastybento) 创建和维护。

{{ addon_description("Limits") }}

## 安装

1. 将 Limits 插件 jar 文件放入 BentoBox 插件的 addons 文件夹

2. 重启服务器

3. 插件将创建一个数据文件夹,里面有一个 config.yml

4. 根据需要编辑 config.yml。

5. 如果进行了更改,请重启服务器

## 命令

有一个用户命令和一个管理员命令,都叫"limits"。管理员可以检查特定岛主的限制。两者都会显示一个带有限制和当前数量的 GUI 面板。

## 设置 - Config.yml

config.yml 有以下部分:

* blocklimits

* blocklimits-nether

* blocklimits-end

* worlds

* entitylimits

* entitylimits-nether

* entitylimits-end

!!! info "按维度限制 (1.28.2+)"
    自 **1.28.2** 起,方块数量、实体数量、限制和偏移量现在会**针对主世界、下界和末地分别独立追踪**。在 `blocklimits` 或 `entitylimits` 中定义的单个限制会分别应用于每个维度。例如 `HOPPER: 10` 允许主世界 10 个、下界 10 个、末地 10 个(整个岛屿共 30 个)漏斗。如需仅覆盖某个维度,请使用可选的 `-nether` / `-end` 部分。

    升级后首次加载时,你现有的单维度数据会自动迁移到**主世界**槽位。磁盘上的格式会发生变化,因此升级前请先备份,并注意升级后不支持降级。

### blocklimits

此部分列出了每种方块材料允许的最大方块数。不要使用非方块材料,因为它们无效。限制会独立应用于每个维度(主世界、下界、末地)。

### blocklimits-nether / blocklimits-end

可选部分,分别用于覆盖下界或末地的 `blocklimits` 默认值。它们在默认配置中是注释掉的;取消注释并添加条目即可设置特定维度的方块限制。

### worlds

此部分列出了特定世界的方块限制。你必须明确命名世界,例如 AcidIsland_world,然后列出材料和限制。世界命名的限制会覆盖上述特定世界的维度默认限制。

### entitylimits

此部分列出了玩家岛屿空间(保护区域和岛屿限制)内的默认实体限制。限制为 5 将允许最多 5 个实体。影响所有类型的生物生成。还包括矿车等实体。自 **1.28.2** 起,实体限制会独立应用于每个维度,因此下界和末地现在会被正确计数和限制(修复了区块卸载时下界/末地计数重置为零的长期问题)。

### entitylimits-nether / entitylimits-end

可选部分,分别用于覆盖下界或末地的 `entitylimits` 默认值。它们在默认配置中是注释掉的;取消注释并添加条目即可设置特定维度的实体限制。

注意:限制 GUI 中只显示前 49 个受限方块和实体。

### entitygrouplimits

!!! note "实验性功能"

以下功能仅在开发版本中可用,你可以在 ci.codemc.org 上找到。

```yaml
entitygrouplimits:
  friendly:
    limit: 2
    entities:
    - COW
    - SHEEP
  monsters:
    limit: 4
    entities:
    - ZOMBIE
    - CREEPER
```

## 权限

岛主可以拥有覆盖默认设置或世界设置的独占权限。支持两种格式:

1. `GAME-MODE-NAME.island.limit.MATERIAL.LIMIT` — 应用于所有维度。

    示例: `bskyblock.island.limit.hopper.10`

2. `GAME-MODE-NAME.island.limit.ENV.MATERIAL.LIMIT` — 仅应用于单个维度,其中 `ENV` 为 `overworld`、`nether` 或 `end` 之一 (1.28.2+)。

    示例: `bskyblock.island.limit.nether.hopper.5`

权限在玩家登录时激活。

使用权限是(在前面加上游戏模式名称,例如 acidisland):

```
GAMEMODE_NAME.limits.player.limits:
  description: 玩家可以使用 limits 命令
  default: true

GAMEMODE_NAME.mod.bypass:
  description: 玩家可以绕过限制 
  default: op

GAMEMODE_NAME.limits.admin.limits:
  description: 玩家可以使用管理员 limits 命令
  default: op
```

完整权限列表在[此处](Permissions)。

## 占位符

{{ placeholders_source(source="Limits") }}

## 更新日志

??? warning "v1.28.0 新内容 — 需要 Java 21"
    **发布于:** 2026-03-xx

    - 🔺 **现在需要 Java 21。** 请在升级前更新服务器的 Java 版本。
    - 修复:潜影箱物品复制漏洞,当物品从受限制的潜影箱移动时可能触发。
    - 修复:铜块在氧化过程中不能正确更新限制计数的问题。

    [在 GitHub 上查看发布记录](https://github.com/BentoBoxWorld/Limits/releases)

??? note "v1.28.1 新内容"
    **发布于:** 2026-03-xx

    - 修复:从旧版本迁移数据库时的迁移错误。
    - 修复:limits GUI 面板中方块限制显示不正确的问题。

    [在 GitHub 上查看发布记录](https://github.com/BentoBoxWorld/Limits/releases)

??? warning "v1.28.2 新内容 — 按维度限制(数据迁移)"
    **发布于:** 2026-06-13

    - 🔺⚙️ **按维度限制。** 方块数量、实体数量、限制和偏移量现在会针对主世界、下界和末地分别独立追踪,修复了区块卸载时下界/末地计数重置为零的长期问题([#43](https://github.com/BentoBoxWorld/Limits/issues/43))。单个 `blocklimits`/`entitylimits` 值现在会分别应用于每个维度,并新增了可选的 `blocklimits-nether`、`blocklimits-end`、`entitylimits-nether` 和 `entitylimits-end` 覆盖部分。
    - 🔺 **数据迁移。** 现有的单维度数据会在首次加载时迁移到**主世界**槽位。磁盘上的格式会发生变化,因此升级前请先备份;升级后不支持降级。
    - 🔺 **按维度权限。** 新的 6 段式格式 `<gamemode>.island.limit.<overworld|nether|end>.<KEY>.<NUMBER>` 可将限制限定到单个维度。现有的 5 段式格式仍然应用于所有维度。
    - 🐛 计数精度修复:床/门重复计数([#86](https://github.com/BentoBoxWorld/Limits/issues/86))、铁傀儡/雪傀儡的方块移除改为以南瓜为基准而非生成方块([#127](https://github.com/BentoBoxWorld/Limits/issues/127))、三个实体计数错误、达到限制时不再消耗刷怪蛋([#134](https://github.com/BentoBoxWorld/Limits/issues/134)),以及重新计数期间的计数泄漏。
    - 🩹 修复了因引用 1.21.9 铜块而在 Minecraft 1.21.8 及更早版本服务器上发生的 `NoSuchFieldError` 崩溃;这些材料现在按名称解析。
    - 🔡 所有捆绑的语言文件已从旧版 `&` 颜色代码转换为 MiniMessage,并在全部 21 种语言中同步了缺失的键。如果你自定义过任何语言字符串,请对照新文件进行检查。

    兼容性: BentoBox API 2.7.1 · Minecraft 1.21.5 – 26.1.2 · Java 21。

    [Release v1.28.2](https://github.com/BentoBoxWorld/Limits/releases/tag/1.28.2)

## 翻译

{{ translations("Limits") }}

## 无法限制的物品

有些物品(目前)无法限制。原因通常是因为有太多方法可以在不被跟踪的情况下移除物品。如果你是程序员并且可以找出如何解决这些问题,请提交 PR!

* 点燃的 TNT

* 唤魔者尖牙

* 羊驼唾沫

* 龙火球

* 区域效果云

* 末影信号

* 小火球

* 火球

* 扔出的经验瓶

* 潜影贝导弹

* 凋灵头颅

* 三叉戟

* 箭

* 光灵箭

* 雪球

* 鸡蛋

* 拴绳

* 末影水晶

* 末影珍珠

* 末影龙

* 物品展示框

* 绘画