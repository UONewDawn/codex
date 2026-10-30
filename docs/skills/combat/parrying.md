---
description: "Parrying on New Dawn: block attacks with a shield, parry chance by skill, Riposte, Shield Bash, fire breath protection, and how to train it."
---

![Parrying](../../assets/flags/flag-parrying.png){ align=right }

# Parrying

## Overview

Parrying is a defensive skill that gives you a chance to absorb damage with your shield.

Starting items if you choose this skill in character creation: Wooden Shield.

## How it works

If you are wearing a shield, each time you get hit, you have a chance to parry the attack and absorb some of the damage.

The chance is calculated by dividing your Parrying skill by 2, if you have 100 Parrying you will have a 50% chance to parry.

The amount of damage reduction depends on the shield's Armor Rating and your Parrying skill. At 100 Parrying a shield counts as half its listed rating plus 1, and less at lower skill.

A parried melee attack loses half of that, while a parried arrow or bolt loses all of it. For example, at 100 Parrying a heater shield (23) takes 6 off a melee hit and 12 off an arrow, before the hit is halved.

In player-vs-player fights, your shield and armor together can stop at most 75% of a hit. See [Armor in PvP](../../game-mechanics/items-and-equipment/armor.md#armor-in-pvp).

Keep in mind that as your shield becomes damaged over time, its AR will gradually decrease as well, down to half when it's almost broken.

This table shows the Armor Rating for each shield type.

<!-- Tear kite shield needs to be added -->

=== "Normal"

    |                           Shield Type                           | AR  |  Item HP  |
    |:---------------------------------------------------------------:|:---:|:---------:|
    |    ![icon](../../assets/items/buckler-shield.png)<br>Buckler    |  8  |  40 - 50  |
    |     ![icon](../../assets/items/wooden-shield.png)<br>Wooden     |  8  |  20 - 25  |
    |     ![icon](../../assets/items/bronze-shield.png)<br>Bronze     |  10 |  25 - 30  |
    |      ![icon](../../assets/items/metal-shield.png)<br>Metal      |  11 |  50 - 65  |
    | ![icon](../../assets/items/metal-kite-shield.png)<br>Metal Kite |  16 |  45 - 60  |
    |     ![icon](../../assets/items/heater-shield.png)<br>Heater     |  23 |  50 - 65  |
    |      ![icon](../../assets/items/order-shield.png)<br>Order      |  30 | 100 - 125 |
    |      ![icon](../../assets/items/chaos-shield.png)<br>Chaos      |  32 | 100 - 125 |

=== "GM Made"

    |                           Shield Type                           | AR  |  Item HP  |
    |:---------------------------------------------------------------:|:---:|:---------:|
    |    ![icon](../../assets/items/buckler-shield.png)<br>Buckler    |  16 |  48 - 60  |
    |     ![icon](../../assets/items/bronze-shield.png)<br>Bronze     |  18 |  30 - 36  |
    |      ![icon](../../assets/items/metal-shield.png)<br>Metal      |  19 |  60 - 78  |
    | ![icon](../../assets/items/metal-kite-shield.png)<br>Metal Kite |  24 |  54 - 72  |
    |     ![icon](../../assets/items/heater-shield.png)<br>Heater     |  31 |  60 - 78  |

=== "Defense"

    |                           Shield Type                           | AR  |  Item HP  |
    |:---------------------------------------------------------------:|:---:|:---------:|
    |    ![icon](../../assets/items/buckler-shield.png)<br>Buckler    |  23 |  40 - 50  |
    |     ![icon](../../assets/items/wooden-shield.png)<br>Wooden     |  23 |  20 - 25  |
    | ![icon](../../assets/items/metal-kite-shield.png)<br>Metal Kite |  31 |  45 - 60  |

=== "Guarding"

    |                           Shield Type                           | AR  |  Item HP  |
    |:---------------------------------------------------------------:|:---:|:---------:|
    |    ![icon](../../assets/items/buckler-shield.png)<br>Buckler    |  28 |  40 - 50  |
    |     ![icon](../../assets/items/wooden-shield.png)<br>Wooden     |  28 |  20 - 25  |
    | ![icon](../../assets/items/metal-kite-shield.png)<br>Metal Kite |  36 |  45 - 60  |

=== "Hardening"

    |                           Shield Type                           | AR  |  Item HP  |
    |:---------------------------------------------------------------:|:---:|:---------:|
    |    ![icon](../../assets/items/buckler-shield.png)<br>Buckler    |  33 |  40 - 50  |
    |     ![icon](../../assets/items/wooden-shield.png)<br>Wooden     |  33 |  20 - 25  |
    | ![icon](../../assets/items/metal-kite-shield.png)<br>Metal Kite |  41 |  45 - 60  |

=== "Fortification"

    |                           Shield Type                           | AR  |  Item HP  |
    |:---------------------------------------------------------------:|:---:|:---------:|
    |    ![icon](../../assets/items/buckler-shield.png)<br>Buckler    |  38 |  40 - 50  |
    |     ![icon](../../assets/items/wooden-shield.png)<br>Wooden     |  38 |  20 - 25  |
    | ![icon](../../assets/items/metal-kite-shield.png)<br>Metal Kite |  46 |  45 - 60  |

=== "Invulnerability"

    |                           Shield Type                           | AR  |  Item HP  |
    |:---------------------------------------------------------------:|:---:|:---------:|
    |    ![icon](../../assets/items/buckler-shield.png)<br>Buckler    |  43 |  40 - 50  |
    |     ![icon](../../assets/items/wooden-shield.png)<br>Wooden     |  43 |  20 - 25  |
    | ![icon](../../assets/items/metal-kite-shield.png)<br>Metal Kite |  51 |  45 - 60  |

### Fire breath

If you have at least 50 Parrying and a shield equipped, your shield also soaks part of a dragon's fire breath. At GM Parrying it takes 40% off the top, and a sturdier, exceptional or magic shield takes off a little more.

This works on its own; Shield Bash doesn't need to be ready.

## Riposte

Every shield fighter gets Riposte. When you parry an attack, even an arrow, your next melee hit on that same attacker within 3 seconds does extra damage. Hitting anyone else doesn't use it up. A spark on your target shows when it lands.

The bonus grows with your Parrying skill:

| Parrying | Against monsters | Against players |
| :------: | :--------------: | :-------------: |
|    50    |       +7%        |       +5%       |
|   100    |       +15%       |      +10%       |

## Shield Bash

Shield Bash is a counter. While it's ready, parrying a melee attack can let you slam your shield into the attacker.

It requires at least 80 Parrying and 80 Anatomy.

Double-click your equipped shield or type **[bash** to ready it, and do the same again to lower it. A buff icon shows while it's ready. It stays ready after a bash, and taking your shield off lowers it.

You can't have Shield Bash and stun ready at the same time. Readying one lowers the other.

### When it goes off

Only when you parry a melee attack. Arrows and bolts never set it off.

Each parry has a chance to bash equal to (Parrying + Anatomy) / 4 percent: 40% at 80/80 and 50% at 100/100. A bash costs stamina, and if it misses you can't try again for 3 seconds.

### What it does

A shield bash throws off your attacker's next swing, breaks any spell they're casting, and stops them from walking or starting a new spell for a moment. They can still fight back, drink potions and bandage.

It hits harder against monsters than against players:

|                                  | Monsters and pets |   Players   |
| :------------------------------: | :---------------: | :---------: |
|           Spell broken           |        Yes        |     Yes     |
|   Can't walk or start a spell    |     3 seconds     | 1.5 seconds |
| Can't be shield bashed again for |     8 seconds     | 12 seconds  |

A player or boss who was just pinned, by a shield bash or an archer's snare, can't be pinned again until 8 seconds after they're free. A bash on them during that time still throws off their swing and breaks their spell.

### Shield size

Heavier shields bash harder, but cost more stamina and take longer to recover.

|                           Shield Type                           | Stamina | Recovery | Next swing delayed (monsters) | Next swing delayed (players) |
| :-------------------------------------------------------------: | :-----: | :------: | :---------------------------: | :--------------------------: |
|    ![icon](../../assets/items/buckler-shield.png)<br>Buckler    |   10    |    8s    |             1.25s             |            0.75s             |
|     ![icon](../../assets/items/wooden-shield.png)<br>Wooden     |   10    |    8s    |             1.25s             |            0.75s             |
| ![icon](../../assets/items/metal-kite-shield.png)<br>Metal Kite |   13    |   10s    |             1.7s              |             1.0s             |
|     ![icon](../../assets/items/heater-shield.png)<br>Heater     |   16    |  11.75s  |             2.0s              |             1.2s             |
|      ![icon](../../assets/items/order-shield.png)<br>Order      |   19    |  13.5s   |             2.4s              |             1.4s             |
|      ![icon](../../assets/items/chaos-shield.png)<br>Chaos      |   20    |   14s    |             2.5s              |             1.5s             |

Bronze, Metal and Wooden Kite shields sit between the Buckler and the Metal Kite.

Recovery is how long you wait after a bash before your shield can bash again.

## Training

Parrying is hard to train because you will only gain when taking damage, it works best if trained while having a low combat skill as you get hit more often.

Gain is based on base damage before armor reduction, getting hit by multiple monsters increases gain speed.

While training this skill you can also gain Strength (primary) and Dexterity (secondary). Visit the [stats](../../game-mechanics/character/stats.md) page to learn more.

## Related skills

- [Swordsmanship](swordsmanship.md)
- [Mace Fighting](mace-fighting.md)
- [Fencing](fencing.md)
- [Anatomy](anatomy.md)
