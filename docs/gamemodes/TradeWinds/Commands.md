# TradeWinds 指令

玩家指令是 **`/tw`**（别名 `/tradewinds`）；管理员指令是 **`/twadmin`**。运行裸 `/tw` 执行默认操作 `go`。

## 玩家指令

| 指令 | 描述 | 权限 |
|------|------|------|
| `/tw go`（别名：`spawn`、`sail`） | 启航——进入你离开它的海洋。在你自己的岛屿上：踩步你的家点。在海上：切换返航（白天方向，夜间星星下的精确距离）。永远不是跨海骑行。 | `tradewinds.island.spawn` |
| `/tw chart` | 提起海图罗盘——已探图岛屿、码头、你的船和家的全息标记。`/tw chart list` 打印文字版本。 | `tradewinds.island.chart` |
| `/tw starchart` | 接收已探图岛屿的星图地图。 | `tradewinds.island.starchart` |
| `/tw rank`（别名：`ranks`） | 你的航海家等级和前十名水手按岛屿已探。 | `tradewinds.island.rank` |
| `/tw claim` | 声称你站着的野生小岛作为你的岛屿（等级和价格门槛适用）。 | `tradewinds.island.claim` |
| `/tw sethome` | 设置你的家点——仅当站在你自己的岛屿内时。 | `tradewinds.island.sethome` |
| `/tw home` | 踩步你的家点——仅当已站在你自己的岛屿内时。 | `tradewinds.island.home` |
| `/tw unclaim` | 将你声称的小岛回归野生。仅所有者，团队必须先清空，没有退款；每块都以被留下的状态保持。 | `tradewinds.island.unclaim` |
| `/tw fine` | 在港口结清你的犯罪记录（返回你为干净）。 | `tradewinds.island.fine` |
| `/tw restart` | 重启你的贸易生涯（受限使用，配置上限）。 | `tradewinds.island.restart` |
| `/tw info` | 关于你所在岛屿的信息。 | `tradewinds.island.info` |
| `/tw settings` | 查看岛屿设置。 | `tradewinds.island.settings` |
| `/tw language` | 选择你的语言。 | `tradewinds.island.language` |
| `/tw warp` | 从岛屿水域的任何地方打开传送对话。**默认操作员**——预期的路径是划行到岛屿边界，它自动提供对话。 | `tradewinds.island.warp` |
| `/tw trade` | 从岛屿保护范围内的任何地方打开岛屿市场。**默认操作员**——预期的路径是停靠并右键商人。 | `tradewinds.island.trade` |
| `/tw prices` | 你的价格日志——你呼叫过的港口支付什么及多久前。仅当 `economy.price-logbook-enabled` 功能标志开启时登记（默认关闭）。 | `tradewinds.island.prices` |

## 管理员指令

`/twadmin` 携带所有标准 BentoBox 管理指令（`version`、`tp`、`getrank`、`setrank`、蓝图等），加上 TradeWinds 特定集合：

| 指令 | 描述 | 权限 |
|------|------|------|
| `/twadmin islands` | 列出最近的贸易岛屿及其类型、科技等级、等级和距离。 | `tradewinds.admin.islands` |
| `/twadmin tpisland <#>` | 从岛屿列表传送到贸易岛屿。 | `tradewinds.admin.tpisland` |
| `/twadmin boat <player>` | 检查玩家的船舶记录直接从数据库：材料、货物、燃料、最后看见位置，以及船体是否真正加载在那里或在某人的包中。 | `tradewinds.admin.boat` |
| `/twadmin boat <player> restore` | 重新生成一艘丢失的活跃船作为玩家包中的一个盖章物品，货物记录完整。在真实船体被加载或携带时拒绝。 | `tradewinds.admin.boat` |
| `/twadmin rank <player>` | 显示玩家的航海家等级：有效岛屿、真实已探计数和调整。 | `tradewinds.admin.rank` |
| `/twadmin rank <player> <rank\|islands\|reset>` | 按等级名或岛屿计数设置玩家等级，或重置调整。真实绘制继续在上面计数。 | `tradewinds.admin.rank` |
| `/twadmin customs` | 显示海关对你所在位置的看法：船上走私品、扫描几率、巡逻强度。 | `tradewinds.admin.customs` |
| `/twadmin priceaudit` | 审计价格覆盖——什么可以出售，什么是战利品，什么无法出售——并将完整报告写入 `price-audit.txt`。 | `tradewinds.admin.priceaudit` |
| `/twadmin warpfail <player>` | 操纵玩家的下一次传送失败进入间隙地（再次运行以清除）。按需测试传送误差路径。 | `tradewinds.admin.warpfail` |
| `/twadmin reflag` | 重新应用安全等级标志到所有贸易岛屿。 | `tradewinds.admin.reflag` |
