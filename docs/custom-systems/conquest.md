---
description: "Conquest is New Dawn's objective-based team PvP mode. Capture and hold points, drain enemy tickets and earn War Tokens."
---

# Conquest

Take control of key positions across a contested battleground, hold them against the enemy, and bleed their tickets dry before yours run out.

Conquest is an objective-based team PvP mode inspired by such game modes as Battlefield's Conquest mode or WoW's Arathi Basin.

## Sing up

You can sign up in the Dawn Event Center, coordinates 5222, 388.

The Dawn Event Center can be accessed by using any public moongate and selecting the upper right option.

After both teams reach the arena minimum player requirement, the match will start after one minute.

## Game rules

- Full PvP is enabled between opposing teams - friendly fire is not
- No mounts allowed
- No pets or followers may enter the arena
- Stealing skill is disabled
- Summoning spells are blocked
- Skill and stat gains do not occur during matches
- Killing yourself awards no points
- Potions, reagents, and other consumables are free - nothing is consumed inside the arena
- Clothing take no damage
- Explosion pots have an 8 second timer
- The aura under your feet reflects your team color (make sure it's enabled in your client)
- Respawn:
    - When you die your items will be reequipped on resurrection
    - You receive a 10-second delay before respawning.
    - You teleport to a randomly chosen respawn spot at a friendly-controlled capture point, or your team's fixed spawn if you hold no points.

### Winning conditions

| Condition                                                     | Result              |
|---------------------------------------------------------------|---------------------|
| A team's tickets reach 0                                      | The other team wins |
| The 45-minute timer expires and one team has more tickets     | That team wins      |
| The timer expires and neither team lost more than 100 tickets | Draw                |
| The timer expires and tickets are exactly equal               | Draw                |

Win, loss, and draw results are announced server-wide and posted to the New Dawn Discord with a full match summary.

## Ticket system

Each team starts with 400 tickets.

Tickets are lost two ways:

1. Deaths: Each time a team member dies in the arena, that team loses 1 ticket.
2. Capture point pressure: Every game tick, the team that controls _fewer_ capture points than the enemy loses tickets equal to the net point disadvantage (e.g., if Fellowship holds 2 points and Shadowlords hold 1, Shadowlords lose 1 ticket per tick).

The match ends immediately when either team's tickets reach 0.

## Capturing points

Each capture point is a physical flag item placed on the map.

Capturing a point:

- Stand near the point. Multiple players at the same Z-level contribute to the capture effort.
- If your team has more players on the point than the enemy, your capture progress ticks up proportional to your numerical advantage each second.
- If both teams have equal numbers on the point, progress halts.
- A neutral point requires progressive ticks of uncontested control to capture.
- A point held by the enemy must first be neutralized before your team can begin capturing it.

Respawning at controlled points:

When you die and respawn, the system checks which points your team controls and spawns you at one of those point's respawn locations. If your team controls no points, you respawn at your team's fixed starting location.

## Scoring

| Action               | Points             |
|----------------------|--------------------|
| Capturing a point    | +2 per capture     |
| Neutralizing a point | +1 per neutralize  |
| Killing an enemy     | +1 per elimination |

## Arena - Old Trinsic

The currently active Conquest instance takes place in Old Trinsic, the walled city from Ultima 7.

> _The Battle for Old Trinsic_

- Minimum 4 players per team to start
- Maximum 12 players per team
- Match duration: 45 minutes
- Starting tickets: 400 per team

### Capture points location

Three capture points are placed across the ruins. The centre point is randomly selected each run from two candidate locations, keeping the meta fresh:

| Point          | Location                                                 |
|----------------|----------------------------------------------------------|
| [A] South Gate | Near the south wall                                      |
| [B] Centre     | Either Town Hall _or_ Fellowship Hall (random per match) |
| [C] North Gate | Near the north wall                                      |

Each capture point has several respawn locations attached to it. When you respawn, if your team controls a point you will spawn at one of that point's respawn spots — closer to the front line.

## War Tokens

War Tokens are the currency earned through Conquest matches. They can be exchanged for [rewards](../game-mechanics/currencies.md#war-tokens-store) at the [Dawn Event Center](../game-mechanics/currencies.md#dawn-event-center).

At the end of a game, tokens are awarded based on your individual points for that match:

- Winners receive their total points plus a +5 win bonus
- Losers receive their total points only
- There is a daily cap of 150 War Tokens per player - once hit, stats still record but no further tokens are awarded until the next day (Central Time)

Check your balance at any time with the `[profile` command.

## Related pages

- [War Tokens Store](../game-mechanics/currencies.md#war-tokens-store)
