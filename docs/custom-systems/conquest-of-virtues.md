# Conquest of the Virtues

Engage in guild-based territorial warfare across four ruined locations in Britannia as the battle between Order and Chaos rages on. The Conquest of the Virtues system pits Order guilds against Chaos guilds in timed battles over capture points, draining the enemy faction's tickets until one side is eliminated or time runs out.

!!! info
    This mode is heavily influenced by Battlefield's Conquest mode.

## Overview

In the aftermath of the Codex War, four significant locations across Britannia lie in ruins. These strategic points become rotating battlegrounds where Order and Chaos fight to dominate capture points and reduce the enemy faction's ticket count to zero.

Each battle is fully automated — the system manages start times, respawning, scoring, and Discord announcements without staff involvement.

## The Four Ruins

### Ruins of Britain

**Location:** East of Britain | **Capture Points:** 5

Once the shining capital of Britannia, Britain fell during the Codex War. Its ruins now serve as a large open battlefield in the heartland.

**Capture Points:** `[A] Ruined NW` · `[B] Ruined NE` · `[C] East Side Park` · `[D] Ruined SE` · `[E] Ruined SW`

### Ruins of Trinsic

**Location:** Northwest of Trinsic | **Capture Points:** 3

The proud city of honor was not spared from the Codex War's devastation. Its ruined walled streets offer defensive positions and a mix of open and confined spaces.

**Capture Points:** `[A] Ruined NW` · `[B] Ruined Middle` · `[C] Ruined SE`

### Ruins of the Shadowlords

**Location:** West of Yew | **Capture Points:** 3

A dark and foreboding location where the Shadowlords once held power. Unlike other ruins, this battle takes place across **three vertical floors** of the same structure, with capture points stacked from ground level to the top.

**Capture Points:** `[A] Main Hall` · `[B] Second Floor` · `[C] Third Floor`

### Ruins of Moonglow

**Location:** Original Moonglow island | **Capture Points:** 5

Where the magical city of Moonglow once stood, only ruins remain. The layout includes a central maze area surrounded by four outer points.

**Capture Points:** `[A] Ruined NW` · `[B] Ruined NE` · `[C] Ruined Maze` · `[D] Ruined SE` · `[E] Ruined SW`

## How It Works

### The Ticket System

Each faction — Order and Chaos — starts a battle with **400 tickets**.

Tickets are lost two ways:

1. **Deaths:** Each time a faction member dies in the region, that faction loses **1 ticket**.
2. **Capture point pressure:** Each game tick, the faction that controls fewer capture points than the enemy loses tickets equal to the **net capture point disadvantage** (e.g., if Order holds 3 points and Chaos holds 1, Chaos loses 2 tickets per tick).

The battle ends immediately when either faction's tickets reach **0**. That faction loses.

### Capture Points

Each capture point is an **8×8 tile platform** marked with a physical flag. The flag rises higher on its pole as progress toward capture increases — providing a visual cue of how contested a point is.

**Capturing a point:**

- Stand on the platform. Players at the same Z-level as the point contribute to capture.
- If your faction has **more players** on the point than the enemy, your progress ticks up each second proportional to your numerical advantage.
- If both factions have equal numbers on the point, progress halts.
- A neutral point requires **20 ticks of uncontested progress** to capture.
- A point already owned by the enemy must first be **neutralized** (20 ticks) before your faction can begin capturing it.

**Flag colors:**

- **White (no hue):** Neutral
- **Blue (hue 101):** Controlled by Order
- **Red (hue 37):** Controlled by Chaos

When a point is captured, fireworks launch from the platform and a region-wide message is broadcast.

Scoreboard notation: a `*` next to a faction name on the scoreboard (e.g., `[Order*]`) means the point is controlled by that faction but is currently being contested.

### Win Conditions

A battle ends when any of the following occur:

| Condition                                                            | Result                             |
| -------------------------------------------------------------------- | ---------------------------------- |
| A faction's tickets reach **0**                                      | The other faction wins             |
| The **60-minute timer** expires and one faction has fewer tickets    | The faction with more tickets wins |
| The timer expires and **neither faction lost more than 100 tickets** | Draw (no winner declared)          |
| The timer expires and **tickets are exactly equal**                  | Draw                               |

Win/loss/draw results are announced server-wide and posted to the New Dawn Discord.

### Availability Cycle

Each of the four ruins operates on an independent rotation:

- After a battle concludes, the region enters a **4-hour cooldown**.
- The system checks all regions every minute and automatically starts any that have become available.
- When a region opens for battle, a server-wide announcement is broadcast describing the current owner (Order, Chaos, or unclaimed) and inviting challengers.

Battles run continuously — no staff action is required to start or manage them.

## Entering a Conquest Region

### During an Active Battle

| Player Type                            | Can Enter? |
| -------------------------------------- | ---------- |
| Order guild member                     | Yes        |
| Chaos guild member                     | Yes        |
| Neutral guild member (non-Order/Chaos) | **No**     |
| Unguilded player                       | **No**     |
| Player on a mount                      | **No**     |
| Player with followers/pets             | **No**     |

