# 银行

**银行**提供了一个**岛屿银行**功能，以便岛屿成员之间共享资金。

由[tastybento](https://github.com/tastybento)创建和维护。

{{ addon_description("Bank") }}

## 介绍

每个岛屿都有一个银行账户。玩家可以从他们的常规经济账户中存入或取出资金到岛屿账户中，这些资金将被汇总。岛屿所有者可以决定哪个等级的团队成员可以通过设置菜单访问账户。有一个`baltop`命令，玩家可以使用它来查看哪个岛屿的资金最多或最少。

### 特点

* 作为一个岛屿团队保存或花费资金
* 竞争拥有游戏中最高的余额
* 查看账户上所有交易的完整历史

### 要求
**银行**要求服务器上安装了使用Vault的经济系统。理想情况下，经济系统应该是多世界意识的，否则资金可能会在世界和游戏模式之间共享。

## 命令
### 玩家命令

默认的玩家命令是`bank`，可以在config.yml中更改。例如，你使用岛屿银行时可以执行`/island bank`。

* `bank deposit <amount>` - 存款到岛屿银行
* `bank withdraw <amount>` - 从岛屿银行取款
* `bank balance` - 查看你的岛屿银行余额
* `bank statement` - 查看你的岛屿银行账户上的存款/取款等花哨声明

### 管理员命令

默认的管理员命令是`bank`，可以在config.yml中更改。

管理员命令通过魔法赚钱。
* `bank give <player> <amount>` - 存款到玩家的岛屿银行
* `bank take <player> <amount>` - 从玩家的岛屿银行取款
* `bank set <player> <amount>` - 将玩家的岛屿银行余额设定为某个金额
* `bank balance <player>` - 查看玩家的岛屿银行余额
* `bank statement <player>` - 查看玩家的岛屿银行账户上的存款/取款等花哨声明

## 占位符

可以在[这里](Placeholders)找到占位符。

## 配置

```
bank:
  # 可以使用银行的BentoBox游戏模式
  game-modes:
  - BSkyBlock
  - AOneBlock
  - AcidIsland
  - SkyGrid
  - CaveBlock
  commands:
    # 用户命令
    user: bank
    # 管理员命令
    admin: bank
  placeholders:
    # 将会注册多少个等级到占位符API。
    # 每个等级有两个占位符：
    # %Bank_[gamemode]_top_name_1% 和岛屿等级：%Bank_[gamemode]_top_value_1%
    # [gamemode] 是bskyblock, acidisland等。
    number-of-ranks: 10
```

## 权限

```
permissions:
  '[gamemode].bank.user':
    description: 玩家可以使用bank命令
    default: true
  '[gamemode].bank.user.balance':
    description: 玩家可以使用银行余额命令
    default: true
  '[gamemode].bank.user.deposit':
    description: 玩家可以使用银行存款命令
    default: true
  '[gamemode].bank.user.withdraw':
    description: 玩家可以使用银行取款命令
    default: true


  '[gamemode].bank.user.statement':
    description: 玩家可以使用银行声明命令
    default: true
  '[gamemode].bank.user.baltop':
    description: 玩家可以使用银行baltop命令
    default: true
  '[gamemode].bank.admin':
    description: 玩家可以使用管理员命令
    default: op
  '[gamemode].bank.admin.balance':
    description: 玩家可以使用管理员余额命令
    default: op
  '[gamemode].bank.admin.give':
    description: 玩家可以使用管理员赠送命令
    default: op
  '[gamemode].bank.admin.take':
    description: 玩家可以使用管理员取款命令
    default: op
  '[gamemode].bank.admin.statement':
    description: 玩家可以使用管理员声明命令
    default: op
  '[gamemode].bank.admin.set':
    description: 玩家可以使用管理员设定命令
    default: op

```

## 喜欢这个插件吗？
你可以[赞助](https://github.com/sponsors/tastybento)以获得更多类似的插件并使这个插件变得更好！

## 更新日志

??? note "v1.9.1 新内容"
    **发布于:** 2026-03-xx

    - **前排名岛屿名称占位符。** 新增 `%Bank_[gamemode]_top_name_1%` 等占位符,用于显示顶级岛屿名称(而不仅仅是玩家名称)。
    - 修复:配置文件中的利息计算选项在某些设置下无法正确应用。

    [在 GitHub 上查看发布记录](https://github.com/BentoBoxWorld/Bank/releases)

## 翻译

{{ translations("Bank") }}