# SERVER PATCH 1.7

## March 11th, 2026

This patch addresses some mechanics used to breach security and makes other adjustments to the game.

## 🛠️ Bug Fixes & Adjustments

- Rare horse breeds now require higher taming skills, with the rarest breeds requiring 90.1 (and their even rarer counterparts requiring 95.1)
- If you don't have animal taming, you can still tame a regular horse, but other horse types now require taming
- Plant bowls only require 5 fertile dirt
- Many of the plant hues have seen a hue adjustment to fit more with the feel of the server
- You can now click "Make #" and enter a number to craft from the crafting menu
- Bear and Deer masks can be crafted by tailors. Ferocious bears and graceful hinds carry some of the materials needed
- Adjusted decay rates on brigand, orc, and rat camps
- Pets will now fallback to the previous command (follow/stay/guard) after combat
- Fixed the issue with not accessing vendor bags unless on the steps (sorry folks!)
- Fixed issue with crafters mark not keeping after a server restart
- Bowyer, Miner, and Rangers now in the correct guilds
- The person you're attempting to resurrect must be on the same Z as you
- Additional checks on various res methods have been implemented as safeguards
- You must maintain LOS on a target you're using bandages on
- Fixed the ban position on the Manor house
- If your account is 7 days old or less, you will get a popup about the Young Player Program, outlining what it does and why you should join (sorry to the lost souls who were roaming the ruins of Britain naked and confused)
- Stacked sheep no longer produce wool
- Adjusted the dirt drop rates on boars, bullfrogs, and earth elementals
- Fixed issue with some east facing small houses having the wrong region shape

!!! tip "Dev Note"
    This always applied in houses, where stacked sheep in houses wouldn't produce wool. This has just been expanded to cover stacked sheep in any location.

- Dueling no longer uses your potions or bandages
- Disabled the "I wish to duel" command, please use the Dawn dueling pits and boards
- The 90 minute timer on pirate maps has been reduced to 60

## 🎯Fletching Change

To incentivize player-crafted items, adjustments have been made to make crafting arrows more worthwhile. Previously, it was cheaper to simply buy arrows from an NPC vendor, while crafting them was actually the most expensive option.

Arrows and bolts are now 5gp from NPC vendors. Shaft cost from NPC vendors has been reduced from 3gp to 2gp. Each board/log can be crafted into 6 shafts (instead of 1), and the price of the Pirate Smuggler has increased from 2,000gp to 3,000gp.

This results in the following cost-per-arrow breakdown, from most to least expensive:

- Pirate Smuggler — 6gp per arrow
- NPC Vendor — 5gp per arrow
- Buy materials & craft — 4gp per arrow (2gp shaft + 2gp feather)
- Craft from board/log — ~2.5gp per arrow (3gp board yields 6 shafts + 2gp feather)

## 📖Bulk Order Deeds

Each bulk order book now has a unique ID that can be easily copied. That ID can be used to programmatically look up information about the book and all BODs within it.

The Portal has been updated to expose this data via API for those who request a token.

Also, vendors no longer require you to sell to them in order to receive a BOD. Instead, you can use the context menu (single-click) to check your status and claim one if available.

### 🔨Carpentry Bulk Order Deeds

<div class="rpg-scroll" markdown="1">
Hear ye, hear ye!

By royal decree, the Carpenters' Guild doth now issue Bulk Order Deeds to all skilled craftsmen who seek their favor. Seek out thy local carpenter, prove thy worth, and take up the mantle of master woodworker. Glory and reward await those whose hands are steady and whose timber is true.
<span class="rpg-signature">Issued by the Carpenters' Guild</span>
</div>
