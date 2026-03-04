# SERVER PATCH 1.3

## February 17th, 2026

This patch continues to address bugs and behaviors reported by the community.

### 🛠️ Bug Fixes & Adjustments

- Placing a new house with interior double-doors will no longer link them together -- opening one will not open the other. If you have an existing house and would like this behavior removed, let me know
- The "I must consider my sins" message will now correctly display your long-term murder count expiration
- You must now meet the minimum taming skill requirement of a pet in order to accept a transfer of it
- You must meet the minimum taming skill of a nightmare in order to ride one
- Young players will now be able to enter the Ocllo Sewers even if another character on the same account is already inside the dungeon
- Adjusted the chances of fishing up ancient sea serpents and artifact clues
- Adjusted the gain rate for skills approaching the 100.0 individual cap while also nearing the 700 total skill cap. This should balance out what I was looking for gain wise. These numbers will continue to be slightly adjusted in game per skill
- Adjusted stats gains so they feel _a little_ faster
- You can no longer reorder runes inside a runebook while it is locked down
- Cleaned up some of the language on the guild war declaration Discord message
- Runebooks that are locked down can now be accessed from 2 tiles away, up from 1
- Anatomy now has a 1-second cooldown between uses
- At GM Magery with no Inscription, Magic Reflect will now absorb up to 8 circles of spells (down from 11). With 100.0 Magery and 100.0 Inscription, it will absorb up to 15
- The single-click buy/sell context menu on vendors now requires you to be within 4 tiles (down from 8), matching the range of the standard vendor buy interaction
- Attempting to cast a spell on a target not in your line of sight will now display a "target cannot be seen" message and drop the cursor appropriately
- Fixed a mislabeled description on repair deeds. Additionally, newly created repair deeds are no longer blessed
- The Animal Lore gump will now display the total number of owners an animal has had on the top
- Hats have been removed from the random magic drop pool that generates weapons, armor, and jewelry
- Charter Paintings & Maps items can now be used while locked down in a house
- Silver weapons will now correctly drop from certain humanoid creatures
- If the clothing item or runebook has a special hue, it will list the hue in the label (will change to hue names in the future)
- When you cast a spell, any weapons or shields will auto-unequip, either on the initial cast, or when you try to land your target
- O'Malley can have an ' in his name now

---

### 🪡 The Tailors Guild Proclamation

By Order of the Grand Weaver's Council:

<div class="rpg-scroll" markdown="1">
The esteemed Tailors Guild, heeding the complaints of craftsmen across Britannia regarding the inferior pigments of recent years, hereby announces the restoration of proper dye standard:

The Purging of Unsightly Hues - The much-maligned dyes previously granted through Bulk Order Deeds have been banished from our realm. New cloth rewards, enchanted sandals, and masks shall now bear colors worthy of true artisans. Those unfortunate souls possessing garments in the old, disagreeable hues may keep them as a reminder of darker times -- or perhaps as kindling.

Let it be known throughout Britannia that the Guild has heard thy grievances and acted swiftly.

<span class="rpg-signature">So witnessed this day by the Council of Master Tailors</span>
</div>

---

### 😈Champions of Evil

I'm continuing to tune champion spawns so they strike a balance between challenge and reward. Right now the scales tip too far toward reward without enough risk to match when it comes to some of the champs, so these changes pull things back toward center.

- The amount of gold dropped per splash pile now scales based on the tier of the champion spawn -- easier tiers yield less, later tiers yield more
- The total gold dropped by champion spawn creatures has been reduced by half
- The Barracoon champ platform has been restored
- Barracoon can now trigger The Piper's Call, a haunting melody that drawing victims close to him

---

### 📜Name Changes

<div class="rpg-scroll" markdown="1">
The Court of Truth in Yew has opened its ledgers to those seeking a fresh start. The court clerk -- a fastidious woman with ink-stained fingers and little patience for indecision -- will hear your request, provided your coin purse is heavy enough and your record is clean... enough.
</div>

- Approach the clerk and say **"I request a name change"**
- If you have not changed your name within the last 14 days and carry sufficient funds, **200,000 gold** will be deducted from your bank box **right away** and you will be presented with the name change gump
- Your first name change will be free

---

### 🪙The Scales Tip in Magincia

<div class="rpg-scroll" markdown="1">
Whispers have spread through every dockside tavern from Ocllo to Paws that there's judge from Yew who hangs out in Bucs Den whose sense of justice bends with the weight of coin. You'll usually find him at The Pirate's Blunder, if you can stomach the company he keeps. He asks no questions. He never has.

But take heed. The nobles of Magincia have grown tired of watching murderers walk free. Gold has been flowing into the courts to see this corruption unraveled, and the judge, ever aware of the noose tightening around his neck, has raised his prices accordingly. Redemption, it seems, does not come cheap.
</div>

- **Pardons now start at 150,000 gold**. Each subsequent pardon doubles in cost -- 300k for a second, 600k for a third. After that, the judge won't help you. You're on your own.
- The judge will now entertain requests from those with up to 20 murders on their record (up from 10). Beyond that, even he won't go near you
- You may now purchase a pardon if you carry at least 1 long-term murder count (used to be 5)
- The pardon is blessed. Carry it with you. If you die and resurrect with it in your pack, it will be consumed automatically. Stat loss will be avoided, and both your short-term and long-term murder counts will be reset to zero.
- If you are alive, you may simply double-click the pardon to consume it and receive the same benefit

!!! warn "A word of advice from the judge himself"
    Purchase your pardon before you need it. You never know when the executioner comes calling -- and he does not sell to the dead.

---

### 🧌Trolls Reemerge

<div class="rpg-scroll" markdown="1">
For years the deep caves and mountain passes of Britannia sat quiet -- unsettlingly so. Travelers moved freely through highland roads that their grandfathers would never have dared walk unarmed before the Codex war. The old-timers muttered that it wouldn't last, that the trolls hadn't gone, only retreated. They were right.

As the citizens of New Dawn have begun building homesteads and laying roots across the land, the disturbance has drawn ancient attention. Cave trolls have been spotted lurking in the deeper reaches of Britannia's caverns, and mountain trolls have returned to the high passes and rocky ridgelines in force. Whether they've been driven out by something deeper underground or simply drawn to the scent of civilization is anyone's guess.

The local town councils have issued warnings: avoid dark caves and mountain passes when possible, and never travel alone.
</div>
