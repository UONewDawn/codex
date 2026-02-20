# Pirate Adventures

Venture into four distinct instanced pirate encounters — a hidden cove hideaway, a crumbling lighthouse, a sunken treasure cave, and an ancient pirate tomb. Each instance is unlocked by activating a **deteriorating pirate map**. Clear the pirates, defeat the boss, and claim the locked reward chest.

## How to Start

### Obtaining Pirate Maps

**Deteriorating pirate maps** drop from **Ship's Strongboxes** or **ancient kraken**. When first obtained, the map is unreadable — its instance type is scrambled and it cannot be activated until restored.

### Restoring the Map

To reveal the map's destination:

1. Have a **Bottle of Vinegar** in your backpack.
2. Double-click the Bottle of Vinegar.
3. Target the deteriorating pirate map in your backpack.
4. You must have **90 Cartography skill** to restore it.

Once restored, the map is renamed (e.g., _"a restored map to a pirate's hideaway"_) and colored to match its instance. It is now ready to activate.

### Activating the Map

1. Double-click the restored map in your backpack.
2. A colored gate appears at your location leading to the instance, and an exit gate appears inside the instance.
3. Both gates close after **1 minute** — enter promptly, and invite any group members quickly.
4. The map is **consumed** on use.

!!! warning "Activation Restrictions"
    You cannot activate a map while:

    - Flagged criminal
    - In active combat
    - Already inside a pirate instance, CTF region, or Codex Rift

### Group Entry

Any player who steps through the entrance gate before it closes (within 1 minute of activation) is added to the instance. The gate color matches the instance type. There is no hard player cap in code, but only one instance of each type runs at a time — if the instance is already active or closing, the map will fail to start.

## The Four Instances

There are four distinct pirate instances. Each has its own environment, enemy roster, boss, duration, and rare items. All run on **Felucca**.

### Pirate Hideaway

**Gate color:** Red/orange · **Duration:** 60 minutes

A secluded cove filled with a full pirate crew — bards, bartenders, cooks, deckhands, navigators, quartermasters, lookouts, captains, bodyguards, and cannoneers operating ship cannons.

**Boss: Captain Dreadstorm** (the Relentless)

- Melee fighter with a Vanquishing Cutlass
- Whirlwind and Shadow Strike special abilities
- When first damaged, immediately summons **4 Pirate Bodyguards**
- High Strength, solid armor rating

---

### Pirate Lighthouse

**Gate color:** Blue · **Duration:** 60 minutes

A decrepit, crumbling lighthouse overrun by pirates and strange sea creatures.

**Boss: Ancient Drowner**

- Mage-type boss
- Periodic **AoE water attack** that requires line of sight
- Periodically **summons Drowners** from fixed spawn points

---

### Pirate Treasure Cave

**Gate color:** Green · **Duration:** 90 minutes

A wrecked ship leading into a hidden cave guarded by the spirit of a shipwrecked captain.

**Boss: Captain Grimjaw** (the Eternally Greedy)

- Melee fighter with a Vanquishing Cutlass and mana pool
- **Poison Gas** special ability on cooldown
- When first damaged, immediately summons **4 Pirate Bodyguards**
- Heaviest HP pool of all bosses (900–1,100 hits)

---

### Pirate Tomb

**Gate color:** Purple · **Duration:** 90 minutes

An ancient tomb where cursed undead pirates guard plundered riches. Features a unique roster of undead enemies:

- **Arcane Corsair** – spellcasting undead pirate
- **Bonebound Brigand** – heavy undead melee fighter
- **Phantom Raider** – ghostly attacker
- **Pirate Mummy** – wrapped undead fighter
- **Pirate Wraith** – wraith variant

**Boss: Ancient Pirate Mummy**

- Periodically launches a **sand area attack** that paralyzes nearby players
- Periodically **spawns additional undead pirates** from fixed spawn points
- Transforms during combat

---

## Instance Flow

### Progression

```
Enter through gate (1-minute window)
  ↓
Clear all pirates in the instance
  ↓
Boss spawns + announcement sent to all players
  ↓
Defeat the boss
  ↓
Reward chest spawns at fixed location inside instance
Gold key appears in the map activator's backpack
Doubloons awarded to all players who dealt damage
  ↓
5-minute grace period to loot
  ↓
All players, pets, and player corpses teleported to the exit point
```

### Instance Timer

Each instance runs for its full duration (60 or 90 minutes). If the boss is not killed before time runs out, the instance ends without a reward chest or doubloons.

If all players leave the instance before completing it, it resets automatically after **15 seconds**.

### Pirate Instance Clock

A physical clock item is placed inside each instance at a fixed location. **Single-click it** to see:

- The instance name
- Time remaining (or current status)
- Number of remaining pirates (or `(Boss)` if the boss is currently alive)

### Spell Restrictions

Inside any active pirate instance, the following spells are blocked:

- Recall, Mark, Gate Travel, Teleport

All other spells function normally.

## Rewards

### Reward Chest

On successful completion (boss killed), a **Pirate's Chest** spawns at a fixed location inside the instance, colored to match the instance type. It is:

- **Locked** (requires 100 Lockpicking skill — lock level ~95–101)
- **Trapped** with an Explosion Trap

The map activator automatically receives a **gold key** in their backpack to open the chest.

### Doubloons

Doubloons can be spent at the Buccaneer's Bazaar.

### Instance Rares

Each instance has a **chance** for one of two rare decorative items to spawn somewhere in the environment at the start. These are free-standing items in the world — find them and pick them up during the instance.

