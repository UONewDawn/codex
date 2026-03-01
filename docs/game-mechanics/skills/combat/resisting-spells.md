![Resisting Spells](../../../assets/Flag_resisting_spells.gif){ align=right }

# Resisting Spells

## Overview

Resisting Spells gives you a chance to reduce the damage taken from harmful spells and shortens the duration of debuffs.

<!-- Not sure if Mana Drain and Mana Vampire have a chance of not having affect at all -->

## Resisting chance

Debuff spells are always shortened in duration and do not check the chance to resist.

The chance of resisting a harmful spell depends on your Resisting Spells skill, the attacker Magery skill, and the Spell Circle they cast.

This is the formula used in the calculation, both formulas are checked and the higher result is used:

`Resisting Spells / 5`

This ensures there is always a minimum chance to resist.

For example, with 30 Resisting Spells you will always have at least a 6% chance to resist any spell.

`Resisting Spells − [ (Attacker Magery − 20) / 5 + (Spell Circle * 5) ]`

This ensures that a Magic arrow is easier to resist than a Flamestrike.

For example, if you have 100 Resisting Spells and the attacker has 100 Magery and hes casting a 8 circle spell, you will have a 44% chance so resist.

If you successfully resist a spell, the damage is cut in half.

## Training

You can train Resisting Spells, Magery, Meditation and Healing at the same time.

It's recommended to keep low Evaluating Intelligence as it will increase your spell damage and make training more difficult.

| Skill    | Cast on yourself |
|----------|------------------|
| 0 - 30   | Train from NPCs  |
| 30 - 55  | Fireball         |
| 55 - 60  | Lighting         |
| 60 - 82  | Energy Bolt      |
| 82 - 100 | Flamestrike      |

## Related skills

- [Magery](../magic/magery.md)
