= 目录
:toc:

= 简介
游戏模式是像 BSkyBlock 或 AcidIsland 这样的附加组件。将其视为游戏模式附加组件的原因是它将创建并向 BentoBox 注册一个 *世界*，并提供 BentoBox 一个 WorldSettings 类对象。

目前，向 BentoBox 注册的世界必须是主世界，但一旦一个世界被注册，任何关联的下界和末地世界也将属于此游戏模式附加组件。

为了说明这一切是如何工作的，让我们看一下 BSkyBlock 代码（为了清晰起见，删除了一些行）：

[source,java]
----
    @Override
    public void onLoad() {
        // 保存 config.yml 中的默认配置
        saveDefaultConfig();
        // 从 config.yml 中加载设置。这将检查是否存在任何问题。
        settings = new Config<>(this, Settings.class).loadConfigObject();
        // 加载或创建世界
        bsbWorlds = new BSkyBlockWorld(this);
    }
----

注释非常清晰，但前两个调用是为了设置 config.yml 文件和设置。在这种情况下，我们使用的是来自 BentoBox 配置 API 的 Config 类，它使得动态保存带有注释的 YAML 文件成为可能。这是一个强大的配置 API。如果您不想使用它，您可以只使用常规的 Bukkit 风格配置系统。我们之所以使用它，是因为它使我们能够自动更新 config.yml 文件。

= 设置类

让我们看一下设置类（同样，为了清晰起见，删除了一些行）：

[source,java]
----
@StoreAt(filename="config.yml", path="addons/BSkyBlock") // 请明确说明该名称应使用什么
@ConfigComment("BSkyBlock 配置 [版本]")
@ConfigComment("此配置文件是动态的，并在服务器关闭时保存。")
@ConfigComment("在服务器运行时无法编辑它，因为更改将")
@ConfigComment("丢失！在服务器离线时使用游戏内设置 GUI 或进行编辑。")
@ConfigComment("")
public class Settings implements DataObject, WorldSettings {

    @ConfigComment("允许用空桶将黑曜石捡起重新变成岩浆")
    @ConfigEntry(path = "general.allow-obsidian-scooping")
    private boolean allowObsidianScooping = true;

...
----

在这里看到的是类声明之前的许多注释，类声明后面是字段声明周围的更多注释。让我们逐一解释：

. 类声明之前的 @StoreAt 注释定义了该配置文件将被存储的位置。它是相对于 BentoBox 插件的数据文件夹的。文件应该只存储在 BentoBox 文件夹中。明确声明此位置非常重要！
. @Comment 注释用于向 YAML 文件中添加注释行。"[版本]" 占位符会自动替换为附加组件的版本号。
. 类必须同时实现 DataObject 和 WorldSettings 接口。DataObject 用于将类保存到数据库中（通过 BBConfig），WorldSettings 用于表示这是一个游戏模式附加组件。
. 字段 "allowObsidianScooping" 被声明，以及一个默认值，它有一个注释注释和一个 @ConfigEntry 注释。此注释用于定义该值将放置在 YAML 文件中的位置。请注意，通常情况下，YAML 条目的放置顺序与它们在代码中编写的顺序相同，除非 @ConfigEntry 强制将它们放置在其他位置。
. 在声明字段之后，您还需要为字段创建一个 getter 和 setter。（在代码中未显示）

请注意，通过实现 WorldSetting 接口，您将不得不 @Override 一些强制性世界设置的 getter。在 BSkyBlock 设置类中，几乎所有这些设置都是从配置文件加载的。唯一的例外是 *Optional<Addon> getAddon()*。这必须返回附加组件实例。目前，附加组件必须设置它。将来，BentoBox 可能会设置它。

= 将世界注册到 BentoBox

现在让我们更仔细地看一下上面提到的 BSkyBlockWorld 类。这个类有三个主要功能：

. 为 BSkyBlock 创建世界（创建世界并为其定义生成器）
. 向 BentoBox 注册主世界和设置类
. 注册在创建新岛屿时将使用的原理图到 IslandCreate 类中

这

是它的实现方式：

[source,java]
----
// 如果不存在则创建世界
islandWorld = WorldCreator.name(worldName).type(WorldType.FLAT).environment(World.Environment.NORMAL)
    .generator(new ChunkGeneratorWorld(addon)).createWorld();

// 将世界和设置与 BentoBox 注册
addon.getPlugin().registerWorld(islandWorld, addon.getSettings());

// 如有必要，创建下界和末地世界（未显示）

// 加载原理图
addon.getPlugin().getSchemsManager().loadIslands(islandWorld);
----

在这段代码中，*addon* 是附加组件实例。getPlugin() 用于获取 BentoBox，registerWorld() 用于注册世界。请注意，您不需要向 BentoBox 注册下界和末地世界。您只需要注册主世界。BentoBox 将假定任何关联的下界或末地也属于您的附加组件，如果它们存在的话。

对于原理图（BentoBox 自己的专有原理图文件格式），您应该为附加组件的每个世界的默认岛屿准备原理图，并将其放在附加组件的原理图文件夹中。它们必须命名为：

* island.schem（必需的）
* nether-island.schem（可选）
* end-island.schem（可选）

要制作原理图，请使用 BentoBox 的 schem 指令（或 BSkyBlock 的或 AcidIsland 的 schem 指令）。

= 注册指令

在注册了世界、相关的世界/游戏模式设置和原理图之后，下一步是让您的附加组件执行某些操作。如果它需要指令，您可以通过扩展 CompositeCommand 来制作它们。让我们看一下 BSkyBlock 如何注册其顶级指令 */island* 和其下的子指令：

[source,java]
----
public class IslandCommand extends CompositeCommand {

    public IslandCommand(BSkyBlock addon) {
        super(addon, "island", "is");
    }

    @Override
    public void setup() {
        setOnlyPlayer(true);
        // 权限
        setPermissionPrefix("bskyblock");
        setPermission("island");
        setWorld(((BSkyBlock)getAddon()).getIslandWorld());
        // 设置子指令
        new IslandAboutCommand(this);
        new IslandCreateCommand(this);
        new IslandGoCommand(this);
        new IslandResetCommand(this);
        new IslandSetnameCommand(this);
        new IslandResetnameCommand(this);
        new IslandSethomeCommand(this);
        new IslandSettingsCommand(this);
        new IslandLanguageCommand(this);
        new IslandBanCommand(this);
        new IslandUnbanCommand(this);
        new IslandBanlistCommand(this);
        // 团队指令
        new IslandTeamCommand(this);
    }
----

注册指令的关键行是：

```
super(addon, "island", "is");
```

这告诉 BentoBox "/island" 是 BSkyBlock 附加组件的顶级指令，它的别名是 "/is"。然后在 setup() 方法中，有一些非常重要的（顶级指令必需的）声明：

```
setWorld(((BSkyBlock)getAddon()).getIslandWorld());
```

这非常重要。它定义了该指令将在其中运行的世界。所有子指令都将使用 getWorld() 方法引用它。

之后，指令实例化了一些子指令，将自身作为参数传递。这些类将使用该参数作为它们各自 super() 调用中的父类。

= 结论

上述内容描述了如果您正在创建新的游戏模式类型附加组件应该做什么。我们正在继续开发 API，因此在未来，某些事情可能会变得更简单。