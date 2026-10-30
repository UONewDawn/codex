---
description: "Patch notes for New Dawn server patch 1.21. Highlights: the Arcane Forge and slayer oils, Shield Bash reworked into a counter with Riposte, Snare reworked to match, armor changes for PvP, readable plant gumps and easier care for full-grown gardens and strong hives, and Remove Trap working on every treasure chest."
---

# SERVER PATCH 1.21

## October 30th, 2026

This patch opens the Arcane Forge, where blacksmiths melt magic gear into slayer oil. It reworks Shield Bash and Snare and adds Riposte for shield fighters, stops heavy magic plate turning PvP hits into 1s, and rebuilds the plant gumps so a full-grown garden and a strong hive need far less daily care. It also comes with a round of fixes and quality-of-life changes.

❗**This patch comes with a required client update. The old client can no longer connect. Close the client, restart the launcher, and let it update.**❗

## 🛠️ Bug Fixes & Enhancements

- Remove Trap now works on treasure map chests. At GM you'll always disarm levels 1 to 4 and disarm level 5 most of the time (before, levels 4 and 5 were impossible even at GM). A failed attempt still won't set the trap off
- Telekinesis is no longer a free pass past a trap. The stronger the trap and the lower your Magery, the more likely your spell jars the mechanism and the trap goes off on you, however far away you're standing. At GM Magery it's always safe on map chests up to level 3, but level 4 and 5 can still bite. This goes for every trapped chest, not just treasure map chests
- Dungeon chests no longer vanish while you're working on them. Every attempt to pick the lock or disarm the trap restarts the chest's despawn clock, so it stays for at least 15 minutes after your last try
- Every pirate chest trap can now be disarmed (some were too strong even for a GM), and their explosions hit a little less hard
- A failed Shield Bash no longer costs you stamina on every hit you take
- Some monsters that know both Wrestling and Parrying could never stun you. Now they can
- In a bulk order book, the Amount column for Large BODs now shows their size (10, 15 or 20) instead of the combined total across every item. Use the detail button to see how far along each item is
- Your Storage Rack loadouts now show up in the rack's context menu by name. Pick one to apply it without opening the rack
- You can now split stacks of thorny vines, cinderstone, glacial shards and refined sugar, and they show as a pile like other stacks. A pile of cinderstone on the ground no longer blocks your way
- Monsters you kill with Provocation now count toward opening a rift gate in the graveyards during a Rift Season. Inside a rift, provoked kills now earn you Rift Shards (Halloween Candy this season) and can drop Codex fragments, just like your own kills

## 🌱 Gardening

The plant gumps have been redesigned to match the beehive gump. Instead of a key of colored pluses and minuses, they now say in plain words what each plant needs and which potion fixes it. A new Help button explains the whole care routine.

- From stage 7, mild problems (Dry or Soggy soil, or a mild ailment) no longer hurt a plant. They only stop it recovering. Full-grown plants also dry out and catch pests half as often, and stage 9 plants a third as often, so a full-grown garden needs tending about every 3 days instead of every day. Seedlings still need daily care
- A dark swarm of flies hovers over any plant that will be hurt at its next growth, and leaves once the plant is cared for
- Growth checks now come exactly every 24 hours instead of drifting an hour earlier each day, and the gump shows how long until the next one. House owners can set a [garden schedule](../game-mechanics/housing.md#garden-schedule) from the house sign's Options so every plant and beehive in the house checks at the same hour
- The Water button now pours from a filled water container in your pack (an empty pitcher used to make it fail). Opening a plant closes any other plant gump, so you can't treat the wrong plant by mistake

See the [Gardening](../game-mechanics/gardening.md) page for the new gump and full details.

## 🐝 Beekeeping

- A strong colony (80,000 bees or more) catches parasites and disease half as often, so a full-strength hive needs tending about every 3 days instead of every day. If it loses bees, the protection is gone until the colony grows back
- A producing hive with a mild case of parasites or disease isn't hurt until its next check, but it won't heal or make its bonus honey and wax until you treat it
- A hive's age stops raising its chance of parasites and disease after 30 days, so Greater Strength and good water and flowers matter again for old hives
- Hives only feed on full-grown flowers that are Healthy or Vibrant
- Growth checks still come exactly every 24 hours, the gump shows how long until the next one, and the house garden schedule moves hives too. Waking a hive from hibernation no longer restarts its timer

See the [Beekeeping](../custom-systems/beekeeping.md) page for full details.

## ⚒️ Arcane Forge

Blacksmiths can now melt magic weapons and armor at the new Arcane Forge into arcane dust, then craft it into slayer oil with reagents dropped by each slayer group's monsters. Coat any weapon and it hits like a slayer until the oil runs out.

See the [Arcane Forge](../custom-systems/arcane-forge.md) page for full details.

## 🛡️ Parrying

Shield fighters get more out of Parrying. With **Shield Bash** ready, parrying a melee attack can let you counter by slamming your shield into the attacker, and it stays ready until you put it away. The bash throws off their next swing, breaks any spell they're casting and stops them in their tracks. It hits harder against monsters than against players. Heavier shields bash harder but cost more stamina and take longer to recover. Double-click your shield or type **[bash** to ready it, and a buff icon shows when it's up. You can't have Shield Bash and stun ready at the same time; readying one lowers the other. Every shield fighter also gets **Riposte**: parry an attacker and your next hit on them within 3 seconds does extra damage.

See the [Parrying](../skills/combat/parrying.md) page for full details.

## 🏹 Archery

Snare got the same treatment as Shield Bash.

- Type **[snare** to ready or lower it (double-clicking your bow still works)
- It stays ready after it lands, and a buff icon shows it and counts down the 20 second cooldown
- 50% chance at 100 Archery and 100 Anatomy (was 25%)
- Costs 10 stamina, only when it lands (was 15 on every hit while ready)
- Hits that don't snare no longer message you or your target
- Bosses are pinned for 1.5 seconds, everything else for 3
- A target that was just pinned by a snare or a shield bash can't be pinned again until 8 seconds after it's free
- Fixed a snare during a world save leaving the target unable to walk after a restart

See the [Archery](../skills/combat/archery.md) page for full details.

## ⚔️ Armor in PvP

Heavy magic armor no longer turns every weapon hit into a 1 in player-vs-player fights. When a player hits another player:

- Armor rating above 48 counts for half. Fortification and invulnerability plate still beat plain plate, and every leather suit, including invulnerability leather, keeps its full rating
- Your armor and shield together can stop at most 75% of a hit

Against a full invulnerability plate suit, a vanquishing katana now averages about 8 a hit instead of 4, and no longer lands 1s. Against plain plate and leather, hits only lose their 1s: a vanquishing katana against GM barbed leather goes from 11.6 to 12.1 a hit, and against invulnerability leather from 8.1 to 9.3. Monsters, pets and summons hitting you, and you hitting them, are unchanged.

See the [Armor](../game-mechanics/items-and-equipment/armor.md#armor-in-pvp) page for full details.
