# SkyGrid

**SkyGrid** 是一个充满了浮动方块的地图，这些方块放置在一个四方格网上。所以每个方向上的每第四个方块是实际的方块，其他的都是空气。原始SkyBlick的创造者SethBling于2012年发布了SkyGrid，它已成为最受欢迎的Minecraft地图之一。

在SkyGrid中玩耍（和生存）有其目标和技巧，网络上有大量的帮助、技巧和方法，使这个游戏非常有趣！

由[tastybento](https://github.com/tastybento)创建和维护。

{{ addon_description("SkyGrid") }}

## 安装

0. 安装BentoBox并至少运行一次服务器以创建其数据文件夹。
1. 将这个jar文件放在BentoBox插件的addons文件夹中。
2. 重启服务器。
3. 插件将创建世界和一个数据文件夹，并且文件夹中会有一个config.yml。
4. 停止服务器。
5. 按照您的意愿编辑config.yml。
6. 如果您做了会影响它们的更改，删除默认创建的任何世界。
7. 重启服务器。

## 配置

SkyGrid 的 `config.yml` 列出了每个世界中组成网格的方块，以及每种方块的权重。最新的文件见[这里](https://github.com/BentoBoxWorld/SkyGrid/blob/master/src/main/resources/config.yml)。

### 刷怪笼生物 { #spawner-mobs }

自 SkyGrid 2.3.0 起，你可以选择网格中的刷怪笼会刷出哪些生物。每个世界都有自己的列表，格式为 `EntityType: weight`：

| 世界 | 列表 |
|---|---|
| 主世界 | `world.spawners` |
| 下界 | `world.nether.spawners` |
| 末地 | `world.end.spawners` |

```yaml
world:
  end:
    spawners:
      ENDERMAN: 45
      ENDERMITE: 54
      SHULKER: 1
```

- 生物按其权重的比例被选中。在上面的例子中，每 100 个末地刷怪笼中有 1 个是潜影贝刷怪笼。
- 要停止生成某一类刷怪笼，删除该生物或将其权重设为 `0`。例如，从 `world.spawners` 中删除 `VILLAGER` 和 `IRON_GOLEM`。
- 要完全不生成刷怪笼，从该世界的方块列表中删除 `SPAWNER`。
- 如果某个列表为空，SkyGrid 会使用其内置列表，并将其写入文件。
- 不能放入刷怪笼的生物（例如 `ARROW`）会被跳过，并在控制台中输出警告。

更改只影响之后生成的区块。

### 网格高度和对齐 { #grid-height-and-alignment }

网格方块每隔 4 格放置一个。自 2.3.0 起，`world.skygrid-height` 会四舍五入到最接近的 4 的倍数（最大 252），使每个玩家区域的中心位于网格层上。

`world.start-x`、`world.start-z` 和 `world.space-around-players` 也应该是 4 的倍数。如果不是，SkyGrid 会记录一条警告，但不会修改它们，因为那样会移动现有世界中的每个区域。

## 权限

权限可以在[这里](Permissions)找到。

## 指令

指令可以在[这里](Commands)找到。

## 占位符

占位符可以在[这里](Placeholders)找到。

## 更新日志

??? warning "v2.2.4 新内容 —— 世界生成修复"
    **发布于：** 2026-11-05

    兼容性：BentoBox API 3.3.1 · Minecraft 1.21.x（在 Paper 26.3 上测试）· Java 21。

    - 🔺 **网格不再充满石头和草。** 原版地形会在网格下方生成，原版地表生成也会把方块替换为草。现在网格位置只会放置你配置中的方块。[PR #88](https://github.com/BentoBoxWorld/SkyGrid/pull/88)
    - 🔺 **区块不再重复。** 每个区块都从相同的随机序列开始，因此同样的图案每 16 格重复一次。现在每个区块都有自己的随机序列。[PR #88](https://github.com/BentoBoxWorld/SkyGrid/pull/88)
    - **甘蔗现在有水了。** 它位于一个小型砂岩水池中，水不会流走。在寒冷的生物群系中水池里的水可能会结冰。[PR #89](https://github.com/BentoBoxWorld/SkyGrid/pull/89)
    - **仙人掌和枯萎的灌木不再悬空。** 它们现在立在砂岩上方的沙子上。[PR #89](https://github.com/BentoBoxWorld/SkyGrid/pull/89)

    🔺 **现有世界：** 已生成的区块不会改变，因此新旧区块交界处会出现明显的不一致。如需一致的网格，请删除你的 SkyGrid 世界并让其重新生成——**这会移除这些世界中的所有岛屿**，请事先与玩家沟通并做好备份。

    [发布 v2.2.4](https://github.com/BentoBoxWorld/SkyGrid/releases/tag/2.2.4)

!!! warning "v2.3.0 新内容 —— 刷怪笼生物，玩家可使用团队和家点命令"
    **发布于：** 2026-11-22

    兼容性：BentoBox API 3.3.1 · Minecraft 1.21.x 和 26.x · Java 21。

    - ⚙️ **可配置的刷怪笼生物。** 新列表 `world.spawners`、`world.nether.spawners` 和 `world.end.spawners` 设定刷怪笼可以包含哪些生物以及各自的常见程度。它们会以与之前相同的概率添加到现有配置中。参见[刷怪笼生物](#spawner-mobs)。[PR #94](https://github.com/BentoBoxWorld/SkyGrid/pull/94)
    - ⚙️ **网格高度与网格对齐。** `skygrid-height` 会四舍五入到最接近的 4 的倍数（最大 252）。网格本身不变，但玩家的出生点最多可能移动 2 格。如果 `start-x`、`start-z` 或 `space-around-players` 不是 4 的倍数，SkyGrid 会发出警告。参见[网格高度和对齐](#grid-height-and-alignment)。[PR #94](https://github.com/BentoBoxWorld/SkyGrid/pull/94)
    - 🔺 **玩家可以使用团队和家点命令。** 有 12 个玩家权限之前没有声明，因此只有操作员拥有：团队的 `invite`、`accept`、`reject`、`kick`、`leave`、`promote` 和 `setowner`，`info`、`near`，以及 `homes`、`renamehome` 和 `deletehome`。现在它们默认授予所有人。参见[权限](Permissions.md)。[PR #92](https://github.com/BentoBoxWorld/SkyGrid/pull/92)
    - ⚙️ **新安装的默认设置。** 八个危险相关的设置对玩家隐藏（`TNT_DAMAGE`、`BLOCK_EXPLODE_DAMAGE`、`FIRE_BURNING`、`FIRE_IGNITE`、`FIRE_SPREAD`、`LEAF_DECAY`、`ENDERMAN_TELEPORT`、`SHULKER_TELEPORT`），`PISTON_PUSH` 会被列出并默认关闭。现有服务器保留其原有的 `config.yml`；如果需要这些设置，请把相应条目复制到 `world.hidden-flags` 和 `world.flags` 中。[PR #93](https://github.com/BentoBoxWorld/SkyGrid/pull/93)

    🔺 **如果你是有意只让操作员或特定等级使用团队或家点命令，** 请在权限插件中将你想继续限制的权限设为否定，例如 `skygrid.island.team.invite`。

    [发布 v2.3.0](https://github.com/BentoBoxWorld/SkyGrid/releases/tag/2.3.0)

## 翻译

{{ translations("SkyGrid") }}