# 查看我

这是一个岛屿提交插件。此插件使玩家能够提交他们的岛屿供管理员考虑。通过这种方式，管理员可以设置全站挑战或比赛，玩家可以进行然后提交他们的岛屿供考虑。管理员获得一个列表提交的GUI，并且他们可以从那里传送到岛屿。一旦岛屿被管理员审核，它可以被删除，或当整个活动结束时，所有提交可以被清除。

由[tastybento](https://github.com/tastybento)创建和维护。

{{ addon_description("CheckMeOut") }}

## 安装

0. 安装BentoBox并至少运行一次服务器以创建其数据文件夹。
1. 将此jar文件放在BentoBox插件的addons文件夹中。
2. 重启服务器。
3. 插件将创建一个数据文件夹，并在文件夹内部会有一个config.yml文件。
4. 停止服务器。
5. 根据你的意愿编辑config.yml文件。
7. 重启服务器。

## 配置

主要的`config.yml`文件包含有关游戏模式插件设置的基本信息。

`panels`允许自定义一些用户可访问的面板。

### config.yml

插件安装成功后，它将创建config.yml文件。这个文件中的每个选项都附有注释。请查阅文件以获取更多信息。
你可以在这里找到最新的配置文件：[config.yml](https://github.com/BentoBoxWorld/CheckMeOut/blob/develop/src/main/resources/config.yml)

### 可自定义的GUI

BentoBox 1.17 API引入了一个功能，允许实现可自定义的GUI。这个插件是第一个使用这个功能的插件之一。我们试图尽可能简单地进行自定义，然而，一些功能需要解释。
你可以在这里找到更多关于BentoBox自定义GUI如何工作的信息：[自定义GUI](/en/latest/Tutorials/generic/Customizable-GUI/)

??? 问题 "如何自定义GUI"
    要自定义插件GUI，你需要拥有1.1版本。这是第一个实现它们的版本。插件将在`/plugins/BentoBox/addons/CheckMeOut`下创建一个名为`panels`的新目录

    目前你可以自定义1个GUI：

    - 主面板：`view_panel` - 包含已提交岛屿的面板。

??? 问题 "什么是`PREVIOUS`|`NEXT`按钮类型？"
    PREVIOUS和NEXT按钮类型允许创建自动分页，当你的岛屿多于GUI中的空间时。
    这些类型在数据下有额外的参数：

    - `indexing` - 表示按钮是否会显示页码。

    示例：
    ```yaml
        icon: tipped_arrow[potion_contents={custom_color:11546150}]
        title: checkmeout.gui.buttons.previous.name
        description: checkmeout.gui.buttons.previous.description
        data:
          type: PREVIOUS
          indexing: true
        action:
          left:
            action: PREVIOUS
            tooltip: checkmeout.gui.tips.click-to-previous
    ```

??? 问题 "什么是`RANDOM`按钮类型？"
    这个按钮允许玩家传送查看一个随机提交。

    - warp动作仅在你安装了Warps插件且玩家有现有的warps标志时可用。
    - visit动作仅在你安装了Visits插件时可用。
    - check动作是默认的插件传送机制。

    示例：
    ```yaml
        icon: DROPPER
        title: checkmeout.gui.buttons.random.name
        description: checkmeout.gui.buttons.random.description
        data:
          type: RANDOM
        actions:
          # Warp动作需要WARP插件。如果没有WARP插件，warp动作将不起作用。
          warp:
            click-type: UNKNOWN
            tooltip: checkmeout.gui.tips.click-to-warp
          # Visit动作需要Visit插件。如果没有Visit插件，visit动作将不起作用。
          visit:
            click-type: UNKNOWN
            tooltip: checkmeout.gui.tips.click-to-visit
          # Check动作需要玩家拥有"[gamemode].checkmeout.admin.check"权限。
          check:
            click-type: UNKNOWN
            tooltip: checkmeout.gui.tips.click-to-check
    ```

??? 问题 "什么是`ISLAND`按钮类型？"
    这个按钮在主面板中可用。
    ISLAND按钮为岛屿对象创建一个动态条目。

    指定标题、描述和图标将覆盖基于数据库数据的动态生成。默认情况下，这些值将从数据库条目中生成。
    这个按钮支持3种不同的操作类型：

    - warp动作仅在你安装了Warps插件且玩家有现有的warps标志时可用。
    - visit动作仅在你安装了Visits插件时可用。
    - check动作是默认的插件传送机制。

    示例： 
    ```yaml
      # icon: PLAYER_HEAD
      title: checkmeout.gui.buttons.island.name
      description: checkmeout.gui.buttons.island.description
      data:
        type: ISLAND
      actions:
        # Warp动作需要WARP插件。如果没有WARP插件，warp动作将不起作用。
        warp:
          # Click type UNKNOWN意味着它接受任何点击类型。
          click-type: UNKNOWN
          tooltip: checkmeout.gui.tips.click-to-warp
        # Visit动作需要Visit插件。如果没有Visit插件，visit动作将不起作用。
        visit:
          # Click type UNKNOWN意味着它接受任何点击类型。
          click-type: UNKNOWN
          tooltip: checkmeout.gui.tips.click-to-visit
        # Check动作需要玩家拥有"[gamemode].checkmeout.admin.check"权限。
        check:
          # Click type UNKNOWN意味着它接受任何点击类型。
          click-type: UNKNOWN
          tooltip: checkmeout.gui.tips.click-to-check
    ```

## 命令

!!! 小贴士
    `[player_command]`和`[admin_command]`是根据你运行的游戏模式而变化的命令。
    游戏模式的`config.yml`文件包含允许你修改这些值的选项。
    例如，在BSkyBlock上，默认的`[player_command]`是`island`，默认的`[admin_command]`是`bsbadmin`。
    请注意，这个插件允许在插件的`config.yml`文件中更改玩家命令别名。

=== "玩家命令"
    - `/[player_command] checkmeout`：提交岛屿供审核。
    - `/[player_command] checkmeout view`：打开GUI，允许查看其他提交的岛屿。

=== "管理员命令"
    - `/[admin_command] checkmeout`：主管理员命令。
    - `/[admin_command] checkmeout check <player>`：传送玩家到提交的岛屿。
    - `/[admin_command] checkmeout clearall`：移除所有提交的岛屿。
    - `/[admin_command] checkmeout delete <player>`：移除<player>提交的岛屿。
    - `/[admin_command] checkmeout seesubs`：打开菜单查看所有提交的岛屿。

## 权限

!!! 小贴士
    `[gamemode]`是一个前缀，根据你运行的游戏模式而变化。
    前缀是游戏模式的小写名称，即如果你使用BSkyBlock，前缀是`bskyblock`。
    类似地，如果你使用AcidIsland，前缀是`acidisland`。

=== "玩家权限"
    - `[gamemode].checkmeout` - 让玩家使用 '/[player_command] checkmeout' 命令提交岛屿。默认为真。
    - `[gamemode].checkmeout.view` - 让玩家使用 '/[admin_command] checkmeout view' 命令查看所有提交的岛屿。默认为真。
    - `checkmeout.icon.[material]` - 允许更改玩家在View GUI中拥有的岛屿图标。默认为假。

=== "管理员权限"
    - `[gamemode].checkmeout.admin.check` - 让玩家使用'/[admin_command] checkmeout check'命令。默认为OP。
    - `[gamemode].checkmeout.admin.delete` - 让玩家使用'/[admin_command] checkmeout delete'命令。默认为OP。
    - `[gamemode].checkmeout.admin.clearsubmissions` - 让玩家使用'/[admin_command] checkmeout clearall'命令。默认为OP。
    - `[gamemode].checkmeout.admin.seesubs` - 让玩家使用'/[admin_command] checkmeout seesubs'命令。默认为OP。

??? 问题 "缺少什么？"
    你可以在这个插件的[addon.yml](https://github.com/BentoBoxWorld/Visit/blob/develop/src/main/resources/addon.yml)文件中找到权限的综合列表。  
    如果下面的列表确实缺少了什么，请告诉我们！

## 常见问题解答

??? 问题 "你能添加特性X吗？"
    请在[这里](https://github.com/BentoBoxWorld/CheckMeOut/issues)添加它。

## Api

### 事件

自从BentoBox 1.17 API实现了一个特性解决了类加载器的问题。想要直接使用事件的插件现在可以做到。

你只需要将CheckMeOut作为依赖项添加到你的项目中。你可以使用Maven来做到这一点：

```xml
<dependency>
    <groupId>world.bentobox</groupId>
    <artifactId>checkmeout</artifactId>
    <version>1.1.0</version>
    <scope>provided</scope>
</dependency>
```

=== "IslandSubmittedEvent"
    !!! 摘要 "描述"
        玩家提交他的岛屿审核后触发的事件。

        类链接：[IslandSubmittedEvent](https://github.com/BentoBoxWorld/CheckMeOut/blob/develop/src/main/java/world/bentobox/checkmeout/events/IslandSubmittedEvent.java)

    !!! 问题 "变量"
        - `UUID uuid` - 提交岛屿的玩家id。
        - `Location location` - 提交的位置。
 
    !!! 示例 "代码示例"
        ```java
        @EventHandler(priority = EventPriority.MONITOR)
        public void onSubmittion(IslandSubmittedEvent event) {
            UUID player = event.getUUID();
            Location location = event.getLocation();
        }
        ```