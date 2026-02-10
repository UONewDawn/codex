# SERVER PATCH 1.0

## January 23, 2026

Those who were in the final round of testing already experienced the majority of the changes.

## 📜General Fixes/Changes📜

- If you reserved a name, they've been tied to your specific accounts. If you can't pick the name you reserved, let us know
- Lowered dungeon tailoring material drop rates
- Lowered rift shard drop chance
- Lowered artifact drop chance
- Lowered rare animal spawn chance
- Added some randomness the time delay between new rifts opening up
- Cleaned up name change gump
- If in a party, you must be in range (30 tiles) to get any fame or karma
- Fixed issue with empty names with forensic eval
- If your house placement fails, you'll see which tile(s) were the cause
- If your pet is set to follow you, it will ignore aggro and attacks and continue to follow
- To balance out the Spirit Summoner build, how strong your summoned pets are (the scaler that gets applied to all stats/skills/armor) now is based on your Animal Lore skill instead of Spirit Speak. Spirit Speak is still used when calculating dispel chances, the duration of your summoned creatures, and when active, any bonus added to healing of your summons
- Adjusted world saves from 20 minutes to 5 minutes
- Adjusted the global weather patterns to align a bit more with the world

## 🧌Spawners🧌

- Converted all the spawners from the ancient XML Spawners code to the native spawning system. Why? XML Spawner is old, poorly coded, and never really fully supported ModernUO and wasn't using any of the advanced features of XML Spawner. This should have no impact on where or how things spawn, all the benefits are in performance and save times.

## 🤖AI and Movement🤖

- Major changes with the AI speed and movement of monsters, NPCs, followers. They should look more smooth when they move, however some of their speeds may still need to be adjusted so your feedback is welcome.

## 📊Player Event Tracking📊

- Added a new event tracking system that captures player activity and eventually will feel into the Portal leaderboards. Currently tracking CTF, Champ Spawns, Pirate Events, Harry, Codex Rifts, Conquests, Smuggler Runs, Rares, Artifacts, Auctions, PvP kills, monster kills, deaths, and logins. More events can be added over time as needed.
- Currently the data is being collected only. Leaderboard generation will be available via the Portal in the future.

## 🛶Boat Control Changes🛶

- When you try to command a boat, it will let the person with the key take control regardless of where on the boat
- If no one on the boat has a key, then check who's the closest to the tillerman, and if the closest person is the one trying to command the boat, they can

## 💻Server & Infrastructure💻

- Upgraded the base OS the server runs on to the latest version
- Server code base updated to upstream with tons of bug fixes and optimizations
- Updated to dotnet 10 for better performance

## 🖥️Client (ClassicUO & Razor)🖥️

- Updated ClassicUO to the latest version with all the changes specific to New Dawn.
- Changed how rain and snow appear in the game
- Item hue now reflects on the type of light it omits
- Added rain sound effects
- Footsteps sounds are now based on the type of ground being stepped on. You can disable this in settings
- Removed alternative light setting so you guys can really hate me

## ⭐Reward System⭐

To better support rewards for various events, a system has been built to give out reward bags when you login based on certain criteria.

📝Note: Rewards are given per person (based on your Discord account), not per account or per character. This makes the items that much more unique and rare.

### 🎇Aurora Beta Reward Bag🎇

If your account was created prior to 5/28/2025, upon login, you will receive an Aurora inspired gift bag as a thank you for helping beta test.

### 🎇Charter Member Bag🎇

If your account is created within the first week of launch, upon login, you will receive a Charter Member gift bag inspired by the original Ultima Online Charter Edition (that still sits on the shelf behind me)

### 🎇Vanguard Reward Bag🎇

If you were an early alpha tester (marked by the role in Discord), an additional thank you for all those hours back in the early days fine-tuning each skill and spell.

### 🎇Welcome Reward Bag🎇

Any new account will get a welcome bag to help start their journey (some gold, bandages, reagents, etc)

## 💫Achievements💫

The Achievement System was rewritten and now tracks player progress across various in-game activities and rewards players with points, titles, and items for completing milestones. Type [ach to see your progress!

- Point System: Each completed achievement awards points that contribute to your total score
- Leaderboards: Global rankings based on total points and completion count
- Categories: The system tracks progress across multiple activity types such as Discovery, Hunting, Crafting

### Rewards

- When you complete an achievement, you receive:
  - Points: Added to your total achievement score
  - Title: Some achievements grant unique titles for your character
  - Items: Certain achievements award physical items (placed in backpack or bank if overloaded)

I want to thank everyone who helped get the server to where it is today. Your testing, your feedback, your discussions -- all helped shape what this project is today
