---
description: "Patch notes for New Dawn server patch 1.20, released October 25th, 2026. Highlights: town Orphanages, rentable Market Stalls in Ocllo, the Battle Bombin' arena game, rebuilt War Calls for Order vs. Chaos, and a reworked Young Player Program."
---

# SERVER PATCH 1.20

## October 27th, 2026

This patch opens orphanages in five towns, puts market stalls up for rent in Ocllo, adds Battle Bombin' to the arena, and turns Order vs. Chaos War Calls into a race to a Final Push, and reworks the Young Player Program, along with a round of fixes and quality-of-life changes.

## 🛠️ Bug Fixes & Enhancements

- The countdown on an explosion potion will only display for the person who throws it
- Food only stacks with food made by the same cook, so shop-bought food can no longer pass as home-cooked for cooking BODs. Splitting a stack keeps its "prepared by"
- Kill statuettes now go straight into the pack of a player with looting rights, drawn by damage dealt, rather than to whoever landed the last hit
- Town NPCs now call the guards on anyone who attacks them, even from a distance
- You can pick a lit explosion potion back up after casting a spell without hitting the cooldown, and duels now use the normal potion cooldown
- Small BODs can be filled from containers in your open bank box or your house (not locked or trapped ones, or corpses), and carpentry and cooking orders no longer eat a matching container along with its contents
- New ash and yew logging achievements, and the mining titles now read properly after "the"
- The titles menu has a new look and a search box, and you can open it from your character profile
- You can't pick locks while on a mount (your arms aren't long enough, and you can't quite get the angle right, sorry UO limitation, nothing I can do about it!)
- The stable lists stay open after a claim, so you can claim several in a row
- The Magic Reflection and Reactive Armor buff icons now stay accurate, including after a restart and after a duel or any CTF/Conquest reset
- Reward points are now centered in the achievement completion popup
- A vendor dismissed while its owner's bank box is full now leaves its gold in the backpack with its goods, instead of losing it
- You can change access on your telescope when it's locked down and you're the home owner
- You can recast night sight before it expires after you get your first warning
- Night sight from the spell, potions and Owl Stew now lasts as long as it's meant to. A bug could make it last much longer
- Fixed snow sometimes following you from a cold area into a warm one
- Duel teams can't include two characters belonging to the same person
- Guilds declaring for Order or Chaos are now announced on Discord, and so are newly named constellations
- If you try to dock your boat without a key, it will tell you (before it would say you aren't the owner)
- Looking through your telescope looks nicer now (shooting stars, twinkling stars, you don't ever need to look at the real night sky again!)
- Bank checks show the blessed tag (they always were blessed)
- Orphanages have officially opened in **Britain**, **Moonglow**, **New Minoc**, **Ocllo** and **Paws**. See the [Orphanages](../custom-systems/orphanages.md) page for full details and yes, I know this is silly

## 🏪 Ocllo Market Stalls

The market in Ocllo has stalls for rent. For a weekly gold fee, you can run your own player vendor from a stall counter, just as if it stood in your house. No house needed. Set out a prop on your counter, like a crate of ingots, bolts of cloth or a crate of potions, to show passers-by what you sell.

Stalls are for traders, so keeping one takes more than rent. Each week your stall needs new goods on the counter, a recent sale to another player, and at least 5 items for sale. A stall that stops trading is warned, then put on notice, then cleared. Whatever happens, your goods go to your bank box.

When a stall frees up, it goes to a name drawn at random from the market waitlist, so there's nothing to camp. Double-click any stall's sign to join it.

See the [Market Stalls](../custom-systems/market-stalls.md) page for full details.

## 💣 Battle Bombin'

A new arena game for 2 to 8 players. Everyone starts in a corner of a walled maze with a bag of bombs. Blast through the breakable walls, grab the upgrades they leave behind (more bombs, bigger blasts, speed, a detonator), and catch your rivals in the blast. Bombs set each other off, your own blast can catch you, and the last player standing wins. Nobody gets hurt: a blast just knocks you out of the game.

Every game counts toward a monthly and an all-time leaderboard. At the end of each month, the top three go into the Past Seasons list. A game only counts when every player is a different person, so your own alts don't count. There are achievements to earn too, with titles for the dedicated: Fuse Lighter, Demolitionist, Powder Keg and Blast Baron. And yes, sometimes some things are just for fun, and the reward is the game itself. This is ok, folks.

See the [Battle Bombin'](../custom-systems/battle-bombin.md) page for full details.

## 🛡️ Order vs. Chaos: War Calls Rebuilt

**TL;DR:** A War Call is now a 25-minute tug-of-war. Hold the outpost to fill your War Meter. Nobody can win until the last 5 minutes, and then the first side to 100% wins. A big lead no longer settles it early, so stay and fight.

War Calls used to be won by whoever owned the outpost longest over 45 minutes, so once a side had a big enough lead the fight was over well before the end. A War Call is now a 25-minute race to the finish:

- At the bell the outpost goes neutral, so owning it beforehand gives no head start
- The outpost has no fortification during the call. Flips take about a minute, a capture locks it for only 30 seconds, and assaults can't be broken
- Each side fills a **War Meter** while it owns the outpost and holds the capture ground: no enemies on it, or more of you than of them. Meters fill at 5% a minute and stop at 90%
- Tearing down the enemy's banner is a **breakthrough** worth 10% of meter
- In the **Final Push**, the last 5 minutes, meters fill at 12% a minute with no cap, and the first side to 100% wins. If time runs out while the side that's behind still holds or is taking the outpost, up to 3 minutes of **overtime** follow
- Respawns there are 20, 40 and 60 seconds, and both sides return farther out
- The higher meter wins 720 season score (1,440 at a Shrine of War), and the winner takes the outpost fully fortified
- If only one faction shows up and it owns the outpost when the call ends, it wins **360 season score** (720 at a Shrine of War). Its players are paid as winners: 30 War Tokens, 5 Faction Points and credit toward Hold the Call
- The War Map, `[Ovc` and the New Dawn client's on-screen display show the countdown and both meters
- `[Ovc` replaces `[OvcPoints` and `[OvcMap`: one window with your rank and points, the season score, any War Call and each side's top three, plus a button for the War Map
- When only one faction answered a War Call, the end-of-call message could name the side that never showed up. It now names the side that answered the call
- Most important change, capturing an outpost sets off fireworks in the captor's faction color

See the [Order vs. Chaos](../custom-systems/order-vs-chaos.md#war-calls) page for full details.

## 🛡️ Order vs. Chaos: Assaults

**TL;DR:** Walking off the capture ground no longer locks you out. Only losing the fight inside the outpost does.

- When the attackers leave the capture ground for a minute, their assault now says it **stalled**, not that it was broken. A stalled assault has no lockout, and you can retake the ground right away. Only a real break, when the attackers have died 3 more times than the defenders in the last 15 minutes, says "broken" and locks the outpost for 15 minutes. See [Defending](../custom-systems/order-vs-chaos.md#defending)

## 🌱 The Young Player Program

These changes are designed to make the Young Player Program a bit more friendly.

- **New players are Young automatically**, whichever city they start in. Extra accounts can opt in once, during their first 5 hours
- **Protection only works on Ocllo Island**, and leaving no longer ends Young. Leaving pauses it, and coming back restores it. You get three departures. The fourth ends Young
- **Young ends** at 120 hours of play, 450 total skill, any murder, or any PvP, fighting back included. Renouncing ends it too
- **Young players can't raise a skill past 80 while on Ocllo.** Go out into the world to master it
- **Young players can now travel freely**: moongates, recall, gate and boats
- **New help for new players:**
  - A guided walk around Ocllo
  - **Way Home**, to get back to the Ocllo healer from almost anywhere
  - A notice each time you leave the island
  - A guide after your first death off the island
  - The **Ocllo Diary**, which earns the title Ocllo Graduate
- Everyone can now hunt on Ocllo and in its sewer, but no one can harm a Young player there

Type `[young` to see your status. See the [Young Player Program](../custom-systems/young-program.md) page for full details.
