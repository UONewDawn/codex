# SERVER PATCH 0.48

**April 7, 2025**

❗This patch contains a client and launcher patches. Be sure to close out of the launcher and client, restart the launcher and let it update.❗

This patch addresses a number of bugs and feedback from beta testers. It also includes an update to the New Dawn login site and game launcher.

## 📜 General Fixes/Changes 📜

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

## 💪 Stamina Loss 💪

As a refresher, instead of dex penalty when wearing armor, you instead lose stamina when taking damage, based on the armor you're wearing.
- The formula used to calc how much stamina you lose based on the type of armor you're wearing has been adjusted

## 👻 Spirit Summoner 👻

- All 8th circle summons have had their base stats/skills increased significantly, before the bonus is applied based on your spirit speak skill. This should make them much stronger, but the balancing act continues
- The spirit summons follow speed has been significantly increased
- The distance in which they stop following you has been increased
- Fixed issue where some mobs could immediately dispel your spirit summon

## 🗺️ Map 🗺️

- Fixed the Paws Shelter and Ocllo dungeon region bounds
- Moonglow has wild life

## 💻 Client & Launcher 💻

- Added shops in Paws & New Minoc and refined shop icons & marker placements across the map (thanks for your efforts updating this file @flyer )
- Updated the login website & game launcher to help make the login process a bit more smooth
