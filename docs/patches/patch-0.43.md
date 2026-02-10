# SERVER PATCH 0.43

**March 8, 2025**

This patch introduces a new system for discovering artifacts throughout the ruins found across the world of New Dawn.

## 🏺Archaeology/Artifact System🏺

### 🗺️Clue Hunting

- Map fragments can be found via fishing 🎣
- Journal pages, book pages type clue will randomly drop on mobs similar to how treasure maps drop
- Decipher clues with 70+ Cartography (maps) or 70+ Inscription (texts). Higher skill of course, you have better odds

### 🛠️Tools & Techniques

Equip your archaeologist's shovel, pick Hammer, and Brush to progress through three excavation stages:

1️⃣ Untouched (Shovel, 80+ Mining)

2️⃣ Excavated (Pick Hammer, 90+ Mining)

3️⃣ Cleared (Brush, 80+ Item ID)

A bag of archaeologist's tools can be purchased at any provisioner.

### Discovery Odds

Artifact chances scale with Mining skill, Cartography/Item ID bonuses, and site quality:

- Common: 40-50%
- Uncommon: 10-20%
- Rare: 1-5%
- Ultra-rare: 0.1-0.5%

📝 Each dig site mixes unique artifacts with common (low value) items archaeologists often find in old ruined towns. Clues are consumed after use.

## 🏴‍☠️ Smugglers' Market Update 🏴‍☠️

Anticipating resource shortages across New Dawn, shady merchants have emerged from the shadows. These "seafaring entrepreneurs" have set up a few trading posts throughout the world. They only conduct business at night, but will sell you whatever you need—at a premium.

## 📜General Fixes/Changes📜

Along with the above updates, just some general changes/fixes

- New players will no longer be defaulted into the young program and spawning in Ocllo. If you want to join the young program, type [young.
- All starting cities spawn you in the right location 😅
- You can only obtain young status 2 times. You all know how to play UO, stop it.
- Blank scroll weight changed from 1 to 0.1
- Craftable runebooks require a higher minimum skill, 64 recall and gate travel scrolls, and 3 pieces of leather
- Spellbooks require 3 pieces of leather, 50 of bloodmoss, spider's silk, and black pearl
- Adjusted some pirate names so they aren't as stupid
- Mages who sell reagents sell them at 3gp a piece and now restock at 999
- Scribes who sell blank scrolls sell them at 3gp a piece and now restock at 999
- Arrows and bolts are for sale from NPCs at larger amounts

🌕 The current phase of the moon will affect how dark it gets at night. A new moon, for example, will make nights very dark, compared to a full moon which will have things a bit brighter at night

🌒 The moon's phases last several in-game days instead of changing throughout the in-game day to be a bit more realistic

🌗 The spyglass can only be used during the night time and tells you the current moon phase

- Fixes Lord/Lady not displaying correctly
- Creatures are given follow orders upon taming
- Fixes turning on target when casting
- Character names are unique to your account -- in other words, you can have multiple characters on your account with the same name
- Implemented the base code for automated seasonal events -- more to come on this
- Relocated the Serpent's Hold moongate

## 🤖Server🤖

In an effort to keep the core server code aligned with the downstream project, the code server code has been merged to the latest version. Most of them (as usual) focus on performance gains, and backend code changes that you won't really notice directly but help long-term.

- Base code merged up to the latest upstream
- Server upgraded from dotnet8 to dotnet9 (numerous performance improvements, including loop optimizations, inlining, etc)
