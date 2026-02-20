# Archaeology System

Uncover lost artifacts and treasures from Britannia's forgotten past through the Archaeology system. Decode clues that drop throughout the world, locate dig sites hidden in the coordinates embedded in the clue text, and excavate using three specialized tools to reveal what lies beneath.

## Overview

The Archaeology system lets adventurers hunt for and excavate historical artifacts from dig sites in Britain and Moonglow. Clues come in five types — map fragments, expedition notes, journal pages, book pages, and digging permits — each decoded using Cartography or Inscription. Excavation itself requires Mining and Item Identification across three tool stages.

## Getting Started

### Obtaining Clues

Clues drop randomly from monsters throughout Britannia (similar to treasure maps). There are **five clue types**, all sharing the same mechanic of containing embedded coordinates:

| Clue Item               | Decoded With |
| ----------------------- | ------------ |
| A torn map fragment     | Cartography  |
| A faded expedition note | Inscription  |
| A partial journal page  | Inscription  |
| A dusty book page       | Inscription  |
| An old digging permit   | Inscription  |

All five types are equally valid — the clue type only determines which deciphering skill you use.

### Obtaining Tools

Purchase (or find) a **Bag of Archaeology Tools**, which contains all three tools needed for excavation:

- **Archaeologist's Sturdy Shovel** — Stage 1 tool (200 uses)
- **Archaeologist's Pick Hammer** — Stage 2 tool (200 uses)
- **Archaeologist's Soft Brush** — Stage 3 tool (200 uses)

Each tool has **200 uses** and breaks permanently when they run out.

## Deciphering Clues

Double-click a clue in your backpack to attempt to interpret it.

**Map Fragments** — requires **70+ Cartography**. A skill check is made against difficulty 70–130. Failure doesn't consume the clue; try again when your skill improves.

**All other clues** (expedition notes, journal pages, book pages, digging permits) — requires **70+ Inscription**. Same skill check range (70–130). Failure doesn't consume the clue.

!!! tip "Skill Check Range"
The check is capped at 100. so higher-than-70 skill improves your success rate.

On success, the clue is marked as interpreted. A gump window opens showing the flavor text, which contains the **X and Y coordinates** of your dig site. The clue also records who decoded it.

Once interpreted, double-clicking the clue again reopens the gump to review the coordinates.

## Finding the Dig Site

The coordinates in the clue text are the exact X, Y location on Felucca. Use a map, landmarks, or rune travel to find the spot. You must be **within 1 tile** of the precise coordinate before your tool will work.

## Excavation Process

All three tools must be used in order. Each use consumes one charge from the tool. If the tool breaks mid-excavation, replace it with another before continuing.

### Stage 1: Untouched → Excavated (Shovel)

Double-click the **Shovel**, then target the clue in your backpack while standing within 1 tile of the dig site.

- Skill check: **Mining 80–100**
- On success: `"You carefully excavate the area."` — clue advances to Stage 2
- On failure: `"You fail to make any progress."` — try again

### Stage 2: Excavated → Cleared (Pick Hammer)

Use the **Pick Hammer** the same way.

- Skill check: **Mining 90–100**
- On success: `"You clear away the debris."` — clue advances to Stage 3
- On failure: `"You fail to make any progress."` — try again

### Stage 3: Cleared → Finished (Brush)

Use the **Brush** the same way.

- Skill check: **Item Identification 80–100**
- On success: a find chance roll determines whether an artifact is discovered
- The clue is **consumed** at this stage regardless of outcome

!!! warning "Wrong Tool"
Using the wrong tool for the current stage gives the message `"This doesn't seem like the right tool for this stage."` No charge is consumed.

## Artifact Find Chance

Clue quality is a hidden stat (1–100) assigned randomly when the clue is created. You have no way to influence it, but higher-quality clues boost your find chance by up to 20%.

With fully capped skills (100 Mining, 100 Cartography, 100 Item ID) and a perfect quality clue (100), your chance is: `10% + 30% + 20% + 10% + 10% = 70%`

With lower skill, typical find rates will be closer to 10–40%.

## Active Dig Regions

Dig sites are spread across **two currently active regions**:

### Britain

Dig zones spread throughout the ruins of Britain.

### Moonglow

Dig zones spread across the Ruins of Moonglow, including the bank area and surrounding ruins.

!!! note "Future Regions"
Minoc, Trinsic, and Yew dig regions are defined in the system but not yet active in-game. Their artifact tables are also drafted. These may be enabled in a future patch.

## Common Artifacts (All Regions)

These can drop from any dig site regardless of region:

| Item            |
| --------------- |
| Broken Pottery  |
| Rusted Fork     |
| Copper Coins    |
| Cloth Fragments |
| Bone Fragments  |
| Broken Bottle   |
| Tattered Cloth  |
| Charred Wood    |

Note: The loot table is weighted — the system rolls against all valid entries for your region. Multiple common items having high chances means you're statistically likely to pull a common find even when you "succeed" on the find roll.

## Strategy & Tips

### Skill Summary

| Skill               | Requirement | Effect                                            |
| ------------------- | ----------- | ------------------------------------------------- |
| Cartography         | 70+         | Decode map fragments; +10% artifact chance at 100 |
| Inscription         | 70+         | Decode all other clue types                       |
| Mining              | 80+         | Stage 1 success; 90+ for Stage 2                  |
| Item Identification | 80+         | Stage 3 success; +10% artifact chance at 100      |

### Optimal Build

- **100 Mining** — maximizes stage success rates and adds +30% find chance
- **100 Cartography** — best map deciphering success and +10% find chance
- **100 Item Identification** — best stage 3 success and +10% find chance
- **100 Inscription** — best success on 4 of the 5 clue types
- Supporting: Magery/Meditation for travel

### Practical Tips

- Stock multiple decoded clues before traveling — clue coordinates are fixed in both Britain and Moonglow, so plan a route.
- All three tools are required; carry spares of each since they break at 200 uses.
- Failed skill checks don't advance the stage, so low-skill archaeologists will burn through tool charges faster.
- The clue is only consumed on Stage 3 completion — abandoning after Stage 1 or 2 wastes the tool uses but not the clue.

## Patch History

The Archaeology system was introduced in **Patch 0.43**:

- **0.43:** Initial implementation — five clue types, three-stage excavation, Britain and Moonglow dig regions, tool system

For detailed changes, see the [patch notes](../patches/index.md).

## Related Systems

- [Achievements](achievements.md) — Track your archaeological discoveries
- [Currencies](../game-mechanics/currencies.md) — Potential future archaeology currency
