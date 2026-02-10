# New Dawn Patch Notes

## SERVER PATCH 0.1 - 0.3

**April 27, 2023**

- Removed necro, bushido, ninja, AOS from core game mechanics
- Basic Welcome gump
- Account limit 2 per person
- House limit set to 2 per account
- Implemented classic single-click ascii labels
- Blessed and newbie labels on items
- Enabled paragons spawn chance
- Option for players to single single-click context menu (typing [contextmenus)
- Corpses turn grey when dead
- Removed notority bonus while in Feluccia
- You must be a friend or higher to see house status on house signs
- Owner must refresh house after 60 days
- Fixed translucent water on ships
- Added set of custom houses
- Moved factions to the newer locations
- Character names must be unique and can't be used by anyone else
- World is fully spawned, all towns, dungeons

## SERVER PATCH 0.4

**April 27, 2023**

- Fishing works on transparent water
- More removal of unicode for ascii messages
- Updated public moongate gump
- Updated young gumps, added basic [young command, ability to rejoin
- If young player leaves Ocllo Island, young is removed
- Added graveyard regions to prevent house placement and allow for future content
- Houses cannot be placed anywhere on Ocllo
- Created Ocllo dungeon region
- Added [skillmenu command to modify all skills to specific values if you don't want to use help and set skill value
- Added restore gates to be used in pvp testing
- Basic animals can't be paragons
- Added Trinsic (WIP, still need lots of polish and the rest of the town still needs conversion)
- Serpent's Hold is 90% finished, still needs polish
- Can't mark in dungeons, nor recall or gate into them. Still need to place exit gates in all dungeons at different levels

## SERVER PATCH 0.5

**April 30, 2023**

- Added an AFK gump for resource gathering
- Fixed issue with vendors not offering any training
- Young players can't place boats
- Boats are limited to two per account
- Increased provo
- Revamped house placement tool gump
- Ocllo dungeon limited to max skill gain
- Lower the range perception of mobs from 16 tiles to 10
- Paragons drop all items in lootpack (100% chance)
- Animal taming range increased to 6
- Changed from 2 accounts, 2 houses per to 3 accounts, 1 house per person
- Implemented ability to change global skill gain factor and individual factor in-game
- Damage will display above heads
- Fix single-click with labels already starting with 'a' or 'an'

## SERVER PATCH 0.6

**May 2, 2023**

- Fixed issue with harming players in Fel
- Removed stam loss from taking steps or at low stam
- Demolished house returns money via bank check in bank
- Young players can't place houses
- Added tall small tower
- Added east facing small houses
- Using an instrument will wear it down
- Musicianship will take one use from the instrument
- Instruments will show worn status
- Additional options to fine-tune skill gains
- Fixed range perception on existing mobs (was 16, now 10)
- Updated AFK gump to be more clear
- Updated ship hues and introduced ship stains (we'll see)
- Enabled the new guild system, access it via Guild on the paperdoll (larger UI overhaul in the future, tie in guild stones somehow)

## SERVER PATCH 0.7

**May 3, 2023**

- Fixed spawners to allow sea life to spawn in the right location, spawn point decision much smarter in general
- Fixed house placement tool for east facing houses
- All potions now stack
- Allow for you to log into 3 accounts at once

## SERVER PATCH 0.8

**May 8, 2023**

- One account/IP allowed in a dungeon
- Instruments show the correct usage status
- All dungeons and levels have there own region
- EVs are a bit tougher
- Lower the chance of a paragon spawn
- Enabled champ artifacts
- Updated guild UI
- Added two new champ spots (Yew & Minoc), moved one (into Blighted)
- Locking down a container won't locked the items in it
- Fixed fishing capcha to only come up at GM
- Paragon gold is doubled on death
- Fields and pots can do damage on anyone
- Purple pots don't stack
- Removed towncheck on spells
- Enable old stealing rules around looting blue corpses and permagray
- Your criminal timer shows up as a debuff

## SERVER PATCH 0.9

**May 17, 2023**

- Added in-game invasion controller
- Added base in-game seasonal event controller
- Added longer animations and slight delay to crafting
- Added the monster stealing system
- Provo and discord break based on a max range of 18 at GM
- Additional checks on the dungeon limit system
- Using provo or discord on controlled followers is a harmful act
- You can cast gate if you're a criminal
- Added Paws
- More map updates to Trinsic area
- Jhelom now has vendors and has been transformed a bit
- Alchemy, blacksmithy, tinkering, carpentry, inscription gain slightly faster
- Skill gains are slowed down a bit if you're a 3x GM or less

## SERVER PATCH 0.10

**May 21, 2023**

- Added LOS check on NPCs when calling guards
- 1% chance for whipping vines to drop a vine deco
- Fixed issue with barding skills and range
- Added tracking of creature kills per player
- At GM Magery and GM Poison, 1% chance to land lethal if within 2 tiles, 10% chance to land deadly if within 3 tiles
- Fire field length has been reduced
- Slight adjustment to skill rates (slight increase on crafting, slight decrease in lore based)
- Added dungeon exit gates throughout dungeons

## SERVER PATCH 0.11

**May 24, 2023**

- GM Item ID can be used on a bag
- Instruments will say exceptional
- Magic reflect buff icon shows
- Fire breath actually does damage!
- Mage AI won't reveal last target if not within 2 tiles (used to be 12)
- Fixed "a Item Name" labels
- Adjusted the bard difficulty formula
- Changed some mobs to the older animations (ie: Balrons)
- Removed Terathan Keep from Harrower
- Added orc scout and Scout AI
- Champs return home if pulled too far
- All dungeons got a slight touch up, still a WIP
- Fixed east facing small brick house sign and door
- Adjusted archery standing still delay to 500ms
- Adjust the amount of fatigue loss on damage to be very low . It's much lower at it's base, and the type of armor material and where it's on your body will add to any additional stam lost penalty (testing this change, can be toggled on/off in game)

## SERVER PATCH 0.12

**May 27, 2023**

- Fixed issue with placing boats
- Adjusted follower speed. If bonded, they match your speed, if not, they are slightly slower.
- Removed dex penalty for armor (stam penalty fatigue is enabled, based on armor material)
- Adjusted the hues on studded, barbed, spined leather
- FIxed wrong healing message
- Ocllo dungeon skill limit raised to 80
- Followers return to you after killing target instead of just wandering around
- Damage on monsters is in line with damage on players (on the high end, still researching the low 1 min damage)

## SERVER PATCH 0.13

**May 28, 2023**

- Block multi-client pvp
- Follow speeds reduced when pet was told to attack first
- Adjusted virtual armor calc
- Converted all armor ratings to match earlier era
- Converted all weapons (speed, min hits, max hits) to earlier era
- Changed OnHit calc for armor and shield to match earlier era

## SERVER PATCH 0.14

**May 29, 2023**

- Fixed issue with provoing mobs outside of the range perception (where it would say they look furious, but then go after you)
- Blocked being able to open house doors from outside a house
- Added 2 second cooldowns on all potions except explosion (no cooldown) and heal (maintains the 10 second cooldown)
- Changed wandering healer logic
- Adjustment to the amount of damage dealt after its calculated (looking for feedback on this)
- Removed alchemy bonus from explosion potions.

Instead, the bonus is applied to the min damage. For example, at GM alchemy, it used to add +10 damage to calculated damage, with a chance to hit at max explosion 30 + 10 = 40 dmg. Now, at GM alchemy, the min/max roll is between 25 and 30, meaning your explosion at GM alchemy will at least do a min of 25 damage instead of 15.

- Adjusted the speed of the katana to be faster after last patch
- Fixed text type on a player corpse. Mobs corpses don't have a chance to be red.
- Dragon scales no longer drop (this will be upgraded in the future for a very low chance and with scaled dragon armor)
- The server will no longer auto-unequip your hands to cast, instead will give you a message saying you need to clear hands (this will be updated to exclude cosmetic items like lanterns, torches, etc)

## SERVER PATCH 0.15

**June 4, 2023**

- Enable casting with spellbook, runebook, lanterns, candles, and/or torches
- Added the Shield Bash ability to Parrying
- Parrying skill and the shield type & quality will absorb fire breath damage
- Removed stable fees
- Adjusted the max slots available based on your total taming, animal lore, and veterinary. GM at all 3 will give you 30 stable slots.
- Added bonded animal limits that can be acquired by the quest giver in the Moonglow Zoo
- Summoned creatures duration from 5th and 8th circle spells is increased based on your Spirit Speak skill
- Summed creatures get a boost in skills and stats based on the circle and the Spirt Speak skill of the caster
- Summoned creatures are tougher to disspell if the summoner has Spirit Speak
- Adjustment to music in the different areas (if you have music on 🎶 )
- Fixed issue with new spell books reporting the incorrect spell count

### 🗾  Map Updates

- The Event Center is now open (thanks @MrRiots!) and can be accesed via Ocllo.
- Moonglow island and the town have been changed. Lycaeum will serve as the main town on Moonglow island.
- Magincia has been cleaned up as well (still WIP)
- Bucs Den got a minor touch up (still WIP)
- Vesper Outpost created (still WIP)

## SERVER PATCH 0.16

**June 24, 2023**

- Adjusted summoning followers count based on if you have Spirit Speak or not
- Additional changes to how armor rating is calculated to be more in like with the weapons damage
- Adjust base damage formula and when damage is cut in half to match archived formula
- Reverted weapons (speed, damage) back to the UOR era numbers. I moved them to T2A numbers, but they were just too low.

🔥 Spirit Speak will now summon all new special creatures for 5th circle. Without Spirit Speak, it's the regular mage summons.

🔥 Spirit Speak will summon boosted 8th level summons. Single-click to see remaining summoned time.

- Added Champion tokens and Harrower shards (in-game currency). This will be expanded to be use in a reward store.

🔥 Added the pirate instance system (WIP - Red is available with spawners to test). A pirate ship has pulled into Dawn's harbor 🏴‍☠️

- Fixed issue with Discord registration. To register, start typing /register on Discord to test.
- Initial implementation of the title system
- Implemented the achievement system. Access via [profile or [achievements. Will be expanded out over time.

## SERVER PATCH 0.17

**July 2, 2023**

- Several adjustments to the different pirates based on feedback
- Added restrictions in the pirate instances (teleport, for example)
- Added several restrictions in the event center
- Added low chance for different type of fish to be pulled up based on if you're on the shore, deep water, or in a dungeon
- Fixed pirate chest so its lootable :LUL:
- Fixed skill achievements from triggering incorrectly
- Implemented in-game control of PvE and PvP spell damage using [spelldamage
- Implemented command to enable insta-hit [InstaHit (which will be used for special events, specific areas -- rightn now it just turns it on or off globally)

## SERVER PATCH 0.18

**July 8, 2023**

- Fixed chain lightning to chain when its two targets, also has a chance to resist
- Fixed some of the names of creatures spawned with spirit speak
- Adjustment to some of the casting times on summoning
- Summoned creatures with mage AI (daemon) won't cast invisibility on themselves
- Dispel and mass dispel have an 80% chance at GM spirit speak to be resisted by a mob that casts the spell. Player dispel continues to have a 50% chance to resist.
- Mobs that auto-dispel and bypass casting (ie: dragons) with a 100% chance when giving or getting melee damage, will have that chance reduced based on the spirit speak skill of the summoner
- Summoned spirit daemons have been toned down a bit
- Increased the min. magery skill required to cast a spell. This should make 7th and 8th not be as successful.
- Changed the casting delay formula to 0.5 * Circle
- Adjustment to the bard difficulty calculation. Dragon barding should feel more natural. Use [BardDifficulty to see the base difficulty.
- Animal lore shows barding difficulty
- Implemented in-game commands to test out changes to the spell fizzle chances (either by changing how its calculated completely, or changing the required min skill to cast as mentioned above) and casting delays
- Set the default values for min/max PvP spell damage based on testing
- Fixed issue in [profile where Disable single-click menu wasn't displaying correctly
- Adjustment to greater explosion potion damage.
-- Damage has been reduced when it hits another player.
-- Base damage against a player is min 5, max 15. With GM alchemy, you add 10 to the min, and 5 to the max, so greater explosion pots would hit min 15, max 20.
- The prompt to use the pirate gate works now
- The pirate counter should be accurate when clicking on the pirate instance clock
- New mages no longer get a newbied bag

## SERVER PATCH 0.19

**July 22, 2023**

- Remove extra spaces in some labels
- Fixed labels on armor and weapons to show quality and crafter
- Added cotton only farmable by young players
- Changed spell range to 10 on all spells except teleport (still 12)
- Pirate instance clock is more clear on remaining enemies
- Fixed issue with pirates attacking through the ship floor (LOS blocked now)
- Fixed issue with single-click label on treasure maps
- Slight adjustment to daemon summoning time
- All regions should now match the new sizes (especially towns)
- 2x damage on non-players will apply to humanoid NPCs
- Additional checks to prevent mobs from spawning under translucent water tiles
- Removed Mahjong, checkers, chess
- Removed the ability for vendors to buy resources
- Added the bosses and spawners for the three others pirate instances
- Added additional pirate instance mobs to be used
- To notice someone snooping, you must have LOS of the snooper
- Magic resist will cut damage by 1/3 instead of 1/2 in PvP combat
- Block the ability to kill players in houses with AoE spells

## SERVER PATCH 0.20

**August 2, 2023**

- Implemented baseline barding difficulty. Previously, the difficulty was calculated by a variety of factors that made it a bit more difficult to fine tune mobs.
- Increased the base barding difficulty on all pirates. I suspect this might still need some adjustment.
- Fixed issue with cooldown on potion use timers
- Every player kill is now tracked and saved to a database for later website extraction
- Buff and debuff spells can now counter potions, and potions can now counter buff and debuff spells
- Added a slight delay to firebombs
- Blocked housing in parts of ruined towns
- Fixed east facing signs on public houses and fixed east facing brick door and sign

## SERVER PATCH 0.21

**August 5, 2023**

- Block housing to be placed in ruined town areas
- Fix public signs one east facing houses
- New players won't spawn with a large harp
- Slight adjustment to barding difficulty on some pirate mobs
- Fix missing tinkering sound
- Added an in-game adjustable explosion potion delay, currently set to 1.5 seconds
- Lowest level mobs don't drop as much gold
- Trapped pouches now change color
- Added the [pouch command that will find a trapped pouched in your bag and open it
- Wands are usable again
- Meditation buff icon clears when meditation is over
- Magic Reflect buff icons goes away when you lose reflect
- Added missing buff icons for Protection and Arch Protection
- Adjust Mind Blast so resist blocks 66% if the damage
- Adjust Mind Blast to max out at 40 damage
- Fixed issue on some weapons when you single-click to get the label
- GMs can see staff items, such as blockers and LOS blockers

## SERVER PATCH 0.22

**August 7, 2023**

- Activate meditation is faster compared to passive
- Explosion potions have a small random delay before they explode (min/max adjustable ingame for testing)
- Some spells weren't reducing the damage correctly when a player successfully resisted the spell.
- Some spells allowed for 12 tile range instead of 10

## SERVER PATCH 0.23

**August 16, 2023**

- Adjustments to the purple pirate map boss, to make them a bit more difficult (still needs some additional tweaks)
- Updated the town of Trinsic to make it more lived in. Fixed Trinsic region issues.
- Enabled "smooth sailing" -- be sure to enable it ClassicUO (Options->General->Smooth boat movements)
- Fixed issue with boat commands not resetting to the right command
- Pirate Cannoneer has LOS checks now
- Removed unused quest items (unicorn ribs, etc
- Can't use ethy in a pirate map instance
- Removed 7 second delay on runebooks & runebooks now have a max of 10 charges
- Adjusted how Tracking works:
-- At GM, you can track up to 100 tiles away, 50 tiles within a dungeon.
-- The mobile being tracked must be in the same region and dungeon level as you
-- Your base chance is calculated by using the total tracking and detect hidden vs total hiding and stealth of mobiles in your range.
-- When tracking a player, after the base chance is calculated, the chance is then also reduced based on the distance. So you have a lesser chance to detect someone 90 tiles away, compared to 20 tiles away.
- When you die, items that stay in your pack (ie: blessed items) will retain the position
- Fixed the label on single-click ethys
- Champ leash was increased from 24 tiles to 90.
- Fixed issue with secure items using 125 lockdowns
- Locked down containers can now be access by anyone in range
- Weapons will display if they are currently poisoned on single-click

## SERVER PATCH 0.24

**August 22, 2023**

❗This patch contains client patches. Be sure to close out of the client, restart the launcher and let it update. Thanks to @flyer for your time remapping all the different vendor/shop locations for the world map❗
- Champion leash has been lowered to 60 (this needs more work to ensure it works for all champs)
- Fixed issue with pirate map bosses disappearing
- Fixed the AI of scouts (orc scout, pirate lookout, etc), will only flee at low health, will hide when fleeing, and reengage when health returns 🕵️
- All pirate mobs have seen skill, stats, and armor increases including some randomization in weapon and shield use, including some additional abilities depending on the pirate
- Ancient Drowner (blue pirate map boss) has been buffed across the board (hits, damage, skills)
- Captain Grimjaw has a larger hit pool and armor rating
- Fixed issue with the healers/vendors disappearing when you finished the pirate map instance
- Potion buffs, when they expire, will send the packet to the client to reflect correctly
- Tracking has been fixed when outside of specific regions
- Fixed issue with corpse hues not displaying correctly (ie: a blue corpse would appear gray)
- Changed loot drops on savages, removed other items not used (for now)
- claim list will now list all your pets in the stable 🐕
- Additional measures to keep the riffraff out of T2A
- Fixed issue with medium or big fish label not displaying correctly
- BODs are no longer blessed
- Removed some rewards (power scrolls, ancient hammer) as BOD rewards
- The BOD timer resets after you turn it in
- Added oak, ash, and yew logs/boards, with low chance of bark fragments or billiant amber (deco for now)
- Changed lumber jacking range to 1
- The waterstained SOS will now display correctly
- Aquarium fish nets have been removed from purchase (and will be obtained another way in a future patch)
- Lowered the chance for a rare fish to be pulled up
- Items like "shoes" or "boots" won't be labeled "an shoes" or "an boots" :NotLikeThis:
- Using the buy or sell single-click context menu when hidden, will reveal you
- Cleaned up the label on the tamer quest sketchbook

## SERVER PATCH 0.25

**September 1, 2023**

❗This patch contains client patches. Be sure to close out of the client, restart the launcher and let it update. ❗

- Serpent's Hold and Moonglow (Lycaeum) have been updated. Thanks to @MrRiots for his amazing work on Serpent's Hold
- Animal sketchbook shows status
- Fixed sketch on enraged bull
- Fixed runebook not showing blessed label
- Playful dolphin is tamable
- Sketching pencil is blessed
- Turning in your completed sketch book gains you a bonding slot (looking to expand this in the future)
- Animal sketching book is auto-assigns when given to start the quest (prevents getting multiple books)
- You can start the quest via the single-click menu. Changed words to "start taming quest" to start the quest
- A players corpse will decay in 1 hour if left untouched, and will decay in 15 minutes after the corpse has been opened
- Fixed the hide/show title button in guild UI
- Added currency counts to [profile
- Combining two piles that exceed 60k will merge correctly and drop the remaining back in the original location
- Houses will decay in 14 days
- New houses with double-doors, opening one door doesn't open both
- When a house falls (IDOCs), a random 1 to 3 hour window is placed in the spot, restricting placement for any new houses
- Fixed labels on shipwrecked items
- Fixed system message when pulling up a special fish
- Wild life and jungle life should more be in line with animals you'd expect to be found in those areas
- Wild life spawners have been updated to include all the animals part of the animal bonding quest
- Removed tmap spots in Paws
- Fishing pole now has 1000 charges, and will report the wear level when you click on it (this sets up the system for other types of fishing poles to be found or made)
- Fixed issue with guards not attacking monsters in town in some situations
- Fixed issue with titles getting cut off on the paperdoll
- Fixed issue with gates and boat movement
- Merged latest code from the main ModernUO project, includes additional save time reductions and other performance enhancements

## SERVER PATCH 0.26

**September 22, 2023**

❗This patch contains client patches. Be sure to close out of the client, restart the launcher and let it update. ❗

🚩🚩Implemented the base CTF system based on the rules found in classic CTF games like in WoW's Warsong Gulch 🚩🚩

- 10v10 capture the flag (Team & Random)
- Two maps (Pirate Treasure Island & Old Trinsic)
- The game ends when one team has scored 3 captures, or after 20 minutes
- After 20 minutes, the team with the most flag captures wins
- If the teams have the same number of captures (tie) at the end of 20 minutes, the team with the most points will be declared the winner
- To score a capture, the capturing team must have their own flag at its base and bring the enemy's flag to that same spot
- If both flags are being carried, neither team can complete a capture
- The flag carrier has 120 seconds to capture the flag before they are killed and the flag drops
- When a flag is dropped, it will return to automatically return to home base in 5 seconds. Another player can pick up the flag during this time.
- When a flag is captured, flags are reset and cannot be picked up for 20 seconds
- When you're killed, everything on your body is returned to your bag, and you'll be resurrected in 10 seconds in at your team's home spawn
- The flag carrier can use the flag on themselves to drop it but won't be able to pick it up again for 5 seconds
- Individual player stats are tracked and recorded at the end of the game. Total points, total damage, flags captured, flags returned, flags stolen, flag carriers killed, players killed, number of deaths, and deaths while guarding the base

🪙  Points are accumulated as you play CTF
  - ▫️ 5 points, capturing the flag
  - ▫️ 4 points, returning the flag
  - ▫️ 4 points, killing the flag carrier
  - ▫️ 3 points, on death, guarding your base
  - ▫️ 2 points, killing someone attacking the flag carrier
  - ▫️ 1 point, on death, helping defend the flag carrier
  - ▫️ 1 point, killing a player

### Additional patch notes outside of CTF

- Detect hidden, when used in your house, will report the stats of the doors (locked or unlocked)
- Detect hidden will boost your chances of revealing someone in your house
- When you lock down an item, it will show [locked down] over it
- Removed the weight limit on locked down containers
- Friends and above can use locked down keys and keyrings
- Friends can use plants
- Cleaned up some apiculture functionality, needs more testing
- Adjustment to NPC speeds (testing)
- Fixed disarm to work when someone has a 2h weapon or shield
- Hires cannot be paragons :LUL:
- Built daily rare system, including achievements, player stat tracking. System currently disabled.
- Runebooks have arrows to allow you to adjust rune entry positions
- The default rune in your book will be highlighted

## SERVER PATCH 0.27

**October 8, 2023**

❗This patch contains client patches. Be sure to close out of the client, restart the launcher and let it update. ❗

### 🪐 🌌 Codex Rifts 🌌 🪐

In the decades following the Codex War, scholars studied the magical artifacts and lore recovered from the fallen forces. They discovered strange otherworldly creatures, dubbed "rift spawns", that had the ability to tear openings between realms and times.

When rift spawn are defeated, there is a small chance a rift gate will form at the site of its demise. These rift gates shimmer with flowed magic and are a window back in time to Britannia during the early dark days of the Codex War.

Traveling through these "codex rifts", players find themselves embroiled in the raging battles of the past. Survivors from that era see the players as allies sent from the future to help turn the tides of war.

Many adventurers have tempted fate and entered a rift gate, hoping to change the course of history by intervening in events before the Codex's destruction. None are known to have succeeded. The currents of time are not so easily altered.
- Rift spawn have a random chance to spawn anywhere in the world. Mobs with higher fame have a higher chance to be spawned as rift spawn
- When a rift spawn is killed, it has a 1% - 50% chance to spawn a rift gate, based on its fame level
- When a gate spawns, only players who were within 16 tiles of the killed rift spawn may enter regardless if they did any damage or not

#### 🌌 Codex Rift Instance

  ▫️ Felucca rules apply

  ▫️ A town region exists in the New Magincia rift

  ▫️ When you enter, you will be ejected in 60 minutes regardless of progress

  ▫️ There will be multiple exit gates throughout the instance similar to dungeons

  ▫️ Within the instance, there will always be 3 out of 8 rift champs active

  ▫️ When a rift master is defeated, there's a chance for a monster statue to drop in your bag

  ▫️ When a rift master is defeated, there is a 5 minute delay before another rift champ is started

### 🚩Capture the Flag🚩

- CTF is now on an automated schedule. For testing purposes, it will kick off a game 10 minutes after the last game completed
- During the signup period, type [ctf to join a team
- Signup period for a game is 5 minutes
- A game won't start if either team has 0 players
- You cannot use the stealing skill in a CTF match
- When carrying the flag, you cannot hide
- When you come back to life, your death robe is deleted
- When a flag is captured, there is a delay before it can be grabbed. This give teams a little time to reset.

### Additional patch notes outside of Codex Rifts & CTF

- Removed additional blocks on locked down keys and keyrings
- Fixed issue with cloth and damage absorption
- Reduced the weight on a single coin from 0.02 stones to 0.01
- Paragons have been removed for the Codex Rift system above
- After you complete a pirate map instance, the time you're removed is reduced from 10min to 5min
- Casting field spells on bridges should be successful

## SERVER PATCH 0.28

**October 30, 2023**

This is largely a maintenance patch 🥱, pulling in changes from the main ModernUO codebase that contains backend server optimizations. A few additional changes are included outside of that.

- Over 45 changes and optimizations from the main ModernUO code branch
- Field spells should cast on bridges and other platforms
- Adjustments to spawn range in the Codex Rifts and other background checks
- Bandage timers have been adjusted
- Increased hits on EV and Blade Spirits
- Adjusted buy and sell rates on various NPCs
- Hirables no longer drop their backpack
- Mana vampire will not drain more than the target has currently and will not put the caster over his maximum mana

## SERVER PATCH 0.29

**November 8, 2023**

- Fixed items (regs, pots, etc) being consumed when playing CTF
- Removed the stamina loss mechanic when running 🏃‍♂️
- Upon a successful stun, casting is disrupted 👊
- You cannot get on a mount that was in combat recently 🏇
- Reds can only use the chaos shrine to resurrect
- Removed guard region in Bucs Den Inn

🌌 Fixed Codex Rift timer gump

🌌 Fixed small issue with player tracking in the Codex Rift instance

🌌 Only allow one account in the Codex Rift instance

- Adjusted EV cast time to be lower ⏱️
- Blade Spirits and Energy Vortex summons are now effected by your Spirit Speak skill
- BS and EV summon times are not effected by Spirit Speak (unlike the other summons that give you a longer summon time)
- BS and EV will now attack the caster, unless they caster is considered a spirit summoner (SS is over 50 and higher than magery) then they will ignore you
- BS and EV have a base 10% chance to poison when they hit you. This scales up with spirit speak, maxing at a 40% chance at GM
- BS and EV that are summoned when you have GM spirit speak can be controlled via commands (ie: all follow, all attack)
- Summoned creatures that are controlled by a spirit summoner will have a different hue

## SERVER PATCH 0.30

**November 11, 2023**

This patch includes a very small and minor client patch. Please restart the launcher to download.

- EVs and BS no longer can be controlled or enhanced by spirit speak (revert from previous patch), however they still won't attack you if you're a spirit summoner
- Changed the base dark gray system font hue to a brighter hue
- Fixed issue with achievements and other customizations not saving correctly

🗺️ Added Moonglow, Trinsic, Serpent's Hold, Skara Brae, and Paws as starting towns

🗺️ Moved Dawn (Event Center) from Trammel to Felucca

- Added additional checks in Dawn to prevent harmful actions (spells, corpse looting, etc.)
- Changed the hue on spirit summons (on the fence with it)
- Removed horse stamina loss

🏴‍☠️Pirate cannons won't shoot the dead

🏴‍☠️You cannot open another pirate map within a pirate map instance

🏴‍☠️If a pirate map instance is abandoned (player count hits 0), the instance will reset in 15 seconds, instead of 5 minutes if you complete or fail

🥷If you use stealth and are over 80 and have 100 hiding, it will hide you and allow you to start moving. All hiding and stealth checks apply

🥷If you have over 80 stealth, you can enable auto-stealth, which will re-stealth you if you exceed your max steps outside the 10 second delay window

🥷The auto-stealth option can be enabled/disabled via single-click on your character

🥷A system message will tell you how many stealth steps you have left

🥷Added button to disguise kit to move disguise before 2 hour timer expires

### 🚩 Capture the Flag🚩

- Fixed issue with potions being consumed in CTF
- Updated the CTF scoreboard
- While signed up for CTF, you will get a message letting you know how much time is left before the game starts
- Reduced wait time between CTF games to 5 minutes (from 10 minutes)
- You cannot hide with the CTF flag in your pack (you can still hide without the flag)
- Fixed issue with CTF flag sometimes insta-returning when dropped by a player
- Prevent boats from being placed in the CTF arena
- If you kill yourself in CTF, you don't receive any points
- Summoning spells are now blocked in CTF

## SERVER PATCH 0.31

**December 28, 2023**

❗This patch contains client patches. Be sure to close out of the client, restart the launcher and let it update. ❗

This patch brings the core server software up to the latest development changes, which include tons of optimization to save times and general performance. It moves the server to the latest version of .NET 8. .NET 8 comes with thousands of improvements across the stack.

Also, this patch includes some changes to how murdering is handled on New Dawn.

- Block boats from being placed in certain areas (pirate map, for example)
- Fixed issue with reg consumption
- Fixed the Dawn achievement now that it's in Felucca
- Block opening a pirate map instance in CTF and the Codex Rift
- Removed fire ants from the Codex Rift spawn

🥷Egg bombs can be made by a cook with 90+ skill. These can be used to hide in combat and has a 25 second cooldown

- Account dungeon restrictions will apply to the Codex Rift
- Change bonding delay from 7 days to  1 day

🚩Fixed hues not applying correctly in CTF

🚩Actually block summons in CTF :NotLikeThis:

### 🔪 Murder Changes 😵

- If you kill yourself, you cannot report anyone for murder, even if they caused 99% of the damage
- If you die in a dungeon with 5+ murders, all your accounts (linked by IP and Discord ID) will be barred from that specific dungeon for 15 minutes.
- If you die in another dungeon, any existing dungeon-specific IP restrictions will reset to 15 minutes.
- Long-term murders will become permanent; once you reach 5 long-term murders, you'll be permanently marked as a murderer.

  ▫️As long as you have between 5 and 10 long-term kills, you can purchase a forged pardon from a corrupt judge at the Yew courthouse.

  ▫️Forged pardons will increase in cost each time you purchase one and will be limited to 3 per character.

  ▫️Upon use of a forged pardon to the judge, your short and long term kills will be set to zero and you will no longer be a murderer (but deep down, we all know you really are, you filthy animal)
- The decay time for short-term murders will be increased to 48 logged-in hours.

  ▫️Short-term murders between 1-4 will decay after 24 logged-in hours. When you reach 5 or more, the decay rate extends to 48 hours.

  ▫️Stat loss for 5+ short-term kills will be raised from 5%-15% to 20%-40%.

  ▫️Example: 25 short term kills, you would incur the max 40% stat/skill loss penalty.
- Updated the "I must consider my sins" gump (WIP, not complete)

### ✍️ Discord Registration

- Added the [discord command to support the registration process
- All accounts must be registered to a Discord account within 1 day of account creation
- After the 1 day grace period, the character will be transported to jail and won't be able to exit until they register
- You can only associate 3 accounts with your discord ID
- Upon registration, you will be promoted to the verified role in Discord which allows you to post images, embeds, etc
- The default (at)everyone role will be limited to basic actions to counter spamming, trolling, etc
- Eventually, you will need to have your phone number registered to you Discord account to connect to here (and thus, to New Dawn)

## SERVER PATCH 0.32

**January 1, 2024**

❗This patch contains a launcher update and client patches. Be sure to close out of the launcher and client, restart the launcher and let it update.❗

Every so often, a patch is required that isn't very exciting. This is one of those. This patch includes an update to the game client and assistant along with backend services that help support integration to Discord when the server is running in production.

### 💻 Client & Assistant 🖱️

- A few style changes to the client UI, along with some backend changes for security
- Removed Closest Humanoid functionality from Razor
- Removed the classicuo scripting commands
- Removed the targeting from scripting that was related to closest humanoid
- Launcher should now launch multiple accounts correctly

### 🤖 Server 🤖

- Fixed issue with spawns not detecting the correct Z-axis (this was a bug in the core server software)
- Several backend changes to allow the server to push messages to Discord (Discord registration should work now, type /register to learn more)
- Server will start block IPs from connecting that are detected as proxy, VPN or Tor exit address
- Fixed issue with achievements not saving
- Setup spawning positions and times for initial 32 server rares that spawn (currently disabled)

## SERVER PATCH 0.33

**January 20, 2024**

❗This patch contains a client patches. Be sure to close out of the launcher and client, restart the launcher and let it update.❗

- Paws has been given a slight facelift
- Rift shards are rewarded when killing a rift master. Based on damage, the top damager gets 5, and it scales down to there
- Any mob killed in a rift has a low chance to give you a rift shard
- All server rare spawns have been set but are disabled
- Coin sounds when you are awarded pirate, champ, and other types of currency
- Added mask, dragon, and runebook dyes to be used for rewards
- Added enhanced logging that can be easily indexed and searched (and some data made available via an API)
- Added a wearable hood (to be obtained as a reward)
- Added a generic wearable shroud (to be obtained as a reward)
- Added reward vendors for Champion Tokens, Harrower Shards, and Codex Shards (found in Dawn) with the initial proposed set of rewards
- Fixed regions in Yew, Paws, and Moonglow
- Added a warning message if a player tries to register using Name#1234
- If you log into a house, private or public, and you aren't a friend, you will be ejected
- Runebooks are set to be accessed by anyone when locked down (ie: in runehouses)
- Fixed issue with the multi-client PvP check
- Orc brutes are slightly less disruptive now.
- Fixed orcish bow label

### 🧵 Tailoring 🪡

- Tailors can now craft special dye, from materials farmed in dungeons.
- To gain this ability, a tailor must join the Tailoring Guild (available at 85.1)
- When they are at 100, if they give the tailoring guildmaster 10,000 gold, they will receieve a tailors dye kit.
- Each dungeon has a specific material, that when crushed down and used with the kit, creates a unique hue for that dungeon
- Each bottle of dye has one use, and any cloth item can be dyed with the bottle

## SERVER PATCH 0.34

**January 22, 2024**

❗This patch contains a client patches. Be sure to close out of the launcher and client, restart the launcher and let it update.❗

Just a small server patch addressing a few bugs, along with a map update. Thanks to @MrRiots for his amazing map design work on Vesper and the Cove Orc fort!

- You can't place houses in sand or swamp areas. This will be changed over time to allow only specific houses to be placed on sand or in swamps
- The new short and long term murder times will now apply
- You can now cast gate when you're a criminal
- The ancient drowner pirate boss will have a LOS check on his AoE
- GM spirit speak will let you see ghosts
- Fix where the ancient mummy timer threw a tantrum and crashed the party
- Pirate boss will be cleared out when a new pirate map is started
- The Vesper moongate has been restored
- Removed the forensics skill requirement on eggbombs

### 🌊 Vesper Rises 🎣

On the shores where the island city of Vesper once stood now rises a modest fishing town, rebuilt over generations by those who remembered the fallen city.

The first to return were bold explorers, venturing into the perilous sunken passageways in search of artifacts and knowledge. They found only ominous remnants of lives tragically bound to the city's watery grave.

It was their stories that called others back, descendants of those who fled Vesper's end. They returned over decades to the shores of their ancestors, building new lives atop the wreckage. Wooden piers and decks now rise where tragedy struck generations before.

The fishing town battles the frigid climate, a bittersweet revival still haunted by its past. Though new life blooms on the surface, the hallowed halls below remain undisturbed. There secrets and spirits keep vigil, leaving Vesper's full fate still known only to the sea.

### 🗻 Cove - Orc Stronghold ⛰️

Cove once found tranquil shelter in the mountain's embrace, but that peace was shattered when orcs tunneled forth from below. Cove's history as a revered haven of healing arts faded into memory.

Now Cove's mighty wall encircles orc warrens instead of archives. Etched prayers on mountain passes are all that remain of Cove's people, lamenting the sanctuary's fate. Orc banners whip atop the battlements that once protected Cove but now fortify its conquerors. Few dare approach the stronghold where orc patrols roam, erasing Cove's noble past. Only cold, pitiless stone bears witness to the fallen sanctuary's fate.

## SERVER PATCH 0.35

**January 24, 2024**

❗This patch contains a client patches. Be sure to close out of the launcher and client, restart the launcher and let it update.❗

This patch addresses some bugs with the [dupe command. and the items it was creating causing client crashes.

- [dupe should no longer cause issues with items
- Serpent Pillar to T2A won't respond to commands

## SERVER PATCH 0.36

**February 9, 2024**

❗This patch contains a client patches. Be sure to close out of the launcher and client, restart the launcher and let it update.❗

This patch includes several bug fixes and changes to the server but also changes how the client code is built and how the server communicates with the client.

### 🤖 Server 🤖

- Fixed issue with champ spawns potentially causing a crash
- Consider My Sins gump doesn't show long term decay (since it doesn't decay)
- Implemented a new mage AI (needs more testing)
- You will now see newer models for some mobs again (no more naked evil mages, Rikktor is a newer model, etc)
- Change drop rate of dye materials in dungeons from 1% to 0.5%
- You can dispel your own summons easily
- Housing blocked in Ocllo
- The guards will whack aggressive creatures

### 📜 Harrower Scroll 📜

- When you place all 6 skulls on the platform blaziers, you are now given a scroll to summon the harrower at a later time
- Before you spawn Harry, you have an option to create a temp guild region around the Harrower (1 hour). Any player not an ally or in your guild will appear orange and attackable. 🍊

### 💻 Client & Assistant 🖱️

- The client is now compiled using Native AOT, a self-contained client that has been ahead-of-time (AOT) compiled to native code. Native AOT apps have faster startup time and smaller memory footprints.
- With that, the initial attempt to add some basic client validation 🕵️
- Removed several features from Razor that already existed in ClassicUO (auto-open corpses, spell name/hues, show incoming player names, etc)
- Modified some default client profile settings

🌃 Removed the ability to change light levels without using a spell or potion in game (learn to love Night Sight again)

## SERVER PATCH 0.37

**March 8, 2024**

❗This patch contains a client patches. Be sure to close out of the launcher and client, restart the launcher and let it update.❗

### General

- Mage AI won't cast field spells (for now)
- Fixed new mage AI to not attack other mobs
- The in-game light level will change with the in-game day/night cycle
- The light level in dungeons is darker
- Update base server code with latest upstream code changes (changes to firewall and server code)

### 🏡 Housing 🏠

- Housing name policy is checked using the naming policy
- Creatures can enter houses now
- You can summon in your house
- Fixed sign direction when switching from public to private on east facing houses
- Adjusted house transfer hue
- Fixed issue with house regions remaining when dropped
- Fixed several of the east facing houses
- Removed large stone dueling pit and large sandstone patio (for now)

### 🏘️  New House Types 🏘️

Three Story Villa, Two Story Brick House, Large Patio with Courtyard, Two Story with Courtyard, Gray Keep Courtyard in back, Gray Keep Courtyard in corner, Merchant Villa

### 💻 Client & Assistant 🖱️

- Fixed issue with light levels not adjusting
- The option to hide roofs have been removed
- When you die, it will always be black and white
- More work on client/assistant validation against the server 🕵️

## SERVER PATCH 0.38

**March 10, 2024**

This is a quick server patch to address the issue with ships and houses. No client side updates needed.
- Fixed issue with ships and houses (thanks for finding these bugs 🐛)
- No more complete darkness between 12:30pm and 1:00pm (in-game time)

## SERVER PATCH 0.39

**March 13, 2024**

❗This patch contains a client patches. Be sure to close out of the launcher and client, restart the launcher and let it update.❗

Another small patch, almost not worth posting any patch notes.

- NPCs will train up to 50 skill points, based on the current skill level of that trainer
- Along with the client update, the night sight spell's effect is based on the caster's magery skill 🧙
- Changes to the server code to address the user count issue

## SERVER PATCH 0.40

**April 24, 2024**

❗This patch contains a client patches. Be sure to close out of the launcher and client, restart the launcher and let it update.❗

🌃 The night sight base scale was changed so it should be brighter when used

🌃 Added greater night sight potions (need 8 spiders silk to craft). They will last 15-25 minutes and will increase light similar to the spell at GM magery

🌃 Increased crafting on night sight potions from 1 spiders silk to 2. Night Sight potions will last 10-20 minutes and won't be as bright as greater night sight potions

- You can now only buy a house tool instead of house deeds 🏠
- Fixed [titles command
- If you spawn into a pirate map when one isn't active, you are teleported to Dawn
- Fixed issue that would set your current bonded pet number to -1
- Changed the trash barrel hue because... why not?
- Changed the Help/Stuck locations and blocked it's use if you have the CTF flag
- Added bone masks
- Tailors can craft hoods at 115 tailoring
- Fixed the existential crisis of containers forgetting how many items they can hold
- Turned off the smart AI on the mage AI
- Lich lord drops more gold
- Bucs Den now has a tailor, stable, and mage shop along with some other small changes throughout the town
- Mysterious black square on the map north of Vesper is gone!

### 🤖 Server 🤖

- Reverts to RunUO NPC speeds, fixes direction glitching, adds movement speed interpolation (core server change)
- Fixed bug that would cause lag spikes in certain situations
- Code base up to date with upstream core server code

### Bulk Order Deeds

- BOD Books are no longer blessed
- Small and Large BODs will show how many rewards points they're worth
- Small and Large BODs will show (complete) when they're complete
- Tailoring BOD rewards have been adjusted:

#### Small BODs:

- 1 point: 80 uncut cloth of random hue 1155, 1164, 1160, 1162
- 50 points: 60 uncut cloth of random hue 1173, 1163, 1158, 1157
- 100 points: 40 uncut cloth of random hue 1165, 1168, 1166, 1169
- 150 points: 20 uncut cloth of random hue 1167, 1172, 1156, 1175 or low chance of sandals - (90/10) of random hue 1161, 1151, 1154, 1150, 1167, 1172, 1156, 1175
- 200 points: 10 uncut cloth of random hue 1161, 1151, 1154, 1150 or low chance of sandals (80/20) of random hue 1161, 1151, 1154, 1150, 1167, 1172, 1156, 1175

#### Large BODs:

- 300 points: 1 of 4 random stretched hides
- 350 points: ore mask dye tier 3 [ore: dull, copper, bronze]
- 400 points: 1 of 4 random tapestry
- 450 points: bear or polar bear rug
- 500 points: 1 of 4 random tailoring shelves
- 550 points: clothing bless deed or low chance of sandals (80/20) of random hue 1109, 1208, 2124, 2130, 1508, 1157, 1254
- 600 points: ore mask dye tier 2 or special mask dye tier 2 (80/20) [ore: agapite, verite]
- 650 points: tailoring powerscroll +5
- 700 points: ore mask dye tier 1 or special mask dye tier 1 (80/20) [ore: shadow iron, gold, valorite]

## SERVER PATCH 0.41

**May 1, 2024**

This is a quick server patch to address a few small issues from the previous patch and make a small adjustment to poisoning

- Fixed logic on the pirate region to not eject NPCs
- Fixed issue with new Discord registration attempts not sending you a message on Discord
- When you attempt to cast poison on a mob, it will now consider your poison skill. At GM poisoning, you have a 50% chance to apply poison even if they're immune. It scales down from 50% (ie: at 55 poisoning, you have a 27.5% chance) (still testing the numbers)

## SERVER PATCH 0.42

**February 16, 2025**

This patch largely focuses on increasing account security and bringing New Dawn's core server codebase up to the latest version. With this patch comes an updated version of the launcher and game files.

In addition, this patch helps in the preparation to move towards an Open Beta and/or Early Access model.

### 🪪Login Process🪪

To help secure New Dawn against DDoS attacks, account stealing, account sharing, excessive accounts, and overall general account security, the login process has been modified.

While the launcher is still required, it will direct you to https://login.uonewdawn.com/ where you'll need to login using your Discord credentials. Upon successful login, authenticate the launcher, click 'Enter Britannia', and select your account to log in.

You can learn more about it here: https://login.uonewdawn.com/why

Note: This process is currently only supported on Windows. Linux support is planned for a future update.

### 📜Fixes/Changes📜

- Fixed Ocllo sewer/dungeon regions and spawners (added additional entrance in graveyard)
- You can't open a corpse that isn't yours in the event center
- Chance of a rift shard dropping can be changed live in game
- Removed New Player Tickets
- Fixed context menu toggle not working (can access it via [profile)
- When farming cotton or flak it has a chance to trigger the resource captcha check
- Farmers have some random banter
- Rewrote the resource captcha system to be more robust
- Disabled achievements for now until the system can be more refined
- Refactored the daily rare system & enabled it (📝Many more rare locations to be added in the future)
- If you somehow get into a dungeon during your ban period you'll be ejected to the event center
- Event Center (Dawn) doesn't allow skill gains and nearly all skills are blocked (📝This area isn't meant to be a safe spot to craft or skill up)
- CTF max player count is capped at 10 and you can only longer gain skills in the CTA arenas
- Idle animals and monsters now only have a 25% chance to make a noise (ie: dog barking, cat meowing, etc)
- Bumped up the skill gain rate on tactics, swords, mace, fencing, and wrestling slightly
- Removed almost 30k items from other facets in the game that aren't accessible

### 🤖Server🤖

- Base code merged up to the latest upstream
- Increased server response speed
- Enhanced memory management
- Fixed numerous bugs in the core server software
- Disabled test mode functionality
- Archived old accounts and IPs so new accounts can be created by those who previously had accounts

### 🗺️Map🗺️

- Created docks closer to Ocllo (east side, north of Moongate)
- Fixed missing wall in Trinsic
- Removed hidden blocker in Trinsic healer building
- New Minoc now has a tavern and inn
- Several other tweaks and changes no one will most likely notice
- Yew (in the Abbey) has been slightly enhanced to not feel as empty and unfinished

### ⚔️Conquest of the Virtues⚔️

Conquest of the Virtues has been enabled (early version of the system). You can read about the overall game here: ⁠Conquest of the Virtues

- Ruins of Britain (east of Britain)
- Ruins of Trinsic (northwest of Trinsic)
- Ruins of the Shadowlords (west of Yew)
- Ruins of Moonglow (where the original Moonglow used to exist)

### 🎶Music🎶

📝While my focus remains core features and security, music and ambience still help bring world to life so I hope to continue to sprinkle that stuff in where I can

- When exploring the world (ie: outside of towns, dungeons, etc) it will randomly play one of the eight available music tracks for exploring
- When you enter a tavern or inn, depending on the location, you will get a different type of ambience. This change of music (or using [where to confirm) lets you know you can log out safely
- Vesper has new music and ambience
- Dagger Island has new music and ambience

## SERVER PATCH 0.43

**March 8, 2025**

This patch introduces a new system for discovering artifacts throughout the ruins found across the world of New Dawn.

### 🏺Archaeology/Artifact System🏺

#### 🗺️Clue Hunting

- Map fragments can be found via fishing 🎣
- Journal pages, book pages type clue will randomly drop on mobs similar to how treasure maps drop
- Decipher clues with 70+ Cartography (maps) or 70+ Inscription (texts). Higher skill of course, you have better odds

#### 🛠️Tools & Techniques

Equip your archaeologist's shovel, pick Hammer, and Brush to progress through three excavation stages:

1️⃣ Untouched (Shovel, 80+ Mining)

2️⃣ Excavated (Pick Hammer, 90+ Mining)

3️⃣ Cleared (Brush, 80+ Item ID)

A bag of archaeologist's tools can be purchased at any provisioner.

#### Discovery Odds

Artifact chances scale with Mining skill, Cartography/Item ID bonuses, and site quality:

- Common: 40-50%
- Uncommon: 10-20%
- Rare: 1-5%
- Ultra-rare: 0.1-0.5%

📝 Each dig site mixes unique artifacts with common (low value) items archaeologists often find in old ruined towns. Clues are consumed after use.

### 🏴‍☠️ Smugglers' Market Update 🏴‍☠️

Anticipating resource shortages across New Dawn, shady merchants have emerged from the shadows. These "seafaring entrepreneurs" have set up a few trading posts throughout the world. They only conduct business at night, but will sell you whatever you need—at a premium.

### 📜General Fixes/Changes📜

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

### 🤖Server🤖

In an effort to keep the core server code aligned with the downstream project, the code server code has been merged to the latest version. Most of them (as usual) focus on performance gains, and backend code changes that you won't really notice directly but help long-term.

- Base code merged up to the latest upstream
- Server upgraded from dotnet8 to dotnet9 (numerous performance improvements, including loop optimizations, inlining, etc)

## SERVER PATCH 0.44

**March 25, 2025**

### 🪴Gardening/Plants🧑‍🌾

Animals (such as bears) that eat things that have seeds in their diet have a chance to drop seeds. As such, animals that spend time in dirt (such as boars) have a chance to drop fertile dirt.

### 📜General Fixes/Changes📜

- Marble Island is blocked (for now) from housing
- Removed the Old Trinsic area from CTF so it can be used for future events
- Developed the base seasonal event code for seasonal event automation
- Houses can no longer be placed within 5 tiles of another house. The 1 tile border of no blocking items still applies. With 1 house per account, the goal here is to not have every inch of open land covered with houses, and remove single chokepoints between houses
- Fixed the cost and stock of mandrake root on mage vendors
- Summoned or controls pets no longer heal themselves
- Dragons (and other mobs with abilities) will actually use them (ie: fire breath)
- Removed broadcast and receiver crystals from vendors
- Fixed crashes due to disabled achievement system
- Changed the buttons on the moongate gump to easier to read for the old people
- Fixed issue with the criminal buff causing the client to have an issue

### 🗺️Map🗺️

- Several areas, randomly sized or located throughout the world, have had all their trees cleared and land leveled to support additional housing
- A bunch of small tweaks no one will notice
- The King's Men Theater has reopened thanks to support from the First Academy of Music

## SERVER PATCH 0.45

**March 29, 2025**

❗This patch contains a client patches. Be sure to close out of the launcher and client, restart the launcher and let it update.❗

This patch addresses several issues found during early beta testing. They also clear up how the young program works. Sorry for the long and unsorted list.

### 📜General Fixes/Changes📜

🌓Improved day-night lighting transitions with enhanced moonlight effects on the level of brightness

🌓Adjusted the day night cycles so its a bright brighter between in-game hours of 8am and 8pm

- Fixed some tracking logic issues that were letting prey slip away
- Escorts now have 40 possible destinations, including taverns, towns, and graveyards
- Guildmasters have unanimously raised registration fees to 5000 gold - they claim inflation is affecting them
- Guild membership now costs 5000 gold, but offers 10% discount on Guild vendor purchases
🌱New cotton and flax fields are sprouting across the world
- Weapons now face the reality of wear and tear (5% chance per use), while acid creatures are particularly harsh on equipment
- Fixed issue with not being able to use item ID on a full container at GM
- Young players can't use the public moongate
- Unguilded players can now enter inactive conquest regions
- Increased gain rates on snooping, meditation, lumberjacking
- Fixed the night sight potions being unusable under certain conditions
- Carpenters sell small wooden boxes and crates
- Fixed price vendors buy back bloodmoss and pearl
🪵Trees now yield more logs total but fewer per harvest
- Fixed label on the different log types
- You can drop a stack of spell scrolls on a spellbook and it will consume 1 scroll (instead of having to split 1 off first)
- Rewrote the code that enforces a single account in dungeons
- Built foundational system for tracking player stats
- The parrying skill will correctly have a chance to gain when sparring with another player
💀Skeletons now drop bones (revolutionary, I know)
🎨Increased materials needed for dungeon dyes (from 10 to 250)
- Alchemists are better stocked with night sight potions
👂Brigands are now a bit more attached to their ears
- Attempting to rejoin the young program will consider how many times you've been in it previously across all characters on the account
- Young players can't enter a codex rift gate
🏴‍☠️Fixed bug preventing you from buying from the pirate smuggler
- Escort corpses now remain as evidence of your failure to protect them
- Sparring no longer mysteriously improves your lumberjacking skills

### 📜Young status will be removed under any of these conditions:

- Your account reaches 120 hours of total playtime ⏳
- Your character's combined skills exceed 450 points 📊
- You venture beyond Ocllo's protected boundaries (town, island, or dungeon/sewers) 🏃‍♂️
- You gain a murder count ⚔️
- You use the [young command to voluntarily exit the program 🚪
- Any crafting skill exceeds 80:

🧵 Tailoring

🔨 Blacksmithy

🪚 Carpentry

🍳 Cooking

🧪 Alchemy

📜 Inscription

### 🐑Sheep Farming🐑

To counter "sheep farms", a few more changes have been made:

- Outdoor sheep now produce wool every 2 hours instead of 4
- Stacking sheep inside houses like cordwood will stop wool production
- Indoor wool production now depends on hunger - treat your sheep well:

Well-fed (18-20): 1.5 hours

Satisfied (10+): 2 hours

Peckish (5+): 6 hours

Hungry (2): 8 hours

Starving: 12 hours

### 🖥️Client🖥️

- Updated client files to include vendor locations in Vesper and Dawn (thanks flyer!)
- Removed tmap spots found in Paws
- Adjusted text position on login screen
- CTRL-SHIFT to locate immovable objects wasn't quite what I had in mind for rare hunting 👀
- Removed unused skills from reset skill button

### 🗺️Map🗺️

- Moonglow's interior spaces now feel more lived-in
- Yew Courthouse/Jail remains a housing-free zone

## SERVER PATCH 0.46

**March 30, 2025**

This patch addresses some bugs introduced in the previous patch with a few other changes based on recent feedback.

### 📜General Fixes/Changes📜

- Refactored some of the logic around checking for multi-client PvP
- You can actually enter dungeons again
- Fixed issue causing you to disconnect when entering an inactive Conquest ruined region
- Disabled the daily rare system. Thank you for your enthusiastic & extensive testing
- The outdoor area in the mountains between Covetous is now considered a dungeon region
- You can disable the moongate prompt using [profile
- Fishing poles nearly broken will have tell you on single-click
- Purchased pets will auto-follow you by default
- New NPC vendors are now mostly vulnerable (with rare exceptions)
- Removed fishing aquarium items for now
- Lowered the chance to pull up rare fish significantly (shore line, deep sea, and dungeon fish)
- Clicking the profile scroll in your paperdoll now opens the same menu as [profile
- Added a "Public Profile" button to your main profile for easy editing/viewing
- If multiple skills are at 100, setting one to "UP" will prioritize it for paperdoll display

### 🛡️ Escort System Updates 🛡️

- Escort rewards now scale with distance from the origin (replacing random 500–1000 payouts).
- "Seekers of Adventure" must now be escorted to a specific dungeon level.
- Successful escorts grant bonuses based on the dungeon level reached.
- Escorts now have a small chance to:

Pay only half the reward

Pay nothing

Rarely grant an artifact clue instead

### 💻Client💻

- Linux support: The client (with Razor) now runs natively on Linux (no Wine required). 🐧Special thanks to @tourist for extensive testing!🐧
- Enabled client verification on the server side

## SERVER PATCH 0.47

**March 31, 2025**

This hotfix patch addresses the server locking up from escort changes and a few other tweaks

### 📜General Fixes/Changes📜

- Moongates now properly maintain their space (no stacking)
- Fixed the troublesome escort system causing server instability
- Teleport magic restored to 12 tiles
- Escort rewards now better scale with journey distance

## SERVER PATCH 0.48

**April 7, 2025**

❗This patch contains a client and launcher patches. Be sure to close out of the launcher and client, restart the launcher and let it update.❗

This patch addresses a number of bugs and feedback from beta testers. It also includes an update to the New Dawn login site and game launcher.

### 📜 General Fixes/Changes 📜

- Scissors will no longer work on newbied or blessed cloth items
- When you carve a body, the heart (with a name) is also able to be taken
- Stealthing while on a mount will reveal you
- Birds, snakes, rabbits, and rats no longer block you if you walk into them with less than max stamina
- While it was considered harmful using provo and discord on someone's pet only, now it's considered a harmful act on all targets (ie: if they're blue, you become a criminal as you would if you casted lightning on a blue)
- Oil cloth can be stacked
- Boards are properly labeled based on the type
- Lowered the chances of getting oak and ash logs (base code to make logs types tree specific being worked on)
- You have 100% success chance to dispel your own summon
- Champs return to the platform when they're 30 tiles away (instead of 60)
- Lowered the skill requirement to obtain an taming quest book to 80 animal taming and lore instead of 100
- Provisioner won't buy kindling
- Leather armor vender will buy bone armor
- Decreased the max darkness in dungeons slightly
- Because NPCs need line of sight to call guards, increased range NPCs can call guards from 8 to 12 tiles
- As long as animal can be seen, and is in line of sight, you can tame them (dropped pathing requirement)
- Adjusted the rare statue drop off rift masters to have the proper label and a random "rift" hue
- Break combat engagement when targets are hidden
- You can lock down a container where the item count exceeds your total lockdowns for the house
- Fixed issue with NPC vendor not giving you a response when you asked for a bulk info update
- Guild wars proposals and war acceptance are sent to Discord
- Captchas now have a gradually increasing chance to appear rather than fixed timers
- The loot packs dropped by all monsters have been adjusted slightly along with several adjustments to overall loot
- Lower casting time on summon spells
- Lowered the chance your armor has to take damage when hit (it was a 25% chance, and 80%+ it would be your chest plate)
- Adjusted hit location probabilities on armor to feel more realistic - Chest (40%), Arms (20%), Legs (15%), Hands/Head (10% each), Neck (5%) (still balancing)
- Big fish now display the date caught

### 💪 Stamina Loss 💪

As a refresher, instead of dex penalty when wearing armor, you instead lose stamina when taking damage, based on the armor you're wearing.
- The formula used to calc how much stamina you lose based on the type of armor you're wearing has been adjusted

### 👻 Spirit Summoner 👻

- All 8th circle summons have had their base stats/skills increased significantly, before the bonus is applied based on your spirit speak skill. This should make them much stronger, but the balancing act continues
- The spirit summons follow speed has been significantly increased
- The distance in which they stop following you has been increased
- Fixed issue where some mobs could immediately dispel your spirit summon

### 🗺️ Map 🗺️

- Fixed the Paws Shelter and Ocllo dungeon region bounds
- Moonglow has wild life

### 💻 Client & Launcher 💻

- Added shops in Paws & New Minoc and refined shop icons & marker placements across the map (thanks for your efforts updating this file @flyer )
- Updated the login website & game launcher to help make the login process a bit more smooth

## SERVER PATCH 0.49

**April 14, 2025**

❗This patch contains a client patches. Be sure to close out of the launcher and client, restart the launcher and let it update.❗

This update addresses both reported bugs and community suggestions, including a persistent issue with gumps causing client instability.

### 📜 General Fixes & Changes 📜

#### Combat & Skills

- Town guards no longer have detect hidden abilities
- Fixed a critical issue where provocation would succeed but break at maximum range
- Mining range increased to 3 tiles for better accessibility
- Taming quest book now requires 80 skill instead of 100, making it more accessible
- Mounted crafting has been disabled
- Mounted lumberjacking has been disabled

#### Storage & Weight Updates

- Boat cargo holds now support up to 6400 weight
- Pack horses and llamas can now carry up to 3200 weight
- Dungeon dye materials are now stackable

#### Fishing Improvements

- New catch-and-release toggle added to fishing poles (sorry, all poles get deleted)
- Slightly increased minimum fishing skill requirement for artifact clues
- Reduced frequency of artifact clues from fishing

#### Quality of Life

- Added [e command for audible emote system
- Pitchers can now be filled from water sources (barrels, troughs, etc.)
- Empty carved corpses will now disappear
- Smuggling pirate restricted to appropriate range
- Smuggling pirate responds to "vendor buy" or single-click buy context menu

#### Visual Updates

- Pottery shards replaced with visually accurate broken pottery
- Player corpses turn gray when transformed to bones (no longer flags as criminal)
- Guild, ally, and enemy corpses now display correct notoriety colors
- Crafted instruments will display maker's mark

### 🖥️ Client Improvements 🖥️

#### Performance & Stability

- Implemented changes to reduce crashes during gump-related macroing/scripting
- Removed delay when selecting the server
- SHIFT-CTRL with All Names selected will properly display corpses
- Improved account dropdown clickability

#### Visual Fixes

- Corrected fire pit lighting effects
- Fixed various object collision issues
- Corrected multiple incorrect static map item names

## SERVER PATCH 0.50

**April 25, 2025**

Welcome to our milestone 50th update! This patch continues to address reported bugs and implements some suggested features. I couldn't have hit this milestone without all of you helping me test, thank you so much.

### 📜General Fixes/Changes📜

- Proper message when you collect an artifact
- Fixed labels on commodity deeds
- Fixed system message when fishing up messages in a bottle
- Pirate smuggler has a single-click context menu
- Fixed system message when fishing
- NPC vendors will buy scrolls but at a rate lower than what it costs to inscribe the scroll

☠️Poisoned weapons will give you some description of the type and amount of poison charges left

☠️Increased the chance of poisoning skill gains

- Potential fix for farmable crops not changing for some people in the client
- You can remove animals from your house with remove thyself but you still can't ban animals
- The polymorph spell now works
- If you cast heal or greater heal on a spirit summon and you have spirit speak active, you will gain a bonus to the amount healed based on your spirit speak skill
- 8th circle spirit summoned creatures have meditation
- Adjusted some of the spirit summon hues
- Healers spawn with a specific hue range
- NPC vendors will now spawn randomly with town specific hues or common hues found in all towns. A few towns have more rare hues found on specific vendors

❄️NPC vendors in snow covered regions spawn with winter appropriate clothing and footwear

### 🤺Combat⚔️

- Made adjustments to how much damage is absorbed on all creatures before total damage is applied. You should see them take more damage, especially when using provo. You should also able to do more damage as a dexxer
- Stamina loss based on your armor now only applies when you take melee damage

## SERVER PATCH 0.51

**(POST BETA) June 7, 2025**

Even though the beta has ended, these changes were made to continue to address reported bugs and implements some suggested features. They will be available next time the server is running.

### 📜General Fixes/Changes📜

- Spirit speak now has a 10 second delay between use
- Item ID now has a 5 second delay between use
- The bankers in Bucs will do business with criminals
- Treasure maps can never be level 0
- Clicking on the tillerman will show your boat status
- You can no longer trade when hidden
- Keyring shows correctly in Tinker NPC
- Context menu on player's shows Trade option
- You can meditate with a spellbook, runebook, or any equipable light (candle, torch, etc)
- Added Eject option context menu when in your house
- Wands have been added to the loot pool of several magic based mobs
- Fixed issue with blocked spell casting in conquest regions
- All characters on all your accounts are considered co-owners on any house

### 🏹Archery🎯

To help make archers more viable, the shooting delay was reduced to 500ms several patches ago. However, they remained underpowered due to lack of a special ability. Archers now have the snare ability.

- Requires at least 80 anatomy and 80 archery
- Double-click your equipped bow to toggle snare
- 25% chance to ensnare at 100 anatomy and 100 archery
- Each attempt (failed or successful) uses 15 stamina when active

After a successful snare:

- The snared target cannot move (but can still attack and cast spells) for 3 seconds
- The snared target will have any spell they were casting disrupted
- The archer cannot snare another target for 20 seconds

### 🏰The Trinsic Terathan Outpost🕷️

When the Avatar destroyed the Codex of Ultimate Wisdom, the magical backlash created spatial anomalies throughout Britannia. One significant manifestation was the appearance of a Terathan fortress near Trinsic.

This structure is believed to be a duplicate of the legendary Terathan Keep from beyond the serpent pillars. When the Codex was destroyed, its vast knowledge took physical form in areas where magical energies were strongest.

The Terathans were immediately drawn to this anomaly and claimed it as their own. The fortress appeared during the final days of the Codex War when Trinsic's defenses were focused on the gargoyle threat.

Today, the Trinsic Terathan Outpost remains one of the region's greatest dangers.

## LOGIN SERVICE PATCH 1.2

**June 8, 2025**

### Beta Participant Name Reservations

This patch introduces a new functionality for beta program participants. Eligible users will now have the ability to reserve up to six (6) character names.

This option can be accessed upon logging in to your account at https://login.uonewdawn.com/ ✨

## SERVER PATCH 1.0

**January 23, 2026**

Those who were in the final round of testing already experienced the majority of the changes.

### 📜General Fixes/Changes📜

- If you reserved a name, they've been tied to your specific accounts. If you can't pick the name you reserved, let us know
- Lowered dungeon tailoring material drop rates
- Lowered rift shard drop chance
- Lowered artifact drop chance
- Lowered rare animal spawn chance
- Added some randomness the time delay between new rifts opening up
- Cleaned up name change gump
- If in a party, you must be in range (30 tiles) to get any fame or karma
- Fixed issue with empty names with forensic eval
- If your house placement fails, you'll see which tile(s) were the cause
- If your pet is set to follow you, it will ignore aggro and attacks and continue to follow
- To balance out the Spirit Summoner build, how strong your summoned pets are (the scaler that gets applied to all stats/skills/armor) now is based on your Animal Lore skill instead of Spirit Speak. Spirit Speak is still used when calculating dispel chances, the duration of your summoned creatures, and when active, any bonus added to healing of your summons
- Adjusted world saves from 20 minutes to 5 minutes
- Adjusted the global weather patterns to align a bit more with the world

### 🧌Spawners🧌

- Converted all the spawners from the ancient XML Spawners code to the native spawning system. Why? XML Spawner is old, poorly coded, and never really fully supported ModernUO and wasn't using any of the advanced features of XML Spawner. This should have no impact on where or how things spawn, all the benefits are in performance and save times.

### 🤖AI and Movement🤖

- Major changes with the AI speed and movement of monsters, NPCs, followers. They should look more smooth when they move, however some of their speeds may still need to be adjusted so your feedback is welcome.

### 📊Player Event Tracking📊

- Added a new event tracking system that captures player activity and eventually will feel into the Portal leaderboards. Currently tracking CTF, Champ Spawns, Pirate Events, Harry, Codex Rifts, Conquests, Smuggler Runs, Rares, Artifacts, Auctions, PvP kills, monster kills, deaths, and logins. More events can be added over time as needed.
- Currently the data is being collected only. Leaderboard generation will be available via the Portal in the future.

### 🛶Boat Control Changes🛶

- When you try to command a boat, it will let the person with the key take control regardless of where on the boat
- If no one on the boat has a key, then check who's the closest to the tillerman, and if the closest person is the one trying to command the boat, they can

### 💻Server & Infrastructure💻

- Upgraded the base OS the server runs on to the latest version
- Server code base updated to upstream with tons of bug fixes and optimizations
- Updated to dotnet 10 for better performance

### 🖥️Client (ClassicUO & Razor)🖥️

- Updated ClassicUO to the latest version with all the changes specific to New Dawn.
- Changed how rain and snow appear in the game
- Item hue now reflects on the type of light it omits
- Added rain sound effects
- Footsteps sounds are now based on the type of ground being stepped on. You can disable this in settings
- Removed alternative light setting so you guys can really hate me

### ⭐Reward System⭐

To better support rewards for various events, a system has been built to give out reward bags when you login based on certain criteria.

📝Note: Rewards are given per person (based on your Discord account), not per account or per character. This makes the items that much more unique and rare.

#### 🎇Aurora Beta Reward Bag🎇

If your account was created prior to 5/28/2025, upon login, you will receive an Aurora inspired gift bag as a thank you for helping beta test.

#### 🎇Charter Member Bag🎇

If your account is created within the first week of launch, upon login, you will receive a Charter Member gift bag inspired by the original Ultima Online Charter Edition (that still sits on the shelf behind me)

#### 🎇Vanguard Reward Bag🎇

If you were an early alpha tester (marked by the role in Discord), an additional thank you for all those hours back in the early days fine-tuning each skill and spell.

#### 🎇Welcome Reward Bag🎇

Any new account will get a welcome bag to help start their journey (some gold, bandages, reagents, etc)

### 💫Achievements💫

The Achievement System was rewritten and now tracks player progress across various in-game activities and rewards players with points, titles, and items for completing milestones. Type [ach to see your progress!
- Point System: Each completed achievement awards points that contribute to your total score
- Leaderboards: Global rankings based on total points and completion count
- Categories: The system tracks progress across multiple activity types such as Discovery, Hunting, Crafting

#### Rewards

- When you complete an achievement, you receive:
  - Points: Added to your total achievement score
  - Title: Some achievements grant unique titles for your character
  - Items: Certain achievements award physical items (placed in backpack or bank if overloaded)

I want to thank everyone who helped get the server to where it is today. Your testing, your feedback, your discussions -- all helped shape what this project is today