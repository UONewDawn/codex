# SERVER PATCH 1.17

## September 24th, 2026

This patch contains several new systems, including major changes to champions, and the introduction of storage racks, arcane lanterns, and more!

## 🛠️ Bug Fixes & Enhancements

- Adjusted the max active rifts from 3 to 4, and the delay between a new spawn from 5-10 min to 2-4 minutes
- Fixed the hue on the dread spider statue, fixed the graphic on the ghoul statue
- Bonded pets can't drop statues
- Fixed the regular spider statue
- Fixed the issue with the wrong barnacled chest dropping
- Reapers and Bog Things have a chance to drop a woodwarden's axe
- White Wrym's are easier to control (same as a dragon)
- The length scales up to 5 minutes when a spirit summoner when you're GM
- Serpents are more willing to chill in your house for a bit longer
- Greater Night Sight kegs created before patch 1.15 have been fixed
- Fixed guild claim regions around the Harrower so that notority is judged correctly
- Terathan Keep now has a dungeon dye and material (2144)
- Dracothraxus will now splash dungeon dye materials and award champ tokens based on the top damager, upon death
- Fixed potion kegs filled from greater night sight potions dispensing regular night sight potions instead
- Fixed webbing from Mephitis never being able to catch a player, and fixed webs freeing each other's victims early
- Added 9 new items to the pirate map reward store including a flag to hoist onto your ship's mast
- Books should now read and save properly now
- Locked down books can only be edited by the author (not the owner of the house)
- The author of a book can enable/disable if their book can be edited by others via the context menu
- Fixed issue that could allow two accounts into a dungeon

## Masonry

- Fixed some of the labels in the masonry craft menu to match the actual item, or that were missing
- Masonry chances have been increased (see examples)

| Entry                             | min  | old max → new max | chance @ 100 |
| --------------------------------- | ---- | ----------------- | ------------ |
| Vase, Large Vase                  | 52.5 | 102.5 → 100.0     | 95% → 100%   |
| Stone Chair                       | 55.0 | 105.0 → 100.0     | 90% → 100%   |
| Stone bench + all 6 medium tables | 65.0 | 115.0 → 102.5     | 70% → 93.3%  |
| Large stone tables (E/S)          | 75.0 | 125.0 → 105.0     | 50% → 83.3%  |
| Fountain Deed                     | 75.0 | 125.0 → 107.5     | 50% → 76.9%  |

## Storage Rack

A lockable storage rack that holds stock of common supplies. The owner decides who else may draw from it, while each player who uses it keeps their own private loadouts and withdrawal settings. Each shelf has a loadout, a saved named set of items and quantities (up to 20 per player, per shelf) and restock the whole set in one click.

How is this different than Razor's restock? When you click Restock in Razor, it simulates the actions you would take if you were to manually copy out the values to your bag and has a slight delay between each action. With the storage rack, when you click your loadout to restock, it's instant.

## Arcane Lantern

A lockable house repository for wand charges. Deposit wands one at a time or drop a whole container of them, and the arcane lantern banks their charges per spell so you can redeem a fresh, fully charged wand later. When the wand is absorbed, it loses some charges during the process. Craftable through Tinkering.

## Bulk Order Deeds

- New BOD gump so you can filter a book by type, quality, quantity and material, with multi-select so you can combine several choices at once rather than one at a time
- Large bulk orders can now be filtered by their set, making a full book far easier to search
- Fixed the copper and gold bulk order reward tiers being assigned the wrong way round
- Combining carpentry deeds made from mismatched wood now tells you so, instead of appearing to do nothing at all

## Houses & Decoration

- House co-owners (and boat owners, for ship hold barrels) can now set how much a trash barrel holds, how long its contents survive, whether filling it empties it immediately, and what color it is
- Fixed the "in danger of collapsing" window so that it matches the published decay timings. The final IDOC stage is now the last hour before a house falls, rather than a rounded-off estimate that could be well over an hour out
- Houses without a courtyard now say so plainly when you try to use a courtyard-only feature, instead of failing without explanation
- Bee hives can only be relocated by the owner of the house they stand in

## Fishing

For all you fishers out there, instead of sitting on a pile of fish, you can now drop them off at your local fishmonger to track the largest catch and smallest catch of the month, year, and all time. Also you can drop off fish and it just tracks the most caught. Like fishing in real life, you do it for the big snag, and for the bragging rights with that picture on social media.

