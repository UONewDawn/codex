# SERVER PATCH 0.31

**December 28, 2023**

❗This patch contains client patches. Be sure to close out of the client, restart the launcher and let it update. ❗

This patch brings the core server software up to the latest development changes, which include tons of optimization to save times and general performance. It moves the server to the latest version of .NET 8. .NET 8 comes with thousands of improvements across the stack.

Also, this patch includes some changes to how murdering is handled on New Dawn.

- Block boats from being placed in certain areas (pirate map, for example)
- Fixed issue with reg consumption
- Fixed the Dawn achievement now that it's in Felucca
- Block opening a pirate map instance in CTF and the Codex Rift
- Removed fire ants from the Codex Rift spawn

🥷Egg bombs can be made by a cook with 90+ skill. These can be used to hide in combat and has a 25 second cooldown

- Account dungeon restrictions will apply to the Codex Rift
- Change bonding delay from 7 days to  1 day

🚩Fixed hues not applying correctly in CTF

🚩Actually block summons in CTF :NotLikeThis:

## 🔪 Murder Changes 😵

- If you kill yourself, you cannot report anyone for murder, even if they caused 99% of the damage
- If you die in a dungeon with 5+ murders, all your accounts (linked by IP and Discord ID) will be barred from that specific dungeon for 15 minutes.
- If you die in another dungeon, any existing dungeon-specific IP restrictions will reset to 15 minutes.
- Long-term murders will become permanent; once you reach 5 long-term murders, you'll be permanently marked as a murderer.

  ▫️As long as you have between 5 and 10 long-term kills, you can purchase a forged pardon from a corrupt judge at the Yew courthouse.

  ▫️Forged pardons will increase in cost each time you purchase one and will be limited to 3 per character.

  ▫️Upon use of a forged pardon to the judge, your short and long term kills will be set to zero and you will no longer be a murderer (but deep down, we all know you really are, you filthy animal)
- The decay time for short-term murders will be increased to 48 logged-in hours.

  ▫️Short-term murders between 1-4 will decay after 24 logged-in hours. When you reach 5 or more, the decay rate extends to 48 hours.

  ▫️Stat loss for 5+ short-term kills will be raised from 5%-15% to 20%-40%.

  ▫️Example: 25 short term kills, you would incur the max 40% stat/skill loss penalty.
- Updated the "I must consider my sins" gump (WIP, not complete)

## ✍️ Discord Registration

- Added the [discord command to support the registration process
- All accounts must be registered to a Discord account within 1 day of account creation
- After the 1 day grace period, the character will be transported to jail and won't be able to exit until they register
- You can only associate 3 accounts with your discord ID
- Upon registration, you will be promoted to the verified role in Discord which allows you to post images, embeds, etc
- The default (at)everyone role will be limited to basic actions to counter spamming, trolling, etc
- Eventually, you will need to have your phone number registered to you Discord account to connect to here (and thus, to New Dawn)
