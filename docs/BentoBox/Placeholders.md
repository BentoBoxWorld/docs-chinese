占位符允许你在其他插件中显示来自 BentoBox 的任何附加组件或游戏模式的数据。反之亦然！

## 如何使用占位符？

### 下载您需要的占位符API。

BentoBox使用[**PlaceholderAPI**](https://www.spigotmc.org/resources/placeholderapi.6245/)作为占位符。

### 启动服务器，您就可以开始了！

无论您使用哪个占位符API，只需启动服务器即可。**无需下载任何扩展**：BentoBox会处理一切！

## 如何在聊天中显示占位符？

如果您正在使用**EssentialsChat**和**PlaceholderAPI**，您**必须**安装[**ChatInjector**](https://www.spigotmc.org/resources/chatinjector-1-13.81201/)才能在聊天中显示占位符。但请注意，有报告称ChatInjector可能会导致问题。

我们建议您使用支持PlaceholderAPI的替代聊天插件，例如[**ChatControl**](https://www.spigotmc.org/resources/chatcontrol%E2%84%A2-the-ultimate-chat-plugin-500-000-downloads-1-2-5-1-14-4.271/)。

## 如何在计分板中显示占位符？

如果您正在使用本身不支持**PlaceholderAPI**但支持**MVdWPlaceholderAPI**的计分板插件（如**Featherboard**），您仍然可以使用BentoBox占位符，但您需要添加**{placeholderapi_[text]}**，并将*[text]*替换为不带*％*字符的占位符，例如*{placeholderapi_bskyblock_island_name}*。

## 如何建议新的占位符？

如果您认为应该为BentoBox或游戏模式添加其他默认占位符，请提交[占位符请求](https://github.com/BentoBoxWorld/BentoBox/issues/new?assignees=&labels=Status%3A+Pending%2C+Type%3A+Enhancement&template=placeholder_request.md&title=Placeholder%3A+)。

## 游戏模式附加组件的默认占位符

所有游戏模式附加组件都会自动注册一些默认占位符。

**可用的默认占位符**

| 占位符 | 描述 | 版本 |
|-------------------------------------------------------|--------------------------------------------------------------------------------|-----------|
| %[gamemode]_world_friendly_name% | 游戏模式世界的名称 | 1.4.0 |
| %[gamemode]_world_islands% | 游戏模式世界中的岛屿数量 | 1.5.0 |
| %[gamemode]_island_distance% | 游戏模式世界中岛屿中心之间距离的一半 | 1.4.0 |
| %[gamemode]_island_distance_diameter% | 游戏模式世界中岛屿之间的距离 | 1.5.0 |
| %[gamemode]_island_protection_range% | 岛屿保护范围的半径 | 1.4.0 |
| %[gamemode]_island_protection_range_diameter% | 岛屿保护范围的直径 | 1.5.0 |
| %[gamemode]_island_owner% | 岛屿所有者的名称 | 1.4.0 |
| %[gamemode]_island_creation_date% | 岛屿的创建日期 | 1.4.0 |
| %[gamemode]_island_name% | 岛屿的名称 | 1.4.0 |
| %[gamemode]_island_center% | 岛屿中心的坐标 | 1.5.0 |
| %[gamemode]_island_center_x% | 岛屿中心的X坐标 | 1.5.0 |
| %[gamemode]_island_center_y% | 岛屿中心的Y坐标 | 1.5.0 |
| %[gamemode]_island_center_z% | 岛屿中心的Z坐标 | 1.5.0 |
| %[gamemode]_island_members_max% | 岛上可以拥有的最大成员数 | 1.5.0 | 
| %[gamemode]_island_members_count% | 岛上的成员、副所有者和所有者数量 | 1.5.0 |
| %[gamemode]_island_members_list% | 岛上至少是成员的玩家名称的逗号分隔列表 | 1.13.0 |
| %[gamemode]_island_coop_list% | 岛上是合作者的玩家名称的逗号分隔列表 | 2.4.2 |
| %[gamemode]_island_trusted_list% | 岛上是受信任者的玩家名称的逗号分隔列表 | 2.4.2 |
| %[gamemode]_island_trustees_count% | 被信任进入岛屿的玩家数量 | 1.5.0 |
| %[gamemode]_island_coops_count% | 与岛屿合作的玩家数量 | 1.5.0 |
| %[gamemode]_island_visitors_count% | 当前访问岛屿的玩家数量 | 1.5.0 |
| %[gamemode]_island_bans_count% | 被禁止进入岛屿的玩家数量 | 1.5.0 |
| %[gamemode]_island_uuid% | 数据库中使用的岛屿的唯一ID | 1.15.4 |
| %[gamemode]_visited_island_protection_range% | 玩家所在岛屿保护范围的半径 | 1.5.2 |
| %[gamemode]_visited_island_protection_range_diameter% | 玩家所在岛屿保护范围的直径 | 1.5.2 |
| %[gamemode]_visited_island_owner% | 玩家所在岛屿所有者的名称 | 1.5.2 |
| %[gamemode]_visited_island_creation_date% | 玩家所在岛屿的创建日期 | 1.5.2 |
| %[gamemode]_visited_island_name% | 玩家所在岛屿的名称 | 1.5.2 |
| %[gamemode]_visited_island_center% | 玩家所在岛屿中心的坐标 | 1.5.2 |
| %[gamemode]_visited_island_center_x% | 玩家所在岛屿中心的X坐标 | 1.5.2 |
| %[gamemode]_visited_island_center_y% | 玩家所在岛屿中心的Y坐标 | 1.5.2 |
| %[gamemode]_visited_island_center_z% | 玩家所在岛屿中心的Z坐标 | 1.5.2 |
| %[gamemode]_visited_island_members_max% | 玩家所在岛屿可以拥有的最大成员数 | 1.5.2 |
| %[gamemode]_visited_island_members_count% | 玩家所在岛屿的成员、副所有者和所有者数量 | 1.5.2 |
| %[gamemode]_visited_island_coop_list% | 玩家所在岛屿上是合作者的玩家名称的逗号分隔列表 | 2.4.2 |
| %[gamemode]_visited_island_trusted_list% | 玩家所在岛屿上是受信任者的玩家名称的逗号分隔列表 | 2.4.2 |
| %[gamemode]_visited_island_members_list% | 玩家所在岛屿上至少是成员的玩家名称的逗号分隔列表 | 1.13.0 |
| %[gamemode]_visited_island_trustees_count% | 被信任进入玩家所在岛屿的玩家数量 | 1.5.2 |
| %[gamemode]_visited_island_coops_count% | 与玩家所在岛屿合作的玩家数量 | 1.5.2 |
| %[gamemode]_visited_island_visitors_count% | 当前访问玩家所在岛屿的玩家数量 | 1.5.2 |
| %[gamemode]_visited_island_bans_count% | 被禁止进入玩家所在岛屿的玩家数量 | 1.5.2 |
| %[gamemode]_visited_island_uuid% | 玩家所在岛屿的唯一ID | 1.15.4 |
| %[gamemode]_has_island% | 玩家是否拥有岛屿 | 1.5.0 |
| %[gamemode]_rank% | 玩家在其岛屿上的等级 | 1.5.0 |
| %[gamemode]_resets% | 玩家重置岛屿的次数 | 1.5.0 | 
| %[gamemode]_resets_left% | 玩家可以重置岛屿的次数 | 1.5.0 |
| %[gamemode]_deaths% | 玩家死亡的次数 | 1.12.0 |
| %[gamemode]_on_island% | 玩家是否在其所属的岛屿上 | 1.13.0 |

## 另请参阅
游戏模式和附加组件也可以带来自己的占位符。我们强烈建议您查看以下页面，它们可能更适合您的需求。

- 游戏模式
    - [AcidIsland](../../gamemodes/AcidIsland/Placeholders)  
    - [AOneBlock](../../gamemodes/AOneBlock/Placeholders)
    - [Boxed](../../gamemodes/Boxed/Placeholders)
    - [BSkyBlock](../../gamemodes/BSkyBlock/Placeholders)
    - [CaveBlock](../../gamemodes/CaveBlock/Placeholders)
    - [SkyGrid](../../gamemodes/SkyGrid/Placeholders)
- 附加组件
    - [Bank](../../addons/Bank/#placeholders)
    - [Challenges](../../addons/Challenges/#placeholders)
    - [Level](../../addons/Level/#placeholders) 
    - [Likes](../../addons/Likes/#placeholders)
    - [Limits](../../addons/Limits/#placeholders)
    - [MagicCobblestoneGenerator](../../addons/MagicCobblestoneGenerator/#placeholders)