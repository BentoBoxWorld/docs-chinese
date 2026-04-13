# BentoBox

**SkyBlock、OneBlock、AcidIsland，更多玩法——一个插件全搞定**

BentoBox 是专为 Paper 服务器打造的岛屿玩法平台。挑选你想要的游戏模式，丢进去，直接开玩。没有分支版本，没有过时代码——一个持续维护、跟进每个 Minecraft 版本的统一平台。

## 可用游戏模式

- **BSkyBlock** — 经典天空方块，ASkyBlock 的正统续作
- **AOneBlock** — 广受欢迎的一块石玩法
- **AcidIsland** — 在酸海中求生
- **Boxed** — 通过完成进度来扩展你的世界
- **CaveBlock** — 地下生存挑战
- **SkyGrid** — 散布方块，极限探险
- **Poseidon** — 水下岛屿挑战
- 以及更多社区创作的游戏模式……

## 为什么服务器管理员选择 BentoBox？

- 在**一台服务器**上同时运行多种游戏模式，共享挑战、传送点、等级和排行榜
- **20+ 功能插件**让你精准定制服务器体验
- 持续活跃维护，始终跟进最新 Minecraft 版本
- **免费开源**——全球超过 1,100 台服务器正在使用
- 提供丰富 API，方便开发者构建自定义插件

[浏览所有插件](BentoBox/About/Addons) | [完整文档](BentoBox/Developer-Documentation)

## 安装方法

1. 将 BentoBox 的 jar 文件放入服务器的 `plugins/` 文件夹
2. 启动服务器
3. 从 [download.bentobox.world](https://download.bentobox.world) 下载你想要的游戏模式和功能插件，放入 `plugins/BentoBox/addons/` 文件夹
4. 重启服务器——完成！

!!! warning "注意：仅支持 Paper"
    旧版本支持 Spigot，但目前我们**只支持 Paper**。

## 支持 BentoBox

请通过成为 [GitHub 赞助者](https://github.com/sponsors/tastybento) 或 [PayPal 捐款](https://www.paypal.me/BentoBoxWorld) 来支持我们。希望你玩得开心，也欢迎资助我们的开发！

## 深入了解
- [你的前 30 分钟](BentoBox/First-Steps) — 安装后要做的事
- [安装 BentoBox](BentoBox/Install-Bentobox)
- [选择游戏模式](gamemodes/Comparison)
- [词汇表](Glossary) — 关键术语解释
- [常见问题](FAQ)
- [从 ASkyBlock 迁移](Converter/index.md)
- [将 BentoBox 世界设置为服务器默认世界](BentoBox/Set-a-BentoBox-world-as-the-server-default-world)
- [数据库转换](BentoBox/Database-transition)

## 关于 BentoBox
- [命令](BentoBox/Commands)
- 权限
    - [BentoBox 权限](BentoBox/Permissions)
    - [AcidIsland 权限](gamemodes/AcidIsland/Permissions)
    - [AOneBlock 权限](gamemodes/AOneBlock/#permissions)
    - [Bank 权限](addons/Bank/#permissions)
    - [Biomes 权限](addons/Biomes/#permissions)
    - [Border 权限](addons/Border/#permissions)
    - [BSkyBlock 权限](gamemodes/BSkyBlock/Permissions)
    - [CaveBlock 权限](gamemodes/CaveBlock/Permissions)
    - [CauldronWitchery 权限](addons/CauldronWitchery/#permissions)
    - [Challenges 权限](addons/Challenges/#permissions)
    - [Chat 权限](addons/Chat/#permissions)
    - [Check Me Out 权限](addons/CheckMeOut/#permissions)
    - [Control Panel 权限](addons/ControlPanel/#permissions)
    - [Dimensional Trees 权限](addons/DimensionalTrees/#permissions)
    - [Extra Mobs 权限](addons/ExtraMobs/#permissions)
    - [Farmers Dance 权限](addons/FarmersDance/#permissions)
    - [Greenhouses 权限](addons/Greenhouses/Permissions)
    - [InvSwitcher 权限](addons/InvSwitcher/#permissions)
    - [Island Fly 权限](addons/IslandFly/#permissions)
    - [Level 权限](addons/Level/#permissions)
    - [Likes 权限](addons/Likes/Permissions)
    - [Limits 权限](addons/Limits/Permissions)
    - [Magic Cobblestone Generator 权限](addons/MagicCobblestoneGenerator/#permissions)
    - [Poseidon 权限](gamemodes/Poseidon/Permissions)
    - [SkyGrid 权限](gamemodes/SkyGrid/Permissions)
    - [Stranger Realms](gamemodes/StrangerRealms/Permissions)
    - [TopBlock 权限](addons/TopBlock/#permissions)
    - [Twerking For Trees 权限](addons/TwerkingForTrees/#permissions)
    - [TopBlock 权限](addons/TopBlock/#permissions)
    - [Upgrades 权限](addons/Upgrades/#permissions)
    - [Visit 权限](addons/Visit/#permissions)
    - [VoidPortals 权限](addons/VoidPortals/#permissions)
    - [Warps 权限](addons/Warps/Permissions)
- [岛屿保护、标志 & 等级](BentoBox/Island-Protection,-Flags-&-Ranks)
    - [标志](BentoBox/Flags)
    - [等级](BentoBox/Island-Protection,-Flags-&-Ranks#ranks)
- [占位符](BentoBox/Placeholders)
- [蓝图](BentoBox/Blueprints)

## 使用 BentoBox 的 API
- [API 介绍](BentoBox/Developer-Documentation)
- [如何从插件获取数据](BentoBox/Request-Handler-API---How-plugins-can-get-data-from-addons)
- [插件](Tutorials/api/Create-an-addon)
    - [addon.yml](BentoBox/How-to-fill-in-the-addon_yml-file)
    - [配置 API](BentoBox/Config-API)
    - [数据库](BentoBox/Database-API)
- [创建游戏模式插件](BentoBox/Creating-a-Game-Mode)
- [内置命令](BentoBox/Commands)
- [元数据 API](BentoBox/MetadataAPI)
- [Javadocs](https://bentoboxworld.github.io/BentoBox)
