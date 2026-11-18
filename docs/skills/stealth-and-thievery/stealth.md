---
description: "Stealth on New Dawn: move while hidden, the 80 Hiding requirement, steps per use, Auto Restealth and hide-and-stealth at GM, armor, and training."
---

![Stealth](../../assets/flags/flag-stealth.png){ align=right }

# Stealth

## Overview

Stealth allows you to move while hidden, staying invisible to others. Essential complement to Hiding skill, enabling mobile stealth gameplay for scouts, thieves, and assassins.

## How it works

You will need at least 80 Hiding or you won't be able to use Stealth.

First you need to be hidden, then use Stealth. If it succeeds you can take a certain number of steps while staying invisible. Running or failing reveals you.

A system message counts down your steps: "You have 7 stealth steps remaining." Taking a step with none left reveals you.

So for example you could Hide, use Stealth, take some steps, use Stealth again to reset the steps and keep moving. Stealth has a 10 second delay, so you may need to stop and wait before you can use it again.

Past 80 Stealth you can skip the Hide step and have Stealth renew itself. See [At GM](#at-gm) below.

Stepping on someone else will also reveal you.

You can't use Stealth while riding a mount.

The armor you wear makes stealth harder. See [Armor](#armor) below.

When stealthing around others there is a chance of being detected. A check is made by comparing your Stealth and DEX against the Detecting Hidden and INT of players around you.

## Steps

This table shows how many steps you can take before using Stealth again based on your skill level.

| Skill | Steps |
|-------|-------|
| 10    | 1     |
| 20    | 2     |
| 30    | 3     |
| 40    | 4     |
| 50    | 5     |
| 60    | 6     |
| 70    | 7     |
| 80    | 8     |
| 90    | 9     |
| 100   | 10    |

## At GM

Two extra tricks open up once your Stealth is **above 80**. They are what make a GM stealther different.

### Hide and stealth in one go

With **GM Hiding** and Stealth above 80, you can use Stealth while you're still visible. It hides you first, then starts stealthing: "You vanish into the shadows undetected."

The normal rules still apply. You can't do it in combat, and if the hide or the stealth check fails you stay visible.

### Auto Restealth

With Stealth above 80, click your character and pick **Enable Auto Restealth** from the context menu. When you run out of steps, Stealth is used for you automatically instead of revealing you: "You continue to move silently through the shadows." Pick **Disable Auto Restealth** to turn it off.

It only works if the 10 second delay is over. Walking 10 steps takes about 4 seconds, so if you walk without stopping you'll still be revealed. Pause for a few seconds before your last step and the restealth goes through. Using any other skill in the meantime also resets the delay.

A failed restealth check reveals you, same as a failed Stealth.

The option turns itself off when the server restarts, so turn it back on after a restart.

### Your chance at GM

At GM you get 10 steps per use. Whether the Stealth check succeeds depends only on your [armor](#armor):

| Armor total | Chance at GM |
|:-----------:|:------------:|
| 0 to 20     | 100%         |
| 24          | 90%          |
| 25          | 88%          |
| 30          | 75%          |
| 35          | 63%          |
| 40          | 50%          |
| 41          | 48%          |
| 42 or more  | Not possible |

## Armor

Only the **type** of armor and the **slot** it's in matter. Quality, color, resource and magic level don't, so better armor never makes you worse at sneaking.

### The short version

- **Free:** leather of any kind, clothing, jewelry and **shields**
- **Fine:** a full suit of studded leather
- **Limited:** metal and bone. **A metal chest plus metal legs is the most you can wear.** Anything else on top, apart from leather, is too much

### The numbers

Metal and bone armor costs the same in every material: plate, dragon, chainmail, ringmail and bone.

| Slot          | Metal or bone | Studded |
|---------------|:-------------:|:-------:|
| Chest         | 25            | 10      |
| Legs          | 15            | 6       |
| Helm          | 10            | -       |
| Arms          | 10            | 4       |
| Gloves        | 5             | 2       |
| Gorget        | 5             | 2       |
| **Full suit** | **70**        | **24**  |

Add up what you're wearing:

- **Under 42:** you can stealth. Every point makes the check a little harder, but at GM Stealth a total of 20 or less never fails
- **42 or more:** "You could not hope to move quietly wearing this much armor."

Some examples:

| Outfit                                  | Total | Stealth?    | Chance at GM |
|-----------------------------------------|:-----:|:-----------:|:------------:|
| Full leather + shield                   | 0     | Always      | 100%         |
| Full studded                            | 24    | Yes         | 90%          |
| Plate chest, rest leather               | 25    | Yes         | 88%          |
| Plate helm, arms, gloves and gorget     | 30    | Yes         | 75%          |
| Plate chest and legs, rest leather      | 40    | Yes, barely | 50%          |
| Plate chest and legs + studded gloves   | 42    | No          | -            |
| Any full suit of metal or bone          | 50+   | No          | -            |

## Training

Train from Thief NPCs to reach around 50.

Stealth can be used on a 10 seconds cooldown. Keep using Stealth while hidden until you reach 100.

Past 60 you need some [armor](#armor) on, because the check gets too easy to give gains:

| Your Stealth | Wear at least | Easy way to get it                  |
|--------------|:-------------:|-------------------------------------|
| up to 60     | nothing       | Leather is fine                     |
| 60 to 80     | 10            | A metal helm, or a studded chest    |
| 80 to 100    | 20            | A metal chest                       |

**A metal chest over leather works from 60 all the way to GM.**

While training this skill you can also gain Dexterity (primary) and Intelligence (secondary). Visit the [stats](../../game-mechanics/character/stats.md) page to learn more.

## Related skills

- [Hiding](hiding.md)
- [Detecting Hidden](detecting-hidden.md)
