# SERVER PATCH 0.32

**January 1, 2024**

❗This patch contains a launcher update and client patches. Be sure to close out of the launcher and client, restart the launcher and let it update.❗

Every so often, a patch is required that isn't very exciting. This is one of those. This patch includes an update to the game client and assistant along with backend services that help support integration to Discord when the server is running in production.

## 💻 Client & Assistant 🖱️

- A few style changes to the client UI, along with some backend changes for security
- Removed Closest Humanoid functionality from Razor
- Removed the classicuo scripting commands
- Removed the targeting from scripting that was related to closest humanoid
- Launcher should now launch multiple accounts correctly

## 🤖 Server 🤖

- Fixed issue with spawns not detecting the correct Z-axis (this was a bug in the core server software)
- Several backend changes to allow the server to push messages to Discord (Discord registration should work now, type /register to learn more)
- Server will start block IPs from connecting that are detected as proxy, VPN or Tor exit address
- Fixed issue with achievements not saving
- Setup spawning positions and times for initial 32 server rares that spawn (currently disabled)
