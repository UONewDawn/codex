# Battleground: Conquest

Take control of key positions across a contested battleground, hold them against the enemy, and bleed their tickets dry before yours run out. Conquest is an objective-based team PvP mode inspired by such game modes as Battlefield's Conquest mode or WoW's Arathi Basin.

## Overview

Two teams are dropped into a dedicated arena. Multiple capture points are scattered across the map. Teams fight to control the majority of those points — every second one team holds more points than the other, the losing side bleeds tickets. The first team to drain the enemy's tickets to zero (or the team holding more when time expires) wins.

## How to Join

Head to **Dawn (Event Center)** and find the Conquest signup book. Use it to register your interest for an available match. You will be placed on a team automatically when signups fill.

### Queue System

Conquest runs on a demand-driven queue matching the CTF flow:

1. The automated queue timer **opens signups** for a Conquest instance.
2. Once the **minimum number of players per team** have signed up, a **2-minute fill window** opens — extra players can still join.
3. After the fill window, all queued players receive a **confirmation gump** to accept entry and teleport into the arena.
4. Players who don't confirm in time are removed. If either team is empty after confirmations, the match is cancelled.
5. The game then has a **1-minute prep period** (blockers at spawn gates prevent early rushing) before combat begins and players are unlocked.

!!! note
Multi-accounting is blocked — if another character tied to your Discord account is already queued or in a Conquest match, you will be denied entry.

## Current Arena — Old Trinsic

The currently active Conquest instance takes place in **Old Trinsic**, the walled city from Ultima 7.

> _The Battle for Old Trinsic_

- Minimum **4 players per team** to start
- Maximum **12 players per team**
- Match duration: **45 minutes**
- Starting tickets: **400 per team**

### Teams

| Team            | Colour     | Spawn Side |
| --------------- | ---------- | ---------- |
| **Fellowship**  | Royal Blue | South      |
| **Shadowlords** | Crimson    | North      |

Your character is tinted with your team's color for the duration of the match.

### Capture Points

Three capture points are placed across the ruins. The centre point is **randomly selected** each run from two candidate locations, keeping the meta fresh:

| Point              | Location                                                 |
| ------------------ | -------------------------------------------------------- |
| **[A] South Gate** | Near the south wall                                      |
| **[B] Centre**     | Either Town Hall _or_ Fellowship Hall (random per match) |
| **[C] North Gate** | Near the north wall                                      |

Each capture point has several respawn locations attached to it. When you respawn, if your team controls a point you will spawn at one of that point's respawn spots — closer to the front line.

## The Ticket System

Each team starts with **400 tickets**.

Tickets are lost two ways:

1. **Deaths:** Each time a team member dies in the arena, that team loses **1 ticket**.
2. **Capture point pressure:** Every game tick, the team that controls _fewer_ capture points than the enemy loses tickets equal to the **net point disadvantage** (e.g., if Fellowship holds 2 points and Shadowlords hold 1, Shadowlords lose 1 ticket per tick).

The match ends immediately when either team's tickets reach **0**.

## Capture Points

Each capture point is a physical flag item placed on the map.

**Capturing a point:**

- Stand near the point. Multiple players at the same Z-level contribute to the capture effort.
- If your team has **more players** on the point than the enemy, your capture progress ticks up proportional to your numerical advantage each second.
- If both teams have equal numbers on the point, progress halts.
- A neutral point requires progressive ticks of uncontested control to capture.
- A point held by the enemy must first be **neutralized** before your team can begin capturing it.

**Respawning at controlled points:**

When you die and respawn, the system checks which points your team controls and spawns you at one of those point's respawn locations. If your team controls no points, you respawn at your team's fixed starting location.

## Win Conditions

| Condition                                                         | Result              |
| ----------------------------------------------------------------- | ------------------- |
| A team's tickets reach **0**                                      | The other team wins |
| The **45-minute timer** expires and one team has more tickets     | That team wins      |
| The timer expires and **neither team lost more than 100 tickets** | Draw                |
| The timer expires and **tickets are exactly equal**               | Draw                |

Win, loss, and draw results are announced server-wide and posted to the New Dawn Discord with a full match summary.

## Respawn System

On death inside an active Conquest:

1. Your items are automatically returned to your **backpack** from your corpse.
2. You receive a **10-second delay** before respawning.
3. On respawn you are **fully healed** (hits, stamina, mana restored to max) and all debuffs, stat mods, curses, poison, transformations, and active spells are cleared.
4. Aggression flags against all players in the arena are cleared.
5. You teleport to a **randomly chosen respawn spot** at a friendly-controlled capture point, or your team's fixed spawn if you hold no points.

## Combat Rules

- Full PvP is enabled between opposing teams — friendly fire is not
- **No mounts** allowed
- **No pets or followers** may enter the arena
- Potions, reagents, and other consumables are **free** — nothing is consumed inside the arena
- Skill and stat gains do not occur during matches

## Scoreboard

A live scoreboard gump is pushed to all participants every few seconds showing:

- **Team tickets** (color-coded: white = healthy, yellow = low, red = critical)
- **Each capture point** and its current controller
- **Per-player stats:** Points / Kills / Deaths / Captures for every active player

## Points & War Tokens

Individual points are tracked during each match and feed into the War Token reward system (shared with [CTF](capture-the-flag.md)).

| Action               | Points                 |
| -------------------- | ---------------------- |
| Capturing a point    | **+2** per capture     |
| Neutralizing a point | **+1** per neutralize  |
| Killing an enemy     | **+1** per elimination |

War Tokens are awarded at the end of the match:

- **Winners** receive their total points plus a win bonus
- **Losers** receive their total points only
- A **daily cap** applies in Conquest, but is separate from the daily CTF cap

Spend War Tokens at the **Commander's War Chest** vendor in Dawn.

## Strategy & Tips

### Offensive

- **Hold majority, not all** — controlling 2 of 3 points is enough to drain the enemy. Spreading too thin chasing all three can cost you points you already held.
- **Contest the contested points first** — a single defender can stall a cap; send enough players to achieve numerical majority before moving on.
- **Respawn at your points** — capturing the center point cuts travel time dramatically after each death.
- **Deaths count** — every kill also costs the enemy a ticket on top of the cap pressure.

### Defensive

- **One defender per point delays captures** — even a solo player slows the enemy's progress and buys time for teammates to rotate.
- **Prioritize the actively contested point** — don't rotate to a safe point; reinforce the one currently being taken.
- **Remember to neutralize first** — you must neutralize an enemy-held point before you can start flipping it, so arrive early.

## Common Questions

**Q: Do I lose items if I die?**
A: No. All equipment is returned to your backpack on respawn.

**Q: Can I use mounts or bring pets?**
A: No. Mounts and followers are not allowed inside the arena.

**Q: Are consumables used up?**
A: No. Potions, reagents, and other consumables are free inside the arena.

**Q: What happens if I log out during a match?**
A: You are removed from the match and ejected to the exit location.

**Q: Can I join with multiple accounts?**
A: No. The system checks your linked Discord account and will block entry if another character is already queued or active.

**Q: What's the daily War Token cap?**
A: Separate from the CTF cap — 75 tokens per day (Central Time). Stats are still recorded after the cap to encourage continued play.

## Related Systems

- [Capture the Flag](capture-the-flag.md) — The other team-based PvP mode, using the same War Token economy
