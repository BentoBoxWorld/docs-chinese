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

### 管理员命令

* `chatspy` - 切换岛屿聊天的开启和关闭
* `teamchatspy` - 切换玩家的聊天是否进入团队频道

配置还包含了必要时记录所有聊天的设置。

## 配置

```
# 聊天插件的配置文件
team-chat:
  gamemodes:
  - BSkyBlock
  - AcidIsland
  - CaveBlock
  - SkyGrid
  # 将团队聊天记录到控制台。
  log: false
island-chat:
  # 列出你希望聊天插件生效的游戏模式。
  gamemodes:
  - BSkyBlock
  - AcidIsland
  - CaveBlock
  - SkyGrid
  # 将岛屿聊天记录到控制台。
  log: false
chat-listener:
  # 设置AsyncPlayerChatEvent的优先级。如果聊天插件与其他监听同一事件的插件冲突，请更改此设置
  # 可接受的值：lowest, low, normal, high, highest, monitor
  priority: normal
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
  '[gamemode].chat.spy':
    description: 玩家可以使用团队或岛屿聊天间谍
    default: op

```

## 喜欢这个插件吗？
你可以[赞助](https://github.com/sponsors/tastybento)来获得更多这样的插件并使这个插件变得更好！

## 翻译

{{ translations("Chat") }}