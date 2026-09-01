# 介绍

BentoBox 依赖于**插件来提供新功能或新游戏模式**。
本教程将指导您完成**创建您的第一个插件**的过程。

创建插件通常比从头开始创建插件更容易更快，因为 BentoBox 提供了[包装器](https://en.wikipedia.org/wiki/Wrapper_function)和关键的 API 功能。
与插件不同，由于 [Java 类加载器的可见性原则](https://www.javatpoint.com/classloader-in-java)，插件可以直接访问其他插件的 API。
此外，它们可以访问 BentoBox 的[配置 API](../../BentoBox/Config-API.md) 和[数据库 API](../../BentoBox/Database-API.md)。

为了顺利学习本教程，您应该有插件开发的先前经验。
插件开发过程确实与后者非常相似，为了简洁起见，我们将在整个教程中假设您理解关键的 Java 概念。

# 准备项目

## 使用预制的插件模板

模板目前不存在。

## 手动创建项目

### 将 BentoBox 作为依赖导入

BentoBox 包含创建和注册插件所需的所有 API。
因此，您应该将其添加为项目的依赖。

BentoBox 使用 Maven，我们的 Maven 仓库由 [CodeMC](https://codemc.org/) 慷慨提供。
但是，您也可以使用 Gradle 来获取 BentoBox。

#### Maven

将以下内容添加到您的 `pom.xml` 文件。

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
    <artifactId>bentobox</artifactId>
    <version>PUT-VERSION-HERE</version>
    <scope>provided</scope>
  </dependency>
</dependencies>
```

#### Gradle

将以下内容添加到您的 `build.gradle` 文件。

```groovy
repositories {
  maven { url "https://repo.codemc.io/repository/bentoboxworld/" }
}

dependencies {
  compileOnly 'world.bentobox:bentobox:PUT-VERSION-HERE'
}
```

如有任何问题，请查看 [Gradle 关于声明依赖的文档](https://docs.gradle.org/current/userguide/declaring_dependencies.html)。

### 设置项目架构

# 创建主插件类

**插件的主类**的工作方式与插件的主类相似。
它最主要处理在加载、启用、重新加载和禁用插件时运行的代码。

主类**继承 `Addon`**。

*示例：*
```java
import world.bentobox.bentobox.api.addons.Addon;

public class MyAddon extends Addon {

}
```

!!! tip
    命名主类时，请考虑以下几点：
    我们建议您保持其名称尽可能接近插件的名称。
    您也可以在类名中追加"Addon"以进一步澄清其目的。

*真实示例*：[Greenhouses](https://github.com/BentoBoxWorld/Greenhouses/blob/develop/src/main/java/world/bentobox/greenhouses/Greenhouses.java)、
[Chat](https://github.com/BentoBoxWorld/Chat/blob/develop/src/main/java/world/bentobox/chat/Chat.java)、
[Biomes](https://github.com/BentoBoxWorld/Biomes/blob/develop/src/main/java/world/bentobox/biomes/BiomesAddon.java)。

## 强制方法

与 Bukkit 插件一样，插件必须重写一些方法才能被正确启用。

因此，您的主插件类应该如下所示：

```java
import world.bentobox.bentobox.api.addons.Addon;

public class MyAddon extends Addon {
    @Override
    public void onEnable() {}
    
    @Override
    public void onDisable() {}
}
```

### onEnable()

此方法在 `#onLoad()` 之后调用。

### onDisable()

此方法在插件被禁用时调用，通常在服务器关闭时发生。

## 可选方法

如果需要，可以重写其他方法。

```java
import world.bentobox.bentobox.api.addons.Addon;

public class MyAddon extends Addon {
    @Override
    public void onLoad() {}

    @Override
    public void onEnable() {}

    @Override
    public void onReload() {}
    
    @Override
    public void onDisable() {}
}
```

### onLoad()
onLoad() 方法中的代码在插件加载时和 onEnable() 之前运行。如果此插件是游戏模式，这是加载配置和设置指令的好地方：
```
    @Override
    public void onLoad() {
        // 从 config.yml 保存默认配置
        saveDefaultConfig();
        // 从 config.yml 加载设置。这也会检查是否有任何问题。
        loadSettings();
        // 注册游戏模式指令
        playerCommand = new DefaultPlayerCommand(this)

        {
            @Override
            public void setup()
            {
                super.setup();
                new IslandAboutCommand(this);
            }
        };
        adminCommand = new DefaultAdminCommand(this) {};
    }
```

### onReload()
此方法中的代码在管理员使用 `bbox reload` 指令重新加载插件时（如果重新加载）运行。

# 创建 addon.yml
addon.yml 是向 BentoBox 描述插件所必需的。它几乎与 Bukkit 使用的 plugin.yml 相同。以下是一个最小示例：

```
name: Bank
main: world.bentobox.bank.Bank
version: 1.0.0
api-version: 1.15.4
authors: tastybento
```
以上标签是强制性的，必须包含在每个 addon.yml 中。<br>

<table cellspacing="0" cellpadding="4" border="1">
   <caption>addon.yml 属性
   </caption>
   <tbody>
       <tr>
           <th>属性
           </th>
           <th>是否必需
           </th>
           <th>描述
           </th>
           <th>示例
           </th>
           <th>备注
           </th>
       </tr>
       <tr style="font-weight: bold;">
           <td>name
           </td>
           <td>是
           </td>
           <td>您的插件的名称。
           </td>
           <td>
               <code>name: MyAddon</code>
           </td>
           <td>
               <ul>
                   <li>字母数字字符和下划线 (a-z,A-Z,0-9, _)</li>
                   <li>用于确定插件的数据文件夹的名称。数据文件夹默认放在 ./addons/ 目录中。</li>
                   <li>最好将 jar 文件命名为相同的名称，例如 'Bank.jar'</li>
               </ul>
           </td>
       </tr>
       <tr style="font-weight: bold;">
           <td>version
           </td>
           <td>是
           </td>
           <td>此插件的版本。
           </td>
           <td>
               <code>version: 1.3.1</code>
           </td>
           <td>
               <ul>
                   <li>版本是任意字符串，但最常见的格式是 MajorRelease.MinorRelease.Build（例如：1.4.1）。</li>
                   <li>通常每次发布新功能或错误修复时，您都会增加此值。</li>
                   <li>
                       在用户输入以下指令时显示
                       <code>/bbox version</code>
                   </li>
               </ul>
           </td>
       </tr>
       <tr>
           <td>description
           </td>
           <td>否
           </td>
           <td>对插件提供的功能的人性化描述。
           </td>
           <td>
               <code>description: This addon is so boxy.</code>
           </td>
           <td>
               <ul>
                   <li>描述可以有多行。</li>
                   <li>
                       在用户输入以下指令时显示
                       <code>/version addonName</code>
                   </li>
               </ul>
           </td>
       </tr>
       <tr>
           <td>authors
           </td>
           <td>是
           </td>
           <td>允许您列出一个或多个作者（如果是协作项目）。如果列出多个作者，则使用 YAML 字符串列表格式。
           这实际上是一个强制项目。
           </td>
           <td>
<code>authors:
- BONNe
- tastybento</code><br>
或<br>
<code>authors: tastybento</code>
           </td>
           <td>
               <ul>
                   <li>您可以列出一个作者或多个作者。</li>
               </ul>
           </td>
       </tr>
       <tr style="font-weight: bold;">
           <td>main
           </td>
           <td>是
           </td>
           <td>指向扩展 Addon 或 Pladdon 的类
           </td>
           <td>
               <code>main: world.bentobox.acidisland.AcidIsland</code>
           </td>
           <td>
               <ul>
                   <li>注意这必须包含完整的命名空间，包括类文件本身。</li>
                   <li>
                       如果您的命名空间是
                       <code>world.bentobox.addon</code>
                       ，您的类文件被称为
                       <code>Myaddon</code>
                        那么这必须是
                       <code>world.bentobox.addon.Myaddon</code>
                   </li>
               </ul>
           </td>
       </tr>
       <tr>
           <td>depend
           </td>
           <td>否
           </td>
           <td>插件需要加载的插件列表。
           </td>
           <td>
               <code>depend: Oneaddon, Anotheraddon</code>
           </td>
           <td>
               <ul>
                   <li>
                       该值用逗号分隔
                   </li>
                   <li>使用所需插件的"name"属性来指定依赖关系。</li>
                   <li>如果此处列出的任何插件未找到，您的插件将无法加载。</li>
                   <li>如果多个插件相互列为依赖，以至于没有插件的依赖可以加载，所有插件都将无法加载。</li>
               </ul>
           </td>
       </tr>
       <tr>
           <td>softdepend
           </td>
           <td>否
           </td>
           <td>插件可能需要但不是强制性的插件列表。
           </td>
           <td>
               <code>softdepend: AcidIsland, BSkyBlock, SkyGrid, CaveBock, AOneBlock</code>
           </td>
           <td>
               <ul>
                   <li>
                       该值用逗号分隔。
                   </li>
                   <li>使用所需插件的"name"属性来指定依赖关系。</li>
                   <li>您的插件将在此处列出的任何插件之后加载。</li>
                   <li>循环软依赖项的加载是任意的。</li>
               </ul>
           </td>
       </tr>
       <tr>
           <td>permissions
           </td>
           <td>否
           </td>
           <td>插件希望注册的权限。每个节点代表要注册的权限。每个权限都可以有其他属性。
           </td>
           <td>
               <pre>permissions:    
  '[gamemode].intopten':
    description: Player is in the top ten.
    default: true
  '[gamemode].island.level':
    description: Player can use level command
    default: true
  '[gamemode].island.top':
    description: Player can use top ten command
    default: true</pre>
           </td>
           <td>
               <ul>
                   <li>权限注册是可选的，也可以从代码完成</li>
                   <li>权限注册允许您设置描述、默认值和子父关系</li>
                   <li>权限名称可以包含 <code>[gamemode]</code> 标记以使权限适用于服务器上所有加载的游戏模式。</li>
               </ul>
           </td>
       </tr>
   </tbody>
</table>

# Pladdons
Pladdons 是 Bukkit 插件和插件的组合。Pladdon 的主要好处是它随 Bukkit 服务器类加载器一起加载，因此其中的数据可以由插件直接访问。如果您正在编写实用程序插件（例如 Level 插件），其他插件编写者可能希望通过 API 在代码中访问它生成的数据。最简单的方法是制作 Pladdon，他们可以直接调用您代码中的方法。如果您**不**希望插件访问插件中的数据，则将其保持为插件。

## 使插件成为 Pladdon
为此，请创建一个推荐名称为 `MyAddonPladdon.java` 的类，其中 MyAddon 是您的插件的名称，并扩展 `Pladdon`。不是创建 `plugin.yml`，而是使用注解声明组件。注解应该如下所示。如果需要，可以将 ApiVersion 更新为最新的服务器版本。

```
@Plugin(name="Pladdon", version="1.0")
@ApiVersion(ApiVersion.Target.v1_16)
@Dependency(value = "BentoBox")
public class LevelPladdon extends Pladdon {
    private Addon addon;
    
    @Override
    public Addon getAddon() {
        if (addon == null) {
            addon = new Level();
        }
        return addon;
    }
}
```

应该定义的唯一方法是 `getAddon()` 方法，它必须返回您的插件的实例。确保您只返回一个实例，以便在多次调用此方法时不会创建重复项。

完成此操作后，插件将像真正的插件一样加载，并且可以由其他插件访问。
