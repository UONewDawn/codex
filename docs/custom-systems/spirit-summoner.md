# Spirit Summoner

The Spirit Summoner is a unique mage archetype that fuses Magery with Spirit Speak, allowing you to channel spirits from beyond the veil to summon fundamentally different — and more powerful — creatures than any ordinary mage can achieve. This is one of New Dawn's most significant custom systems.

## What Is a Spirit Summoner?

A Spirit Summoner is any character who meets two simultaneous conditions:

- **Spirit Speak ≥ 50**
- **Spirit Speak ≥ Magery** (equal counts — you simply cannot have Magery exceed Spirit Speak)

Once both conditions are met, every summoning spell you cast is enhanced through the spirit summoner path. If your Magery ever exceeds your Spirit Speak, or Spirit Speak drops below 50, you lose spirit summoner status and revert to normal mage summoning.

### Proximity Hints

As you approach the requirements, the system provides feedback:

| Closeness to Qualifying          | Message                                   |
| -------------------------------- | ----------------------------------------- |
| Spirit Speak within 10 of Magery | _"You sense restless spirits nearby..."_  |
| Spirit Speak within 6 of Magery  | _"Ghostly whispers swirl around you..."_  |
| Spirit Speak within 3 of Magery  | _"The veil between worlds grows thin..."_ |

---

## Summon Duration

Spirit Summoner summons use a Spirit Speak-based duration formula instead of the fixed durations normal mages receive:

| Spirit Speak | Duration    |
| ------------ | ----------- |
| 50           | 6 minutes   |
| 60           | 6.8 minutes |
| 70           | 7.6 minutes |
| 80           | 8.4 minutes |
| 90           | 9.2 minutes |
| 100          | 10 minutes  |

This applies to 5th circle spirit creatures **and** all 8th circle summons (elementals and daemon).

---

## Stat Scaling

The strength of your spirit summons scales with two skills working together: **Spirit Speak** and **Animal Lore**.

### The Stat Scaler Formula

This scaler is applied as a percentage increase to **all base stats, all skills, and armor** on the creature at the moment of summoning:

- Strength, Dexterity, Intelligence (and their derived pools)
- All skill values
- Armor (additional scaling: `statScaler × AL/100`)

Both 5th circle and 8th circle summons use the same scaler value. The only difference is that 5th circle summons are also forced to 1 control slot.

!!! tip "Animal Lore is Core"

    At GM Animal Lore (100), you receive the full 35% stat boost. Without Animal Lore, the scaler is zero and your summons receive no stat enhancement at all. **Animal Lore is not optional — it is the primary stat multiplier for the entire system.**

### Stat Scaler by Animal Lore

| Animal Lore | Stat Scaler | Result (% boost to all stats/skills) |
| ----------- | ----------- | ------------------------------------ |
| 0           | 0.00        | +0%                                  |
| 25          | 0.0875      | +8.75%                               |
| 50          | 0.175       | +17.5%                               |
| 75          | 0.2625      | +26.25%                              |
| 100         | 0.35        | +35%                                 |

---

## 5th Circle: Spirit Creature Pool

When a Spirit Summoner casts the 5th circle Summon Creature spell, the game picks randomly from a special pool of spirit creatures instead of the standard summons. All spirit creatures are summoned with 1 control slot and use the Spirit Speak duration formula.

| Creature       | Notable Ability                                                               |
| -------------- | ----------------------------------------------------------------------------- |
| Polar Bear     | —                                                                             |
| Panther        | —                                                                             |
| Giant Serpent  | 80% chance to inflict Greater or Deadly poison on hit                         |
| Imp            | —                                                                             |
| Spiritual Soul | —                                                                             |
| Scorpion       | 80% chance to inflict Greater or Deadly poison on hit; Poisoning skill 80–100 |
| Dire Wolf      | —                                                                             |
| Giant Spider   | Inflicts regular poison on hit                                                |

---

## 8th Circle: Enhanced Summons

Spirit Summoners' 8th circle summons (Air Elemental, Earth Elemental, Fire Elemental, Water Elemental, Daemon) receive the full stat scaling treatment and appear with a distinctive spirit hue.

### Spirit Hues

| Creature        | Hue  |
| --------------- | ---- |
| Daemon          | 2152 |
| Earth Elemental | 2191 |
| Fire Elemental  | 2191 |
| Water Elemental | 2177 |
| Air Elemental   | 2177 |
| Other           | 2178 |

### Daemon: Reduced Control Slots

A spirit-summoned Daemon costs only **3 follower slots** (vs. 4 for a standard Daemon) and is named _"Spirit of [name]"_.

### No Scrolls for 8th Circle

Spirit Summoners **cannot cast 8th circle summon spells from scrolls**. The system returns the message:

> _"A spirit summoner must channel their will directly through the arcane words."_

