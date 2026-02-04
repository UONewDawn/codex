# Combat System

Master combat mechanics in New Dawn and become a formidable warrior.

!!! note "New Dawn Combat Changes"
    New Dawn features several significant combat modifications from classic UO. See the [What's Different](../getting-started/whats-different.md) guide for a complete overview, or read the sections below for detailed mechanics.

## New Dawn Combat Modifications

### Stamina Loss System (Replaces Dex Penalty)

New Dawn removes the classic dexterity penalty from armor and replaces it with a stamina loss system:

**How It Works:**

- When you take damage, you lose stamina based on your armor
- Armor type (plate, chain, leather) affects stamina drain
- Hit location matters (chest takes more hits = more stamina loss)
- Armor material (iron, valorite, etc.) affects the penalty

**Hit Location Probabilities:**

- Chest: 40%
- Arms: 20%
- Legs: 15%
- Hands/Head: 10% each
- Neck: 5%

**Benefits:**

- Wear heavy armor without movement penalty
- Stamina management becomes tactical
- Different armor types remain meaningful
- Running doesn't drain stamina (Patch 0.29)

### Archery Modifications

**Standing Still Delay:**

- 500ms delay when standing still before shooting
- Encourages movement in archer PvP
- Prevents insta-hit archery

**Snare Ability:**

- Requires **80+ Anatomy** and **80+ Archery**
- **25% chance at GM** to immobilize target for 3 seconds
- Disrupts spell casting
- **20-second cooldown**
- **15 stamina cost**
- Makes archery more tactical

### Parrying Enhancements

**Shield Bash:**

- Custom ability added to Parrying skill
- Provides offensive option for shield users

**Fire Breath Protection:**

- Parrying skill and shield quality absorb fire breath damage
- Makes shields valuable against dragons and other fire-breathers
- Scales with parrying skill

### Explosion Potion Changes

**Delay Mechanics:**

- **1.5-second base delay** before explosion
- **Small random variation** in explosion time
- **No potion cooldown** (heal potions have 10s cooldown)
- **2-second cooldown** on other potions

**Damage Formula:**

- Alchemy bonus applies to **minimum damage** (not total)
- Base damage vs players: min 5, max 15
- GM Alchemy adds +10 to min, +5 to max
- GM Alchemy result: 15-20 damage vs players

### Poison System Enhancements

**Poisoning vs Immune Mobs:**

- GM Poisoning: **50% chance** to poison normally immune creatures
- Scales from 0% at low skill to 50% at GM
- Makes Poisoning viable against more content

**GM Magery + GM Poison Combination:**

- **1% chance for Lethal poison** within 2 tiles
- **10% chance for Deadly poison** within 3 tiles
- Rewards dual-skill investment

### Weapon & Armor Values

- Converted to **UOR (Ultima Online: Renaissance) era** values
- Initially changed to T2A but reverted for better balance (Patch 0.16)
- Damage formulas adjusted to match weapon changes

### PvP Spell Damage

- Custom min/max damage ranges for player vs player
- Adjustable in-game for balance
- **Magic Resist cuts damage by 1/3** (not 1/2 like classic)
- **Spell range: 10 tiles** for most spells (Teleport remains 12)

## Combat Basics

### Engaging in Combat

To attack a target:

1. **War Mode:** Press Tab or click the peace/war icon
2. **Target:** Click on your target
3. **Auto-Attack:** Your character will attack automatically

### Combat Calculations

**Hit Chance Formula:**

```text
Attack Skill vs. Defender's Defense Skill
Modified by: Tactics, Anatomy, Weapon accuracy
```

**Damage Formula:**

!!! warning
        These need refinement. Confirm your template in the Discord community.

```text
Base Weapon Damage
× Strength modifier
× Tactics bonus
× Anatomy bonus
+ Critical hit chance
```

## Weapon Types

### Melee Weapons

- **Swords:** Balanced damage and speed
- **Fencing:** Fast attacks, lower damage
- **Maces:** Slower, higher damage, good vs. armor

### Ranged Weapons

- **Archery:** Bows and crossbows

## Combat Skills

**Essential:**

- Weapon Skill (your choice)
- Tactics
- Anatomy
- Healing

**Supportive:**

- Parrying
- Resisting Spells
- Magery (utility)

## Defense Mechanics

### Armor

**Armor Rating (AR):**

- Reduces incoming physical damage
- Different materials offer different AR
- Can be magical with extra properties

**Armor Types:**

- **Plate:** Highest protection, heaviest
- **Chain:** Medium protection and weight
- **Leather:** Light protection, allows meditation

### Parrying

- Requires shield equipped
- Blocks incoming attacks
- Higher skill = more blocks

## Healing in Combat

### Bandages

- Primary healing method
- Takes time to apply (several seconds)
- Can be interrupted by damage
- Scales with Healing and Anatomy skill

### Healing Spells

- **Heal:** Moderate restoration
- **Greater Heal:** Strong restoration
- Instant but costs mana

### Potions

- **Heal Potions:** Instant HP restoration
- **Cure Potions:** Remove poison
- **Refresh Potions:** Restore stamina

## Combat Strategies

!!! warning
    These need refinement. Confirm your template in the Discord community.

### Melee Combat

1. **Engage:** Move to target
2. **Attack:** Auto-attack begins
3. **Special Move:** Use when appropriate
4. **Heal:** Bandage when low HP
5. **Manage Stamina:** Don't run out

### Ranged Combat

1. **Distance:** Stay at range
2. **Kite:** Move while shooting
3. **Heal:** Bandage between shots
4. **Ammo:** Watch ammunition count

### Magic Combat

1. **Pre-buff:** Apply Protection, Magic Reflection
2. **Damage:** Cast offensive spells
3. **Control:** Summons or fields
4. **Heal:** Greater Heal as needed

## PvP Combat

### Basic PvP

- **Notoriety System:** Blue, gray, red players
- **Criminal Actions:** Attacking innocents
- **Murder Counts:** Killing blues
- **Stat Loss:** Penalty for reds

### PvP Tips

!!! tip "PvP Success"
    - Keep moving (harder to hit)
    - Manage resources (bandages, potions, regs)
    - Use Line of Sight (LOS)
    - Practice combos and timing
    - Join practice PvP sessions

## Monster Combat (PvM)

### Monster Difficulty

- **Weak:** Orcs, ettins (for beginners)
- **Medium:** Ogres, lizardmen
- **Strong:** Dragons, demons, balrons
- **Boss:** Special named creatures

### Tactics

**Solo:**

- Assess monster before engaging
- Keep escape route clear
- Bandage timing is critical

**Group:**

- Tank draws aggro
- Damage dealers attack
- Healer supports
- Focus fire priority targets

## Status Effects

### Poison

- **Levels:** Lesser, Normal, Greater, Deadly, Lethal
- **Cure:** Cure potions or spells
- **Prevention:** Poison resistance

### Paralysis

- Frozen in place
- Can't move or cast
- Wears off after time
- Can be dispelled

## Combat Macros

### Essential Macros

```text
[Bandage Self] - Quick self-heal
[Use Last] - Reuse last item (potions)
[Target Last] - Attack same target
[War/Peace Toggle] - Quick mode switch
```

---

**Train hard, fight smart, conquer all!**
