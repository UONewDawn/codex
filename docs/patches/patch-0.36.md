# SERVER PATCH 0.36

**February 9, 2024**

❗This patch contains a client patches. Be sure to close out of the launcher and client, restart the launcher and let it update.❗

This patch includes several bug fixes and changes to the server but also changes how the client code is built and how the server communicates with the client.

## 🤖 Server 🤖

- Fixed issue with champ spawns potentially causing a crash
- Consider My Sins gump doesn't show long term decay (since it doesn't decay)
- Implemented a new mage AI (needs more testing)
- You will now see newer models for some mobs again (no more naked evil mages, Rikktor is a newer model, etc)
- Change drop rate of dye materials in dungeons from 1% to 0.5%
- You can dispel your own summons easily
- Housing blocked in Ocllo
- The guards will whack aggressive creatures

## 📜 Harrower Scroll 📜

- When you place all 6 skulls on the platform blaziers, you are now given a scroll to summon the harrower at a later time
- Before you spawn Harry, you have an option to create a temp guild region around the Harrower (1 hour). Any player not an ally or in your guild will appear orange and attackable. 🍊

## 💻 Client & Assistant 🖱️

- The client is now compiled using Native AOT, a self-contained client that has been ahead-of-time (AOT) compiled to native code. Native AOT apps have faster startup time and smaller memory footprints.
- With that, the initial attempt to add some basic client validation 🕵️
- Removed several features from Razor that already existed in ClassicUO (auto-open corpses, spell name/hues, show incoming player names, etc)
- Modified some default client profile settings

🌃 Removed the ability to change light levels without using a spell or potion in game (learn to love Night Sight again)