- A new records book tracks the largest and smallest example of every species ever turned in, with the angler's name and the date
- Leaderboards for monthly, yearly and all-time fishing, alongside a feed of recent turn-ins
- Records and rankings credit whoever actually caught the fish, not whoever handed it to the judge
- Only fish caught after the record system went live are eligible, so nobody can empty a pre-existing hoard onto the judge on day one (sorry folks!)
- You can only pull up big fish at GM fishing
- You will get AFK resource gump checks while fishing regardless of skill when fishing in deep water

## Skills & Spells

- At GM you now see an item's exact durability values instead of the condition description
- Reworked the duration for Spirit Speak, with added effects for spirit summoners. Using the skill again while it is still applied refreshes it to full duration
- Summons belonging to a spirit summoner now resist a monster's auto-dispel, scaled by the summoner's Spirit Speak. Uncontrolled summons such as EVs and blade spirits hold a weaker bond and resist less
- Fixed targeted spells failing when line of sight was briefly interrupted; the cast now retries rather than being wasted

## Achievements

- New Ancient and Enraged Kraken hunting achievements
- Dracothraxus has a one off achievement for dealing the most damage to Dracothraxus
- A new set of achievements for stealing from other players, counted by item type and by category

## Moongate Runes

You can now purchase Moongate Runes, that when consumed with codex fragments, change the hue (and thus the light) of your 7th circle spell gate. Higher end ones also change the actual gate itself.

- You can access and change your moongates and hues using `[moongates`
- These are bound per character, and cannot be unbound

## Salvagers Tapestry

No longer do you have to store all your treasure maps, SOS and and messages in a bottle in chests. Instead, mark (store) them on your tapesty of Britannia!

- Reward item found on the Pirate Reward store
- Drop items on the map, and they are marked (stored) and easily viewable and sortable
- Get one or a group with a few clicks
- You can hold a max of 500 on each tapestry

## CTF Points

Scoring has changed a bit in CTF to hopefully make it a bit more rewarding for all those involved.

### New Point Table

Every role now earns points: fighters, healers, defenders and flag runners. Points still convert to War Tokens 1:1, and the daily cap is unchanged (for now)

A few notes:

- The old "Defending" points are gone. They paid the victim for dying near the enemy who had their flag. Assists on the carrier and Carrier Escort now reward the same effort
- Guarding is capped at 20 points per match. Without the cap, a long standoff at one base could pay up to 80 points

| Action                                            | Before | Now             | Notes                                                                                                                                             |
| ------------------------------------------------- | ------ | --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Kill** (killing blow)                           | 1      | **2**           | Killing a teammate no longer gives points.                                                                                                        |
| **Assist**                                        | —      | **1**           | You dealt 15+ damage to an enemy in the 20 seconds before someone else killed them.                                                               |
| **Flag Carrier Kill**                             | 5      | **6**           | Killing blow on an enemy flag carrier (2 kill + 4 bonus).                                                                                         |
| **Flag Carrier Assist**                           | —      | **3**           | An assist on an enemy flag carrier.                                                                                                               |
| **Heal Assist**                                   | —      | **1**           | You healed a teammate in the 20 seconds before they got a kill or assist.                                                                         |
| **Healing**                                       | —      | **1 per 40 HP** | Only HP you actually restore counts: no overhealing, no self-heals, no potions. The teammate must have taken enemy damage in the last 30 seconds. |
| **Cure**                                          | —      | **1**           | Curing a poisoned teammate who is in combat. Once every 20 seconds.                                                                               |
| **Flag Steal**                                    | —      | **2**           | Taking the flag from the enemy base. Once per minute.                                                                                             |
| **Flag Capture**                                  | 5      | 5               | Unchanged.                                                                                                                                        |
| **Flag Relay**                                    | —      | **2**           | You carried the flag earlier in the run and a teammate capped it. Stacks with Escort or Team Capture.                                             |
| **Escort**                                        | —      | **2**           | You were within 12 tiles of the capper.                                                                                                           |
| **Team Capture**                                  | —      | **1**           | Every other active teammate gets a share of each capture.                                                                                         |
| **Flag Return**                                   | 4      | 4               | Unchanged. Once per minute.                                                                                                                       |
| **Base Raid**                                     | +3     | **+2**          | Bonus for a kill inside the enemy's base.                                                                                                         |
| **Base Defense**                                  | —      | **+2 / +1**     | Bonus for a kill / assist near your own base.                                                                                                     |
| **Carrier Escort**                                | —      | **+2 / +1**     | Bonus for a kill / assist near your team's flag carrier.                                                                                          |
| **Guarding**                                      | —      | **1 every 15s** | You're near your own base while an enemy is there too. Up to 20 per match.                                                                        |
| **"Defending"** (points for dying near your flag) | 1–2    | **Removed**     | Replaced by assists and Carrier Escort, which reward fighting instead of dying.                                                                   |

