# SERVER PATCH 0.14

**May 29, 2023**

- Fixed issue with provoing mobs outside of the range perception (where it would say they look furious, but then go after you)
- Blocked being able to open house doors from outside a house
- Added 2 second cooldowns on all potions except explosion (no cooldown) and heal (maintains the 10 second cooldown)
- Changed wandering healer logic
- Adjustment to the amount of damage dealt after its calculated (looking for feedback on this)
- Removed alchemy bonus from explosion potions.

Instead, the bonus is applied to the min damage. For example, at GM alchemy, it used to add +10 damage to calculated damage, with a chance to hit at max explosion 30 + 10 = 40 dmg. Now, at GM alchemy, the min/max roll is between 25 and 30, meaning your explosion at GM alchemy will at least do a min of 25 damage instead of 15.

- Adjusted the speed of the katana to be faster after last patch
- Fixed text type on a player corpse. Mobs corpses don't have a chance to be red.
- Dragon scales no longer drop (this will be upgraded in the future for a very low chance and with scaled dragon armor)
- The server will no longer auto-unequip your hands to cast, instead will give you a message saying you need to clear hands (this will be updated to exclude cosmetic items like lanterns, torches, etc)