## Enemy Types

### Hideaway Pirates

| Mob                  | Role                                              |
| -------------------- | ------------------------------------------------- |
| Pirate Bard          | Support/distraction                               |
| Pirate Bartender     | Melee                                             |
| Pirate Bodyguard     | Heavy melee (also summoned by Captain Dreadstorm) |
| Pirate Cannon        | Environmental hazard                              |
| Pirate Cannoneer     | Operates cannons, ranged attacks                  |
| Pirate Captain       | Elite melee commander                             |
| Pirate Cook          | Melee                                             |
| Pirate Deckhand      | Light melee                                       |
| Pirate Lookout       | Scout type, can hide and stealth                  |
| Pirate Navigator     | Melee                                             |
| Pirate Quartermaster | Melee                                             |

### General Pirate Types (across instances)

| Mob                 | Notes                |
| ------------------- | -------------------- |
| Pirate              | Standard melee       |
| Pirate Sailor       | Standard melee       |
| Pirate Skeleton     | Undead melee         |
| Pirate Zombie       | Undead melee         |
| Scurvy Surgeon      | Utility/healer type  |
| Venomweb Privateer  | Ranged/poison        |
| Nightmare Arachnid  | Large spider variant |
| Ancient Sea Serpent | Sea creature         |
| Ancient Kraken      | Large sea creature   |

### Skill Scaling

Pirate stats are rolled on a **rank 1–9 scale** per enemy type, covering:

- **Combat skills** (Swords, Fencing, Macing, Archery, Wrestling)
- **Support skills** (Tactics, Anatomy, Parry)
- **Magic skills** (Magery, Eval Int, Meditation)
- **Defense skills** (Magic Resist)

## Buccaneer's Bazaar

The **Buccaneer's Bazaar** is run by **Captain Marrow** (the trader), a vendor you can double-click to open the store. The store can be disabled by staff; if so, Captain Marrow will not accept customers.

**Items for sale (default prices):**

| Item                                    | Cost              |
| --------------------------------------- | ----------------- |
| Pirate Painting (Sunken Sun)            | 20 doubloons      |
| Pirate Painting (2 additional variants) | 20 doubloons each |
| Pet Parrot                              | 50 doubloons      |
| Parrot Perch                            | 25 doubloons      |
| Pirate Cargo (decorative crate)         | 35 doubloons      |
| Pirate Cannon (housing deco)            | 50 doubloons      |
| Pirate Sea Chart                        | 40 doubloons      |
| Bucket of Ship Stain – Base             | 75 doubloons      |
| Bucket of Ship Stain – Dark Blue        | 75 doubloons      |
| Bucket of Ship Stain – Dark Red         | 75 doubloons      |
| Bucket of Ship Stain – Dark Green       | 75 doubloons      |
| Bucket of Ship Stain – Dark Purple      | 75 doubloons      |
| Bucket of Ship Stain – Dark Gray        | 75 doubloons      |

Buckets of Ship Stain are used to recolor your ship.

!!! note "Prices"
    Default prices are listed above. Actual in-game prices may differ if adjusted by staff.

## The Smuggler's Market

### What is it?

Shady merchants have set up trading posts throughout the world, selling resources and supplies at premium prices. These merchants only conduct business at night.

**Features:**

- Available only during nighttime hours
- Sell resources at premium prices
- Multiple locations across Britannia
- Accept gold only

**What They Sell:**

- Basic resources (ore, leather, wood, etc.)
- Reagents
- Potions
- Other supplies

!!! tip "Night Trading"
    If you're desperate for supplies, smugglers offer a convenient (if expensive) alternative during night hours.

## Strategy & Tips

### Map Restoration

- Stock up on Bottles of Vinegar before you start hunting for maps.
- The 90 Cartography requirement means you'll need a dedicated cartographer or a character with that skill trained.

### Group Composition

- **Tank or Tamer:** Boss fights are sustained — having something to absorb aggro matters.
- **Healer/Support:** Especially important in the Tomb where the Ancient Pirate Mummy paralyzes.
- **Damage dealers:** More damage means a faster clear before the timer pressure matters.

### Tactics

- Eliminate **Lookouts and Scouts** early — they hide and re-engage, making it hard to determine if the area is truly clear.
- **Cannoneers** deal significant ranged damage; take them out before they fire repeatedly or position out of their arc.
- The boss spawns only after **all regular pirates** are dead — clear methodically to avoid missing strays that stall the boss trigger.
- The **Treasure Cave** and **Tomb** have 90-minute timers rather than 60 — use that extra time on larger groups or harder clearing.

### Chest Key

The chest key goes to the **map activator** only. Make sure the activator has backpack space when completing the instance.

## Patch History

Pirate Adventures were introduced in **Patch 0.16** and have received extensive updates:

- **0.16:** Initial pirate instance system
- **0.17:** Pirate restrictions added
- **0.18:** Instance counter and improvements
- **0.19:** LOS blocking for cannons, label fixes
- **0.20:** Barding difficulty adjustments
- **0.23:** Ancient Drowner buffs, ethereal mount restrictions
- **0.24:** Extensive pirate AI and stat improvements, Captain Grimjaw buffs
- **0.25:** Instance timer adjustments (completion 10min → 5min grace period)
- **0.30:** Boss timer fixes
- **0.43:** Smuggler merchants added

For detailed changes, see the [patch notes](../patches/index.md).

## Related Systems

- [Currencies](../game-mechanics/currencies.md) - Pirate doubloons and rewards
- [Achievements](achievements.md) - Pirate-related achievements
