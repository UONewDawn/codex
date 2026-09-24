# Arcane Lantern

An Arcane Lantern is a lockable house item that stores wand charges. Drop wands into it and the lantern keeps a bank of charges **for each spell**. Later you can draw out a fresh, fully charged wand.

<!-- TODO: screenshot of the lantern in a house -->
<!-- TODO: screenshot of the Arcane Lantern gump -->

## Getting an Arcane Lantern

Arcane Lanterns are crafted with **Tinkering**.

| Skill              | Materials                                             |
| ------------------ | ----------------------------------------------------- |
| 75 – 125 Tinkering | 5 Valorite Ingots, 2 Blue Diamonds, 5 Codex Fragments |

## Setting It Up

1. Place the lantern in your house and **lock it down**.
2. The house owner or a co-owner uses it first and becomes the **lantern owner**.
3. The lantern owner can set **Access** from the context menu:

| Setting | Who can use it                                       |
| ------- | ---------------------------------------------------- |
| Private | The house owner, co-owners and friends (the default) |
| Public  | Anyone                                               |

You must be within **2 tiles** of the lantern to use it. Picking a lantern back up clears its owner, but the lantern **keeps its stored wands and charges**.

## Supported Wands

| Spell          | Max charges per redeemed wand |
| -------------- | ----------------------------- |
| Magic Arrow    | 30                            |
| Harm           | 30                            |
| Fireball       | 15                            |
| Lightning      | 20                            |
| Heal           | 25                            |
| Greater Heal   | 5                             |
| Clumsy         | 30                            |
| Feeblemind     | 30                            |
| Weaken         | 30                            |
| Mana Drain     | 30                            |
| Identification | 175                           |

## Depositing Wands

- **Drop a single wand** on the lantern, or
- **Drop a container** of wands. The lantern takes every wand it can use from the top level of the container and gives the container back to you with anything it refused.

Wands must be **identified**. Unidentified wands are refused.

Each spell has its own bank. Fireball charges can only come back out as a Fireball wand.

!!! warning "The infusion isn't free"
    Absorbing a wand costs something:

        - **Charge burn:** each wand loses a random amount of its charges, from 0 up to **20%** (about 10% on average). For example, a 30-charge wand loses between 0 and 6 charges.
        - **Shattering:** each wand has a **10%** chance to shatter. Its charges are still saved, but it doesn't add a **wand** to the lantern (see below).

        The lantern tells you how many charges were absorbed, burned, or lost.

## Redeeming Wands

The lantern tracks two numbers per spell: **Wands** and **Charges**. Redeeming a wand uses **one wand** and up to that spell's **max charges** (see the table above), and gives you a new, identified wand.

For example, if you have 3 Fireball wands and 100 Fireball charges banked, you can draw out three 15-charge Fireball wands. The remaining 55 charges wait until you deposit another Fireball wand.

That's why shattering matters: a shattered wand saves its charges but adds no wand, so you need more wands to get those charges back out.

## Limits

- Up to **100,000 wands** and **100,000 charges** per spell, per lantern.
- If a spell's charge bank is full, charged wands for that spell are refused, not destroyed.
