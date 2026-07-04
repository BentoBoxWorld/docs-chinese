# 聊天

**聊天**插件提供了**团队聊天**和**岛屿聊天**功能，让玩家可以与访客或岛屿成员私密交谈。

由[tastybento](https://github.com/tastybento)创建和维护。

{{ addon_description("Chat") }}

## 岛屿聊天

启用后，聊天将仅限于岛屿上的玩家，包括访客。管理员或版主可以使用间谍命令监听岛屿聊天。

## 团队聊天

启用后，聊天将仅发送给团队成员。团队玩家可以切换他们的聊天是否进入团队聊天频道。管理员可以使用间谍命令监听所有团队聊天。

## 命令
### 玩家命令

* `chat` - 切换岛屿聊天的开启和关闭
* `teamchat` - 切换玩家的聊天是否进入团队频道
* `muteteamchat`（别名 `mtc`）- 静音传入的团队聊天消息，无需禁用团队聊天。需要 `[gamemode].chat.team-chat.mute` 权限。当玩家离开或被踢出团队时，静音状态会自动清除。

### 管理员命令

* `chatspy` - 切换岛屿聊天间谍的开启和关闭
* `teamchatspy` - 切换团队聊天间谍的开启和关闭

配置还包含了必要时记录所有聊天的设置。

## 配置

```yaml
# 聊天插件的配置文件
team-chat:
  # 列出你希望团队聊天生效的游戏模式。
  gamemodes:
  - BSkyBlock
  - AcidIsland
  - CaveBlock
  - SkyGrid
  # 如果玩家在游戏世界外，团队聊天仍然可以为一个游戏模式存在。
  default-teamchat-gamemode: ''
  # 每个游戏模式的额外世界，其中应该捕获团队聊天。
  # 适用于玩家仍然希望团队聊天工作的共享生成点/中心世界。
  # 如果多个游戏模式覆盖一个世界，聊天可能会发送到多个团队。
  # 示例：
  #   extra-chat-worlds:
  #     BSkyBlock:
  #       - world
  #       - world_nether
  #       - spawn_world
  extra-chat-worlds: {}
  # 将团队聊天记录到控制台。
  log: false
island-chat:
  # 列出你希望岛屿聊天生效的游戏模式。
  gamemodes:
  - BSkyBlock
  - AcidIsland
  - CaveBlock
  - SkyGrid
  # 将岛屿聊天记录到控制台。
  log: false
chat-listener:
  # 设置 AsyncPlayerChatEvent 的优先级。如果聊天插件与其他监听同一事件的插件冲突，请更改此设置。
  # 可接受的值：lowest、low、normal、high、highest、monitor
  priority: NORMAL
```

## 权限

```
permissions:
  '[gamemode].chat.team-chat':
    description: 玩家可以使用团队聊天
    default: true
  '[gamemode].chat.island-chat':
    description: 玩家可以使用岛屿聊天
    default: true
  '[gamemode].chat.team-chat.mute':
    description: 玩家可以使用 /is muteteamchat 静音传入的团队聊天
    default: true
  '[gamemode].chat.spy':
    description: 玩家可以使用团队或岛屿聊天间谍
    default: op
```

## 喜欢这个插件吗？
你可以[赞助](https://github.com/sponsors/tastybento)来获得更多这样的插件并使这个插件变得更好！

## 更新日志

??? note "v1.4.0 新内容"
    **发布于：** 2026-04-13

    - **额外世界中的团队聊天** — 团队聊天现在可以在游戏模式世界外工作。在 `config.yml` 中使用 `team-chat.extra-chat-worlds` 列出每个游戏模式的额外世界（生成点、中心等），其中应该捕获团队聊天。
    - **静音团队聊天** — 玩家可以使用 `/is muteteamchat` 静音传入的团队聊天，无需离开他们的团队。静音在离开/被踢出团队时自动清除。
    - **MiniMessage 迁移** — 所有 23 个语言文件已从旧版 `&` 颜色代码转换为 MiniMessage。如果你自定义了语言文件，请将 `&a` → `<green>` 等更新，或删除它们以重新生成。
    - 错误修复：玩家在没有岛屿的情况下使用 `/is teamchat` 时的空指针异常。

    [发布 v1.4.0](https://github.com/BentoBoxWorld/Chat/releases/tag/1.4.0)

??? note "v1.4.1 新内容"
    **发布于：** 2026-04-26

    - 🔡 **捷克语语言文件修复** — `cs.yml` 中 `island-chat-spy` 条目的 YAML 格式错误，导致服务器启动时出现 `ScannerException`。请在重启前删除 `plugins/BentoBox/addons/Chat/locales/cs.yml`，以便从已修复的版本重新生成。

    [发布 v1.4.1](https://github.com/BentoBoxWorld/Chat/releases/tag/1.4.1)

## 翻译

{{ translations("Chat") }}