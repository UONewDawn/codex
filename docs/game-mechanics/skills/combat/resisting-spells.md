![Resisting Spells](../../../assets/Flag_resisting_spells.gif){ align=right }

# Resisting Spells

## Overview

Resisting Spells gives you a chance to reduce the damage taken from harmful spells and shortens the duration of debuffs.

If resisted, Mana Drain and Mana Vampire will have no affect.

## Resisting chance

Debuff spells are always shortened in duration and do not check the chance to resist.

The chance of resisting a harmful spell depends on your Resist skill, the attacker Magery skill, and the Spell Circle they cast.

This is the formula used in the calculation, both formulas are checked and the higher result is used:

`Resisting Spells / 5`

This ensures there is always a minimum chance to resist.

For example, with 30 Resisting Spells you will always have at least a 6% chance to resist any spell.

`Resisting Spells − (Attacker Magery − 20) / 5 + (Spell Circle * 5)`

This ensures that a Magic arrow is easier to resist than a Flamestrike.

For example, if you have 100 Resist and the attacker has 100 Magery and hes casting a 8th circle spell, you will have a 44% chance to resist.

If you successfully resist a spell, the damage is reduced by 50%.

## Damage calculation

The damage calculation is:

`(Base Spell Damage - 50% [if Resisted]) + Eval Intelligence Damage Modifier`

- First, the resist chance is applied, if you resist the spell, the base damage is reduced by 50%.

- Next, the Eval Int modifier is applied, if the attacker has no Eval Int, it reduces the damage by an additional 50%.

This means Resisting Spells also provides a passive damage reduction against attackers with no Eval Int, even if the spell is not resisted.

## Eval Int Damage Modifier

If your Resist is higher than your attacker Eval Int, then the calculation is:

`(1 + (Attacker Eval Int - Your Resist) / 200 )`

If your Resist is lower than your attacker Eval Int, then the calculation is:

`(1 + (Attacker Eval Int - Your Resist) / 500 )`

If you have 100 Resist and the attacker has 100 Eval Int, they will have no benefits from Eval Int.

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
