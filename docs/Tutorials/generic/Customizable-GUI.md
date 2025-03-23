## Customizable GUI's

BentoBox 1.17 introduced an API for GUI customization. However, due to the number of required changes, not everything is yet customizable, and only few addons has implemented this feature.

Example of customizable GUI:
```yaml
# The name of the panel. It must be the same as file name.
panel_name:
  # Title of the panel
  title: "The Panel Title"
  # Panel Type:
  # INVENTORY - chest GUI type
  # HOPPER - hopper GUI type
  # DROPPER - dropper/dispenser GUI type.
  type: INVENTORY
  # Background item for empty slots
  background:
    # Icon for the element.
    # Write format can be found in: https://docs.bentobox.world/en/latest/BentoBox/ItemParser/
    icon: BLACK_STAINED_GLASS_PANE
    # Title of the element
    title: "&b&r" # Empty text
    # Description of the element
    description: "I am background"
  # Border item for non-empty border slots
  border:
    # Icon for the element.
    # Write format can be found in: https://docs.bentobox.world/en/latest/BentoBox/ItemParser/
    icon: BLACK_STAINED_GLASS_PANE
    # Title of the element
    title: "&b&r" # Empty text
    # Description of the element
    description: "I am border"
  # Rows that must be always visible
  force-shown: [2,4]
  # Content of the GUI.
  content:
    # Row number from 1 to 6
    2:
      # Column number
      2: reusable_button_one
      3: reusable_button_one
      4: reusable_button_one
      5: reusable_button_one
      6: reusable_button_one
      7: reusable_button_one
      8: reusable_button_one
    3:
      1:
        # Icon for the element.
        # Write format can be found in: https://docs.bentobox.world/en/latest/BentoBox/ItemParser/
        icon: tipped_arrow[potion_contents={custom_color:11546150}]
        # Title of the element.
        title: "Button One"
        # Description of the element
        description: "Button description"
        # Data is used for defining some functions that are used for addons.
        # The content of it depends on addon/gui implementation.
        data:
          type: ADDON_THING
        # Actions allow specifying what button should do. Addons can specify extra parameters.
        action:
          # available options can be found here: [ClickType](https://hub.spigotmc.org/javadocs/spigot/org/bukkit/event/inventory/ClickType.html)
          left:
            # Addons can define a type of click. 
            type: ADDON_THING
            # Tooltips are a text that will be added to the button description at the end.
            tooltip: "Tooltip for a button"
      9:
        # Icon for the element.
        # Write format can be found in: https://docs.bentobox.world/en/latest/BentoBox/ItemParser/
        icon: STONE
        # Title of the element.
        title: "Button Twi"
        # Description of the element
        description: "Button description"
        # Data is used for defining some functions that are used for addons.
        # The content of it depends on addon/gui implementation.
        data:
          type: ADDON_THING
        # Actions allow specifying what button should do. Addons can specify extra parameters.
        action:
          # available options can be found here: [ClickType](https://hub.spigotmc.org/javadocs/spigot/org/bukkit/event/inventory/ClickType.html)
          left:
            # Addons can define a type of click. 
            type: ADDON_THING
            # Tooltips are a text that will be added to the button description at the end.
            tooltip: "Tooltip for a button"
    5:
      2: reusable_button_two
      3: reusable_button_two
      4: reusable_button_two
      5: reusable_button_two
      6: reusable_button_one
      7: reusable_button_two
      8: reusable_button_two
  # The reusable buttons that are used inside content part multiple times.
  reusable:
    # The id of reusable
    reusable_button_one:
      # Icon for the element.
      # Write format can be found in: https://docs.bentobox.world/en/latest/BentoBox/ItemParser/
      icon: GLASS
      # Title of the element.
      title: "Reusable Button One"
      # Description of the element
      description: "Button description"
      # Data is used for defining some functions that are used for addons.
      # The content of it depends on addon/gui implementation.
      data:
        type: ADDON_THING
      # Actions allow specifying what button should do. Addons can specify extra parameters.
      action:
        # available options can be found here: [ClickType](https://hub.spigotmc.org/javadocs/spigot/org/bukkit/event/inventory/ClickType.html)
        left:
          # Addons can define a type of click. 
          type: ADDON_THING
          # Tooltips are a text that will be added to the button description at the end.
          tooltip: "Tooltip for a button"
    reusable_button_two:
      # Icon for the element.
      # Write format can be found in: https://docs.bentobox.world/en/latest/BentoBox/ItemParser/
      icon: DIRT
      # Title of the element.
      title: "Reusable Button Two"
      # Description of the element
      description: "Button description"
      # Data is used for defining some functions that are used for addons.
      # The content of it depends on addon/gui implementation.
      data:
        type: ADDON_THING
      # Actions allow specifying what button should do. Addons can specify extra parameters.
      action:
        # available options can be found here: [ClickType](https://hub.spigotmc.org/javadocs/spigot/org/bukkit/event/inventory/ClickType.html)
        left:
          # Addons can define a type of click. 
          type: ADDON_THING
          # Tooltips are a text that will be added to the button description at the end.
          tooltip: "Tooltip for a button"
```

