# 词汇表

新来 BentoBox？本页解释了文档中使用的关键术语。

---

## 插件（Addon）
扩展 BentoBox 新功能的文件（`.jar`）。插件放在 `plugins/BentoBox/addons/` — **不是**在你服务器的 `plugins/` 文件夹中。有两种类型：[游戏模式插件](#游戏模式)和[功能插件](#功能插件)。见[插件](BentoBox/About/Addons.md)。

## 管理员命令（Admin Command）
每个游戏模式都有一个仅管理员命令来管理岛屿、设置和玩家。对于 BSkyBlock 是 `/bsb`，对于 AcidIsland 是 `/acid admin` 等。确切的命令列在每个游戏模式的文档中。

## 蓝图（Blueprint）
创建新岛屿时使用的已保存建造岛屿模板。BentoBox 配备了默认蓝图，但管理员可以在游戏中创建自己的。蓝图存储在 `plugins/BentoBox/blueprints/` 中。见[蓝图](BentoBox/About/BlueprintsSummary.md)。

## 蓝图束（Blueprint Bundle）
分组在一起的一组命名蓝图（主世界、地狱和末地各一个）。当玩家创建新岛屿时，他们可能会看到束的选择。每个束可以有自己的图标、描述和权限要求。

## 合作（Coop）
给予不是完整团队成员的玩家的临时岛屿等级。合作玩家的访问在授予它的团队成员登出时过期。见[团队](BentoBox/About/Teams.md)。

## 功能插件（Feature Addon）
在游戏模式之上添加额外功能（挑战、飞行、传送点等）的插件。功能插件是可选的。见[插件](BentoBox/About/Addons.md)。

## 标志（Flag）
单个保护或设置开关，控制岛屿上或游戏世界中是否允许某事。标志通过游戏内设置 GUI 管理。示例：访客是否可以破坏方块、苦力怕是否可以爆炸、叶方块是否腐烂。见[保护](BentoBox/About/Protections.md)。

## 游戏模式（Game Mode）
定义玩家游戏的游戏世界类型的插件 — 世界类型、岛屿如何生成以及总体挑战。示例：BSkyBlock、AcidIsland、AOneBlock。你必须至少安装一个游戏模式才能让 BentoBox 做任何事情。见[游戏模式](BentoBox/About/GameModes.md)。

## 岛屿（Island）
属于玩家或团队的游戏世界的受保护区域。每个玩家在每个游戏模式中获得一个岛屿。当玩家第一次运行主命令时，岛屿会自动创建。见[岛屿管理](BentoBox/About/IslandManagement.md)。

## 岛屿距离（Island Distance）
世界网格中相邻岛屿中心之间的间隔。在游戏模式的 `config.yml` 中设置一次，**岛屿存在后无法更改**。保护范围永远不能超过此值的一半。见[常见问题](FAQ.md#how-do-i-change-the-island-distance)。

## 地区（Locale）
包含特定语言中 BentoBox 或插件的所有游戏内文本的语言文件。地区文件位于 `plugins/BentoBox/locales/` 中。见[多语言支持](BentoBox/About/Multilingual.md)。

## 所有者（Owner）
创建了岛屿或转移了所有权给他们的玩家。每个岛屿总是恰好有一个所有者。所有者对他们的岛屿设置和团队有完全控制。

## 占位符（Placeholder）
其他插件可以使用的短代码，如 `%bskyblock_island_name%`，来显示 BentoBox 数据 — 例如在聊天、计分板或全息图中。BentoBox 使用 PlaceholderAPI。见[占位符](BentoBox/Placeholders.md)。

## 玩家命令（Player Command）
玩家用来与游戏模式交互的主要命令。对于 BSkyBlock 是 `/island`（或 `/is`），对于 AOneBlock 是 `/oneblock`（或 `/ob`）等。确切的命令列在每个游戏模式的文档中。

## 保护范围（Protection Range）
岛屿中心周围受保护的区域的半径。没有其他玩家可以在此区域内构建、破坏或交互，除非有权限。总是小于或等于[岛屿距离](#岛屿距离)的一半。可以通过管理员命令或玩家权限扩大。

## 等级（Rank）
分配给与特定岛屿相关的玩家的信任级别。从最低到最高：**被禁止**、**访客**、**合作**、**被信任**、**成员**、**副所有者**、**所有者**。等级控制玩家在岛屿上可以采取的操作。见[团队](BentoBox/About/Teams.md)。

## 重置（Reset）
当玩家删除自己的岛屿并用新岛屿重新开始时。玩家可以重置的次数是可配置的。见[岛屿管理](BentoBox/About/IslandManagement.md#resetting-an-island)。

## 副所有者（Sub-Owner）
低于所有者但高于成员的岛屿等级。副所有者拥有几乎所有与所有者相同的权限。一个岛屿上可以存在多个副所有者。

## 被信任（Trusted）
不是完整团队成员的玩家的永久访客等级。与[合作](#合作)不同，被信任的状态在授予玩家登出时不会过期。见[团队](BentoBox/About/Teams.md)。

## 访客（Visitor）
任何在他们不拥有或不属于的岛屿上的玩家的默认等级。访客可以做什么由岛屿所有者通过设置 GUI 控制。

## 世界设置（World Settings）
适用于整个游戏模式世界的保护和行为设置，而不仅仅是单个岛屿。只有管理员可以更改这些。通过 `/[admin_command] settings` 访问。见[保护](BentoBox/About/Protections.md)。
