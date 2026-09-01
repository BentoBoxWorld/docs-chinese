# TradeWinds 权限

默认值被选择为使虚拟安装以预期的游戏进行，不需要权限插件：水手需要的一切都是 `true`，跳过航行的捷径是 `op`，真正的门槛（声称等级、声称价格）在 `config.yml` 中而不是权限中。

## 玩家权限

| 权限 | 描述 | 默认 |
|------|------|------|
| `tradewinds.island` | 允许使用 TradeWinds 玩家指令 | `true` |
| `tradewinds.island.spawn` | 允许 `/tw go`——通往海洋的大门，以及在规则内回家的方式。从外部它将玩家返回到他们离开的水域；在他们自己的岛屿上它踩步他们的家点；在海上任何其他地方它告诉他们方向和距离回家，永远不是骑行。 | `true` |
| `tradewinds.island.chart` | 允许查看海图（浮动全息图、岸上列表） | `true` |
| `tradewinds.island.starchart` | 允许接收星图地图 | `true` |
| `tradewinds.island.rank` | 允许查看航海家等级和已探岛屿前十 | `true` |
| `tradewinds.island.claim` | 允许声称野生小岛作为玩家岛屿。真正的门槛在配置中——航海家等级（`claims.minimum-rank`）和价格（`claims.price`）——所以这默认保持开启；关闭它来彻底禁用声称。 | `true` |
| `tradewinds.island.sethome` | 允许在你自己的岛屿上设置家点——仅当站在其保护范围内时（所有者或团队成员）。 | `true` |
| `tradewinds.island.home` | 允许踩步你的家点——仅当已站在你自己的岛屿内时，所以它是周围的便利，永远不是跨海回家的方式。 | `true` |
| `tradewinds.island.unclaim` | 允许所有者将声称的小岛回归野生。需要团队先清空；没有退款；每块都以被留下的状态保持。 | `true` |
| `tradewinds.island.fine` | 允许在港口结清犯罪记录。默认开启——一个无法支付声誉的玩家没有办法回头除了等待。 | `true` |
| `tradewinds.island.restart` | 允许重启贸易生涯（配置上限） | `true` |
| `tradewinds.island.prices` | 允许商人日志——你呼叫过的港口支付什么及多久前。价格仅通过访问市场或购买港口报告进入它，所以这是将玩家自己的知识读回给他们。 | `true` |
| `tradewinds.island.info` | 允许使用岛屿信息指令 | `true` |
| `tradewinds.island.settings` | 允许查看岛屿设置（编辑是等级门槛） | `true` |
| `tradewinds.island.language` | 允许使用语言指令 | `true` |
| `tradewinds.island.warp` | 捷径：从岛屿水域的任何地方打开传送对话。默认关闭——预期的路径是划行到岛屿边界，它自动提供对话。授予以跳过航行。 | `op` |
| `tradewinds.island.trade` | 捷径：从岛屿保护范围内的任何地方打开市场。默认关闭——预期的路径是停靠并右键商人。授予以跳过行走。 | `op` |

## 管理员权限

| 权限 | 描述 | 默认 |
|------|------|------|
| `tradewinds.admin` | 允许使用 TradeWinds 管理指令 | `op` |
| `tradewinds.admin.islands` | 允许列出最近的贸易岛屿 | `op` |
| `tradewinds.admin.tpisland` | 允许传送到贸易岛屿 | `op` |
| `tradewinds.admin.boat` | 检查玩家的船舶记录直接从数据库：货物、燃料、最后看见位置，船体是否真正加载在那里——并从数据库恢复一艘丢失的活跃船作为他们包中的物品。 | `op` |
| `tradewinds.admin.rank` | 检查或设置玩家的航海家等级——在他们真实已探计数上储存一个调整，所以晋升、降级和重置都起作用，声称门槛和排行榜随之。 | `op` |
| `tradewinds.admin.customs` | 显示你位置处的海关状态（走私、扫描几率、巡逻） | `op` |
| `tradewinds.admin.priceaudit` | 审计价格覆盖并将报告写入 `price-audit.txt` | `op` |
| `tradewinds.admin.warpfail` | 操纵玩家的下一次传送失败，将他们扔进间隙地 | `op` |
| `tradewinds.admin.reflag` | 允许重新应用安全等级标志到所有岛屿 | `op` |
| `tradewinds.admin.*` | 所有 TradeWinds 管理权限 | `op` |
