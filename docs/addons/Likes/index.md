# 点赞

**点赞**让玩家可以对其他岛屿进行点赞、点踩或评星。

由[BONNe](https://github.com/BONNe)创建和维护。

{{ addon_description("Likes") }}

## 安装

0. 安装BentoBox并至少运行一次服务器以创建其数据文件夹。
1. 将这个jar文件放入BentoBox插件的addons文件夹中。
2. 重启服务器。
3. 插件将创建一个数据文件夹，并且文件夹内将有一个config.yml文件。
4. 停止服务器。
5. 按你想要的方式编辑config.yml文件。
7. 重启服务器。

## 配置

主要的`config.yml`文件包含有关游戏模式插件设置的基本信息。

`panels`允许自定义一些用户可访问的面板。

### config.yml

插件成功安装后，它将创建config.yml文件。这个文件中的每个选项都附有注释。请检查文件以获取更多信息。
你可以在这里找到最新的配置文件：[config.yml](https://github.com/BentoBoxWorld/Likes/blob/develop/src/main/resources/config.yml)

一些配置选项可以通过游戏中的管理GUI进行更改。然而，有些选项不能更改。

最重要的配置选项是模式：

!!! 摘要 "点赞模式"
    mode: 允许改变插件工作的模式

    - LIKES - 只允许对岛屿添加点赞。
    - LIKES_DISLIKES - 允许对岛屿添加点赞和点踩。
    - STARS - 允许对岛屿添加星级评分。

你一次只能使用一种模式。

### 可自定义的GUI

BentoBox 1.17 API引入了一个功能，允许实现可自定义的GUI。这个插件是第一个使用这个功能的插件之一。我们试图尽可能简单地进行自定义，然而，一些功能需要解释。
你可以在这里找到更多关于BentoBox自定义GUI如何工作的信息：[自定义GUI](/en/latest/Tutorials/generic/Customizable-GUI/)

??? 问题 "如何自定义GUI"
    要自定义插件GUI，你需要拥有2.2版本。这是第一个实现它们的版本。插件将在`/plugins/BentoBox/addons/Likes`下创建一个名为`panels`的新目录

    目前你可以自定义3个GUI：

    - 查看面板：`view_panels` - 允许查看给玩家岛屿点赞的面板。
    - 排行面板：`top_panel` - 包含按某种值排名的顶尖岛屿的面板。
    - 管理面板：`manage_panels` - 允许添加点赞/点踩或星级的面板。

    查看和管理面板包含每种模式的3个不同面板。

## 命令

!!! 小贴士
    `[player_command]` 和 `[admin_command]` 是根据你运行的游戏模式而不同的命令。
    游戏模式的`config.yml`文件包含允许你修改这些值的选项。
    例如，在BSkyBlock上，默认的`[player_command]`是`island`，默认的`[admin_command]`是`bsbadmin`。

=== "玩家命令"
    - `/[player_command] likes`：打开添加/删除点赞、点踩或星级的GUI。
    - `/[player_command] likes top`：打开显示点赞、点踩或星级排名前的岛屿的GUI。
    - `/[player_command] likes view <player>`：打开显示谁给岛屿添加了点赞或星级的GUI。

=== "管理员命令"
    - `/[admin_command] likes`：打开管理员GUI。
    - `/[admin_command] likes settings`：打开管理员设置GUI。

## 权限

!!! 小贴士
    `[gamemode]` 是一个根据你运行的游戏模式而不同的前缀。
    前缀是游戏模式的小写名称，即如果你使用BSkyBlock，前缀是`bskyblock`。
    类似地，如果你使用AcidIsland，前缀是`acidisland`。

=== "玩家权限"
    - `[gamemode].likes` - (默认：`true`) - 允许玩家使用`/[player_command] likes`命令。
    - `[gamemode].likes.top` - (默认：`true`) - 允许玩家使用`/[player_command] likes top`命令。
    - `[gamemode].likes.view` - (默认：`true`) - 允许玩家使用`/[player_command] likes top`命令。
    - `[gamemode].likes.icon.[MATERIAL]` - (默认：`false`) - 允许在Top GUIs中更改岛屿所有者的图标。

=== "管理员权限"
    - `[gamemode].likes.view.others` - (默认：`op`) - 允许玩家使用`/[player_command] likes view <player>`命令。
    - `[gamemode].likes.bypass-cost` - (默认：`op`) - 允许绕过插件操作的成本。
    - `[gamemode].likes.admin` - (默认：`op`) - 允许使用`/[admin_command] likes`命令。
    - `[gamemode].likes.admin.settings` - (默认：`op`) - 允许使用`/[admin_command] likes settings`命令。

??? 问题 "缺少什么？"
    你可以在这个插件的[addon.yml](https://github.com/BentoBoxWorld/Likes/blob/develop/src/main/resources/addon.yml)文件中找到权限的综合列表。  
    如果下面的列表确实缺少了什么，请告诉我们！

## 占位符

{{ placeholders_source(source="Likes") }}

## 常见问题解答

??? 问题 "你能添加功能X吗？"
    请在[这里](https://github.com/BentoBoxWorld/Likes/issues)添加。

??? 问题 "我可以禁用点踩吗？"
    是的，点赞插件支持3种工作模式：

    - Likes: 只允许对岛屿添加点赞
    - LikesDislikes: 允许添加点赞和点踩
    - Stars: 允许使用1至5星评价玩家岛屿
    
??? 问题 "我可以查看其他玩家的点赞吗？"
    是的，但你需要一个权限：`[gamemode].likes.view.others`。
    
    拥有这个权限的玩家可以使用`/[playercmd] likes view <player>`来查看其他玩家的点赞。
    
??? 问题 "我可以只为某些岛屿更改显示图标吗？"
    是的，这是可能的。
    
    有两种方式：
    
    1. 使用管理员GUI，你可以为它选择岛屿和显示的方块。
    2. 给岛屿所有者添加权限：`[gamemode].likes.icon.[MATERIAL]`
        
    注意，PLAYER_HEAD将转换为岛屿所有者的头像。

## 翻译

{{ translations("Likes") }}

## API

自Likes 2.2.0和BentoBox 1.17版本起，其他插件可以直接访问Likes插件数据。

### Maven 依赖

Likes为其他插件提供了API。这涵盖了2.2.0及之后的版本。

!!! 注意
    将Likes依赖添加到你的Maven POM.xml中：

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
                <artifactId>likes</artifactId>
                <version>2.2.0</version>
                <scope>provided</scope>
            </dependency>
        </dependencies>
    ```

使用最新的Likes版本。

Likes的JavaDocs可以在[这里](https://ci.codemc.io/job/BentoBoxWorld/job/Likes/ws/target/apidocs/index.html)找到。

### 事件

=== "LikeAddEvent"
    !!! 摘要 "描述"
        当玩家给岛屿添加新的点赞时触发的事件。

        事件仅为信息性质。不能被取消。

        类链接：[LikeAddEvent](https://github.com/BentoBoxWorld/Likes/blob/develop/src/main/java/world/bentobox/likes/events/LikeAddEvent.java)

    !!! 问题 "变量"
        - `UUID user` - 添加点赞的玩家的id。
        - `String islandId` - 接收点赞的岛屿的id。
        
    !!! 示例 "示例"
        ```java
        @EventHandler(priority = EventPriority.MONITOR)
        public void onLike(LikeAddEvent event) {
            UUID user = event.getUser();
            String islandId = event.getIslandId();
        }
        ```  

=== "LikeRemoveEvent"
    !!! 摘要 "描述"
        当玩家从岛屿上移除他的点赞时触发的事件。

        事件仅为信息性质。不能被取消。

        类链接：[LikeRemoveEvent](https://github.com/BentoBoxWorld/Likes/blob/develop/src/main/java/world/bentobox/likes/events/LikeRemoveEvent.java)

    !!! 问题 "变量"
        - `UUID user` - 移除点赞的玩家的id。
        - `String islandId` - 失去点赞的岛屿的id。
        
    !!! 示例 "示例"
        ```java
        @EventHandler(priority = EventPriority.MONITOR)
        public void onLikeRemove(LikeRemoveEvent event) {
            UUID user = event.getUser();
            String islandId = event.getIslandId();
        }
        ```  

=== "DislikeAddEvent"
    !!! 摘要 "描述"
        当玩家给岛屿添加新的点踩时触发的事件。

        事件仅为信息性质。不能被取消。

        类链接：[DislikeAddEvent](https://github.com/BentoBoxWorld/Likes/blob/develop/src/main/java/world/bentobox/likes/events/DislikeAddEvent.java)

    !!! 问题 "变量"
        - `UUID user` - 添加点踩的玩家的id。
        - `String islandId` - 接收点踩的岛屿的id。

    !!! 示例 "示例"
        ```java
        @EventHandler(priority = EventPriority.MONITOR)
        public void onDislike(DislikeAddEvent event) {
            UUID user = event.getUser();
            String islandId = event.getIslandId();
        }
        ```  

=== "DislikeRemoveEvent"
    !!! 摘要 "描述"
        当玩家从岛屿上移除他的点踩时触发的事件。

        事件仅为信息性质。不能被取消。

        类链接：[DislikeRemoveEvent](https://github.com/BentoBoxWorld/Likes/blob/develop/src/main/java/world/bentobox/likes/events/DislikeRemoveEvent.java)

    !!! 问题 "变量"
        - `UUID user` - 移除点踩的玩家的id。
        - `String islandId` - 失去点踩的岛屿的id。

    !!! 示例 "示例"
        ```java
        @EventHandler(priority = EventPriority.MONITOR)
        public void onDislikeRemove(DislikeRemoveEvent event) {
            UUID user = event.getUser();
            String islandId = event.getIslandId();
        }
        ```  

=== "StarsAddEvent"
    !!! 摘要 "描述"
        当玩家给岛屿添加新的星级评分时触发的事件。

        事件仅为信息性质。不能被取消。

        类链接：[StarsAddEvent](https://github.com/BentoBoxWorld/Likes/blob/develop/src/main/java/world/bentobox/likes/events/StarsAddEvent.java)

    !!! 问题 "变量"
        - `UUID user` - 添加星级的玩家的id。
        - `String islandId` - 接收星级的岛屿的id。
        - `int value` - 添加的星级值（从1到5）

    !!! 示例 "示例"
        ```java
        @EventHandler(priority = EventPriority.MONITOR)
        public void onStarsAdd(StarsAddEvent event) {
            UUID user = event.getUser();
            String islandId = event.getIslandId();
            int value = event.getValue();
        }
        ```  

=== "StarsRemoveEvent"
    !!! 摘要 "描述"
        当玩家从岛屿上移除他的星级评分时触发的事件。

        事件仅为信息性质。不能被取消。

        类链接：[StarsRemoveEvent](https://github.com/BentoBoxWorld/Likes/blob/develop/src/main/java/world/bentobox/likes/events/StarsRemoveEvent.java)

    !!! 问题 "变量"
        - `UUID user` - 添加星级的玩家的id。
        - `String islandId` - 失去星级的岛屿的id。

    !!! 示例 "示例"
        ```java
        @EventHandler(priority = EventPriority.MONITOR)
        public void onStarsRemove(StarsRemoveEvent event) {
            UUID user = event.getUser();
            String islandId = event.getIslandId();
        }
        ```  

### 插件请求处理器

直到BentoBox 1.17版本，我们因为使用的类加载器问题导致无法访问BentoBox环境之外的数据。
这意味着数据只能从其他插件访问。但是BentoBox实现了PlAddon功能，这意味着不再需要请求处理器。

更多关于插件请求处理器的信息可以在[这里](/en/latest/BentoBox/Request-Handler-API---How-plugins-can-get-data-from-addons/)找到。

=== "island-likes"
    !!! 摘要 "描述"
        返回给定世界中岛屿存储的岛屿喜欢数据。

    !!! 问题 "输入"
        - `world-name`: 字符串 - 世界的名称。
        - `island`: 字符串 - 岛屿的UUID。

    !!! 成功 "输出"
        输出是一个`Map<String, Object>`，包含以下键：

        - `likes`: 长整型 - 给定岛屿设置的喜欢数量。
        - `dislikes`: 长整型 - 给定岛屿设置的不喜欢数量。
        - `rank`: 长整型 - 给定岛屿的排名。
        - `stars`: 双精度 - 给定岛屿的平均星级值。
        - `placeByLikes`: 整型 - 给定岛屿在喜欢排名中的位置。
        - `placeByDislikes`: 整型 - 给定岛屿在不喜欢排名中的位置。
        - `placeByRank`: 整型 - 给定岛屿在排名中的位置。
        - `placeByStars`: 整型 - 给定岛屿在星级排名中的位置。
        - `likedBy`: List<UUID> - 喜欢给定岛屿的玩家UUID列表。
        - `dislikedBy`: List<UUID> - 不喜欢给定岛屿的玩家UUID列表。
        - `staredBy`: Map<UUID, Integer> - 以星级数量为玩家UUID点赞给定岛屿的映射。


    !!! 失败
        如果没有提供`world-name`，或者`world-name`不存在或不是游戏模式世界，或者没有提供岛屿，或者岛屿数据为空，此处理器将返回一个空映射。

    !!! 示例 "代码示例"
        ```java
        public Map<String, Object> getLikesData(String worldName, String islandUUID) {
            return (Map<String, Object>) new AddonRequestBuilder()
                .addon("Likes")
                .label("island-likes")
                .addMetaData("world-name", worldName)
                .addMetaData("island", islandUUID)
                .request();
        }
        ```

=== "top-ten-likes"
    !!! 摘要 "描述"
        返回一个`Map<String, Number>`，包含给定排名中前10个岛屿UUID及其值。

    !!! 问题 "输入"
        - `world-name`: 字符串 - 世界的名称。
        - `type`: 字符串 - 排名类型。支持：STARS, LIKES, DISLIKES, RANK。

    !!! 成功 "输出"
        一个映射包含前10名岛屿的UUIDs，映射到其岛屿的顶级值。

    !!! 失败
        如果没有提供`world-name`，或者`world-name`不存在或不是游戏模式世界，或者提供的排名类型没有任何数据，此处理器将返回一个空映射。

    !!! 示例 "代码示例"
        ```java
        public Map<String, Number> getTopTenLikes(String worldName, String type) {
            return (Map<String, Number>) new AddonRequestBuilder()
                .addon("Likes")
                .label("top-ten-likes")
                .addMetaData("world-name", worldName)
                .addMetaData("type", type)
                .request();
        }
        ```
        