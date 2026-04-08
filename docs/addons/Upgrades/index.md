# Upgrades

**Upgrades** 允许你以金钱和岛屿等级为代价升级岛屿大小、实体/方块限制。

此插件旨在为岛屿添加进度曲线和金钱用途。

由 [Ikkino](https://github.com/Guillaume-Lebegue) 创建和维护。

{{ addon_description("Upgrades", true) }}

## 安装

1. 将 Upgrades 插件 jar 文件放入 BentoBox 插件的 addons 文件夹
2. 重启服务器
3. 插件将创建一个数据文件夹,里面有一个 config.yml
4. 根据需要编辑 config.yml。
5. 如果进行了更改,请重启服务器

## 命令

!!! tip
    `[player_command]` 是一个根据你运行的游戏模式而不同的命令。
    游戏模式的 `config.yml` 文件包含允许你修改此值的选项。
    例如,在 BSkyBlock 中,默认的 `[player_command]` 是 `island`。

有一个用户命令可以打开带有升级的 GUI。

`/[Player command] upgrade`

## 设置 - Config.yml

config.yml 有以下部分:

* range-upgrade
* block-limits-upgrade
* entity-limits-upgrade
* command-upgrade
* gamemodes
* entity-icon
* command-icon

!!! tip
    所有 `upgrade`、`island-min-level` 和 `vault-cost` 字段都是数学表达式。因此:

    * 可以使用 +、-、*、/、^、(、)
    * 可以使用 sqrt()、sin()、cos()、tan()
    * `[level]` 被替换为此升级的实际等级
    * `[islandLevel]` 被替换为来自 level 插件的岛屿等级 **(可以为 0)**
    * `[numberPlayer]` 被替换为团队中的玩家数量

### 通用

一个升级按"阶段"划分,可以随意命名

示例:
```yml
tier1:
  max-level: 5
  upgrade: "5"
  island-min-level: "2"
  vault-cost: "[level]*100"
  permission-level: 1
```

* `max-level` 是此阶段的最高等级。
* `upgrade` 是每个等级给予的数量。
* `island-min-level` 是购买此升级所需的最低岛屿等级。它由 [Level 插件](/addons/Level) 提供。
* `vault-cost` 是购买此升级的费用 **(>= 0)**
* `permission-level` 是购买此升级所需的权限等级(参见权限)。

### 范围升级

此升级增加岛屿的保护范围。

范围增加在 `upgrade` 字段中给出。

示例:
```yaml
range-upgrade:
  tier1:
    max-level: 5
    upgrade: "5"
    island-min-level: "2"
    vault-cost: "[level]*100"
  tier2:
    max-level: 10
    upgrade: "3"
    island-min-level: "4"
    vault-cost: "[level]*[numberPlayer]*200"
```

!!! warning "最大范围"
    你应该始终检查,即使在最大升级时,保护范围也不会超过岛屿之间的大小。

### 方块限制升级

此升级增加 [Limits 插件](/addons/Limits) 中设置的方块限制。

要添加到限制中的数字由 `upgrade` 字段给出。

示例:
```yaml
block-limits-upgrade:
  HOPPER:
    tier1:
      max-level: 2
      upgrade: "1" 
      island-min-level: "2"
      vault-cost: "[level]*100"
    tier2:
      max-level: 5
      upgrade: "1"
      island-min-level: "4"  
      vault-cost: "([level]-2)*[numberPlayer]*700"
      permission-level: 1
```

!!! tip "方块"
    方块列表可以在[这里](https://hub.spigotmc.org/javadocs/bukkit/org/bukkit/Material.html)找到

### 实体限制升级

此升级增加 [Limits 插件](/addons/Limits) 中设置的实体限制。

所有实体都需要有相应的图标(参见: [entity-icon](#entity-icon))

要添加到限制中的数字由 `upgrade` 字段给出。

示例:
```yaml
entity-limits-upgrade:
  CHICKEN:
    tier1:
      max-level: 2
      upgrade: "1"
      island-min-level: "2"
      vault-cost: "[level]*100"
    tier2:
      max-level: 5
      upgrade: "1"
      island-min-level: "4"
      vault-cost: "([level]-2)*[numberPlayer]*700"
      permission-level: 3
```

!!! tip "实体"
    实体列表可以在[这里](https://hub.spigotmc.org/javadocs/spigot/org/bukkit/entity/EntityType.html)找到

### 命令升级

此升级在每次升级时运行给定的命令。

所有命令升级都需要有相应的图标(参见: [command-icon](#command-icon))

在配置中:

* 部分的名称是升级的真实名称
* `name` 字段只是显示名称。不在权限中使用。
* `console` 字段指定命令是应由控制台启动还是由玩家启动
* `command` 字段是包含要运行的所有命令的列表。它们按列表顺序启动

!!! tip "命令字段"
    在命令字段中:

    * `[player]` 被替换为购买升级的玩家的名字
    * `[level]` 被替换为升级的等级

示例:
```yaml
command-upgrade:
  lambda-upgrade:
    name: "Lambda upgrade"
    tier1:
      max-level: 1
      island-min-level: "2"
      vault-cost: "[level]*100"
      console: true
      command:
        - "say [player] has upgrade his lambda to level [level]"
    tier2:
      max-level: 2
      island-min-level: "2"
      vault-cost: "[level]*200"
      console: true
      command: 
        - "say [player] has upgrade his lambda to level [level]"
        - "say [player] has reached the max level"
```

### 游戏模式

可以在每个游戏模式之间设置升级差异。

示例:
```yaml
gamemodes:
  BSkyBlock:

    range-upgrade:
      tier3:
        max-level: 15
        upgrade: "5"
        island-min-level: "6"
        vault-cost: "[level]*[numberPlayer]*500"

    block-limits-upgrade:
      HOPPER:
        tier1:
          max-level: 2
          upgrade: "1"
          island-min-level: "2"
          vault-cost: "[level]*200"
```

### 实体图标

本部分用于将实体链接到图标。

语法如下:

`ENTITY: MATERIAL`

示例:
```yaml
entity-icon:
  CHICKEN: CHICKEN_SPAWN_EGG
```

!!! tip "实体"
    实体列表可以在[这里](https://hub.spigotmc.org/javadocs/spigot/org/bukkit/entity/EntityType.html)找到

!!! tip "材料"
    材料列表可以在[这里](https://hub.spigotmc.org/javadocs/bukkit/org/bukkit/Material.html)找到

### 命令图标

本部分用于将命令升级链接到图标。

语法如下:

`NAME: MATERIAL`

`NAME` 是命令升级的真实名称(!=显示名称)

示例:
```yaml
command-icon:
  lambda-upgrade: GRASS
```

!!! tip "材料"
    材料列表可以在[这里](https://hub.spigotmc.org/javadocs/bukkit/org/bukkit/Material.html)找到

## 权限

可以有购买升级的权限。

要做到这一点,应该将大于 0 的 `permission-level` 添加到升级中。要购买升级,玩家需要有一个大于或等于此等级的等级。默认情况下,玩家在任何地方都有 0 级。

权限如下:

`[GAMEMODE].upgrades.[UPGRADE].[LEVEL]`

其中:

* `[GAMEMODE]` 是应设置此权限的游戏模式的名称
* `[UPGRADE]` 是升级的名称(参见: [升级名称](#升级名称))
* `[LEVEL]` 是要给玩家的等级

示例:

`bskyblock.upgrades.range-upgrade.2`

!!! warning
    权限为小写

!!! tip
    因为权限是在运行时创建的,所以它不会出现在权限列表中

### 升级名称

**范围升级**:

`rangeupgrade` | 示例: `bskyblock.upgrades.range-upgrade.1`

**方块限制升级**:

`limitsupgrade-[BLOCK]` | 示例: `bskyblock.upgrades.limitsupgrade-hopper.8`

**实体限制升级**:

`limitsupgrade-[ENTITY]` | 示例: `bskyblock.upgrades.limitsupgrade-chicken-hopper.4`

**命令升级**:

`command-[NAME]` | 示例: `bskyblock.upgrades.command-lambda-upgrade.6`

`NAME` 是命令升级的真实名称(!=显示名称)

## 翻译

{{ translations("Upgrades") }}