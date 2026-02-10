# SERVER PATCH 0.26

**September 22, 2023**

❗This patch contains client patches. Be sure to close out of the client, restart the launcher and let it update. ❗

🚩🚩Implemented the base CTF system based on the rules found in classic CTF games like in WoW's Warsong Gulch 🚩🚩

- 10v10 capture the flag (Team & Random)
- Two maps (Pirate Treasure Island & Old Trinsic)
- The game ends when one team has scored 3 captures, or after 20 minutes
- After 20 minutes, the team with the most flag captures wins
- If the teams have the same number of captures (tie) at the end of 20 minutes, the team with the most points will be declared the winner
- To score a capture, the capturing team must have their own flag at its base and bring the enemy's flag to that same spot
- If both flags are being carried, neither team can complete a capture
- The flag carrier has 120 seconds to capture the flag before they are killed and the flag drops
- When a flag is dropped, it will return to automatically return to home base in 5 seconds. Another player can pick up the flag during this time.
- When a flag is captured, flags are reset and cannot be picked up for 20 seconds
- When you're killed, everything on your body is returned to your bag, and you'll be resurrected in 10 seconds in at your team's home spawn
- The flag carrier can use the flag on themselves to drop it but won't be able to pick it up again for 5 seconds
- Individual player stats are tracked and recorded at the end of the game. Total points, total damage, flags captured, flags returned, flags stolen, flag carriers killed, players killed, number of deaths, and deaths while guarding the base

🪙  Points are accumulated as you play CTF
  - ▫️ 5 points, capturing the flag
  - ▫️ 4 points, returning the flag
  - ▫️ 4 points, killing the flag carrier
  - ▫️ 3 points, on death, guarding your base
  - ▫️ 2 points, killing someone attacking the flag carrier
  - ▫️ 1 point, on death, helping defend the flag carrier
  - ▫️ 1 point, killing a player

## Additional patch notes outside of CTF

- Detect hidden, when used in your house, will report the stats of the doors (locked or unlocked)
- Detect hidden will boost your chances of revealing someone in your house
- When you lock down an item, it will show [locked down] over it
- Removed the weight limit on locked down containers
- Friends and above can use locked down keys and keyrings
- Friends can use plants
- Cleaned up some apiculture functionality, needs more testing
- Adjustment to NPC speeds (testing)
- Fixed disarm to work when someone has a 2h weapon or shield
- Hires cannot be paragons :LUL:
- Built daily rare system, including achievements, player stat tracking. System currently disabled.
- Runebooks have arrows to allow you to adjust rune entry positions
- The default rune in your book will be highlighted
