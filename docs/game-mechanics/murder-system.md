# Player Murder System Guide

## Overview

The murder system tracks player kills and applies consequences for those who engage in player killing (PKing). This system uses both **short-term** and **long-term** murder counts to regulate PvP behavior and provide pathways for redemption.

---

## How Murder Counts Work

### Important: Reporting is Required

**Murder counts are NOT automatic.** When you kill another player, the victim receives a gump (dialog box) asking if they want to report you as a murderer. **Only if they choose to report you** will you receive murder counts.

- The gump appears **4 seconds** after death
- Victims can choose **"Yes"** (report) or **"No"** (don't report)
- If multiple players killed the victim, they can choose to report each one individually
- **Exception**: Members of the Thieves Guild cannot report murders (guards won't take reports of a thief's death)
- Once someone reports you, they cannot report you again for the same incident for **5 minutes**

When you ARE reported, you receive **two types** of murder counts:

### 1. Short-Term Murders

- **Duration**: Decays over time based on your total count
  - **Under 5 murders**: Each count decays after **16 hours** of in-game play time
  - **5 or more murders**: Each count decays after **24 hours** of in-game play time
- **Purpose**: Tracks recent PK activity and determines eligibility for stat loss
- **Decay**: Only decays while you're **logged in** (based on game time, not real time)

### 2. Long-Term Murders (Kills)

- **Duration**: Decays over time based on your total count
  - **Under 5 long-term kills**: Each count decays after **48 hours** of in-game play time
  - **5 or more long-term kills**: **Does not decay** — requires a Forged Pardon to clear
- **Purpose**: Your permanent murder record
- **Visibility**: This is your "Kills" count that determined if you're red

---

## Murder Count Decay System

### Key Points

- Murder counts **only decay while you are online**
- Counts decay **one at a time** as their timers expire
- When you log out, your decay progress is saved
- When you log back in, the system resumes tracking from where it left off

### Decay Timeline Examples:

**Example 1: Player with 3 short-term murders**

- Each murder will decay after 16 hours (under 5)
- Total time to clear all 3: **48 hours** of being logged in

**Example 2: Player with 6 short-term murders**

- First 2 murders decay at 24 hours each (while at 6 and 5)
- Remaining 4 murders decay at 16 hours each (while below 5)
- Total time to clear all 6: **(2 × 24) + (4 × 16) = 112 hours** of being logged in

**Example 3: Player with 10 short-term murders**

- First 6 murders decay at 24 hours each (from 10 down to 4)
- Remaining 4 murders decay at 16 hours each (below 5)
- Total time to clear all 10: **(6 × 24) + (4 × 16) = 208 hours** of being logged in

---

## Stat and Skill Loss on Resurrection

### Overview

If you have **5 or more short-term murders** when you die, you will suffer **stat and skill loss** upon resurrection. This penalty is **severe** and increases with the number of murders you have accumulated.

### How the Penalty Works

When you resurrect with 5+ short-term murders:

1. **Your stats (STR, INT, DEX) are reduced**
2. **Your skills are reduced**
3. **Your short-term murder count is reset to 0** (the penalty "pays off" your short-term murders)
4. You receive a message showing the exact percentage of loss

### Loss Calculation

The percentage of stat/skill loss is calculated as follows:

| Short-Term Murders | Loss Percentage | You Keep |
| ------------------ | --------------- | -------- |
| **5**              | 15.0%           | 85%      |
| **6**              | 15.5%           | 84.5%    |
| **7**              | 16.0%           | 84%      |
| **8**              | 16.5%           | 83.5%    |
| **9**              | 17.0%           | 83%      |
| **10**             | 17.5%           | 82.5%    |
| **15**             | 20.0%           | 80%      |
| **20**             | 22.5%           | 77.5%    |
| **25+**            | 25.0% (max)     | 75%      |

**Formula**: Base 15% + 0.5% per murder above 5 (capped at 25% loss)

### What Gets Reduced

#### Stats (STR, INT, DEX)

- Each stat is multiplied by the retention percentage (what you keep)
- **Minimum floor**: Stats won't drop below 10
- Example: With 100 STR and 10 murders (17.5% loss), you'd have ~83 STR after resurrection

#### Skills

- Each skill is multiplied by the retention percentage
- **Minimum floor**: Skills won't drop below 35.0
- Example: With 100.0 Swordsmanship and 10 murders (17.5% loss), you'd have ~82.5 Swordsmanship

### Important Notes

⚠️ **This penalty is severe!**

- At 5 murders, you lose **15% of all stats and skills**
- At 10 murders, you lose **17.5% of all stats and skills**
- At 25+ murders, you lose **25% of all stats and skills** (maximum penalty)

💡 **The penalty clears your short-term murders**

- After resurrection, your short-term murder count is reset to 0
- This means you "pay off" your murders with the stat/skill loss
- Your long-term murders (kills) remain unchanged

🎯 **Avoiding the Penalty**

1. **Stay below 5 short-term murders** - No penalty at 4 or fewer
2. **Use a Forged Pardon** - Resets both murder types without penalty
3. **Wait for decay** - Let murders decay below 5 before dying
4. **Don't die** - The penalty only applies on resurrection

### Strategic Considerations

**When to Take the Penalty:**

- If you have 5-20 murders and can't afford a pardon
- If you need to clear murders quickly to avoid the 20+ lockout for pardons
- If you're confident you can regain stats/skills through training

**When to Avoid the Penalty:**

- Use a Forged Pardon if you can afford it (no stat/skill loss)
- Stay alive and let murders decay naturally if possible
- Keep murders below 5 if you engage in risky PvP

---

## Dungeon Death Penalty

If you have **5 or more short-term murders** and die inside a dungeon, you are subject to a **dungeon re-entry lockout**:

- **Lockout duration:** 5 minutes before you can re-enter the dungeon
- This applies only to dungeon deaths — dying in the overworld is unaffected

---

## The Corrupt Judge & Pardons

### Finding the Judge

**Dryden the Judge** has long since abandoned any pretense of impartiality. Rumor places him at **The Pirate's Blunder** in **Buc's Den** — a man who asks no questions, provided the coin is right. The nobles of Magincia have been pushing the courts to root out this corruption, and Dryden's prices have risen accordingly.

### How to Request a Pardon

1. Find Dryden the Judge at The Pirate's Blunder in Buc's Den
2. Say: **"I request a pardon"**
3. If eligible, the Judge will provide you with a **Forged Pardon**

### Eligibility Requirements

You can request a pardon if you meet **ALL** of the following criteria:

| Requirement          | Details                                               |
| -------------------- | ----------------------------------------------------- |
| **Minimum Murders**  | Must have at least **1** long-term murder (kill)      |
| **Maximum Murders**  | Must have **20 or fewer** short-term murders          |
| **Previous Pardons** | Can only receive **3 pardons maximum** from the Judge |
| **Sufficient Gold**  | Must have enough gold in your bank                    |

### Pardon Pricing

The cost doubles with each pardon you purchase:

| Pardon Number  | Cost         |
| -------------- | ------------ |
| **1st Pardon** | 150,000 gold |
| **2nd Pardon** | 300,000 gold |
| **3rd Pardon** | 600,000 gold |

**Note**: Gold is automatically withdrawn from your bank account.

---

## Using a Forged Pardon

Once you receive a **Forged Pardon**:

1. The pardon is **blessed** — it will not be lost on death
2. It is **bound to you** — only you can use it
3. Keep it in your **backpack**

**There are two ways the pardon is consumed:**

**On death (automatic):** If you die and resurrect with the pardon in your backpack, it is consumed automatically. Stat and skill loss is avoided, and both your short-term and long-term murder counts are reset to 0.

**While alive (manual):** Double-click the pardon at any time to consume it and receive the same benefit — counts cleared, no penalty.

Upon use you receive a message: _"Redemption is granted. Your sins are now but shadows of the past."_

---

## Important Notes

### ⚠️ Things to Remember:

- **Murder counts only decay while online** - Logging out pauses all decay timers
- **You can only get 3 pardons total** - Choose when to use the Judge's services wisely
- **Pardons get expensive fast** - 150k, 300k, then 600k; plan accordingly
- **21+ murders locks you out** - If you accumulate more than 20 short-term murders, the Judge will not help you
- **Pardons auto-trigger on resurrection** - A pardon in your backpack is consumed automatically if you would suffer stat loss
- **Pardons are character-bound** - You cannot trade or give them to other players
- **The Judge keeps records** - He tracks how many pardons you've purchased

### 💡 Strategy Tips:

1. **Not all kills become counts** - Remember, victims must report you, so diplomacy matters
2. **Monitor your murder count** - Don't let it exceed 20 if you want the option to buy a pardon
3. **Carry the pardon** - Once purchased, keep it in your pack so it auto-triggers if you die
4. **Let murders decay naturally if possible** - Save gold by waiting, but this requires long play sessions
5. **Plan your PvP carefully** - Each kill has consequences that last many hours
6. **Thieves Guild members can't report** - They're criminals themselves, so guards won't take their reports

---

## Summary

The murder system is designed to:

- **Track** player killing behavior accurately through reportable murder counts
- **Punish** excessive PKing through severe stat/skill loss on resurrection (5+ murders)
- **Discourage** long-term murderous behavior through time-based decay consequences
- **Provide** a redemption path through the Corrupt Judge for those willing to pay
- **Balance** risk vs. reward for those who choose the darker path

Whether you're a noble hero or a notorious villain, understanding this system will help you navigate the consequences of your actions in the world.

_Remember: With great power comes great responsibility... or at least, great expense and stat loss._
