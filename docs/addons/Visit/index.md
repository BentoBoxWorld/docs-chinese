# 访问插件

**访问**是一个简单的BentoBox插件，允许访问其他玩家的岛屿。
这是Warps插件的另一种选择。

由[BONNe](https://github.com/BONNe)创建和维护。

{{ addon_description("Visit") }}

## 安装

1. 将插件jar文件放入BentoBox插件的addons文件夹中
2. 重启服务器
3. 运行`/[admin_cmd] visit`命令来配置插件

## 配置

很多插件设置在管理员GUI中公开，但有些没有。
更改命令标签需要重新启动服务器。

### config.yml

插件成功安装后，将创建config.yml文件。此文件中的每个选项都有注释，请查看获取更多信息。
你可以在[这里](https://github.com/BentoBoxWorld/Visit/blob/develop/src/main/resources/config.yml)找到最新的配置文件。

### 自定义GUI

BentoBox 1.17 API引入了一个功能，允许实现自定义GUI。这个插件是第一个使用这个功能的插件之一。我们尽可能简化自定义，但有些功能需要解释。
你可以在[这里](/en/latest/Tutorials/generic/Customizable-GUI/)找到更多关于BentoBox自定义GUI如何工作的信息。

??? question "如何自定义GUI"
    要自定义插件GUI，你需要有1.5版本。这是第一个实现它们的版本。插件将在`/plugins/BentoBox/addons/Visit`下创建一个名为`panels`的新目录

    目前你可以自定义2个GUI：

    - 主面板：`main_panel` - 包含所有岛屿的面板。
    - 管理面板：`manage_panel` - 包含一些配置选项的面板。

    每个GUI包含只支持自己的功能。

??? question "什么是`PREVIOUS`|`NEXT`按钮类型？"
    `PREVIOUS`和`NEXT`按钮类型允许在GUI中有更多岛屿而空间不足时创建自动分页。
    这些类型在数据下有额外的参数：
 
    - `indexing` - 指示按钮是否显示页码。

    示例：
    ```yaml
        icon: tipped_arrow[potion_contents={custom_color:11546150}]
        title: visit.gui.buttons.previous.name
        description: visit.gui.buttons.previous.description
        data:
          type: PREVIOUS
          indexing: true
        action:
          left:
            action: PREVIOUS
            tooltip: visit.gui.tips.click-to-previous
    ```

??? question "什么是`SEARCH`按钮类型？"
    这个按钮在主面板中可用。
    它创建一个允许按特定岛屿搜索的按钮。

    示例：
    ```yaml
        icon: PAPER
        title: visit.gui.buttons.search.name
        # 描述是动态生成的。但是，你可以手动设置。
        # description: visit.gui.buttons.search.description
        data:
          type: SEARCH
        actions:
          left:
            type: INPUT
            tooltip: visit.gui.tips.left-click-to-edit
          right:
            type: CLEAR
            tooltip: visit.gui.tips.right-click-to-clear
    ```

??? question "什么是`FILTER`按钮类型？"
    这个按钮在主面板中可用。
    它创建一个允许按某些属性过滤岛屿的按钮。

    示例：
    ```yaml
        # 图标是动态生成的。但是，你可以手动设置。
        # icon: SANDSTONE
        title: visit.gui.buttons.filter.name
        # 描述是动态生成的。但是，你可以手动设置。
        # description: visit.gui.buttons.filter.description
        data:
          type: FILTER
        actions:
          left:
            type: UP
            tooltip: visit.gui.tips.left-click-to-cycle
          right:
            type: DOWN
            tooltip: visit.gui.tips.right-click-to-cycle
    ```

??? question "什么是`ISLAND`按钮类型？"
    这个按钮在主面板中

可用。
    `ISLAND`按钮为岛屿对象创建一个动态条目。

    指定标题、描述和图标将基于数据库数据覆盖动态生成。默认情况下，这些值将从数据库条目生成。
    这个按钮支持3种不同的动作类型：

    - `VISIT`类型允许玩家访问岛屿
    - `CONFIRM`类型允许玩家在config中启用ask-payment-confirmation时确认访问
    - `CANCEL`类型允许玩家在config中启用ask-payment-confirmation时取消访问

    示例：
    ```yaml
      # 数据是动态生成的。但是，设置它们将覆盖它。
      # icon: PLAYER_HEAD
      # title: visit.gui.buttons.island.name
      # description: visit.gui.buttons.island.description
      data:
        type: ISLAND
      actions:
        - click-type: left
          type: VISIT
          tooltip: visit.gui.tips.click-to-visit
        - click-type: left
          type: CONFIRM
          tooltip: visit.gui.tips.left-click-to-confirm
        - click-type: right
          type: CANCEL
          tooltip: visit.gui.tips.right-click-to-cancel
    ```

??? question "什么是`PAYMENT`按钮类型？"
    这个按钮在管理面板中可用。
    它创建一个允许设置访问玩家岛屿的支付值的按钮。

    示例：
    ```yaml
        icon: ANVIL
        title: visit.gui.buttons.payment.name
        # 描述是动态生成的。但是，你可以手动设置。
        # description: visit.gui.buttons.payment.description
        data:
          type: PAYMENT
        actions:
          left:
            type: CHANGE
            tooltip: visit.gui.tips.click-to-change
    ```

??? question "什么是`OFFLINE`按钮类型？"
    这个按钮在管理面板中可用。
    它创建一个允许设置玩家是否可以在岛屿成员不在线时访问岛屿的按钮。

    示例：
    ```yaml
        icon: REDSTONE_LAMP
        title: visit.gui.buttons.offline.name
        # 描述是动态生成的。但是，你可以手动设置。
        # description: visit.gui.buttons.offline.description
        data:
          type: OFFLINE
        actions:
          left:
            type: TOGGLE
            tooltip: visit.gui.tips.click-to-toggle
    ```

??? question "什么是`ALLOWED`按钮类型？"
    这个按钮在管理面板中可用。
    它创建一个允许一键禁用访问的按钮。这是通过设置面板更改`ALLOW_VISITS_FLAG`标志值的快捷方式。

    示例：
    ```yaml
        icon: PUMPKIN_PIE
        title: visit.gui.buttons.enabled.name
        # description: visit.gui.buttons.enabled.description
        data:
          type: ALLOWED
        actions:
          left:
            type: TOGGLE
            tooltip: visit.gui.tips.click-to-toggle
    ```

## 命令

!!! 小贴士
    `[player_command]` 和 `[admin_command]` 是根据你运行的游戏模式而不同的命令。
    游戏模式的`config.yml`文件包含允许你修改这些值的选项。
    例如，在BSkyBlock上，默认的`[player_command]`是`island`，默认的`[admin_command]`是`bsbadmin`。
    注意，这个插件允许在插件`config.yml`文件中更改玩家命令别名。

=== "玩家命令"
    - `/[player_command] visit <player>`：打开GUI或访问目标玩家的岛屿。
    - `/[player_command] visit configure`：打开GUI，允许管理访问设置。
    - `/[player_command] visit setlocation`：允许更改访客出生点位置。

=== "管理员命令"
    - `/[admin_command] visit <player>`：打开GUI，允许编辑插件设置和配置岛屿数据。

## 权限

!!! tip
    `[gamemode]` 是一个根据你运行的游戏模式而不同的前缀。
    前缀是游戏模式的小写名称，即如果你使用BSkyBlock，前缀是`bskyblock`。
    类似地，如果你使用AcidIsland，前缀是`acidisland`。

=== "玩家权限"
    - `[gamemode].visit` - 让玩家使用`/[player_command] visit`命令。
    - `[gamemode].visit.configure` - 让玩家使用`/[admin_command] visit configure`命令。
    - `[gamemode].visit.setlocation` - 让玩家使用`/[admin_command] visit setlocation`命令。
    - `visit.icon.[material]` - 允许更改访问面板中玩家拥有的岛屿的图标。

=== "管理员权限"
    - `[gamemode].admin.visit` - 让玩家使用`/[admin_command] visit`命令及其子命令。
    
??? question "缺少什么？"
    你可以在这个插件的[addon.yml](https://github.com/BentoBoxWorld/Visit/blob/develop/src/main/resources/addon.yml)文件中找到权限的综合列表。  
    如果下面的列表确实缺少了什么，请告诉我们！

## 标志

插件引入了2个BentoBox保护标志：

- ![pumpkin_pie](https://static.wikia.nocookie.net/minecraft_gamepedia/images/a/ac/Pumpkin_Pie_JE2_BE2.png){: loading=lazy width=16px } ALLOW_VISITS_FLAG：岛屿设置中的标志，允许启用/禁用岛屿访问。
- ![paper](https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f2/Paper_JE2_BE2.png){: loading=lazy width=16px } RECEIVE_VISIT_MESSAGE_FLAG：岛屿设置中的标志，允许启用/禁用岛屿成员接收访问/离开消息。


## 常见问题解答

??? question "你能添加功能X吗？"
    请在[这里](https://github.com/BentoBoxWorld/Visit/issues)添加。

??? question "玩家可以更改访客被传送的地点吗？"
    是的，玩家可以使用命令：`/[player_cmd] visit setlocation`来设置。但是，请注意，访客不会被传送到“危险”的地点，如果位置不安全，他们将被传送到更安全的位置。

??? question "管理员可以更改访客被传送的地点吗？"
    是的，管理员可以使用命令：`/[admin_cmd] setspawnpoint`来设置。但是，请注意，访客不会被传送到“危险”的地点，如果位置不安全，他们将被传送到更安全的位置。

??? question "玩家可以有自定义图标吗？"
    是的，通过添加权限`visit.icon.[material]`给岛屿所有者，可以更改访问面板中岛屿的图标。

??? question "我不想使用经济系统。我可以完全禁用它吗？"
    是的，配置选项`disable-economy`将完全禁用所有经济部分。

??? question "如何允许/不允许岛屿成员更改访问值？"
    岛屿所有者（和拥有`CHANGE_SETTINGS`权限的成员）可以通过设置面板编辑`RANKED_COMMANDS`访问。那里将有`/[player_cmd] visit configure`命令。

??? question "如何允许/不允许岛屿成员更改访问位置？"
    岛屿所有者（和拥有`CHANGE_SETTINGS`权限的成员）可以通过设置面板编辑`RANKED_COMMANDS`访问。那里将有`/[player_cmd] visit setlocation`命令。



## 翻译

{{ translations("Visit") }}

## API

从Visit 1.4.0和BentoBox 1.17开始，其他插件可以直接访问Visit插件的数据。

### Maven 依赖

Visit 为其他插件提供了 API。这涵盖了 1.5.0 及以后的版本。

!!! note
    将 Visit 依赖添加到你的 Maven POM.xml 中：

    ```xml
        <repositories>
            <repository>
                <id>codemc-repo</id>
                <url>https://repo.codemc.io/repository/bentoboxworld/</url>
            </repository>
        </repositories>

        <dependencies>
            <dependency>
                <groupId>world.bentobox</groupId>
                <artifactId>visit</artifactId>
                <version>1.5.0</version>
                <scope>provided</scope>
            </dependency>
        </dependencies>
    ```

使用最新的 Visit 版本。

Visit 的 JavaDocs 可以在[这里](https://ci.codemc.io/job/BentoBoxWorld/job/Visit/ws/target/apidocs/index.html)找到。

### 事件

=== "VisitEvent"
    !!! summary "描述"
        在玩家被传送到岛屿之前但在支付之后触发的事件。

        可以取消。（取消时不退还支付）

        类链接：[VisitEvent](https://github.com/BentoBoxWorld/Visit/blob/develop/src/main/java/world/bentobox/visit/events/VisitEvent.java)

    !!! question "变量"
        - `User player` - 尝试访问岛屿的玩家的 id。
        - `Island island` - 玩家尝试访问的岛屿。
        - `boolean cancelled` - 事件是否被取消的布尔值。

    !!! example "代码示例"
        ```java
        @EventHandler(priority = EventPriority.MONITOR)
        public void onVisit(VisitEvent event) {
            UUID player = event.getPlayer();
            User user = event.getUser();
            Island island = event.getIsland();

            boolean cancelled = event.isCancelled();
        }
        ```