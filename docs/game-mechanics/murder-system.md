# Player Murder System

The murder system tracks player kills and applies consequences for those who engage in player killing (PKing). This system uses both **short-term** and **long-term** murder counts to regulate PvP behavior and provide pathways for redemption.

## Murder Counts

When you kill another player, the victim receives a gump asking if they want to report you as a murderer. Only if they choose to report you will you receive murder counts.

- When a player reports you for a kill, you receive both a short‑term and a long‑term murder count simultaneously.
- Once someone reports you, they cannot report you again for 5 minutes.
- Members of the Thieves Guild cannot report murders.
- Killing a member of your own party doesn't give a murder count, and attacking one doesn't flag you as a criminal. See the [Parties](parties.md) page.

## Counts Decay

Murder counts decay one at a time, and the length of the decay timer depends on how many counts you currently have. The timer only progresses while you're logged in. Logging out pauses it, and when you return, the decay resumes exactly from where it stopped.

### Short term

- Short-term kills under 5, will decay every 16 hours.
- Short-term kills equal or over 5, will decay every 24 hours.

### Long term

Long term murder counts only decay while you have less than five. Once you reach five or more, they won't decay anymore, and the only way to remove those counts is by using Forged Pardons.

- Long-term kills under 5, will decay every 24 hours.
- Long-term kills equal or over 5, won't decay anymore.

## The Corrupt Judge & Pardons

![image](../assets/screenshots/dryden-npc.png){ .center-img }

Dryden the Judge has long since abandoned any pretense of impartiality. Rumor places him at The Pirate's Blunder in Buc's Den. A man who asks no questions, provided the coin is right. The nobles of Magincia have been pushing the courts to root out this corruption, and Dryden's prices have risen accordingly.

### Forged Pardon request

Once you found Dryden the Judge, say `I request a pardon` to receive one.

#### Requirements

You can request a pardon if you meet **ALL** of the following criteria:

| Requirement          | Details                                               |
|----------------------|-------------------------------------------------------|
| **Minimum Murders**  | Must have at least **1** long-term murder (kill)      |
| **Maximum Murders**  | Must have **20 or fewer** short-term murders          |
| **Previous Pardons** | Can only receive **3 pardons maximum** from the Judge |
| **Sufficient Gold**  | Must have enough gold in your bank                    |

**Note**: Gold is automatically withdrawn from your bank account.

#### Pricing

The cost doubles with each pardon you purchase:

| Pardon Number  | Cost         |
|----------------|--------------|
| **1st Pardon** | 150.000 gold |
| **2nd Pardon** | 300.000 gold |
| **3rd Pardon** | 600.000 gold |

### Using a Forged Pardon

Once you receive a **Forged Pardon**:

1. The pardon is **blessed** - it will not be lost on death
2. It is **bound to you** - only you can use it
3. Keep it in your **backpack**

**There are two ways the pardon is consumed:**

**On death (automatic):** If you die and resurrect with the pardon in your backpack, it is consumed automatically. Stat and skill loss is avoided, and both your short-term and long-term murder counts are reset to 0.

**While alive (manual):** Double-click the pardon at any time to consume it and receive the same benefit: counts cleared, no penalty.

Upon use you receive a message: _"Redemption is granted. Your sins are now but shadows of the past."_

## Stat and Skill Loss on Resurrection

If you have five or more short‑term murder counts when you die, you'll suffer stat and skill loss upon resurrection.

!!! Note
    Your short‑term murder count is also reset to zero - but only when you die with five or more short‑term counts.

### Loss Calculation

The percentage of stat/skill loss is calculated as follows:

| Short-Term Murders | Loss Percentage | You Keep |
|--------------------|-----------------|----------|
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

- Stats won't drop below 10
- Skills won't drop below 35.0

## Dungeon Death Penalty

If you have five or more short‑term murder counts when you die inside a dungeon, you'll be locked out of all dungeons for five minutes.
