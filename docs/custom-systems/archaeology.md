---
description: "New Dawn's Archaeology system: decode clues, dig the Codex War ruins beneath the towns, and fill a Field Register with what you find."
---

# Archaeology System

Britannia's towns burned through a quarter century of the Codex War and were rebuilt stone by stone. Beneath their streets lies the burn layer, and in it everything the war left behind.

Decode clues that drop throughout the world, find the dig site from the X, Y in the clue, and excavate it with three tools. Most of what comes out of the ground is war-layer spoil: bone, charred wood, broken bottles. Now and then you find a town's notable piece, more rarely a rare one, and once in a long while a legendary find the whole shard hears about.

## Template

These are the core skills:

- Inscription - decodes most clues, can be used from another character
- Cartography - decodes map fragments, and adds up to +10% find chance at 100
- Mining - breaks ground (70+) and works the rubble (80+)
- Item Identification - brushes out the find (70+), and adds up to +10% find chance at 100

This is a suggested template:

- Magery
- Meditation
- Cartography
- Lockpicking
- Mining
- Item identification
- Inscription / Hiding / Resisting spells

That can also work for [Mining](../skills/resource-gathering/mining.md) and [Treasure Hunting](../game-mechanics/treasure-hunting.md).

## Clues

Clues randomly drop from monsters, and turn up in paragon chests, pirate strongboxes, and occasionally while fishing. An escort who can't pay may hand you one instead.

They come in five types. The only difference between them is the skill needed to decode them.

Double-click a clue in your backpack to try to decode it. Failure doesn't use up the clue, so you can try again when your skill improves.

| Clue Type               | Decoded With | Skill |
|-------------------------|--------------|-------|
| A torn map fragment     | Cartography  | 70+   |
| A faded expedition note | Inscription  | 70+   |
| A partial journal page  | Inscription  | 70+   |
| A dusty book page       | Inscription  | 70+   |
| An old digging permit   | Inscription  | 70+   |

Once decoded, opening the clue shows the X, Y of the dig site. Single-click a decoded clue to see which ruin it leads to and how promising the site looks:

