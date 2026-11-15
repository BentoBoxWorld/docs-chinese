# 玩家指南 { #player-guide }

初来乍到 BentoBox 服务器？这个页面涵盖了基础内容：获取你的岛屿、邀请朋友、保护你的岛屿和四处移动。

!!! info "你的服务器命令"
    这个页面使用 `/island`，这是 SkyBlock（BSkyBlock）的命令。其他游戏模式有他们自己的命令：例如 `/ob` 用于 OneBlock，`/ai` 用于 AcidIsland，`/cave` 用于 CaveBlock。在任何你看到 `/island` 的地方替换为相应的命令。你的服务器也可能关闭了某些功能或更改了默认设置。

## 开始使用 { #get-started }

输入 **`/island`**。

- 如果你还没有岛屿，系统会让你选择一个（如果有选择的话），然后将你传送到该岛屿。
- 如果你已经有了一个，`/island` 会把你送回家。

就这样。其他一切都是可选的。

## 四处移动 { #getting-around }

| 命令 | 作用 |
|---|---|
| `/island` 或 `/island go` | 传送你到你的岛屿 |
| `/island sethome` | 将你的家点设置为你现在所站的位置 |
| `/island sethome <name>` | 设置一个额外的命名家点，如果你的服务器允许超过一个的话 |
| `/island go <name>` | 传送到一个命名的家点 |
| `/island homes` | 列出你的所有家点 |
| `/island spawn` | 传送你到游戏模式的生成点 |
| `/island info` | 显示你所在岛屿的详细信息 |
| `/island near` | 显示附近岛屿的名称 |

## 与朋友一起玩 { #playing-with-friends }

你有两种方式让朋友帮助你。

**作为团队加入。** 团队成员永久共享岛屿。

1. 邀请他们：`/island team invite <name>`。他们必须在线。
2. 他们用 `/island team accept` 接受（或点击**接受**按钮，如果出现弹出窗口）。

!!! warning "加入别人的岛屿"
    当你接受团队邀请时，你通常会**失去自己的岛屿**。系统会先要求你确认。根据服务器的设置，你的物品栏也可能会被清空。

**让他们帮助但不加入。** 他们保留自己的岛屿。

- `/island team trust <name>`：他们可以帮助，直到你用 `/island team untrust <name>` 移除他们。
- `/island team coop <name>`：他们可以帮助，直到你的团队中的每个人都离线。

打开 **`/island team`** 来查看你的团队、邀请玩家和从菜单中管理等级。

| 命令 | 作用 |
|---|---|
| `/island team leave` | 离开团队。所有者不能在没有将岛屿交给别人的情况下离开 |
| `/island team kick <name>` | 移除一个成员 |
| `/island team promote <name>` | 给成员更多权限 |
| `/island team demote <name>` | 取消成员的权限 |
| `/island team setowner <name>` | 将你的岛屿转给另一个成员 |

## 保护你的岛屿 { #keeping-your-island-safe }

你的岛屿受到保护。访客可以四处查看，但不能破坏方块、打开箱子或伤害你的动物，除非你允许。

打开 **`/island settings`** 来选择访客、合作玩家、信任的玩家和团队成员可以做什么。点击一个设置来循环选择允许的等级。

| 命令 | 作用 |
|---|---|
| `/island settings` | 选择每个等级可以做什么 |
| `/island lock` | 锁定你的岛屿，使访客无法进入（再次运行来解锁） |
| `/island expel <name>` | 将访客赶出你的岛屿 |
| `/island ban <name>` | 禁止一个玩家进入你的岛屿 |
| `/island unban <name>` | 解除禁止 |
| `/island banlist` | 查看谁被禁止了 |

有些东西被阻止了，你不确定为什么？消息通常会说明什么不被允许。问你的岛屿所有者，或检查 `/island settings`。

## 你的岛屿 { #your-island }

| 命令 | 作用 |
|---|---|
| `/island setname <name>` | 命名你的岛屿 |
| `/island resetname` | 移除名称 |
| `/island language` | 改变 BentoBox 消息的语言 |
| `/island reset` | 从新的岛屿开始。**你的旧岛屿被删除。** 你的服务器可能限制你有多少次重置 |

## 你的服务器可能有的额外功能 { #extras-your-server-may-have }

服务器通过附属添加功能。一些常见的：

| 命令 | 附属 | 作用 |
|---|---|---|
| `/island level` | [Level](../addons/Level/index.md) | 计算你的岛屿等级 |
| `/island top` | [Level](../addons/Level/index.md) | 显示顶级岛屿 |
| `/island challenges` | [Challenges](../addons/Challenges/index.md) | 打开挑战菜单 |
| `/island warps` | [Warps](../addons/Warps/index.md) | 列出玩家传送点；在告示牌的第一行写 `[Welcome]` 来添加你的 |
| `/island bank` | [Bank](../addons/Bank/index.md) | 你的岛屿的共享银行 |
| `/island fly` | [IslandFly](../addons/IslandFly/index.md) | 在你的岛屿上飞行 |

输入 `/island help` 来查看你可用的每个命令。
