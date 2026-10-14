---
description: "Patch notes for New Dawn server patch 1.11, released May 13th, 2026. Highlights: Masonry, Dungeon of the Week (DOTW) and Cooking Bulk Order Deeds."
---

# SERVER PATCH 1.11

## May 13th, 2026

Alongside with bug fixes and quality-of-life improvements, this update includes some new systems such as the Dungeon of the Week and Masonry.

## 🛠️ Bug Fixes & Enhancements

- Oshii trees no longer reproduce
- Removed the dismiss button from the new player vendor gump
- Fixed issue with Codex Rift gump not being able to be closed
- Fixed issue with some tmaps that came from pirate instance chests
- Fixed issue with name change clerk
- Fixed overlap of the BOD book ID on the previous button
- Added some additional info to BOD gumps to help with clarityd
- Fixed region issue with the Wood Framed Stone Manor
- The nightmare achievement tier has been adjusted to reflect the spawn rate
- If someone is banned from your house, all characters (new and old) across all 3 of their accounts are banned
- Mining takes 6 seconds to extract any resources instead of 1 second
- Reduced the chance to get gems from mining
- Savages drop tribal dyes instead of tribal paint
- Added a NPC Carpenter's Guild
- Carpenters can now craft the counter table with no legs and the counter table with a green runner with no logs
- You must have a fishing pole in your hand to fish, and a mining tool to mine
- Pirate maps will give you a confirmation prompt before you spawn the gate
- The pirate cargo reward, when double-clicked, lets you select 1 of the 4 pirate hues
- Adjusted the size of the region around Lord Oaks
- Potential fix to the issue where you pet appeared "stuck"
- Fixed issue with pet follow speeds:
    - A bonded pet will now keep up with you both on a mount or while running
    - A non-bonded pet will fall behind slightly when you're on a mount or while running
    - A spirit summoner summons will keep up with you both on a mount or while running
- Removed shafts from being purchased from NPCs (for now)
- Completed auctions will be posted in #sell
- Refined some of the messages the server sends to Discord

## 🗿🔨 Masonry 

<div class="rpg-scroll" markdown="1">
**A Notice from the Carpenter's Guild of Britain**
_Posted by order of the Guildmaster, for the attention of all members in good standing._

It has come to the Guild's attention that ore elementals -- those ill-tempered masses of living rock disturbed by use of the gargoyle pickaxe -- have been found carrying something unexpected among their remains. Pages. Old ones. Dense with measurements, diagrams, and the kind of hard-won knowledge that doesn't come from a library.

Our scholars believe them to be pages from an ancient masonry manual, authored by craftsmen who worked stone long before Britain's now ruined walls were laid. How the pages came to rest inside creatures of living ore is a question we've chosen not to dwell on. What matters is what they teach.

The Guild hereby announces that Grandmaster Carpenters may now learn *Masonry*.

Those who recover enough of these pages and study them carefully will find their craft expanded -- stone and wood worked together into forms that standard carpentry never permitted. This is not a separate discipline. It is the natural extension of a lifetime spent understanding what materials can do when pushed to their limits.

Seek out the elementals. Bring the gargoyle pickaxe. The pages won't come to you.
<span class="rpg-signature">By chisel and timber, The Carpenter's Guild of New Minoc</span>
</div>

A few notes:

- Adjusted the difficulty on the various ore elementals to scale better for the system mechanics on the server
- Increased the chances of spawning an elemental when using a gargoyle pickaxe
- Low chance for a marble, stone, or sandstone elemental to spawn, which have a chance to drop masonry pages and stone, sandstone, and marble blocks
- Toggle ore mining or stone/ore mining by single-clicking your mining tool
- Purchase the book from the Stone Crafter NPC, collect the four missing pages to learn masonry
    - Enables you to mine up granite and use stone blocks to craft new items
    - You can purchase a mallet and chisel from them too

## 🐉 Dungeon of the Week (DOTW)

Introducing the Dungeon of the Week system! Britannia's dungeons have always had their own character, and this system is designed to give you a reason to venture into ones you might not otherwise visit.

### How it works:

Every Monday around 8AM CT, 4 of the 10 available dungeons are randomly assigned one of four weekly bonuses. All four are active simultaneously, so there's always more than one reason to head underground.

- 🪙 Gold Rush - Creatures drop double gold and bonus loot
- 💎 Collector's Week - Rare items may drop from creatures
- 🌀 Rift Surge - Rift shard, rift spawns, and rift gates have a higher chance to drop from creatures
- 🏫 Scholar's Week - Skill gains are faster

### Checking the current rotation

Along with being announced on Discord, you can type `[dotw` in game to see which dungeons are active and what bonus each one is running this week.

## 🧑‍🍳 Cooking Bulk Order Deeds

Is there a list? There is a list. Are cooking BODs on that list? It was not on that list. And yet..

You can now get cooking BODs from your local cook or baker, with rewards scaled to your points that are cooking and baking themed. Your kitchen deserves to look like someone actually lives there.

## 🛠️ Carpentry Bulk Order Deeds

- Furniture, containers, or cabinet BODs will never require special logs
- Instruments, staves, and wooden shields when crafted will display the hue of the material
- Instruments, staves, and wooden shield BODs now require the item to be crafted with the correct material to be combined
- Fixed missing cliloc message on carpentry BODs that require a specific log type

## 💰 In-Game Currency

Your pirate doubloons, champ tokens, harrower shards, rift shards, and war tokens are shared across all characters on an account. Each citizen of New Dawn has their own identity, their own history, their own place in Britannia -- and keeping currency tied to the character who earned it was part of reinforcing that.

But unlike reputation, skills, or the name people know you by, reward currency reflects the effort of the player behind the character -- not the character themselves. I understand that distinction. It should follow you, not just one of your citizens.

That said, this doesn't extend across accounts. For now, I try to view each account as its own entity, and the game is balanced around that assumption for now.

!!! note
    When the server starts up, it will migrate all your character currencies to your new account wallet that you can view using `[profile`

## ⛳ CTF & Conquest ⚔️

- When you die in CTF, dueling, or Conquest, your items will be reequipped on resurrection
- Adjusted the Conquest countdown to 45 seconds before the game starts
- Explosion pots have an 8 second timer inside duel, Conquest, and CTF battlegrounds
- Prevent you from signing up or switching teams after CTF or Conquest has started
- You no longer double-click the flag to cap, instead you stand next to your flag base and it will capture
- All conquest messages go to #conquest
- Those who didn't a Conquest tester reward should get one when you log in

## 🐙 Ink of the Deep 🌊

<div class="rpg-scroll" markdown="1">
**From the Journal of Marney, Ward of the Docks at Skara Brae**

_These pages were found among her effects by Yorl, and copied here with his blessing._

I know what pirates look like. I know better than most.

I was mending net past where the lanterns reach when the boat came in quiet. No colors flying. Just men moving with the kind of purpose that makes you go still without deciding to. But they weren't raiding. They were working -- pulling octopus and cuttlefish from the shallows, not for eating, and boiling the ink down in iron pots right there on the water's edge. Then soaking their clothes in it. Slow and deliberate, like a ritual.

The black that came out didn't reflect anything back. Like looking at a gap where something used to be. My mother was buried in black. It was nothing like that.

I didn't tell Yorl. I wrote it down here instead.

<span class="rpg-signature">-- Marney</span>
</div>

You can now extract ink from the rare catches of octopus and cuttlefish. The ink can be used on a purchased dyetub to create a limited use black ink dye tub.