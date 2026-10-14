---
description: "Patch notes for New Dawn server patch 1.18, released October 13th, 2026. Highlights: Halloween Rift Season: The Eight Nightmares and Trick or Treat."
---

# SERVER PATCH 1.18

## October 13th

This patch continues to build on the previous patches, making enhancements to existing systems, while introducing a few new features.

## 🛠️ Bug Fixes & Enhancements

- Greater explosion pots pulled from the storage rack no longer stack
- Storage rack now has an audit log showing items added/removed (last 200)
- After Harrower is killed, the guild region is removed in 10 minutes
- The guild region for Harrower is increased from 30x30 to 50x50
- Additional changes to the fish leaderboard, which will now handle big fish differently, and let keep a log of all turned in big fish
- Revamped the rewards gump so it's easier to see larger items
- Added hunting achievements for sandstone, stone and marble elementals
- You can change the sex of your character at the county clerk for 500k
- The range to purchase from a player vendor is now 5 tiles
- Fixed lumberjacking bug causing higher failure rates and little to no Battle Lumberjackin' encounters
- The stable claim's list will let you sort by stabled, type, and name
- Ghosts that wander more than 30 tiles from their corpse (or whose corpse has decayed) can no longer see other players or creatures. Only vendors, guild members and party members remain visible, so you can still find a healer
- AFK resource checks now come at a more natural pace instead of popping up the moment the timer runs out
- You won't get a AFK check simply for using your axe
- The house gump had a slight makeover while fixing the issue with the clear courtyard option not displaying if your house was public
- Silvani damage will count towards the total champ damage
- Expanded out some additional rift related achievements
- Those annoying kids got a little smarter it seems
- Monsters you pull up fishing will go straight for you
- Crafting menu clicks are now ignored until the Make # batch finishes, and you'll see a message. Step away from your spot to cancel a batch early
- Failed attempts used to count toward your Make # total. Batches now keep going until they've made the full amount, or until you run out of materials, your tool breaks, or you step away
- Collector's Week Tier 3 changed: dungeon statues may now be gilded bronze or gold, replacing the double roll
- Revamped the `[profile` UI

## 🎃 Halloween Rift Season: The Eight Nightmares

Starting soon, every town rift is taken over by its own horror story.

- Each rift now has **four waves** before its **mini-boss** appears
- Clear all eight to call up the season boss
- All rift kills pay out **Halloween Candy** in place of Rift Shards. Spend it at the Reaper's Hollow Market
- Any Halloween rift creature can drop a super rare **Phantom Fleet Chart**. Mini-bosses drop one far more often

See the [Rift Seasons](../custom-systems/rift-seasons.md) page for every rift's waves and mini-boss.

### Trick or Treat

During the Halloween rift season, say "trick or treat" and pick a shopkeeper to beg candy from. Sometimes you get a treat, sometimes a trick! Shopkeepers remember you, so don't push your luck.

