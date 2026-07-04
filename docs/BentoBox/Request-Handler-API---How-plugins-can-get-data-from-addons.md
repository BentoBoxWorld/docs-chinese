# 请求处理程序 API
此 API 使插件作者能够从附加组件请求数据。附加组件作者可以决定他们希望公开的确切数据。由于 Java 安全规则对类加载器的限制，插件无法直接访问附加组件内的任何类。

## 使用 Level 附加组件的示例

Level 附加组件公开两个请求处理程序 [LevelRequestHandler](https://github.com/BentoBoxWorld/Level/blob/develop/src/main/java/world/bentobox/level/requests/LevelRequestHandler.java) 和 [TopTenRequestHandler](https://github.com/BentoBoxWorld/Level/blob/develop/src/main/java/world/bentobox/level/requests/TopTenRequestHandler.java)。以下是插件从 LevelRequestHandler 获取玩家等级的方式：

### LevelRequestHandler

标签：`island-level`

输入映射：

* 键：`world-name` -> String
* 值：`player` -> UUID

因此，获取玩家等级的代码示例如下：

```
UUID uuid = player.getUniqueId();
String worldName = player.getWorld().getName();
Long result = (Long)AddonRequestBuilder
    .addon("Level")
    .label("island-level")
    .addMetaData("world-name", worldName)
    .addMetaData("player", uuid)
    .request();
```

您可以通过查看附加组件的代码或其文档来了解附加组件公开了哪些数据。

# 从附加组件暴露数据
要暴露数据，请为扩展 [AddonRequestHandler](https://bentoboxworld.github.io/BentoBox/world/bentobox/bentobox/api/addons/request/AddonRequestHandler.html) 的每个元素创建类。然后在您的附加组件中注册请求处理程序。例如：

```
        // Register request handlers
        registerRequestHandler(new LevelRequestHandler(this));
        registerRequestHandler(new TopTenRequestHandler(this));
```

处理程序应在其构造函数中定义其标签，例如：

```
    public LevelRequestHandler(Level addon) {
        super("island-level"); // 标签是 "island-level"
        this.addon = addon;
    }
```

标签对于您的附加组件必须是唯一的。

然后，覆盖接受映射作为参数的 `handle` 方法：

```
    @Override
    public Object handle(Map<String, Object> map) {
```

您可以定义映射的内容，但对象绝不能是您的附加组件中的任何唯一类。它只能是所有插件都存在的类。如果您尝试引用隐藏类，插件将生成异常。因此，整数、长整数、Bukkit 位置、世界等都没有问题。

记录您的映射将是什么是个好习惯，因为插件作者会使用它：

```
        /*
            What we need in the map:
            0. "world-name" -> String
            1. "player" -> UUID
            What we will return:
            - 0L if invalid input/player has no island
            - the island level otherwise (which may be 0)
         */
```

之后处理映射并提供结果：

```

        if (map == null || map.isEmpty()
                || map.get("world-name") == null || !(map.get("world-name") instanceof String)
                || map.get("player") == null || !(map.get("player") instanceof UUID)
                || Bukkit.getWorld((String) map.get("world-name")) == null) {
            return 0L;
        }

        return addon.getIslandLevel(Bukkit.getWorld((String) map.get("world-name")), (UUID) map.get("player"));
    }
```

请注意，您返回的是 `Object`，所以插件作者需要将其转换为正确的形式，在这种情况下是 `long`。通过执行适当级别的参数检查来保护您的附加组件免受错误的映射格式是个好习惯。





