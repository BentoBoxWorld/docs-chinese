# 占位符 { #placeholders }

占位符让其他插件显示 BentoBox 信息：玩家的岛屿名称或计分板上的等级、聊天中的等级、全息中的岛屿数量等。

## 设置 { #setting-up }

1. 安装 [PlaceholderAPI](https://www.spigotmc.org/resources/placeholderapi.6245/)。
2. 重启服务器。

就这样。BentoBox 自己将其占位符注册到 PlaceholderAPI；没有要用 `/papi ecloud` 下载的扩展。

然后在支持 PlaceholderAPI 的任何插件中使用占位符（计分板、标签列表、聊天、全息等）。

## 占位符如何命名 { #how-placeholders-are-named }

每个游戏模式注册自己的每个占位符的副本，以游戏模式的名称开头（小写）：

```
%bskyblock_island_name%
%aoneblock_island_members_count%
%acidisland_rank%
```

下面的表格将此前缀写作 `[gamemode]`。来自附属的占位符以附属名开头，然后是游戏模式，例如 `%Level_bskyblock_island_level%`；它们列在每个[附属的页面](../addons/Level/index.md#placeholders)上。

有两种类型：

- `[gamemode]_island_...` 关于**玩家自己的岛屿**在那个游戏模式中。
- `[gamemode]_visited_island_...` 关于**玩家站在上面的岛屿**，可能是某人别人的。

## 在游戏中查找占位符 { #finding-a-placeholder-in-game }

| 命令 | 作用 |
|---|---|
| `/bentobox placeholders` | 打开菜单来浏览 BentoBox 和附属中的每个占位符，以及打开或关闭单个占位符 |
| `/bentobox dump-placeholders` | 将每个已注册占位符写入 `plugins/BentoBox/placeholder-dump.md` |
| `/papi parse me %bskyblock_island_name%` | 显示占位符为你返回什么（PlaceholderAPI 命令） |

## BentoBox 占位符 { #bentobox-placeholders }

这些对每个游戏模式都被注册。

{{ placeholders_source("BentoBox") }}

### 编号占位符 { #numbered-placeholders }

以 `_<n>` 结尾的占位符为每个数字注册一次：

- `island_member_name_<n>`、`island_member_rank_<n>` 和 `island_banned_name_<n>`（及其 `visited_island_` 版本）从 1 到 50，用于逐行列出团队或禁止列表，例如 `%bskyblock_island_member_name_1%`。
- `island_name_<n>` 和 `island_memberlist_<n>` 从 1 到玩家可以拥有的岛屿数量（`concurrent-islands`）。参见[多个岛屿](ConcurrentIslands.md)。

### 标志占位符 { #flag-placeholders }

每个保护标志、岛屿设置和世界设置都有一个占位符：`flag_` 后跟标志的 ID（小写）。

| 标志类型 | 返回 |
|---|---|
| 保护标志 | 玩家岛屿上允许的最低等级，例如 `成员` |
| 岛屿设置 | 玩家岛屿为 `true` 或 `false` |
| 世界设置 | 游戏模式的世界为 `true` 或 `false` |

```
%bskyblock_flag_break_blocks%    → Member
%bskyblock_flag_pvp_overworld%   → false
```

标志 ID 列在[标志](Flags.md)中。由附属添加的标志会自动获得占位符。

## 游戏模式页面 { #game-mode-pages }

每个游戏模式的页面列出这些占位符及其自己的前缀已填充，连同游戏模式自己的占位符：

[AcidIsland](../gamemodes/AcidIsland/Placeholders.md) · [AOneBlock](../gamemodes/AOneBlock/Placeholders.md) · [Boxed](../gamemodes/Boxed/Placeholders.md) · [BSkyBlock](../gamemodes/BSkyBlock/Placeholders.md) · [CaveBlock](../gamemodes/CaveBlock/Placeholders.md) · [ChunkBlock](../gamemodes/ChunkBlock/Placeholders.md) · [Poseidon](../gamemodes/Poseidon/Placeholders.md) · [SkyGrid](../gamemodes/SkyGrid/Placeholders.md) · [TradeWinds](../gamemodes/TradeWinds/Placeholders.md)

## 故障排除 { #troubleshooting }

**占位符显示为文本（`%bskyblock_island_name%`）而不是值。**
检查 PlaceholderAPI 已安装，显示它的插件支持 PlaceholderAPI，以及占位符没有在 `/bentobox placeholders` 中关闭。某些聊天插件需要额外设置或插件来在聊天消息中解析占位符。用 `/papi parse me <placeholder>` 测试。

**占位符为空。**
玩家在那个游戏模式中没有岛屿，或对于 `visited_island_` 占位符，不站在岛屿上。

**来自附属的占位符不存在。**
检查附属已安装且为那个游戏模式启用。附属占位符以附属名开头，然后是游戏模式：`%Level_bskyblock_island_level%`。还要检查它没有在 `/bentobox placeholders` 中关闭。

**我需要一个不存在的占位符。**
在 GitHub 上[请求一个](https://github.com/BentoBoxWorld/BentoBox/issues/new?labels=Status%3A+Pending%2C+Type%3A+Enhancement&template=placeholder_request.md&title=Placeholder%3A+)。
