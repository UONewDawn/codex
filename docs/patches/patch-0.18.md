# SERVER PATCH 0.18

**July 8, 2023**

- Fixed chain lightning to chain when its two targets, also has a chance to resist
- Fixed some of the names of creatures spawned with spirit speak
- Adjustment to some of the casting times on summoning
- Summoned creatures with mage AI (daemon) won't cast invisibility on themselves
- Dispel and mass dispel have an 80% chance at GM spirit speak to be resisted by a mob that casts the spell. Player dispel continues to have a 50% chance to resist.
- Mobs that auto-dispel and bypass casting (ie: dragons) with a 100% chance when giving or getting melee damage, will have that chance reduced based on the spirit speak skill of the summoner
- Summoned spirit daemons have been toned down a bit
- Increased the min. magery skill required to cast a spell. This should make 7th and 8th not be as successful.
- Changed the casting delay formula to 0.5 * Circle
- Adjustment to the bard difficulty calculation. Dragon barding should feel more natural. Use [BardDifficulty to see the base difficulty.
- Animal lore shows barding difficulty
- Implemented in-game commands to test out changes to the spell fizzle chances (either by changing how its calculated completely, or changing the required min skill to cast as mentioned above) and casting delays
- Set the default values for min/max PvP spell damage based on testing
- Fixed issue in [profile where Disable single-click menu wasn't displaying correctly
- Adjustment to greater explosion potion damage.
-- Damage has been reduced when it hits another player.
-- Base damage against a player is min 5, max 15. With GM alchemy, you add 10 to the min, and 5 to the max, so greater explosion pots would hit min 15, max 20.
- The prompt to use the pirate gate works now
- The pirate counter should be accurate when clicking on the pirate instance clock
- New mages no longer get a newbied bag
