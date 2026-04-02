# BentoBox 配置 API

这是一个可选的 API，为 YAML 文件增强了 Bukkit 配置 API。BentoBox 配置 API 添加了以下功能：

1. 配置文件保存后可以保留注释
2. 更新你的插件时，配置文件可以更新新的设置
3. 配置类也是获取和设置设置的地方

如果你不想使用此 API，可以使用标准 Bukkit API 方法，如 saveDefaultConfig()、getConfig() 等。

## 入门 - 一个例子

假设我们想为新插件创建一个配置文件。也许它看起来像这样：

```yaml
# This is my config.yml file
# It is for my addon

world:
  # This is the name of the world.
  name: My_world_name
  # Size - minimum is 10, max is 100
  size: 100
```

### ConfigObject
要使用配置 API，我们创建一个实现 `ConfigObject` 的新类：

```java
public class Settings implements ConfigObject {

}
```

现在我们必须指定此配置对象的保存位置。位置相对于插件的数据文件夹。

```java
@StoreAt(filename="config.yml") // Explicitly call out what name this should have.
public class Settings implements ConfigObject {

}
```

### @ConfigEntry
接下来，我们必须添加想要在配置中的数据字段。为此，我们使用 `@ConfigEntry` 注解：

```java
@StoreAt(filename="config.yml") // Explicitly call out what name this should have.
public class Settings implements ConfigObject {
    @ConfigEntry(path = "world.name")
    private String worldName = "My_world_name";

    @ConfigEntry(path = "world.size")
    private int worldSize = 100;
}
```

注意字段如何有分配给它们的默认值。

### 获取器和设置器
接下来，我们必须添加获取器和设置器来访问这些字段。获取器和设置器的名称以及参数名称必须符合 [JavaBeans 命名约定](https://www.oreilly.com/library/view/javaserver-pages-3rd/0596005636/ch20s01s01.html)：

```java
@StoreAt(filename="config.yml") // Explicitly call out what name this should have.
public class Settings implements ConfigObject {
    @ConfigEntry(path = "world.name")
    private String worldName = "My_world_name";

    @ConfigEntry(path = "world.size")
    private int worldSize = 100;

    public String getWorldName() {
        return worldName;
    }
    public void setWorldName(String worldName) {
        this.worldName = worldName;
    }
    public int getWorldSize() {
        return worldSize;
    }
    public void setWorldSize(int worldSize) {
        this.worldSize = worldSize;
    }
}
```

### `@ConfigComment`
接下来，我们可以使用 `ConfigComment` 注解添加注释：

```java
@StoreAt(filename="config.yml") // Explicitly call out what name this should have.
@ConfigComment("This is my config.yml file") // Note that the comment will automatically
@ConfigComment("It is for my addon") // be proceeded with a # and space
public class Settings implements ConfigObject {
    @ConfigEntry(path = "world.name")
    @ConfigComment("This is the name of the world.")
    private String worldName = "My_world_name";

    @ConfigEntry(path = "world.size")
    @ConfigComment("Size - minimum is 10, max is 100")
    private int worldSize = 100;

    public String getWorldName() {
        return worldName;
    }
    public void setWorldName(String worldName) {
        this.worldName = worldName;
    }
    public int getWorldSize() {
        return worldSize;
    }
    public void setWorldSize(int worldSize) {
        this.worldSize = worldSize;
    }
}
```

### 加载和保存

要在 Addon 类中加载配置，请执行以下操作：

```java
Settings settings = new Config<>(this, Settings.class).loadConfigObject();
```

要在 Addon 类中保存配置，请执行以下操作：

```java
Settings settings = new Settings();
new Config<>(this, Settings.class).saveConfigObject(settings);
```

对于插件来说，最好的做法是加载设置，然后立即保存它们。这将使配置文件与最新的选项和注释保持同步。要创建初始配置，请使用 Addon 的 `saveDefaultConfig()` 方法保存存储在插件 jar 中的默认 config.yml。如果你使用的是不同于 config.yml 的文件，可以使用 `saveResource(resourcePath, replace)` 方法。

### 默认配置文件
在插件 jar 中设置默认 config.yml 文件。然后使用标准 `saveDefaultConfig()` 方法将其保存到插件的文件系统中。所以整体方法如下：

1. saveDefaultConfig() - 如果不存在，这将从 jar 保存默认 config.yml。
2. 使用 Config API 加载配置以获取管理员设置
3. 使用 Config API 保存配置以使用最新的设置选项和注释更新 config.yml

就这样！请阅读 JavaDocs 以获取有关此 API 的更多信息。
