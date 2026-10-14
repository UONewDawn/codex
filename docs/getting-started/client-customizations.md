---
description: "Replace item art and gump (UI) graphics in the New Dawn client with your own PNG or BMP images. Where files go and how to name them."
---

# Custom Art & Gumps

The New Dawn client can swap out selected item art and gump (UI) graphics with your own images. Drop a `.png` or `.bmp` into the right folder, name it after the graphic it replaces, and restart the client.

!!! tip "Don't want to make your own?"
    [Custom Packs](custom-packs.md) has ready-made sets of reagents, gems, bags, spell icons and more. Download one, extract it into your client folder, and the files land in the right place for you.

## Where the files go

Inside your client folder (the one containing `ClassicUO.exe`):

```
Data/
└── Custom/
    ├── Art/      <- item graphics (things you see in the world and in your backpack)
    └── Gumps/    <- UI graphics (container backgrounds, spell icons, panels)
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

Custom images are loaded **once, when the client starts**. After adding, changing, or removing a file, fully close and restart the client.

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