You must cast from your own skill. Scrolls work normally for non-spirit-summoner characters.

---

## Summon Healing Bonus

When you heal a summoned creature and you have the ability to hear ghosts, your heal receives a bonus:

At GM Spirit Speak (100), you heal your spirit summons for up to **50% more** than the base heal amount.

---

## Dispel Resistance

Spirit Summoned creatures are harder to dispel. Resistance is governed by your Spirit Speak at the time of the dispel attempt.

### Player-Cast Dispel / Mass Dispel

At GM Spirit Speak: **50% chance** to resist a player's Dispel or Mass Dispel.

### NPC/Monster Auto-Dispel

At GM Spirit Speak: **80% chance** to resist auto-dispel triggered by a monster's melee attack.

### NPC-Cast Dispel (e.g. a monster casting the spell)

At GM Spirit Speak: **99% chance** to resist a dispel spell cast by an NPC creature.

!!! note "Dispel Resistance Applies to Spirit Summons Only"
    Resist chances only apply to creatures that were enhanced through the spirit summoner path. Standard summons cast while you happen to have Spirit Speak do not receive resistance.

---

## Blade Spirits and Energy Vortex

Blade Spirits and Energy Vortex are **not** affected by Spirit Summoner status. Both spells summon their creatures through a different code path that bypasses the spirit summoner system entirely:

- They do **not** receive the stat scaler
- They do **not** attack a spirit summoner
- Their duration (random 40–120 seconds) is **not** affected by Spirit Speak
- They cannot be commanded (`all follow`, `all attack`, etc.)

This is working as designed. If you want controllable summons, use 5th or 8th circle spirit summons instead.

---

## Comparison: Spirit Summoner vs. Standard Mage

| Aspect                   | Standard Mage             | Spirit Summoner                |
| ------------------------ | ------------------------- | ------------------------------ |
| 5th Circle Summons       | Random standard creatures | Unique spirit creature pool    |
| 8th Circle Stats         | Base stats                | +35% at GM Animal Lore         |
| 8th Circle Duration      | Fixed                     | 6–10 min (Spirit Speak scaled) |
| Daemon Control Slots     | 4                         | 3                              |
| 8th Circle Scrolls       | Yes                       | No                             |
| Dispel Resist (player)   | None                      | Up to 50% (GM SS)              |
| Dispel Resist (NPC auto) | None                      | Up to 80% (GM SS)              |
| Dispel Resist (NPC cast) | None                      | Up to 99% (GM SS)              |
| Summon Heal Bonus        | Standard                  | Up to +50% (GM SS)             |
| Spirit Hue               | No                        | Yes                            |
| Blade Spirits/EV         | They attack you           | They ignore you                |

---

## Building a Spirit Summoner

### Core Skills

| Skill                   | Level | Notes                                                                 |
| ----------------------- | ----- | --------------------------------------------------------------------- |
| Magery                  | 100   | Required for all summon spells                                        |
| Spirit Speak            | 100   | Must be ≥ Magery; controls duration, healing bonus, and dispel resist |
| Animal Lore             | 100   | Required for full stat scaling — do not skip this                     |
| Evaluating Intelligence | 100   | Spell power                                                           |
| Meditation              | 100   | Mana regeneration                                                     |

### Optional Supporting Skills

- **Resisting Spells** — PvP survivability
- **Wrestling** — Defensive skill, avoids spell disruption
- **Inscription** — Spell damage bonus

### Stats

- **Intelligence:** 100+ (primary mana pool)
- **Dexterity:** 25–50 (casting speed)
- **Strength:** 25–75 (reagent carrying and equipment requirements)

---

## Combat Tips

### PvM

1. Open with a 8th circle summon (Daemon for damage, or Elemental preference)
2. Use 5th circle spirit creatures as additional meatshields / poison deliverers
3. Keep Spirit Speak ≥ Magery so your summons remain spirit-enhanced
4. Heal spirit summons — your bonus heal makes this efficient at GM Spirit Speak

### PvP

- Dispatch 8th circle summons early; they're durable and dispel-resistant
- Giant Serpent and Scorpion spirit creatures are useful for persistent poison pressure
- Blade Spirits and Energy Vortex still provide raw pressure but cannot be directed

---

## Patch History

- **0.15:** Initial Spirit Speak summon enhancements introduced
- **0.16:** Custom 5th circle spirit creature pool added
- **0.18:** 8th circle enhancements; dispel resistance system added
- **0.29:** Spirit Summoner requirements formalized (SS ≥ 50, SS ≥ Magery)
- **0.48:** Follow speed and distance increases for spirit summons; additional 8th circle stat boosts
- **1.0:** Animal Lore synergy added; Spirit Speak now governs healing bonus and summon duration

For the full change history, see the [patch notes](../patches/index.md).

---

## Related Systems
