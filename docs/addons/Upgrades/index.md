# Upgrades

**Upgrades** 通过让玩家购买岛屿升级——扩展保护范围、更高的方块/实体限制、自定义命令、刷怪笼增益和农作物生长增益——为玩家提供进度曲线,可使用金钱、物品、权限或岛屿等级进行购买。

由 [tastybento](https://github.com/tastybento) 创建和维护。

{{ addon_description("Upgrades", true) }}

!!! warning "1.0.0 版本是完全重写"
    Upgrades 1.0.0 用完全**数据库驱动的架构**取代了旧的基于配置文件的系统。升级定义、层级、价格和奖励现在存储在 BentoBox 的数据库中,完全通过游戏内界面管理。**旧的 `config.yml` 不再使用** — 如果从 0.x 版本升级,请在安装 1.0.0 之前删除它。

## 安装

1. 将 Upgrades 插件 jar 文件放入 BentoBox 插件的 addons 文件夹。
2. 重启服务器。
3. 首次运行时,系统会自动创建 8 个示例升级,让你快速开始。
4. 使用 `/[admin_command] upgrades` 在游戏内自定义或创建升级。

## 工作原理

升级、层级、价格和奖励存储在 BentoBox 的数据库(YAML、JSON、MySQL、MongoDB 等)中。无需编辑大型配置文件。所有升级数据由插件自动加载、缓存和保存。

首次安装时,播种器会创建 8 个示例升级。一旦删除示例升级,下次重启时不会重新播种。要重新触发播种,从插件数据文件夹中删除 `.seeded-gamemodes` 标记文件。

## 命令

!!! tip
    `[player_command]` 和 `[admin_command]` 是根据你运行的游戏模式而不同的命令。

=== "玩家命令"
    - `/[player_command] upgrade`: 打开升级购买面板。

=== "管理员命令"
    - `/[admin_command] upgrades`: 打开管理员 GUI,用于创建、编辑和删除升级及其层级。

## 价格类型

每个升级层级可以要求以下任意组合的价格(必须全部满足才能购买):

| 类型 | 描述 |
|---|---|
| **金钱** | Vault 经济费用 |
| **物品** | 玩家物品栏中必须有特定物品 |
| **权限** | 玩家必须拥有特定权限节点 |
| **岛屿等级** | 最低岛屿等级(需要 Level 插件) |

## 奖励类型

每个升级层级可以授予以下任意组合的奖励:

| 类型 | 描述 |
|---|---|
| **范围** | 增加岛屿保护范围 |
| **方块限制** | 提高方块类型的限制(需要 Limits 插件) |
| **实体限制** | 提高实体类型的限制(需要 Limits 插件) |
| **实体组限制** | 提高实体组的限制(需要 Limits 插件) |
| **命令** | 购买时运行控制台或玩家命令 |
| **刷怪笼增益** | 乘以刷怪笼生成速率 |
| **农作物生长增益** | 乘以农作物生长速度 |

## 等级公式变量

在价格公式中,可以使用以下变量:

- `[level]` — 正在购买的当前升级等级
- `[islandLevel]` — 岛屿当前等级(来自 Level 插件;可能为 0)
- `[numberPlayer]` — 岛屿团队中的玩家数量

## 权限

插件根据升级配置自动授予权限。查看 [addon.yml](https://github.com/BentoBoxWorld/Upgrades/blob/develop/src/main/resources/addon.yml) 了解当前权限列表。

## API

`UpgradeAPI` 类公开给其他插件,用于以编程方式查询和修改升级数据。

## 更新日志

??? warning "v1.0.0 新内容 — 完全重写,需要操作"
    **发布于:** 2026-04-12

    - **数据库驱动的升级系统。** 所有升级、层级、价格和奖励现在存储在 BentoBox 数据库中——无需编辑配置文件。
    - **新管理员 GUI。** `/[admin_command] upgrades` 打开完整的游戏内管理界面,通过 GUI 和聊天输入创建和编辑升级。
    - **新奖励类型:** 刷怪笼增益(乘以刷怪笼速率)和农作物生长增益(乘以农作物生长速度)。
    - **模板化玩家面板。** 玩家升级面板现在是 BentoBox `TemplatedPanel` — 可通过 `panels/upgrades_panel.yml` 完全自定义。
    - **完整的 `UpgradeAPI`** 用于从其他插件进行编程访问。
    - 首次安装时自动播种 8 个示例升级。
    - 与 Limits 插件 1.28 的兼容性修复。

    🔺 **与 0.x 版本不向后兼容。** 安装前删除旧的 `config.yml` 和任何现有升级数据。没有自动迁移。

    [发布 v1.0.0](https://github.com/BentoBoxWorld/Upgrades/releases/tag/1.0.0)

??? note "v1.0.1 新内容"
    **发布于:** 2026-04-12

    - **播种器修复。** 示例升级在被删除后不再每次重启都重新生成。播种器现在在持久性 `.seeded-gamemodes` 标记文件中跟踪已播种的游戏模式。

    [发布 v1.0.1](https://github.com/BentoBoxWorld/Upgrades/releases/tag/1.0.1)

## 翻译

{{ translations("Upgrades") }}
