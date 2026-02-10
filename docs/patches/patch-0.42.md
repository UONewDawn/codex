# SERVER PATCH 0.42

**February 16, 2025**

This patch largely focuses on increasing account security and bringing New Dawn's core server codebase up to the latest version. With this patch comes an updated version of the launcher and game files.

In addition, this patch helps in the preparation to move towards an Open Beta and/or Early Access model.

## 🪪Login Process🪪

To help secure New Dawn against DDoS attacks, account stealing, account sharing, excessive accounts, and overall general account security, the login process has been modified.

While the launcher is still required, it will direct you to https://login.uonewdawn.com/ where you'll need to login using your Discord credentials. Upon successful login, authenticate the launcher, click 'Enter Britannia', and select your account to log in.

You can learn more about it here: https://login.uonewdawn.com/why

Note: This process is currently only supported on Windows. Linux support is planned for a future update.

## 📜Fixes/Changes📜

- Fixed Ocllo sewer/dungeon regions and spawners (added additional entrance in graveyard)
- You can't open a corpse that isn't yours in the event center
- Chance of a rift shard dropping can be changed live in game
- Removed New Player Tickets
- Fixed context menu toggle not working (can access it via [profile)
- When farming cotton or flak it has a chance to trigger the resource captcha check
- Farmers have some random banter
- Rewrote the resource captcha system to be more robust
- Disabled achievements for now until the system can be more refined
- Refactored the daily rare system & enabled it (📝Many more rare locations to be added in the future)
- If you somehow get into a dungeon during your ban period you'll be ejected to the event center
- Event Center (Dawn) doesn't allow skill gains and nearly all skills are blocked (📝This area isn't meant to be a safe spot to craft or skill up)
- CTF max player count is capped at 10 and you can only longer gain skills in the CTA arenas
- Idle animals and monsters now only have a 25% chance to make a noise (ie: dog barking, cat meowing, etc)
- Bumped up the skill gain rate on tactics, swords, mace, fencing, and wrestling slightly
- Removed almost 30k items from other facets in the game that aren't accessible

## 🤖Server🤖

- Base code merged up to the latest upstream
- Increased server response speed
- Enhanced memory management
- Fixed numerous bugs in the core server software
- Disabled test mode functionality
- Archived old accounts and IPs so new accounts can be created by those who previously had accounts

## 🗺️Map🗺️

- Created docks closer to Ocllo (east side, north of Moongate)
- Fixed missing wall in Trinsic
- Removed hidden blocker in Trinsic healer building
- New Minoc now has a tavern and inn
- Several other tweaks and changes no one will most likely notice
- Yew (in the Abbey) has been slightly enhanced to not feel as empty and unfinished

## ⚔️Conquest of the Virtues⚔️

Conquest of the Virtues has been enabled (early version of the system). You can read about the overall game here: ⁠Conquest of the Virtues

- Ruins of Britain (east of Britain)
- Ruins of Trinsic (northwest of Trinsic)
- Ruins of the Shadowlords (west of Yew)
- Ruins of Moonglow (where the original Moonglow used to exist)

## 🎶Music🎶

📝While my focus remains core features and security, music and ambience still help bring world to life so I hope to continue to sprinkle that stuff in where I can

- When exploring the world (ie: outside of towns, dungeons, etc) it will randomly play one of the eight available music tracks for exploring
- When you enter a tavern or inn, depending on the location, you will get a different type of ambience. This change of music (or using [where to confirm) lets you know you can log out safely
- Vesper has new music and ambience
- Dagger Island has new music and ambience
