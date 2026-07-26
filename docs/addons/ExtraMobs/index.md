# ExtraMobs
ExtraMobs 调整了一些生物生成规则,以获得烈焰人、凋灵骷髅和潜影贝。
由 [BONNe](https://github.com/BONNe) 创建和维护。
{{ addon_description("ExtraMobs", beta=True) }}
## 安装
1. 将插件 jar 文件放入 BentoBox 插件的 addons 文件夹
2. 重启服务器
3. 在游戏中,你可以更改允许使用当前插件的标志。
## 信息
此插件不会更改 Minecraft 生成规则。相反,它使用其他自然生成的生物,如果满足所有条件,则将它们的类型更改为新实体。
##### 对于凋灵骷髅和烈焰人:
如果满足以下条件,插件将按照配置中的几率将僵尸猪人替换为烈焰人或凋灵骷髅:
- 给定的世界由游戏模式插件生成。
- 给定的世界是下界
- 僵尸猪人站在下界砖、下界砖台阶或下界砖楼梯上。
##### 对于潜影贝:
如果满足以下条件,插件将按照配置中的几率将末影人替换为潜影贝:
- 给定的世界由游戏模式插件生成。
- 给定的世界是末地
- 末影人站在紫珀块、紫珀楼梯或紫珀台阶上。
##### 对于守卫者:
如果满足以下条件,插件将按照配置中的几率将鳕鱼、鲑鱼或热带鱼替换为守卫者:
- 给定的世界由游戏模式插件生成。
- 给定的世界是主世界
- 给定位置的生物群系是深海或其任何变体
- 鱼生成位置上方的第一个方块是海晶石、海晶石砖或暗海晶石(方块、台阶和楼梯)。
## 配置

最新的 `config.yml` 可在[此处](https://github.com/BentoBoxWorld/ExtraMobs/blob/develop/src/main/resources/config.yml)查看。

??? note "disabled-gamemodes"
    列出本插件不应生效的游戏模式。每一项单独占一行，以 `-` 开头。

    默认值：`[]`（为空，即插件在所有游戏模式中都生效）

??? note "nether-chances"
    在下界替换僵尸猪人的几率。`wither-skeleton` 和 `blaze` 各是一个 0.0–1.0 范围内的概率。

    默认值：`wither-skeleton: 0.01`、`blaze: 0.1`

??? note "end-chances"
    `shulker` —— 在末地把末影人替换为潜影贝的几率。

    默认值：`0.1`

??? note "overworld-chance"
    `guardian` —— 在主世界把鳕鱼、鲑鱼或热带鱼替换为守卫者的几率。

    默认值：`0.1`

??? note "gamemode-settings"
    按游戏模式区分的替换规则，可覆盖上面的全局几率。1.15.0 新增。

    每个键都是游戏模式插件的确切名称（区分大小写），每个游戏模式最多可以定义三个环境小节——`world:` 表示主世界、`nether:` 表示下界、`end:` 表示末地。每个小节是一组规则，每条规则包含 `old`（要被替换的 `EntityType`）、`new`（替换后的 `EntityType`）和 `chance`（0.0–1.0）。

    对应环境下会先按顺序尝试该游戏模式的规则，然后才轮到全局默认值。如果某条规则匹配了正在生成的实体**并且**概率判定通过，就执行替换，本次事件的处理到此结束。如果没有规则匹配，或者所有匹配规则的概率判定都失败，则回退到全局的 `nether-chances` / `end-chances` / `overworld-chance` 值。

    默认值：`{}` —— 需要主动启用，因此未在此列出的游戏模式仍然沿用全局几率。

    ```yaml
    gamemode-settings:
      BSkyBlock:
        nether:
          - old: ZOMBIFIED_PIGLIN
            new: WITHER_SKELETON
            chance: 0.05
          - old: ZOMBIFIED_PIGLIN
            new: BLAZE
            chance: 0.1
        end:
          - old: ENDERMAN
            new: SHULKER
            chance: 0.3
        world:
          - old: COD
            new: GUARDIAN
            chance: 0.15
      AcidIsland:
        end:
          - old: ENDERMAN
            new: SHULKER
            chance: 0.5
    ```

## 兼容性

- [x] BentoBox 3.14.0 或更高版本
- [x] Paper Minecraft 1.21.x
- [x] Java 21 或更高版本

本插件支持所有游戏模式插件。

## 翻译

{{ translations("ExtraMobs") }}

## 更新日志

!!! note "v1.15.0 新内容 — 需要 Java 21 和 BentoBox 3.14.0"
    **发布于：** 2026-05-31

    兼容性：BentoBox API 3.14.0+ · Paper Minecraft 1.21.x · Java 21+。

    - ⚙️ **按游戏模式区分的生成替换规则。** 新增的 `gamemode-settings` 配置块可以为每个 BentoBox 游戏模式分别定义替换规则，而不再是整台服务器共用一套全局设置。它默认为 `{}`，需要主动启用，因此未列出的游戏模式仍沿用原有的全局几率值。详见上面的"配置"章节。
    - 🔺 **现在需要 Java 21 和 BentoBox 3.14.0。** 升级前请确认服务器同时满足这两项要求。
    - **新增 Pladdon 入口点和 `plugin.yml`，** 使本插件作为现代 BentoBox 插件加载。
    - 测试套件基于 JUnit 5 与 MockBukkit 重建，新增了带 SonarCloud 分析的 GitHub Actions 构建，并修复了若干可维护性问题。

    [发布 v1.15.0](https://github.com/BentoBoxWorld/ExtraMobs/releases/tag/1.15.0)