See the [Trick or Treat](../custom-systems/rift-seasons.md#trick-or-treat) section for details.

## ⚔️ Order vs. Chaos: The War for Britannia

Order vs. Chaos is now a full open-world war. Fight for outposts across Felucca, earn War Tokens, climb the ranks, and help your faction win the monthly season.

- Your faction is your guild's type. Join an Order or Chaos guild to take part
- Capture **Watchtowers**, **Field Camps**, **Supply Depots** and **Shrines of War**, each granting your faction a bonus
- Take heads and ears from enemy faction members and turn them in at your Herald
- War Tokens are now the Order vs. Chaos payout, spent at the new faction stores
- Faction Points are no longer spent. They are your lifetime rank and never go down
- Five ranks per faction, each with its own title and store wares
- Monthly seasons with a winner's bonus, an underdog bonus, and Champions of the Season
- New War Map (`[OvcMap`), `[OvcPoints` command, Herald upgrades and 13 new achievements
- "Ear" no longer triggers the Herald on words like hear or year

See the [Order vs. Chaos](../custom-systems/order-vs-chaos.md) page for full details.

## Masonry Expansion

Stonecrafters have three new categories, **Hearths & Stoves**, **Monuments** and **Columns & Pedestals**, plus new decorations.

- Fire pits, stoves, ovens, fireplaces and hearths. You can cook on them, and bake in the ovens and stone stove
- 21 grave markers, from simple gravestones to tomb slabs, a grave obelisk and a stone spire
- Stone and marble pedestals, plus sandstone and marble columns
- The sandstone fountain, small urn and small tower sculpture can now be crafted
- Stonework takes the color of the granite used to make it, and hearths, stoves and fireplaces keep their color when turned back into a deed
- Most monuments and columns can be flipped with an interior decorator

See the [Masonry](../skills/crafting/carpentry.md#masonry-crafting) section for every recipe.

## Housing

House owners can now buy more space from the house sign: open Info and choose Expand storage.

- +20 lockdowns: gold from your bank, plus 3 perfect emeralds in your backpack
- +1 secure container: gold from your bank, plus 3 dark sapphires in your backpack
- Each kind starts at 500,000 gold and costs 100,000 more every time you buy it for the same house

See the [Housing](../game-mechanics/housing.md#expanding-storage) page for full details.

## Stealth & Armor

Stealth now depends on what kind of armor you wear and where you wear it, not how good it is. Upgrading your armor no longer makes you worse at sneaking.

- Leather armor and shields never hurt Stealth, whatever their quality, color or magic level
- Studded leather costs a little. Metal and bone armor cost more, and heavier pieces like chests and legs cost the most
- A single heavy piece over lighter gear is still workable, but a full heavy suit still makes stealth impossible
- The Stealth skill check is a little more forgiving overall

See the [Stealth](../skills/stealth-and-thievery/stealth.md#armor) page for the full armor table.

## Dungeon Treasure Chests, Lockpicking & Remove Trap

Dungeon treasure chests now respawn faster, hold better loot, and reward both lockpickers and trap removers.

- Unlocked chests break apart after 5 minutes so a fresh chest can spawn in their place
- Level 3 and level 4 chests hold much more gold and always contain gems
- Chests (level 2 and up) can contain the dungeon's dye material when picked with Lockpicking
- New **masterwork** level 4 chests need 95.0 Lockpicking and hold far more loot
- Grandmaster lockpickers can find **hidden compartments** holding rare items found nowhere else
- Remove Trap now salvages parts of the trap, and disarming before picking improves the loot
- Level 4 locks give Lockpicking gains all the way to 100.0, and level 4 explosion traps can no longer kill most characters outright

See the [Dungeon Treasure Chests](../game-mechanics/dungeon-treasure-chests.md) page for full details.

## We like, we like to party!

- Parties can now hold up to 40 members
- Party leaders can give individual members permission to invite new players
- Party leaders can turn fame and karma sharing on or off with the "Share" button in the party window (or /share)
- Attacking a party member or their pet no longer flags you as a criminal, and killing one doesn't give a murder count
- Your party can loot your corpse by default. Fixed the Loot button and /loot command not reflecting or changing this setting
- The party window now shows the names of members who are out of range

See the [Parties](../game-mechanics/parties.md) page for full details.

## Sea Encounters

Deep water is no longer a quiet place to fish. Fish from the deck of your boat in Felucca's deep water long enough, and something will come out of the fog to meet you.

- Watch for warnings like "A fog bank gathers along the horizon"
- Pirate Raiders, a Distressed Fisherman, a Derelict or a Ghost Ship sails up beside you and throws a boarding line onto your deck
- Clear the deck crew, then claim what's in the hold
- Once the encounter is won, the ship sinks. You have two minutes to get off

### 🎃 The Phantom Fleet (Halloween)

Creatures in the Halloween rifts sometimes drop a Phantom Fleet chart marked with a spot at sea. Sail there and use it from the deck of your own boat to call one of four haunted ships.

- Each Phantom Fleet boss drops Soul Coins. Spend them with Mortlake the wreck warden at the Phantom Fleet Exchange
- Charts only work while the Phantom Fleet sails during the Halloween Rift Season

See the [Sea Encounters](../custom-systems/sea-encounters.md) page for full details.

## Astronomy: The Night Sky Awaits ✨

Willebrord the Astronomer has pitched his tent east of Moonglow (4707, 1127). One thousand constellations are hidden in the New Dawn night sky, and only you can discover and name them.

- Craft a telescope with Tinkering (80+ skill) and lock it down in your house
- Search the sky at night. Each constellation appears in only one period of the in-game night
- Chart a discovery with a star chart crafted with Cartography (50+ skill), then name it
- Be the first to hand it to Willebrord and your constellation is recorded forever in the Constellation Ledger. You also receive a brass orrery and the recipe for the Bloodrift Telescope
- Each account may claim 2 discoveries per week

See the [Astronomy](../custom-systems/astronomy.md) page for full details. Clear skies, astronomers! 🌌

## Treasure Hunting: Rare Finds

Treasure chests now sometimes hold more than gold. The higher the map level, the better your odds.

### Coin Collecting

Britannia's money has a history, and some of it is still buried. Treasure chests (and to a lesser extent artifact clues) can now hold old coins, tokens and banknotes from three eras: The Crown Years, The Codex War and The Rebuilding.

- The catalog lists 86 issues. Some turn up often; a few have been seen only a handful of times
- Where you dig matters. Pieces tend to surface near the towns that issued them
- Many issues also exist in rarer varieties. The catalog doesn't list them; you'll know one when you find it
- Bankers sell the Coin Collector's Book for 1,000 gold. Drop a piece onto it to mount it permanently
- Complete the Base Set for the title Numismatist, or the Master Set for Master Numismatist

See the [Coin Collecting](../custom-systems/coin-collecting.md) page for full details.

### Ultima Busts & Grave Dirt

- Very rarely, a chest comes up with a stone bust of one of fourteen great figures from Britannia's history. Find all fourteen to earn the title Curator of Britannia
- Grave dirt is a rare decorative find, with an achievement of its own

See the [Treasure Hunting](../game-mechanics/treasure-hunting.md#rare-finds) page for full details.

## Client Update

The goal with these updates is to enhance the overall experience, but also still stay true to the the early years of UO. One could easily turn the UO client into another modern MMO client, and with some of the changes over the year, you could argue that the New Dawn client has moved that way a little.

### Built-in Assistant

Razor is the best assistant for Ultima Online, so the goal here isn't to try to change hearts and minds, instead the goal of this was to create a near perfect 1:1 look, feel, and featured assistant that is built into the client

If you want to try it out, disable Razor in the launcher, and open the client normally. After you're logged in, you will see an Assistant button the top bar you can use

See the [Built-in Assistant](../getting-started/built-in-assistant.md) page for more.

### Parties

- Parties can now have up to 40 members, shown in a new scrolling party window
- Party members who are far away now show their names instead of blank entries
- The party leader can let other members send invites
- The party leader can turn fame/karma sharing on or off (button or /share)

### Interface

- Options search: a search box in Options finds any setting and takes you straight to it
- Enhanced buff bar (optional): time left is always visible, shown either as an icon grid or as cooldown-style bars. You can choose the sort order, and buffs can flash when they're about to run out
- Connection window: when expanded, it now shows a live graph of upload and download traffic
- The advanced skills window now lists only the skills used on New Dawn

### World & Visuals

- Moving boats now leave a wake and bow spray, and boats sitting still have water lapping around them. Turn this off with "Show boat water effects" in Options
- xBR zoom smoothing (optional): smooths the world when zoomed in (Options → Video → Zoom)
- Nights are no longer too dark, and night sight is no longer dimmed or tinted blue if you have the Sun/Moon feature on

### Fixes

- The Disarm macro and the Disarm ability no longer ready Stun by mistake
- Pressing Tab while typing in a text box no longer toggles war mode
- Re-casting a buff now resets its timer right away
- Tooltips with countdowns no longer flicker