# 银行

**银行**提供了一个**岛屿银行**功能，以便岛屿成员之间共享资金。

由[tastybento](https://github.com/tastybento)创建和维护。

{{ addon_description("Bank") }}

## 介绍

每个岛屿都有一个银行账户。玩家可以从他们的常规经济账户中存入或取出资金到岛屿账户中，这些资金将被汇总。岛屿所有者可以决定哪个等级的团队成员可以通过设置菜单访问账户。有一个`baltop`指令，玩家可以使用它来查看哪个岛屿的资金最多或最少。

### 特点

* 作为一个岛屿团队保存或花费资金
* 竞争拥有游戏中最高的余额
* 查看账户上所有交易的完整历史

### 要求
**银行**要求服务器上安装了使用Vault的经济系统。理想情况下，经济系统应该是多世界意识的，否则资金可能会在世界和游戏模式之间共享。

## 指令
### 玩家指令

默认的玩家指令是`bank`，可以在config.yml中更改。例如，你使用岛屿银行时可以执行`/island bank`。

* `bank deposit <amount>` - 存款到岛屿银行
* `bank withdraw <amount>` - 从岛屿银行取款
* `bank balance` - 查看你的岛屿银行余额
* `bank statement` - 查看你的岛屿银行账户上的存款/取款等花哨声明

### 管理员指令

默认的管理员指令是`bank`，可以在config.yml中更改。

管理员指令通过魔法赚钱。
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
    # 用户指令
    user: bank
    # 管理员指令
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
    description: 玩家可以使用bank指令
    default: true
  '[gamemode].bank.user.balance':
    description: 玩家可以使用银行余额指令
    default: true
  '[gamemode].bank.user.deposit':
    description: 玩家可以使用银行存款指令
    default: true
  '[gamemode].bank.user.withdraw':
    description: 玩家可以使用银行取款指令
    default: true


  '[gamemode].bank.user.statement':
    description: 玩家可以使用银行声明指令
    default: true
  '[gamemode].bank.user.baltop':
    description: 玩家可以使用银行baltop指令
    default: true
  '[gamemode].bank.admin':
    description: 玩家可以使用管理员指令
    default: op
  '[gamemode].bank.admin.balance':
    description: 玩家可以使用管理员余额指令
    default: op
  '[gamemode].bank.admin.give':
    description: 玩家可以使用管理员赠送指令
    default: op
  '[gamemode].bank.admin.take':
    description: 玩家可以使用管理员取款指令
    default: op
  '[gamemode].bank.admin.statement':
    description: 玩家可以使用管理员声明指令
    default: op
  '[gamemode].bank.admin.set':
    description: 玩家可以使用管理员设定指令
    default: op

```

## 喜欢这个插件吗？
你可以[赞助](https://github.com/sponsors/tastybento)以获得更多类似的插件并使这个插件变得更好！

## 更新日志

??? note "v1.10.1 新内容"
    **发布于：** 2026-06-21

    bug 修复版本 — 即插即用替换，无配置或本地化更改。

    - 🐛 **经济由附属提供时，银行不再禁用自己。** BentoBox 在早期钩子阶段挂接 Vault，在附属启用之前。如果到那时没有经济插件注册提供者，那个早期钩子就被丢弃 — 所以当经济来自附属时（例如 [InvSwitcher](../InvSwitcher/index.md)，在其自己的 `onEnable()` 中注册按世界 Vault 经济），Bank 找不到 Vault 提供者并以*"需要 Vault"*关闭自己。Bank 现在在放弃之前重试 Vault 钩子，并声明 `InvSwitcher` 为 `softdepend`，以便在存在时优先启用，使加载顺序确定。

    [发布 v1.10.1](https://github.com/BentoBoxWorld/Bank/releases/tag/1.10.1)

??? warning "v1.10.0 新内容 — 破坏性变更（Java 21、BentoBox 3.14.0、MiniMessage）"
    **发布于:** 2026-06-16

    一个现代化版本。Bank 现在面向 **Java 21、Paper 1.21.11 和 BentoBox 3.14.0**，其整个语言文件集已迁移到 BentoBox 的 **MiniMessage** 颜色格式。

    - 🔡 **新占位符 `%Bank_[gamemode]_latest_transaction%`** — 显示用户最近的岛屿银行交易，格式为 `[用户名] [交易类型] $[金额]`（例如 `tastybento Deposited $500.0`）。完全本地化。
    - 🔡 **完整语言覆盖** — Bank 现在覆盖完整的 BentoBox 语言集（23 种语言）。
    - 🔡 🔺 **MiniMessage 语言文件格式。** 所有语言文件从旧版 `&`/`§` 颜色代码转换为 MiniMessage。任何自定义的 Bank 语言文件必须重新用 MiniMessage 语法表达 — 备份它们，删除旧文件使其重新生成，然后重做编辑。
    - 🔺 **平台现代化。** 构建升级到 Java 21 / Paper 1.21.11 / BentoBox 3.14.0；`plugin.yml` `api-version` 升级到 1.21；测试套件迁移到 JUnit 5 + MockBukkit。
    - 🐛 加强了银行交易历史解析防止格式错误的条目并本地化了最近交易占位符回退文本。

    🔺 **更新:** 在安装此版本之前，更新 BentoBox 到 3.14.0 并确保服务器运行 Java 21。首先备份任何自定义语言文件。

    [发布 v1.10.0](https://github.com/BentoBoxWorld/Bank/releases/tag/1.10.0)

??? note "v1.9.1 新内容"
    **发布于:** 2026-03-28

    - **排行榜岛屿名称占位符。** `%Bank_[gamemode]_top_island_<number>%` 现在公开每个排行榜位置的岛屿名称（不只是所有者名称）。岛屿名称与所有者名称和余额一起缓存。
    - ⚙️ 利息复利文档和配置注释已更正 — `compound-periods-per-year` 计算有一个差一错误，导致复利计算略有不正确。通过替换旧 jar 来更新你的配置注释。

    [发布 v1.9.1](https://github.com/BentoBoxWorld/Bank/releases/tag/1.9.1)

## 翻译

{{ translations("Bank") }}