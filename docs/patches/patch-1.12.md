# SERVER PATCH 1.12

## June 10th, 2026

Alongside with bug fixes and quality-of-life improvements, this update introducing bee keeping, and some pirate map changes.

## 🛠️ Bug Fixes & Enhancements

- Fixed Iolo's player vendor drop message to show the correct days left
- Fishing nets show the hue on single-click
- Dracothraxus has been modified to have a larger hit pool, a bit stronger, and a new special attack
- Dracothraxus will now spawn in every dungeon
- Increased the price of iron ingots on the tinker NPC
- First time name changes are actually free from the county clerk
- Dungeon tailoring dyes will now apply to masks and footwear (sandals, boots, thigh boots)
- You can no longer mine from a house
- Increase the max barkeep count from 2 to 5 in houses
- New players who change their name from "Generic Player" won't trigger a Discord message
- Increase the treasure map level on Elder Gazers
- Added ancient liches to the pool that can drop repond slayers
- Added an initial delay on mobs that use fire breath
- Fixed the cooking apron so it increases cooking, not tailoring
- Fixed issue with the cooking counter addon (missing hue and placement order)
- Fixed issue with house raffle stone not firing at the end of the raffle without manual intervention
- The guild gumps have been redesigned a bit
- Fixed issue where spirit summoned pets would be red (and attackable) for some but blue (and non-attackable) for others. They're now blue as intended, same as a normal pet would be
- Fixed some speed issue with pets (still a few outstanding issues I pack in next patch)
- Adjusted the max skill requirement on plate chest/tunic
- Adjusted the BOD rewards for blacksmithing, combining some of the lower-end runic hammers into a single reward, and adding new deco rewards
- Fixed desert region and music
- Trash barrels will reject containers with the number of items that would trigger auto-trash deletion
- Added new hued sandals to the Riftwalker reward store
- Revamped the Help gump to encourage people to use #submit-a-ticket
- Spellbooks can only be obtained on a new character or crafted from a player, no longer sold from NPCs
- Adjusted charges from 600 to 200 on the ancient smithy hammer
- Fixed the issue with the hued lantern rewards not displaying correctly
- Changed the hue on yellow plants to 1719 so the bright yellow version that's more unique (doesn't apply to already existing plants)
- Ore elementals don't like being on ships or in-houses and will no longer resist magic when in there

!!! note
    This one might ruffle some feathers - I know other shards handle it differently. But using trapped mobiles in houses or on boats as a skill or resource farm isn't something I've ever felt comfortable with. Feedback welcome, and I'm open to revisiting it down the road

- Barnacled and rusty chests are now usable containers

!! note
    Existing chests will remain how they are, simply deco with a message saying they cannot be opened. If you want the updated working container, let me know and I'll swap it for you. If you want to keep the (now no longer available option) non-usable one, you can do that as well. All future fished up chests will be usable.

## 🏴‍☠️ Pirate Maps 🦜

- The particpant and pet count is locked after the gate disappears at the beginning of the instance start, instead of at the end
- After defeating the pirate map boss, the chest has a chance to have a silver slayer and a usable chest that matches the instance color/hue (two seperate chance rolls)
- Added achievements based on the pirate maps
- Pirates are now affected by slayer weapons
- Updated the pirate lookouts with a new scout AI (sorry in advance)
- Pirates no longer reduce your karma and fame
- Added pirate flags, pirate shelf, and sandals in the 4 pirate hues to the reward store

### 💀 Difficulty Scale

To make the pirate maps a bit more challenging experience for players who want one, you can now scale up the difficulty before you launch the gate to enter.

- Before you open the pirate gate, you now select the difficulty scaler
- All enemy pirates and bosses stats, skills, hits, will be scaled up based on the difficulty you pick
- The pirate treasure chest's gold, weapons, gems, etc will scale up based on the difficulty you beat the map with
- The pirate reward vendor 

## ⚔️ Dungeon of the Week

A few fixes and adjustments to the DOTW system