Players who do not meet these requirements will be turned back at the region border.

### While the Region is Inactive

All players may enter inactive regions freely. No PvP is enforced during the dormant period.

## Respawn System

Conquest uses an **in-region respawn** system rather than sending players to the nearest town.

On death inside an active conquest region:

1. Your items are automatically returned to your **backpack** from your corpse.
2. You receive a 10-second count before respawning.
3. On respawn, you are **fully healed** (hits, stamina, mana restored to max) and all debuffs, curses, stat mods, poison, transformations, and active spells are removed.
4. Aggression flags against all players in the region are cleared.
5. You spawn at a **friendly-controlled capture point** chosen at random. If your faction controls no points, you spawn at your faction's **fixed respawn location** for that region.

You cannot bring a mount or followers into the region, so neither will be present on respawn.

## Spell Restrictions

The following spells are **blocked** inside active conquest regions:

**Teleportation (all blocked):**

- Mark
- Recall
- Gate Travel
- Teleport

**Summoning (all blocked):**

- Energy Vortex
- Blade Spirits
- Summon Creature
- Summon Daemon
- Air, Fire, Earth, and Water Elemental

All other spells function normally.

## Combat Rules

- Full PvP is enabled between Order and Chaos guild members in active regions.
- You may not harm or benefit players who are not in an Order or Chaos guild while inside the region.
- Housing placement is disabled in all conquest regions.
- Standard New Dawn PvP rules otherwise apply.

## In-Game Scoreboard

While a battle is active, a live scoreboard gump is pushed to all faction players in the region every few seconds. It displays:

- **Order tickets** and **Chaos tickets** (color-coded: white = healthy, green = declining, yellow = low, red = critical below 50)
- **Each capture point** and its current controller (`[Order]`, `[Chaos]`, `[Neutral]`, or `[Order*]`/`[Chaos*]` when actively being contested)
- **Per-player stats:** Kills / Deaths / Captures for every Order and Chaos player currently in the region

The scoreboard closes automatically when the battle ends.

## Checking Conquest Status

Use the command `[conquest` in-game to open the Conquest Overview, which shows all four ruins, their current status (Active / Inactive), the current owner (Order / Chaos / Unclaimed), the live ticket score if active, and the time remaining or time until the next battle.

## Strategy & Tips

### Offensive Strategy

- **Capture points multiply pressure** — holding 3 of 5 points generates 2× ticket drain compared to a single net point.
- **Contest outnumbered points first** — a single defender can stall a capture; send enough players to achieve majority.
- **Respawn at captured points** — taking and holding interior points reduces your travel time between deaths.
- **Thin their tickets with deaths** — each kill also costs the enemy a ticket on top of the capture pressure.

### Defensive Strategy

- **Spread out** — one player per point is efficient ticket defense even if they can't solo-hold against a rush.
- **Prioritize the contested point** — don't rotate to a point already safe; reinforce the one currently being taken.
- **Neutralize before capping** — you must neutralize an enemy-held point before capturing it, so start early.

### Entry Restrictions to Note

- You cannot enter on a mount — dismount before crossing the border.
- Pets and followers are left behind — plan your build accordingly.
- Neutral/unguilded players cannot enter during active battles.

## Stat Tracking

The following per-player stats are tracked per battle and recorded at the end:

- **Kills** (credited to your faction)
- **Deaths** (charged against your faction)
- **Captures** (capture points successfully taken or neutralized)

These feed into the server's Player Tracking system and may be used for future leaderboards or rewards.

## Common Questions

**Q: Can solo players participate?**
A: Only if they are in an Order or Chaos guild. Unguilded players cannot enter active conquest regions.

**Q: Do I need to be online 24/7 to hold territory?**
A: Each battle lasts 60 minutes and regions rotate every 4 hours. You only need to be present for the battle itself.

**Q: What happens if my guild disbands mid-battle?**
A: You lose your guild affiliation and would no longer count as Order or Chaos for capturing purposes.

**Q: Can small guilds compete?**
A: Yes. Capture point majority is based on the number of players on a point at that moment — a coordinated small group focusing one point at a time can outperform a larger but spread-thin force.

**Q: What happens if I die and my faction holds no capture points?**
A: You respawn at your faction's fixed spawn location for that region.

**Q: What if neither team wins when time runs out?**
A: If neither faction lost more than 100 tickets by the end of the 60-minute battle, the result is declared a draw with no winner.

## Related Systems

- [PvP & Murder System](../game-mechanics/pvp/index.md) - Conquest involves full PvP
- [Guilds](../community/index.md) - Guild system information

## Patch History

- **0.42:** Initial implementation with four ruined locations and guild-based territory control
- **0.46:** Unguilded player restrictions
- **1.x:** Ticket system, capture point mechanics, respawn system, scoreboard, and spell restrictions fully implemented

For detailed changes, see the [patch notes](../patches/index.md).
