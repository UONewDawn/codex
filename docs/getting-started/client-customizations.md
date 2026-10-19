---
description: "Replace item art and gump (UI) graphics in the New Dawn client with your own PNG or BMP images, and make your own built-in assistant themes. Where files go and how to name them."
---

# Custom Art, Gumps & Themes

The New Dawn client can swap out selected item art and gump (UI) graphics with your own images. Drop a `.png` or `.bmp` into the right folder, name it after the graphic it replaces, and restart the client.

You can also make your own colour themes for the [Built-in Assistant](built-in-assistant.md) window. See [Custom assistant themes](#custom-assistant-themes) below.

!!! tip "Don't want to make your own?"
    [Custom Packs](custom-packs.md) has ready-made sets of reagents, gems, bags, spell icons and more. Download one, extract it into your client folder, and the files land in the right place for you.

## Where the files go

Inside your client folder (the one containing `ClassicUO.exe`):

```
Data/
└── Custom/
    ├── Art/        <- item graphics (things you see in the world and in your backpack)
    ├── Gumps/      <- UI graphics (container backgrounds, spell icons, panels)
    └── Assistant/  <- built-in assistant themes (.json files)
```

The client creates these folders the first time it starts, so if they are missing, launch the client once and close it.

Only the top level of each folder is scanned. Images in subfolders are ignored.

## Naming your files

The file name must be the **graphic ID** of the image you are replacing. You can write the ID in hex or decimal:

| Format  | Example      | Replaces        |
| ------- | ------------ | --------------- |
| Hex     | `0x0E75.png` | Backpack (item) |
| Decimal | `3701.png`   | Backpack (item) |

- Hex IDs **must** start with `0x` (upper or lower case). `0E75.png` without the prefix is read as decimal and will not work.
- Leading zeros are optional: `0xE75.png` and `0x0E75.png` are the same.
- Supported formats: `.png` and `.bmp`. Anything else is ignored.
- If two files point at the same ID (for example `0xE75.png` and `3701.png`), only one of them is used.

For **Art**, use the _item ID_ as shown in tools like UOFiddler or the `[props` gump, not the raw `art.mul` index. The client adds the `0x4000` offset itself.

## Making the image

- **Transparency:** use a 32-bit PNG with an alpha channel. Soft edges and partial transparency are supported.
- **Size:** keep the image the same size as the original graphic. Items are positioned relative to the size of their image, so a larger or smaller image will sit differently in the world and in containers. Gumps are drawn from their top-left corner, so a larger gump will spill past the area the original filled.
- **Hued items:** if the server colors an item (dyed, magic, etc.), the client recolors your image the same way it does the original: it reads the brightness of each pixel and ignores its color. Items that are only partially hued (such as clothing trim) recolor only the pure gray pixels. For art that is often hued, draw it in grayscale so the hue comes out correctly.

## What can be replaced

Only graphics on the shard's allow list can be replaced. Files for any other ID are skipped. This stops a stray file from changing something important to gameplay.

**Art (`Data/Custom/Art`)**

| Category       | IDs                                                                                                              |
| -------------- | ---------------------------------------------------------------------------------------------------------------- |
| Empty bottle   | `0x0F0E`                                                                                                         |
| Reagents       | `0x0F7A`, `0x0F7B`, `0x0F84`, `0x0F85`, `0x0F86`, `0x0F88`, `0x0F8C`, `0x0F8D`                                   |
| Gems           | `0x0F0F` – `0x0F30`                                                                                              |
| Jewelry        | `0x1085` – `0x108A`                                                                                              |
| Containers     | `0x0E75` (backpack), `0x0E79` (pouch)                                                                            |
| Bandages       | `0x0E21`                                                                                                         |
| Arrows         | `0x0F3F`, `0x0F42`                                                                                               |
| Bolts          | `0x1BFB`, `0x1BFE`                                                                                               |
| Daggers        | `0x0F51`, `0x0F52`                                                                                               |
| Scissors       | `0x0F9E`, `0x0F9F`                                                                                               |
| Tongs          | `0x0FBB`, `0x0FBC`                                                                                               |
| Smith's hammer | `0x13E3`, `0x13E4`                                                                                               |
| Boat sails     | `0x3E3F`–`0x3E42`, `0x3E57`–`0x3E5C`, `0x3E6A`–`0x3E6E`, `0x3E70`–`0x3E74`, `0x3EC8`–`0x3ED2`, `0x3EDC`–`0x3EE7` |

**Gumps (`Data/Custom/Gumps`)**

| Category                 | IDs                                                                                                                                                                                                                                                                           |
| ------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Paperdoll backdrop       | `0x082D`                                                                                                                                                                                                                                                                      |
| Container gumps          | `0x0009` (coffin), `0x003C` (backpack), `0x003D` (bag), `0x003E` (barrel), `0x003F` (basket), `0x0040`, `0x0049` (wooden chest), `0x0042` (brass-trimmed chest), `0x0043` (wooden box), `0x0044`, `0x004C` (crate), `0x004A` (metal chest), `0x004B` (gilded chest), `0x00A8` |
| Framed panel             | `0x0866`                                                                                                                                                                                                                                                                      |
| Spell icons              | `0x08C0` – `0x08FF`                                                                                                                                                                                                                                                           |
| Login & character select | `0xF100` – `0xF12A`                                                                                                                                                                                                                                                           |

The shard maintains this list. If you want a graphic added, ask staff.

## Applying your changes

Custom art and gump images are loaded **once, when the client starts**. After adding, changing, or removing a file, fully close and restart the client.

To go back to the original graphic, delete your file (or move it out of the folder) and restart.

To remove a [pack](custom-packs.md), delete the files listed under **Files and checksum** on its card, then restart.

## Troubleshooting

If an image does not show up, check the client log. Every skipped file is logged along with the reason:

| Log message                                         | Cause                                               | Fix                                       |
| --------------------------------------------------- | --------------------------------------------------- | ----------------------------------------- |
| `is not a decimal or 0x-hex graphic id, skipping`   | The file name isn't a valid ID                      | Rename to e.g. `0x0E75.png` or `3701.png` |
| `is not in the allow list, skipping`                | That ID can't be replaced                           | Check the tables above                    |
| `declared more than once`                           | Two files map to the same ID                        | Remove one of them                        |
| `zero-sized image` / other `custom image` errors    | The file is empty, corrupt, or not really a PNG/BMP | Re-export the image                       |
| `outside the range of this client's art/gump files` | The ID doesn't exist in your client's data files    | Double-check the ID                       |

!!! note
    A bad file never crashes the client or stops other custom images from loading. It is skipped.

## Custom assistant themes

The [Built-in Assistant](built-in-assistant.md) comes with a set of themes: Classic, Dark, Midnight, Slate, Forge, Grove and Parchment. You can add your own with a small text file. No tools are needed, just a text editor.

### Where the file goes

Put the file in `Data/Custom/Assistant` inside your client folder, and name it `theme.<Name>.json`:

```
Data/
└── Custom/
    └── Assistant/
        ├── theme.Amethyst.json
        └── theme.Deep Sea.json
```

- The file name **must** start with `theme.` and end with `.json`. Anything else in the folder is ignored.
- The part in the middle is the theme's name. It is shown in the list, unless the file gives a `name` of its own.
- The assistant remembers your choice by the file name. If you rename the file, pick the theme again.
- Only the top level of the folder is read. Files in subfolders are ignored.

### Picking your theme

Open the assistant and go to **General**, then **Window**, then **Theme**. Your themes are listed below a line, after the built-in ones. If the file names an author, it is shown next to the theme, for example **Amethyst (by Quick)**.

The folder is read again every time the assistant window opens. You don't need to restart the client while you work on a theme:

1. Save your changes to the file.
2. Pick the theme again from the **Theme** list. The window reopens with your changes.

If the file is deleted, or no longer loads, the assistant goes back to the Classic theme.

### The example: Amethyst

Amethyst is plum-black with dusky violet borders and pale lilac highlights. Copy it into `Data/Custom/Assistant/theme.Amethyst.json` to try it, or use it as a starting point for your own. It lists every setting a theme has:

```json
{
  "name": "Amethyst",
  "author": "Quick",
  "base": "Dark",

  // text
  "text": "0x0481",
  "dim": "#A096B4",
  "accent": "#C8A0F0",
  "danger": "#DC5064",
  "group": "#C8A0F0",
  "textOutline": true,

  // window
  "windowFill": "#1A1224ED",
  "headerFill": "#0F0A16AA",
  "panelBorder": "#4A3866",
  "divider": "#4A3866C8",
  "groupBorder": "#4A3866",

  // lists and text boxes
  "listFill": "#0A061282",
  "listBorder": "#4A3866",
  "selectedFill": "#6A3CA096",
  "hoverFill": "#FFFFFF12",
  "textBoxFill": "#120C1AF0",
  "textBoxBorder": "#66508A",

  // buttons and tabs
  "buttonFace": "transparent",
  "buttonHoverFace": "transparent",
  "buttonBorder": "#66508A",
  "buttonHoverBorder": "#B48CE6",
  "tabFace": "transparent",
  "tabHoverFace": "transparent",
  "selectedTabFace": "#6A3CA06E",
  "tabBorder": "#66508A",
  "tabHoverBorder": "#B48CE6",
  "tileFace": "#0A061282",
  "tileBorder": "#4A3866",
  "tileHoverBorder": "#B48CE6",

  // dropdowns
  "comboFace": "#0A061282",
  "comboHoverFace": "#0A061282",
  "comboOpenFace": "#0A061282",
  "comboBorder": "#4A3866",
  "comboHoverBorder": "#B48CE6",
  "comboOpenBorder": "#B48CE6",
  "comboHoverOverlay": "#FFFFFF12",
  "comboArrow": "#DCD2EB",
  "dropdownFill": "#1A1224FA",

  // scrollbars
  "scrollTrack": "#0000003C",
  "scrollThumb": "#66508A",
  "scrollThumbHover": "#8268AA",
  "scrollThumbPressed": "#A088C8",
  "scrollArrow": "#DCD2EB",
  "scrollArrowHover": "#FFFFFF1E",

  // checkboxes, radio buttons and focus
  "checkFill": "#120C1A",
  "checkBorder": "#7A62A0",
  "checkBorderHover": "#CDAAF5",
  "checkMark": "#C8A0F0",
  "squareMarks": false,
  "focusBorder": "#CDAAF5"
}
```

You don't have to list every setting. Anything you leave out comes from the `base` theme, so a theme can be as short as this:

```json
{
  "author": "Quick",
  "base": "Midnight",
  "accent": "#E8C060",
  "windowFill": "#000000F0"
}
```

Comments (`// like this`) and a comma after the last setting are allowed. Setting names can be written as `windowFill`, `WindowFill` or `window_fill`.

### Name, author and base

| Setting  | What it does                                                                                                                         |
| -------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| `name`   | The name shown in the Theme list. If you leave it out, the name from the file name is used.                                          |
| `author` | Your name, shown in the list next to the theme's name.                                                                               |
| `base`   | The built-in theme to start from: `Classic`, `Dark`, `Midnight`, `Slate`, `Forge`, `Grove` or `Parchment`. Classic if you leave it out. |

Start from the built-in theme closest to what you want. A light theme is easier to make from `Classic` or `Parchment`, and a dark one from `Dark`.

### Writing colours

Colours are written as hex codes, like the ones any colour picker or image editor shows:

| Format                        | Example         | Meaning                                                    |
| ----------------------------- | --------------- | ---------------------------------------------------------- |
| `"#RRGGBB"`                   | `"#4A3866"`     | A solid colour                                             |
| `"#RRGGBBAA"`                 | `"#1A1224ED"`   | A colour with transparency: `00` is invisible, `FF` solid  |
| `[r, g, b]` or `[r, g, b, a]` | `[74, 56, 102]` | The same thing as numbers from 0 to 255                    |
| `"transparent"`               | `"transparent"` | Nothing drawn at all                                       |

Fills can be see-through, so the game shows through the window. The **Opacity** slider under the Theme fades the whole window on top of that.

### Writing text colours

The game draws text in UO hues, not in any colour, so the five text settings (`text`, `dim`, `accent`, `danger`, `group`) take a hue instead:

| Format          | Example       | Meaning                                                    |
| --------------- | ------------- | ---------------------------------------------------------- |
| A hue number    | `1153`        | Exactly this hue, as shown by the assistant's `>hue` command |
| A hex hue       | `"0x0481"`    | The same, in hex                                           |
| A colour        | `"#C8A0F0"`   | The hue that looks closest to this colour                  |

Hue `0x0481` (1153) is the near-white most dark themes use for text. Text colours can't be see-through.

### Every setting

**Text**

| Setting       | What it colours                                                                      |
| ------------- | ------------------------------------------------------------------------------------ |
| `text`        | Normal text                                                                          |
| `dim`         | Help text, empty lists and other quieter text                                        |
| `accent`      | Highlights: search results and links                                                 |
| `danger`      | Delete and Clear buttons, and Recording on the minimized bar                         |
| `group`       | The title of each group box                                                          |
| `textOutline` | `true` draws a black outline around text. Light text needs it to read over the game; dark text on a light theme doesn't. |

**Window**

| Setting       | What it colours                       |
| ------------- | ------------------------------------- |
| `windowFill`  | Behind everything in the window       |
| `headerFill`  | Header bands: the minimized bar, dialog title bars, table headings |
| `panelBorder` | Window and panel frames, and slider handles |
| `divider`     | Lines under the tabs and between sections |
| `groupBorder` | The frame around each group box       |

**Lists and text boxes**

| Setting         | What it colours                                    |
| --------------- | -------------------------------------------------- |
| `listFill`      | Behind lists, trees and the script editor          |
| `listBorder`    | The frame around them                              |
| `selectedFill`  | The selected row in a list                         |
| `hoverFill`     | The row under the mouse                            |
| `textBoxFill`   | Behind text and number boxes                       |
| `textBoxBorder` | The frame around them                              |

**Buttons and tabs**

| Setting             | What it colours                                                          |
| ------------------- | ------------------------------------------------------------------------ |
| `buttonFace`        | A button                                                                 |
| `buttonHoverFace`   | A button under the mouse                                                 |
| `buttonBorder`      | A button's frame                                                         |
| `buttonHoverBorder` | A button's frame under the mouse                                         |
| `tabFace`           | A tab                                                                    |
| `tabHoverFace`      | A tab under the mouse                                                    |
| `selectedTabFace`   | The open tab                                                             |
| `tabBorder`         | A tab's frame                                                            |
| `tabHoverBorder`    | A tab's frame under the mouse                                            |
| `tileFace`          | Big picture buttons, like the facings on the Doors page                  |
| `tileBorder`        | Their frame                                                              |
| `tileHoverBorder`   | Their frame under the mouse (`hoverFill` is drawn over them too)         |

**Dropdowns**

| Setting             | What it colours                                    |
| ------------------- | -------------------------------------------------- |
| `comboFace`         | A dropdown box                                     |
| `comboHoverFace`    | A dropdown box under the mouse                     |
| `comboOpenFace`     | A dropdown box while its list is open              |
| `comboBorder`       | A dropdown box's frame                             |
| `comboHoverBorder`  | Its frame under the mouse                          |
| `comboOpenBorder`   | Its frame while open                               |
| `comboHoverOverlay` | Drawn over the box while it's under the mouse or open |
| `comboArrow`        | The arrow on the right of the box                  |
| `dropdownFill`      | Behind the open list of choices                    |

**Scrollbars**

| Setting              | What it colours                          |
| -------------------- | ---------------------------------------- |
| `scrollTrack`        | The track the scrollbar slides in        |
| `scrollThumb`        | The part you drag                        |
| `scrollThumbHover`   | That part under the mouse                |
| `scrollThumbPressed` | That part while it's being dragged       |
| `scrollArrow`        | The arrows at each end                   |
| `scrollArrowHover`   | Behind an arrow under the mouse          |

**Checkboxes, radio buttons and focus**

| Setting            | What it colours                                                                              |
| ------------------ | -------------------------------------------------------------------------------------------- |
| `checkFill`        | Inside a checkbox or radio button                                                            |
| `checkBorder`      | Its frame                                                                                    |
| `checkBorderHover` | Its frame under the mouse                                                                    |
| `checkMark`        | The tick or dot                                                                              |
| `squareMarks`      | `true` draws square radio buttons and a filled square for a tick, like Classic; `false` a tick and round radio buttons |
| `focusBorder`      | Around a hotkey box that's waiting for you to press a key                                    |

### Sharing a theme

A theme is one file. To share yours, send the `.json` file. Others save it into their own `Data/Custom/Assistant` folder and pick it from the list.

### When a theme doesn't look right

A mistake in a theme file never stops the client or the assistant. The client log says what was skipped:

| Log message                                   | Cause                                                       | Fix                                                        |
| --------------------------------------------- | ----------------------------------------------------------- | ---------------------------------------------------------- |
| `is not named theme.<Name>.json, skipping`    | The file name doesn't start with `theme.`                   | Rename it, for example to `theme.Amethyst.json`            |
| `is not valid json`                           | A missing quote, comma or bracket                           | Check the line the message points to                       |
| `is not a theme setting, ignored`             | A misspelled setting name                                   | Check it against the tables above                          |
| `is not a colour` / `is not a hue`            | A value written the wrong way                               | See [Writing colours](#writing-colours); that setting comes from the base theme until it's fixed |
| `is not a built-in theme`                     | `base` names a theme that doesn't exist                     | Use one of the built-in theme names; Classic is used until then |
| `another file is already named`               | Two files have the same name in different upper/lower case  | Remove one of them                                         |
