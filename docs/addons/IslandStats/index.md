# 岛屿统计

**岛屿统计** 为每个岛屿而不是每个玩家保存统计数据。它从怪物死亡开始：每个怪物在岛屿上死亡了多少只，以及一个玩家击杀了多少只。它适用于所有游戏模式。

由 [tastybento](https://github.com/tastybento) 创建和维护。

{{ addon_description("IslandStats") }}

## 安装

1. 将 IslandStats 附属的 jar 文件放入 BentoBox 插件的 addons 文件夹。
2. 重启服务器。
3. 附属将创建一个数据文件夹，其中包含 config.yml。
4. 根据需要编辑 config.yml。
5. 如果进行任何更改，请重启服务器。

IslandStats 需要 BentoBox 3.23.0 或更高版本、Minecraft 26.2 或更高版本和 Java 25。

!!! warning "计数从安装附属时开始"
    IslandStats 不读取旧的玩家统计数据，所以每个岛屿都从零开始。

## 统计

该附属为每个怪物类型保存两个计数：

| 统计 | 计数 |
|---|---|
| `KILL_ENTITY` | 玩家在岛屿上击杀的怪物。与原版 `KILL_ENTITY` 玩家统计的含义相同。 |
| `ENTITY_DEATH` | 岛屿上因任何原因死亡的怪物：玩家、怪物农场、跌落伤害、熔岩。 |

死亡计入其发生地所在保护区域的岛屿。玩家和盔甲架不计数。访客的击杀计入 `KILL_ENTITY`，除非 `count-visitor-kills` 关闭。岛屿上的每次死亡始终计入 `ENTITY_DEATH`。

该附属不使用原版玩家统计，因为它们只记录归功于玩家的击杀，也不记录怪物所在的位置。这样会遗漏怪物农场，并把击杀记到击杀者的岛屿上，而不是怪物死亡的岛屿。

### 统计对话框

`/[player_command] stats` 打开一个对话框：

- 摘要页面显示每个统计的总数，以及一个打开它的按钮。
- 每个统计页面从最多到最少列出怪物，并有上一页、下一页、返回和关闭按钮。
- 怪物名称以可翻译的文本形式发送，因此每个玩家以其自己的客户端语言看到它们。

### 存储

统计通过 BentoBox 数据库 API 存储，所以它们进入 BentoBox 配置使用的任何数据库。每个岛屿有一条记录。使用 JSON 数据库时，它们位于 `plugins/BentoBox/database/IslandStatsData/`。计数发生在内存中，更改的岛屿按计时器保存（`save-interval`），并在服务器停止时保存。删除或重置岛屿时，其统计也会被删除。

## 配置

最新的 `config.yml` 可以在[这里](https://github.com/BentoBoxWorld/IslandStats/blob/develop/src/main/resources/config.yml)找到。

??? note "disabled-gamemodes"
    此处列出的游戏模式被 IslandStats 忽略。

    默认值：`[]`

    ```yaml
    disabled-gamemodes:
      - BSkyBlock
    ```

??? note "count-visitor-kills"
    计算岛屿上由不是成员的玩家击杀的怪物，例如访客或合作成员。这只影响"由玩家击杀"统计。岛屿上的每次怪物死亡始终计入"所有怪物死亡"统计。

    默认值：`true`

??? note "ignored-entities"
    从不计数的实体类型。使用 Bukkit 实体类型名称。盔甲架是服务器的活生物体，所以默认被忽略。

    默认值：`ARMOR_STAND`

??? note "save-interval"
    更改的统计写入数据库的频率（分钟）。统计在内存中计数，服务器停止时总是保存。最小值为 1。

    默认值：`5`

??? note "dialog.page-size"
    统计对话框的每一页显示多少行怪物。范围 1 到 50。

    默认值：`15`

## 命令

!!! tip
    `[player_command]` 和 `[admin_command]` 是根据你运行的游戏模式而不同的命令。
    游戏模式的 `config.yml` 文件包含允许你修改这些值的选项。
    例如，在 BSkyBlock 上，默认 `[player_command]` 是 `island`，默认 `[admin_command]` 是 `bsbadmin`。

=== "玩家命令"
    - `/[player_command] stats`：打开你的岛屿的统计对话框。

=== "管理员命令"
    - `/[admin_command] stats <player>`：显示该玩家的岛屿统计。玩家看到对话框，控制台收到统计为聊天行。
    - `/[admin_command] stats <player> reset`：询问确认后清除岛屿的统计。

!!! warning "使用你所在世界的命令"
    `/[player_command] stats` 仅在该游戏模式的世界中有效。例如，在 OneBlock 世界中使用 OneBlock 命令，而不是 `/is`，以便在多个游戏模式中拥有岛屿的玩家看到正确的岛屿。

## 权限

!!! tip
    `[gamemode]` 是一个前缀，根据你运行的游戏模式而不同。

| 权限 | 默认值 | 它允许什么 |
|---|---|---|
| `[gamemode].island.stats` | true | `/[player_command] stats`，打开你的岛屿的统计 |
| `[gamemode].admin.stats` | op | `/[admin_command] stats <player> [reset]` |

## 占位符

{{ placeholders_source("IslandStats") }}

`<entity>` 是小写的怪物类型，如 `zombie` 或 `iron_golem`。使用 PlaceholderAPI 时，占位符看起来像 `%IslandStats_bskyblock_island_kill_entity_zombie%`。

## 对于附属开发者

其他附属可以通过管理器读取计数：

```java
IslandStats stats = (IslandStats) BentoBox.getInstance().getAddonsManager().getAddonByName("IslandStats").orElseThrow();
long zombies = stats.getManager().getCount(island, IslandStat.KILL_ENTITY, EntityType.ZOMBIE);
long allDeaths = stats.getManager().getTotal(island, IslandStat.ENTITY_DEATH);
```

??? note "v1.0.0 的新增内容——第一个版本"
    **发布时间：** 2026年10月4日

    第一个版本。兼容性：BentoBox API 3.23.0 · Minecraft 26.2 及更高版本 · Java 25。[Release 1.0.0](https://github.com/BentoBoxWorld/IslandStats/releases/tag/1.0.0)

    - 每个岛屿的怪物击杀和死亡计数（`KILL_ENTITY` 和 `ENTITY_DEATH`）。
    - 带有 `/[player_command] stats` 的统计对话框，以及 `/[admin_command] stats <player> [reset]` 的管理员查看和重置。
    - 岛屿总数、每个怪物计数和玩家站在其上的岛屿的占位符。
    - 🔡 此版本仅包含 `en-US` 区域设置。欢迎翻译。

## 翻译

{{ translations("IslandStats") }}
