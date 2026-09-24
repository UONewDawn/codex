# Storage Rack

A Storage Rack is a lockable house item that holds a stock of common supplies such as reagents, potions, bandages, ammo, ingots, hides and boards. Instead of piling everything in chests, you drop your supplies onto the rack and it keeps a count of each one.

Each player who uses a rack builds their own **loadouts**. A loadout is a named kit, such as "PvP Mage" or "Tamer Run", with the amount of each item you want to carry. One click refills you up to those amounts.

<!-- TODO: screenshot of the rack in a house -->
<!-- TODO: screenshot of the Storage Rack gump -->

## How is this different from Razor's restock?

Razor's Restock simulates what you would do by hand: it moves each item into your bag one at a time, with a short delay between each move. The storage rack is part of the server, so applying a loadout is **instant**.

## Getting a Storage Rack

Storage Racks are crafted with **Carpentry**.

| Skill                | Materials                   |
| -------------------- | --------------------------- |
| 84.2 – 100 Carpentry | 35 Logs, 10 Codex Fragments |

## Setting It Up

1. Place the rack in your house and **lock it down**. A rack does nothing until it is locked down.
2. The house owner or a co-owner double-clicks it. That player becomes the **rack owner**.
3. The rack owner can use the context menu to set **Access** and **Appearance**.

If the rack is not locked down, double-clicking it gives this message: _"This must be locked down in a house before it can be used."_ Picking a rack back up clears its owner, so the next person to lock it down and open it can claim it.

!!! warning "House collapse"
    The rack's stock belongs to the house. If the house collapses, the rack and **everything stored on it are deleted**. They are not left on the ground like other lockdowns.

## Access

The rack owner chooses who else may use the rack:

| Setting       | Who can use it                                                                   |
| ------------- | -------------------------------------------------------------------------------- |
| Owner Only    | Only the rack owner (the default)                                                |
| Co-Owners     | House co-owners                                                                  |
| Friends       | House friends                                                                    |
| Guild Members | Members of the **rack owner's** guild, even if the house belongs to someone else |
| Everyone      | Anyone                                                                           |

The **stock is shared** by everyone with access. **Loadouts and bag settings are private**. Every player keeps their own on each rack.

You must be within **2 tiles** of the rack to use it.

## What It Holds

| Category | Items                                                                                                               |
| -------- | ------------------------------------------------------------------------------------------------------------------- |
| Reagents | Black Pearl, Blood Moss, Garlic, Ginseng, Mandrake Root, Nightshade, Spider's Silk, Sulphurous Ash                  |
| Potions  | Greater Heal, Greater Cure, Total Refresh, Greater Explosion, Greater Strength, Greater Agility, Greater Nightsight |
| Supplies | Bandage, Blank Scroll, Empty Bottle                                                                                 |
| Ammo     | Arrow, Crossbow Bolt                                                                                                |
| Ingots   | Iron, Dull Copper, Shadow Iron, Copper, Bronze, Gold, Agapite, Verite, Valorite                                     |
| Hides    | Hides, Spined, Horned, Barbed                                                                                       |
| Wood     | Board, Oak, Ash, Yew                                                                                                |

A rack can hold up to **50,000 of each item**.

## Depositing

You can deposit in several ways:

- **Drag and drop** a stack onto the rack.
- **Drop a container** onto the rack. It takes everything it can use from the top level of that container and gives the container back to you with whatever was left.
- Use **Deposit** in the gump or **Add to Storage Rack** in the context menu, then target:
  - **yourself** to sweep the top level of your backpack
  - **a container** within reach, such as a bag or a chest on the floor
  - **a single item**

Sweeps only look at the **top level** of a container. Items inside bags within that container are left alone.

!!! note "Plain stock only"
    The rack stores a count, not the actual items. Each withdrawal is a brand new item. For that reason, the rack refuses anything that would lose something when it comes back out.

## Withdrawing

Each row in the gump shows how many are stored. Enter an amount in the **Withdraw** box and click to take it out. If you leave the amount blank, you get 1.

### Your Bag

By default, withdrawals go into your backpack. Click **Set Bag** and target a container inside your backpack to have withdrawals and loadouts go there instead. Click **Clear** to switch back to your backpack. If that bag is full, items go to your main backpack. If you move the bag out of your pack, the rack switches back to your backpack and tells you so.

## Loadouts

A loadout is a named set of items with a **maximum** amount for each. You can have up to **20 loadouts per rack**.

- Click **New Loadout**, name it (up to 50 characters), and set a Max for each item you want.
- Click a loadout to **apply** it. The rack counts what you already carry in the top level of your backpack and your chosen bag, then **only tops you up** to the Max.
- If the rack runs short on something, the rack gives you what it has and tells you what was missing (for example _"Mandrake Root (12 short)"_).
- If you already carry everything on the list, the rack tells you so.
- Loadouts can be edited or deleted from the Loadouts panel.

!!! tip "Top-level only"
    Only items in the top level of your backpack (and your chosen bag) count toward a loadout. Supplies tucked into other bags deeper in your pack don't count, so you may get topped up anyway.

### Compact Mode

Click **Compact** to switch to a small panel that shows only your loadouts, the Deposit button, and your bag. Click **Expand** to return to the full view. The rack remembers your choice.

## Appearance

The rack owner can change the rack's look from **Appearance** in the context menu:

- **Case:** three shelf styles. The first is free. The others cost **250,000 gold** each to unlock.
- **Contents:** decorative fills that show items on the shelves. Each costs **250,000 gold** to unlock.
- **Turn:** switch which way the rack faces. You can also use the house Interior Decorator's "Turn".

Unlock costs are taken from your bank first, then from gold in your backpack. Unlocks belong to that rack.

<!-- TODO: screenshots of the case styles and fills -->