- `[Old Trinsic ruins]`: the site is in the ruins of Old Britain, Old Moonglow, Old Yew, Old Trinsic or Old Minoc. Each of the five ruins is equally likely.
- `[looted site]`, `[worked site]` or `[undisturbed site]`: an undisturbed site gives a better chance of a good find. See [What You Find](#what-you-find).

That makes it easy to sort a stack of clues and dig one town at a time. Decoded clues can be traded, so a scribe can decode clues and sell them to diggers.

## Archaeology Tools

A bag of Archaeology Tools can be purchased from Provisioner NPCs for 8,000 gp.

Inside you'll find:

- Archaeologist's Sturdy Shovel - Stage 1 tool
- Archaeologist's Pick Hammer - Stage 2 tool
- Archaeologist's Soft Brush - Stage 3 tool

Each tool has 200 uses, shown when you single-click it. A use is spent each time you finish a stage, so a bag lasts about 200 digs. Missed swings cost nothing.

## Finding the Dig Site

The coordinates in the clue are the exact X, Y location. Use a map, landmarks, or rune travel to find the spot. Dig sites are always on open ground, never inside a wall, a house or water.

You must be within 1 tile of the spot for your tool to work. If you use a tool within 5 tiles of it, you'll be told which way to go: "The ground looks disturbed a few paces to the north-east."

## Excavation

Double-click a tool and target the clue in your backpack while standing at the dig site. Each stage takes **3 successful swings**, about 3 seconds apart. After a swing the target cursor comes back by itself, so you can keep digging without double-clicking the tool again.

The first swing opens an **excavation**, a dirt mound that anyone passing can see. It grows as you work, and fills back in 10 minutes after your last swing.

| Stage | Tool | Skill needed | Swing check |
|-------|------|--------------|-------------|
| 1. Break ground | Shovel | Mining 70 | Mining 50 – 100 |
| 2. Clear rubble | Pick Hammer | Mining 80 | Mining 60 – 100 |
| 3. Brush out the find | Brush | Item Identification 70 | Item Identification 50 – 100 |

- Below the skill needed for a stage, you're told so, and no use is spent.
- At the skill needed you'll land 40 – 50% of your swings. At 100 every swing lands.
- Each finished stage tells you what you've reached: topsoil, then rubble, then the burn layer of the war.
- Progress belongs to the digger. If a half-dug clue changes hands, or the excavation fills back in before you finish, the dig starts again with the shovel.
- The clue is used up when the brush stage is finished.

## What You Find

Every finished dig turns something up. The find goes into your backpack, or into your bank box if your pack is full.

How good the find is depends on your **find chance**: 10%, plus up to 30% from Mining, up to 20% from the clue's site, up to 10% from Cartography and up to 10% from Item Identification. It's capped at 75%.

| Tier | Chance per dig | With a 60% find chance |
|------|----------------|------------------------|
| Legendary | 0.4% × find chance | about 1 in 400 |
| Rare | 6% × find chance | about 1 in 28 |
| Uncommon | 33% × find chance | about 1 in 5 |
| Common | everything else | about 3 in 4 |

A 60% find chance is a grandmaster miner with grandmaster Item Identification digging an average site.

Each tier draws from the town's own finds, plus Ancient Runes among the rares in every ruin. A legendary find is announced to the whole shard.

Single-click a find to see its tier, who unearthed it and when. Finds dug before patch 1.23 show only their tier.

Each finished dig can also turn up a coin for [Coin Collecting](coin-collecting.md).

## Field Register

A **field register** is a book for your finds. Provisioners sell it for 50,000 gp.

Drop a find onto the register in your backpack to enter it. The find is used up.

- The register has a page for common finds and one for each ruin. Double-click it to browse them. Finds you haven't entered yet show greyed out.
- Each kind of find can be entered once. A second copy of an uncommon, rare or legendary find is refused, so you can keep it or trade it.
- Common finds can always be entered. Every common find you enter adds to your **spoil** count.
- Each entry in the register has a short history of the find, whether you've entered one yet or not.
- Single-click the register to see how many finds and how much spoil it holds, and who keeps it.

### Achievements

Register achievements are under **Collections / Archaeology**. You earn a rung when the find you enter takes the register past it. Handing a full register to another character doesn't give them its rungs.

| Achievement | Requirement | Title |
|-------------|-------------|-------|
| A Few Shards to The Whole Burn Layer | Enter 5, 10, 15, 20, 25, 30, 35, 40 and 47 different finds | |
| Spoil Sorter to Spoil Master | Enter 25, 50, 100, 250 and 500 pieces of spoil | |
| Ash Sifter | Enter 1,000 pieces of spoil | Ash Sifter |
| Antiquary of Britain, Moonglow, Yew, Trinsic or Minoc | Every find from that town's ruins, legendaries aside | Antiquary of *town* |
| War Historian | Every ruin's page, legendaries aside | War Historian |

The **Relic Hunter** chain under PvM / Archaeology still counts every find you dig up.

## Artifacts

Common finds turn up beneath every town.

|                                         Artifact                                          |                  Found at                  |
|:-----------------------------------------------------------------------------------------:|:------------------------------------------:|
|       ![icon](../assets/items/ancient-armor-fragment.png)<br>Ancient Armor Fragment       |                Old Trinsic                 |
|        ![icon](../assets/items/ancient-crafting-mold.png)<br>Ancient Crafting Mold        |                 Old Minoc                  |
|          ![icon](../assets/items/ancient-mining-pick.png)<br>Ancient Mining Pick          |                 Old Minoc                  |
|            ![icon](../assets/items/ancient-parchment.png)<br>Ancient Parchment            |                Old Moonglow                |
|              ![icon](../assets/items/ancient-sextant.png)<br>Ancient Sextant              |                Old Moonglow                |
|          ![icon](../assets/items/ancient-shield-boss.png)<br>Ancient Shield Boss          |                Old Trinsic                 |
|      ![icon](../assets/items/ancient-silver-necklace.png)<br>Ancient Silver Necklace      |                Old Britain                 |
|        ![icon](../assets/items/ancient-smithing-tong.png)<br>Ancient Smithing Tong        |                 Old Minoc                  |
|          ![icon](../assets/items/ancient-weapon-hilt.png)<br>Ancient Weapon Hilt          |                Old Trinsic                 |
|       ![icon](../assets/items/ancient-writing-stylus.png)<br>Ancient Writing Stylus       |                Old Britain                 |
|              ![icon](../assets/items/astrolabe-piece.png)<br>Astrolabe Piece              |                Old Moonglow                |
|               ![icon](../assets/items/bent-horseshoe.png)<br>Bent Horseshoe               |                Old Trinsic                 |
|                ![icon](../assets/items/bone-fragment.png)<br>Bone Fragment                |                 Every town                 |
|                ![icon](../assets/items/broken-bottle.png)<br>Broken Bottle                |                 Every town                 |
|               ![icon](../assets/items/broken-pottery.png)<br>Broken Pottery               |                 Every town                 |
|             ![icon](../assets/items/ceremonial-staff.png)<br>Ceremonial Staff             |                Old Britain                 |
|                 ![icon](../assets/items/charred-wood.png)<br>Charred Wood                 |                 Every town                 |
|             ![icon](../assets/items/commanders-seal.png)<br>Commander's Seal              |                Old Trinsic                 |
| ![icon](../assets/items/deteriorated-cloth-fragments.png)<br>Deteriorated Cloth Fragments |                 Every town                 |
|        ![icon](../assets/items/handful-of-bent-nails.png)<br>Handful Of Bent Nails        |                 Old Minoc                  |
|         ![icon](../assets/items/mysterious-runestone.png)<br>Mysterious Runestone         |                Old Moonglow                |
|             ![icon](../assets/items/old-copper-coins.png)<br>Old Copper Coins             |                 Every town                 |
|               ![icon](../assets/items/royal-wax-seal.png)<br>Royal Wax Seal               |                Old Britain                 |
|                  ![icon](../assets/items/rusted-fork.png)<br>Rusted Fork                  |                 Every town                 |
|             ![icon](../assets/items/soldiers-buckle.png)<br>Soldier's Buckle              |                Old Trinsic                 |
|             ![icon](../assets/items/soot-stained-mug.png)<br>Soot-Stained Mug             |                 Old Minoc                  |
|    ![icon](../assets/items/tarnished-silver-utensils.png)<br>Tarnished Silver Utensils    |                Old Britain                 |
|               ![icon](../assets/items/tattered-cloth.png)<br>Tattered Cloth               |                 Every town                 |

## Related pages

- [Inscription](../skills/magic/inscription.md)
- [Cartography](../skills/utility-and-support/cartography.md)
- [Mining](../skills/resource-gathering/mining.md)
- [Item Identification](../skills/utility-and-support/item-identification.md)
- [Coin Collecting](coin-collecting.md)
