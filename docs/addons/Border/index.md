# Border

**Border** 可以在玩家无法通过的岛屿周围创建并显示边界。
边界可以是:

- 原版的世界边界
- 一个自定义边界,当玩家靠近时会显示(可以在配置中设置视觉效果)。

由 [tastybento](https://github.com/tastybento) 创建和维护。

{{ addon_description("Border") }}

## 安装

1. 重启服务器(启用插件并生成 `config.yml` 文件)
2. 将插件 jar 文件放入 `plugins/BentoBox/addons` 文件夹
3. 在 `config.yml` 中自定义设置(可选) 
4. 重启服务器以应用新设置

## 命令

!!! tip
    `[player_command]` 是一个根据你运行的游戏模式而不同的命令。
    游戏模式的 `config.yml` 文件包含允许你修改此值的设置。
    例如,在 BSkyBlock 中,默认的 `[player_command]` 是 `island`。

### border
**命令**: `/[player command] border`
**描述**: 打开/关闭边界。
**权限**: `[gamemode].border.toggle`。默认: `op`。 
**注意**: 自 Version 3.0.0 起需要权限。

### border type {...}  
**命令**: `/[player command] border type {barrier | vanilla}`
**描述**: 设置边界类型。不带参数运行可在可用类型之间切换。
**权限**: `[gamemode].border.type`。默认: `true`。
**示例**: `/[player command] border type barrier`

### border color {red|green|blue}
**命令**: `/[player command] border color {red | green | blue}`
**描述**: 为玩家设置原版世界边界颜色。仅在使用原版边界类型时适用。
**权限**: `[gamemode].border.color.red`、`[gamemode].border.color.green`、`[gamemode].border.color.blue`（或 `[gamemode].border.color.*` 表示全部）。默认: `op`。
**示例**: `/[player command] border color green`

!!! tip
    `[gamemode]` 是一个根据你运行的游戏模式而不同的前缀。
    前缀是游戏模式的小写名称,即如果你使用 BSkyBlock,前缀就是 `bskyblock`。
    类似地,如果你使用 AcidIsland,前缀就是 `acidisland`。

## 配置

`config.yml` 文件包含设置。
除非明确说明,否则默认值通常就是示例值。

### 禁用游戏模式 
你可以使用此设置禁用插件。
默认情况下,Border 将在 BentoBox 服务器上的所有游戏模式世界中运行。

你可以通过在新行的开头写上 `-` 并接上游戏模式的名称来禁用它。
示例禁用 BSkyBlock:

```yml
disabled-gamemodes:
  - BSkyBlock  
```

默认值:

```yml
disabled-gamemodes: []
```

### 边界类型
新玩家获得的默认边界种类。有两种选择：

- `VANILLA` —— 使用 Minecraft 自带的圆形世界边界效果（你在原版游戏中看到的晃动的墙）。它可以被染上颜色。
- `BARRIER` —— 使用不可见的屏障方块和彩色粒子，只有当你靠近边缘时才会出现。

拥有权限的玩家可以使用 `/[player command] border type` 切换自己的边界。如果他们没有权限，就会使用你在这里设置的类型。

```yml
type: VANILLA
```

### 原版边界颜色
原版世界边界的颜色。仅在边界类型为 `VANILLA` 时使用。  
可选值为 `RED`、`GREEN` 或 `BLUE`。拥有权限的玩家可以使用 `/[player command] border color` 选择自己的颜色。

```yml
color: BLUE
```

### 弹回物品
如果为 `true`，玩家向边界扔出的物品会被弹回内侧，而不是飞出去。设置为 `false` 可让扔出的物品穿过。

```yml
bounce-back: true
```

### 返回传送
控制如果玩家设法穿过边界(例如在同一个世界传送),是否应将他们传送回他们的岛屿。

如果你希望玩家被传送回来,请设置为 `true`。

**警告**: 如果你将此值设置为 `false`,同时将 `use-barrier-blocks` 设置为 `false`,玩家将能够直接穿过边界。

```yml
return-teleport: true
```

!!! tip
    如果你想 **只用此插件来显示** 玩家的边界,请使用以下设置:
    ```yml
    use-barrier-blocks: false
    return-teleport: false 
    ```

### 返回传送安全方块
仅在 `return-teleport` 为 `true` 时使用。如果玩家被传送回边界内侧并落在不安全的地方（例如悬崖上方或岩浆中），此设置会在他们脚下放置一个安全方块，使他们不会受伤。

```yml
return-teleport-safety-block: true
```

### 使用屏障方块
仅适用于 **不** 使用原版边界类型的玩家。

- `true`: 边界将由屏障方块组成。
- `false`: 不会有基于屏障方块的边界。这意味着当离开岛屿时,玩家是否被传送回去取决于 `return-teleport` 设置。

```yml 
use-barrier-blocks: true
```

### 默认边界行为
如果玩家拥有适当的权限,他们可以使用命令打开和关闭边界。
此设置将默认值设置为打开或关闭;将其设置为 `true` 以默认打开。

```yml
show-by-default: true  
```

### 显示最大保护范围边界
仅适用于 **不** 使用原版边界类型的玩家。

设置为 `true` 以在最大保护范围显示屏障(🚫)粒子。
这对于像 Boxed 这样玩家的保护区域可以移动的游戏模式很有用。

请注意,这些 **不是屏障方块**,而是 _粒子_,所以"空气"只是 _看起来像_ 它们。

```yml
show-max-border: true
```

### 显示粒子
启用/禁用插件显示的所有类型的墙粒子(边界和最大保护范围粒子)。

如果你不想显示 **任何** 墙粒子,请设置为 `false`。

```
show-particles: true  
```

### 屏障偏移
仅适用于 **不** 使用原版边界类型的玩家。

通常边界正好位于玩家保护范围的边缘。此设置将屏障**向外**推移你所给定的方块数，因此玩家可以在撞到墙之前走出他们的受保护区域一小段距离。

需要了解的重点：

- 它**不会**扩大受保护区域 —— 玩家仍然无法在多出的空间建造或保护，他们只能站在那里。
- 无论你设置多大的数值，边界都不会超出岛屿间距。
- 最小值（也是默认值）为 `0`，表示边界正好位于保护范围上。

```yml
barrier-offset: 0
```

## 占位符

| 占位符 | 描述 | 版本 |
|---|---|---|
| `%Border_color%` | 玩家当前的边界颜色(red/green/blue) | 4.8.0 |

## 常见问题

??? question "我怎么改变边界的大小？"
    边界本身没有独立的大小 —— 它是围绕每个岛屿的**保护范围**绘制的。所以要让边界变大或变小，你需要改变保护范围。

    - 通过类似 `[gamemode].island.range.<number>` 的权限给玩家更大的范围（例如 `bskyblock.island.range.150`）。
    - 管理员可以用管理员范围命令为特定岛屿设置范围，例如 `/bsbadmin range set <player> <number>`。
    - 范围永远不能大于**岛屿间距的一半**，而该间距在世界创建时设置一次，之后无法更改。

    完整细节请参阅[岛屿范围和间距](../../BentoBox/About/IslandManagement.md#岛屿范围和间距)。

??? question "我可以让边界比岛屿的范围稍大一些吗？"
    可以！使用 `config.yml` 中的 `barrier-offset` 设置。它会将边界向外推移你所选择的方块数，因此玩家可以在撞到墙之前走出他们的受保护区域一小段距离。

    请记住这只会移动墙 —— 它**不会**给玩家任何可以建造或保护的额外土地。参见上面的[屏障偏移](#屏障偏移)设置。

??? question "屏障和原版边界类型有什么区别？"
    - **原版**使用 Minecraft 内置的世界边界效果 —— 你在普通游戏中已经熟悉的闪烁的墙。你可以将它染成红色、绿色或蓝色。
    - **屏障**使用不可见的屏障方块加上彩色粒子，只有当你靠近边缘时才会显示。

    拥有权限的玩家可以用 `/[player command] border type` 在两者之间切换。

??? question "我不想要一堵实体墙 —— 能否只显示一条玩家可以穿过的线？"
    可以。设置 `use-barrier-blocks: false` 使其没有实体墙，并设置 `return-teleport: false` 使玩家不会被拉回。这样就只剩下视觉边界。在 `config.yml` 中加入：

    ```yml
    use-barrier-blocks: false
    return-teleport: false
    ```

??? question "我怎么改变边界的颜色？"
    颜色只在**原版**边界类型下有效。在 `config.yml` 中用 `color` 设置一个服务器范围的默认值（`RED`、`GREEN` 或 `BLUE`）。拥有权限的玩家可以在游戏中用 `/[player command] border color {red|green|blue}` 选择自己的颜色。

??? question "我怎么关闭边界？"
    玩家可以用 `/[player command] border` 打开或关闭自己的边界（他们需要 `[gamemode].border.toggle` 权限）。要让所有人默认关闭，请在 `config.yml` 中设置 `show-by-default: false`。

??? question "边界没有显示 —— 我该检查什么？"
    - 确保该游戏模式没有列在 `config.yml` 的 `disabled-gamemodes` 下。
    - 检查玩家是否确实打开了边界（`/[player command] border`），以及 `show-by-default` 是否为 `true`。
    - 边界只在你自己岛屿的保护范围周围显示，所以你需要靠近边缘才能看到它。
    - 如果你使用**屏障**类型并设置了 `show-particles: false`，那么在你触碰之前墙是不可见的 —— 这是预期行为。

??? question "你能添加某个功能 X 吗？"
    请在[问题追踪器](https://github.com/BentoBoxWorld/Border/issues)上提出请求。

## 更新日志

??? note "v4.7.0 → v4.8.2 新内容"
    **发布于:** 2026-02-16 至 2026-04-04

    - **原版世界边界颜色选择。** 使用原版边界类型的玩家现在可以通过 `/[player_command] color {red|green|blue}` 选择自己的边界颜色——红色、绿色或蓝色。
    - 新占位符 `%Border_color%`，返回玩家当前的边界颜色。
    - 新权限 `[gamemode].color.red`、`[gamemode].color.green`、`[gamemode].color.blue`（或使用 `[gamemode].color.*` 授予全部颜色）。默认值：op。
    - 错误修复：玩家位于所有岛屿区域之外时，边界传送可被绕过（4.7.0）。
    - 错误修复：玩家在岛屿之间传送时原版世界边界未重置——导致 Bedrock/Geyser 玩家进入受限状态（4.8.1）。
    - 错误修复：在某些配置下 `%Border_color%` 占位符抛出空值错误（4.8.1）。
    - 错误修复：边界在原版下界和末地世界中错误地被激活（4.8.1）。

    [发布 v4.7.0](https://github.com/BentoBoxWorld/Border/releases/tag/4.7.0) · [v4.8.0](https://github.com/BentoBoxWorld/Border/releases/tag/4.8.0) · [v4.8.1](https://github.com/BentoBoxWorld/Border/releases/tag/4.8.1) · [v4.8.2](https://github.com/BentoBoxWorld/Border/releases/tag/4.8.2)

??? note "v4.8.3 新内容"
    **发布于：** 2026-04-26

    - 🔡 所有语言文件从旧版 `&` 颜色代码转换为 MiniMessage 格式。
    - 🔡 所有非英语语言文件添加了缺失的 `set-color` 键。
    - 🔡 修复了波兰语、乌克兰语和中文语言文件的错误。
    - 🔺 最低 BentoBox API 版本提升至 **3.12.0**。

    🔺 **如果您维护自定义语言文件覆盖**（位于 `plugins/BentoBox/addons/Border/locales/`），请在重启前将颜色代码从 `&a` 样式迁移至 MiniMessage 标签（如 `<green>`）。

    [Release v4.8.3](https://github.com/BentoBoxWorld/Border/releases/tag/4.8.3)

??? note "v4.8.4 新内容"
    **发布于：** 2026-05-26

    - 🐛 **修复 Paper/Purpur 1.21.10 上的 `NoSuchMethodError: WorldBorder.changeSize`。** 4.8.3 构建针对 Paper 1.21.11 编译,而该版本重命名了世界边界方法,因此在 1.21.10 服务器上使用 `/[player_command] bordertype vanilla` 时原版边界类型会崩溃。Border 现在使用跨版本兼容的 `setSize` API,可在 **1.21.10 和 1.21.11** 上运行。
    - 🐛 修复 Modrinth 发布工作流(构件路径错误)。

    无需更改配置或语言文件。如果你之前用 `bordertype barrier` 绕过此问题,安装 4.8.4 后即可切换回 `vanilla`。

    [发布 v4.8.4](https://github.com/BentoBoxWorld/Border/releases/tag/4.8.4)

## 翻译

{{ translations("Border") }}

## 来源
想要贡献?在 [GitHub](https://github.com/BentoBoxWorld/docs/blob/master/docs/addons/Border/) 上查看本文档的源代码。