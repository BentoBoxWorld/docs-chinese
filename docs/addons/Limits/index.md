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

* worlds

* entitylimits

### blocklimits

此部分列出了每种方块材料允许的最大方块数。不要使用非方块材料,因为它们无效。限制适用于所有游戏世界。

### worlds

此部分列出了特定世界的方块限制。你必须明确命名世界,例如 AcidIsland_world,然后列出材料和限制。

### entitylimits

此部分列出了玩家岛屿空间(保护区域和岛屿限制)内的默认实体限制。限制为 5 将允许主世界中最多 5 个实体。影响所有类型的生物生成。还包括矿车等实体。请注意,下界和末地不再支持实体限制,因为限制需要加载区块以计数实体,这会导致太多卡顿。

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

岛主可以拥有覆盖默认设置或世界设置的独占权限。格式是:

格式为 `GAME-MODE-NAME.island.limit.MATERIAL.LIMIT`

示例: `bskyblock.island.limit.hopper.10`

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