- Fixed the issue with the Boon of the Slayer, mainly around slayer's not dropping as much as they should
- Fixed the incorrect descriptions when entering a dungeon, cleaned up the general descriptions you see in Discord and in `[dotw`
- Pets now see a boost in skill gains during Scholar's Week
- Refactored how the DOTW system handles when a monster that was killed in a dungeon to prevent double processing 
- Lowered the chances to get rift shards during DOTW during normal mobs, however, increased the amount you get when killing a rift spawn (sorry, the rift shard gravy train is over)

## 🐝 Apiculture (Beekeeping)

<div class="rpg-scroll" markdown="1">
**A Notice from the Beekeepers of the Realm**
_Circulated by the Society of Apiarists, for the attention of all who tend hive and harvest._

It has come to the Society's attention that the ancient practice of apiculture -- the keeping of bees, the harvesting of their gifts, and the working of wax into useful form -- has been largely forgotten in these modern times. What was once common knowledge among rural steaders and traveling chandlers has slipped away, leaving most folk unable to tell clover honey from heather, or common tallow from virgin beeswax.

The Society finds this unacceptable.

Effective immediately, the craft of Apiculture is open to all who would pursue it. Beehives may be tended, worked, and harvested by those patient enough to learn their rhythms. Raw wax may be rendered and assessed. Honey may be extracted, identified, and put to use -- provided the one doing the identifying has developed the palate to recognize what they're holding.

That last part is worth dwelling on. A jar of honey handed to someone with an untrained tongue is just sweetness. The same jar in the hands of a skilled taster is something else entirely -- a named varietal, a known quantity, a tradeable commodity worth considerably more than its humble origins suggest. Taste Identification is not a skill the Society invented. It is simply one we've found ourselves relying on more than most.

Tend your hives. Learn your wax. Develop your palate.

The bees won't wait for you to be ready.
<span class="rpg-signature">By comb and candle, The Society of Apiarists of New Dawn</span>
</div>

### 🐝 Bee Hives

- You can now maintain bee hives, head to the beekeeper in Ocllo to purchase a deed
- Beehives require a water tub or water barrel as a water source, which can be crafted by carpenters. These can be refilled
- Beehives (like plants) "grow" every 24 hours from when the hive was placed
- Beehives (like plants) deal with parasites and diseases so you can store various potions to help manage those
- Beehives will use water each time they "grow"
- As your beehives grow in population, they will require more water and flowers
- If you beehive dies, you must destroy it to start over. It will not return the deed
- Beehives that are too close to other beehives will require more flowers and water
- Several new achievements have been created to support the beekeeping system

### 💐 Flowers

- Beehives require flowers that can be obtained from gardening.
- Flowers must be in non-decorative mode
- Flowers that are around beehives will see a slight boost in resistance to parasites and health
- Certain flowers slightly increase the chances that the harvested honey will be of a rarer quality

The following flowers make the bees happy:

🌼 Campion, Poppies, Snowdrops, Lilies, Flax Flowers, Foxglove, Orfluer, WaterLily, Cattails, Hops

### 🍯 Honey

- To harvest honey, you must have a hive tool (which can also be purchased at the beekeeper)
- Cooking recipes now require honey extracted from hives, not NPC bought
- After you extract honey, you can use taste ID to identify the type of honey (quality)
- Your item identification skill also helps in your ability to idendity the honey
- Honey comes in a variety type types (with the correct flowers increases the chances

Clover, Wildflower, Buckwheat, OrangeBlossom, Lavender, Heather, Sourwood, Tupelo

- The Beekeeper will offer Honey Orders every 24 hours, which will require you to complete with the various honey you harvest
- You will recieve Apiary Marks when you turn in completed money orders. These Apiary Marks can be used to purchase items from the Beekeeper

### 🐝 Beeswax

- After you harvest the raw beeswax, you'll also need a wax processing pot that you can purchase from the beekeper
- After you process the raw beeswax, you can use taste id to identify the type of wax