### FAQ

??? question "Can I set a multi-linguistic title and description?"
    Yes, you can. Every text in the GUI will always try to use BentoBox localization. It means that if you specify a text that links to a translation, it will use it.
    F.e.:
    ```yaml
    tooltip: panels.tooltips.left
    ```
    will try to get translation string from any of BentoBox locales:
    ```yaml
    panels:
      tooltips:
        left: "Left Click Tooltip"
    ```

??? question "What is type?"
    In Spigot plugins you can specify 3 types of inventories, that players can interact:
    - `INVENTORY` - simple inventory like chests with 27 till 54 slots.
    - `HOPPER` - hopper inventory with 5 slots.
    - `DROPPER` - dropper inventory with 9 slots.
    
    Other inventories, like enchanting and anvil, are not supported by Spigot and requires extra plugins. That is reason why BentoBox currently do not support them.

??? question "What is background?"
    The background item allows setting unified item for all empty spaces that will be left in the GUI.
    It requires to have icon and title. If you do not want to have it, just remove `background` lines.
    The only required thing under `background` is icon. `title` and `description` can be removed.
    ```yaml
        icon: BLACK_STAINED_GLASS_PANE
        title: "The title of background item"
        description: "The description of background item"
    ```

??? question "What is border?"
    The border item allows setting unified item all around the GUI. It will replace only empty spaced.
    It requires to have icon and title. If you do not want to have it, just remove `border` lines.
    The only required thing under `background` is icon. `title` and `description` can be removed.
    ```yaml
        icon: BLACK_STAINED_GLASS_PANE
        title: "The title of border item"
        description: "The description of border item"
    ```

??? question "Can I set empty text and hide tooltip?"
    Unfortunately, Minecraft servers cannot disable text and tooltip rendering for clients. Only for modded clients (like fabric or forge) it can be done.
    The closest you can get is to set an empty text with: `&b&r`


??? question "What is `force-shown`?"
    In inventory GUI's we try to remove all completely empty lines. This allows to set dynamic size of GUI's for different number of available elements in them. However, sometime you want always to see a specific line. Force-show option allows to do it, and you can list integers with lines (from 0-6).

??? question "What is reusable?"
    In some GUI's you would have a lot of repeating items that you would need to specify, like challenges or biomes. Reusable allows to create a single element that will be replaced in all places where object is required from content part.

??? question "How to properly fill `conetent`?"
    Content requires to specify row number (from 1 to 6) as first thing and column number for each button (from 1 to 9). It does not require to specify every slot, just the ones you want to fill. Everything else will be either empty, background or border.
    
    Note, that some GUI types does not have multiple rows or less columns.

??? question "What is `data` for buttons?"
    Data is a way how we implemented a feature for addons to use custom functions. Like Challenges addon has two type of data: CHALLENGE and LEVEL. Each addon has its own data, and it may contain more things than a type.

??? question "What is `actions` for buttons?"
    `Actions` allows implementing different things that will happen if player use different click options on the buttons.
    All click options can be found here: [ClickType](https://hub.spigotmc.org/javadocs/spigot/org/bukkit/event/inventory/ClickType.html)
    Be aware, not all options are usable by players.

    `action` supports tooltip generation. Tooltips will be always added at the end of the button description and will be in the order of actions.
