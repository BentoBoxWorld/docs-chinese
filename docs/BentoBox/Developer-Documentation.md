# 欢迎来到 BentoBox 开发者文档！

BentoBox 是一个平台插件，支持一套可在其上运行的插件 API。其架构与 Bukkit 插件系统几乎相同。你可以创建像 BSkyBlock 这样的游戏模式插件，为玩家提供你自己的游戏模式体验，或者你可以开发实用程序插件，如 Warps，使任何游戏模式（甚至普通世界）中的玩家都可以使用传送牌。

## Pladdons

由于服务器运作方式的改变（代码在加载时的重新映射），现在建议所有插件现在都在 Bukkit 插件包装器内运行，该包装器由 BentoBox 提供，称为 Pladdon -
Pladdons = Plugin + Addon。通过成为插件，它们在加载时将被正确重新映射，这对于 Paper 等服务器很重要。

Pladdon 包装器的任务是生成附加组件实例，并在通过 `getAddon` 方法请求时提供它。

由于附加组件是插件，它们将被服务器列为插件，但它们仍应放在 `Bentobox/Addons` 文件夹中。

# JavaDocs

Javadocs 在这里：[https://javadocs.bentobox.world](https://ci.codemc.io/job/BentoBoxWorld/job/BentoBox/javadoc/)

核心 API 包是 world.bentobox.bentobox.api.\*。这些包中的方法会尽可能长期保持稳定。api 包之外的方法和类可能会频繁或大幅度改变。

# 示例插件

@BONNe 在这里维护了一个示例插件：[https://github.com/BONNePlayground/ExampleAddon](https://github.com/BONNePlayground/ExampleAddon)

# 可取消的玩家重置事件

*BentoBox 3.17.0 新增。*

当玩家离开队伍或其岛屿被重置时,BentoBox 可能会清空他们的物品栏、末影箱、金钱、生命值、饥饿度和经验值,并将其驯服的动物恢复野生——具体取决于每个游戏模式的 `island.reset.on-leave` 设置。现在,这些重置动作在执行**之前**都会触发一个**可取消的**事件,因此插件可以否决单个重置,而不是全有或全无。如果监听器取消了该事件,BentoBox 就会跳过该动作。

这些事件位于 `world.bentobox.bentobox.api.events.player`:

| 事件 | 触发时机(之前) |
| --- | --- |
| `PlayerTamedRemovalEvent` | 将玩家驯服的动物恢复野生 |
| `PlayerResetEnderChestEvent` | 清空末影箱 |
| `PlayerResetInventoryEvent` | 清空物品栏 |
| `PlayerResetMoneyEvent` | 扣除玩家余额 |
| `PlayerResetHealthEvent` | 重置生命值 |
| `PlayerResetHungerEvent` | 重置饥饿度 |
| `PlayerResetExpEvent` | 重置经验值 |

所有事件都继承自 `PlayerBaseEvent`(实现了 `Cancellable`),并携带玩家 UUID、岛屿和世界。监听方式是标准的 Bukkit 方式:

```java
@EventHandler
public void onInventoryReset(PlayerResetInventoryEvent e) {
    if (shouldKeepInventory(e.getPlayerUUID())) {
        e.setCancelled(true); // 物品栏将不会被清空
    }
}
```

事件通过一个小型构建器 API 构建和分发:

```java
PlayerEvent.builder()
    .reason(PlayerEvent.Reason.INVENTORY_RESET)
    .involvedPlayer(uuid)
    .island(island)
    .world(world)
    .build();
```

这完全是新增的——所有类都是新的,没有更改任何现有 API,因此 3.17.0 与现有插件二进制兼容。[Inventory Switcher 插件](../addons/InvSwitcher/index.md)使用这些事件在重置时保护按世界的物品栏和余额。参见 [Release 3.17.0](https://github.com/BentoBoxWorld/BentoBox/releases/tag/3.17.0)。

# 模态对话框 { #modal-dialogs }

*BentoBox 3.21.0 新增。*

`world.bentobox.bentobox.api.dialogs` 封装了 Paper 的模态对话框系统，该系统需要 **Minecraft 26 或更高版本**。对话框与 Panels API 并列存在：面板是一个玩家可以随手点掉的物品栏，而对话框是玩家必须作答的模态窗口。核心用它来实现命令确认、`/island go` 目的地选择器、队伍邀请，以及首次加入时的游戏模式选择器。

| 类 | 用途 |
| --- | --- |
| `Dialogs` | `Dialogs.isSupported()` —— 当前服务端能否显示对话框 |
| `DialogBuilder` | 流式构建器：`title`、`body`、`escapable`、`pause`、`confirmation`、`button`、`build` |
| `DialogButton` | 一个标签、一个可选的提示文本，以及一个 `Consumer<User>` 点击处理器 |
| `BBDialog` | 构建好的对话框 —— 用 `show(User)` 显示它 |

`title(...)`、`body(...)` 和 `DialogButton.of(...)` 都既可以接收一个 Adventure `Component`，也可以接收一个 `User` 加一个本地化键引用（以及可选的变量），因此对话框文本的翻译方式与插件其余部分完全一致。整条链路都基于 `Component`，所以点击动作得以保留。

```java
if (!Dialogs.isSupported()) {
    // 26 之前的服务端：回退到你原有的聊天或面板流程
    askInChat(user);
    return;
}
new DialogBuilder()
    .title(user, "myaddon.confirm.title")
    .body(user, "myaddon.confirm.body", "[name]", island.getName())
    .confirmation(
        DialogButton.of(user, "myaddon.confirm.yes", u -> doTheThing(u)),
        DialogButton.of(user, "myaddon.confirm.no", u -> u.sendMessage("myaddon.confirm.cancelled")))
    .build()
    .show(user);
```

!!! warning "务必提供回退方案"
    请像核心那样检查 `Dialogs.isSupported()`，并为更旧的服务端保留原有的聊天或面板行为。按钮的点击处理器运行在主线程上，因此可以直接调用 Bukkit API。

参见 [Release 3.21.0](https://github.com/BentoBoxWorld/BentoBox/releases/tag/3.21.0)。