- Healing only counts real work. Self-heals, potions and healing a teammate at full HP earn nothing.
- Idle players get no share. "Active" means you fought, helped a teammate, or scored in the last 90 seconds. The CTF region records this whenever someone does something harmful or helpful. That gate keeps AFK players out of capture shares and guarding points.
- The scoreboards have been updated to include the new columns, and the Discord end-of-match summary now lists assists and healing.

## New Dawn Client - 1.7

- The character selection screen now shows a real paperdoll for each character, including equipment, hair and facial hair, rather than a name on its own
- When you delete your character, you're prompted to first enter the name to confirm
- The client is now told where the shard sits in its day/night cycle and how long a full cycle lasts, so the sun, moon and directional shadows track the real shard time
- Lights now fade in and out as they come and go from the screen
- World map has smooth scrolling
- The alternative journal will now save your custom tabs and filters and has a larger buffer
- Improved the login experience if your token has expired
- Fixed issue with capturing screenshots when you're killed in game
- You can remove the padding from CTRL-SHIFT name plates to take up less space
- Added new client effects for special hues (future)

## 💀 Champion

Previously, every champion token came from damage dealt to the champion itself. If you spent the
encounter thinning the horde and died or had to leave before the champion appeared, you walked away
with nothing.

Now, when a champion is defeated, everyone who helped clear the spawn is paid champion tokens based
on how much of the horde they killed, scaled against the top spawn killer for that encounter (the
same way tokens are scaled to the top damager on the champion itself). The single highest spawn
killer earns a bonus on top.

Kills are weighted by the level they happened at — a level 15 creature is not a mongbat:

- Levels 1–4 — ×1 per kill
- Levels 5–8 — ×2 per kill
- Levels 9–12 — ×3 per kill
- Level 13+ — ×4 per kill

Deeper levels pay more each, but there are far fewer of them, so levels 1–8 still hold about two
thirds of all the reward in a spawn. Turning up at level 12 will not out-earn the people who ground
it out from the beginning.

For a deeper analysis, check out https://docs.uonewdawn.com/champion-token-rework

### Overworld Champions

The Overworld Champions are now part of a world event system.

- World Champion spawns activate on a schedule throughout the day and can no longer be activated with Valor
- Each one is announced in-game and in Discord about 15 minutes ahead, with a final warning 5
  minutes out, so there is time to travel. The exact location is named in the final warning
- Only one overworld champion runs at a time
- If enough people answer the call and gather at the site before the countdown ends, it starts early
- Progress is posted to Discord as the champ advances to encourage public participation, and
  everyone at the altar sees level advances and white skulls as they happen
- Higher tiered mobs from the spawn have a chance to drop an Overworld Omen, a one-time use item
  that can activate an overworld champion outside of the daily schedule

**About the omen:** break it while standing inside an overworld champion's spawn area and the
champion begins in 5 minutes. It will refuse if an event is already running or counting down, if
that location is still on cooldown from its last run, or if the daily summon cap (2) has been used.
The omen is only consumed when it actually works — every rejection leaves it in your pack.

### Additional Changes

- Champion tokens, skulls, and artifacts are now awarded once per player rather than once per
  account
- There are two separate token payouts — one for champion damage, one for spawn kills — and your
  best character is picked automatically for each. They do not have to be the same character, so a
  dedicated spawn killer is paid for that work even if another of your characters topped the damage
- The champion skull and artifact draws are scored on damage, so you get one entry in each rather
  than one per account
- Your other characters are skipped for those draws rather than penalized: rewards are forfeited,
  not transferred to the winning character
- Damage and spawn kills are still tracked normally on every account, and every character with
  looting rights still earns Valor
- Gold, loot and the goodies drop are untouched
- Champion tokens are now awarded for clearing the spawn, not just for fighting the champion
- Spawn kill tokens are paid when the champion dies. If a level's kill bar expires and resets, the
  progress banked toward it is lost — and if the spawn decays all the way back to the start,
  everything banked is lost. Hold the line
- A minimum contribution is required to qualify, so tagging a handful of creatures won't earn a
  payout
- Champion spawn creatures also have a small chance to drop a token directly into your wallet
  (you'll get a message). This one pays out all through the spawn, so it still rewards you even if
  the spawn decays before a champion ever appears
- If you get a champion skull, you get a system message with a sound
