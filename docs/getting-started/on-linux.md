# Linux Installation Guide

These steps have been tested on Ubuntu and Debian.

!!! warning
    Many distros offer outdated versions of Wine that don't have the right tools for handling ClickOnce applications.

    The automated setup script has been tested using the latest Wine-Staging version from winehq.org
    
    Wine setup steps will differ based on the specific OS version you are running. Refer to the guide in the below URL and modify these commands accordingly. The examples assume Noble (Ubuntu 24.04 / Linux Mint 22)

    https://gitlab.winehq.org/wine/wine/-/wikis/Debian-Ubuntu

## Launcher

[Download New Dawn Game Launcher](https://newdawn.nyc3.cdn.digitaloceanspaces.com/newdawn-launcher.zip)

## System Prerequisites

### Enable 32-bit architecture support

Wine needs 32-bit libraries even on a 64-bit system:

```bash
sudo dpkg --add-architecture i386
```

### Install prerequisite packages

```bash
sudo apt install dirmngr ca-certificates software-properties-common curl wget cabextract winbind -y
```

### Add the WineHQ GPG key

```bash
sudo mkdir -pm755 /etc/apt/keyrings
wget -O - https://dl.winehq.org/wine-builds/winehq.key | sudo gpg --dearmor -o /etc/apt/keyrings/winehq-archive.key -
```

### Add the WineHQ repository

```bash
sudo wget -NP /etc/apt/sources.list.d/ \
  https://dl.winehq.org/wine-builds/ubuntu/dists/noble/winehq-noble.sources
```

### Update and install Wine Staging

```bash
sudo apt update
sudo apt install --install-recommends winehq-staging -y
```

Verify it installed correctly:

```bash
wine --version
```

You should see something like:

```
wine-11.x (Staging)
```

### Install Winetricks (latest version from source)

!!! warning
    **Don't use the apt version of winetricks** — it's usually too old. Get it directly:

```bash
sudo wget -O /usr/local/bin/winetricks https://raw.githubusercontent.com/Winetricks/winetricks/master/src/winetricks
sudo chmod +x /usr/local/bin/winetricks
```

## Install Script

Run this as a script, or run each line manually depending on your comfort level.

!!! note
    Edit the values under Configuration to reflect your own setup

```bash
#!/bin/bash
# =============================================================================
# UO New Dawn — Linux Wine Setup Script
# =============================================================================
# Prerequisites:
#   - Wine Staging installed from WineHQ
#   - winetricks installed at /usr/local/bin/winetricks
#   - ~/Downloads/NewDawnLauncher.exe already present
#
# Usage:
#   chmod +x uond-setup.sh
#   ./uond-setup.sh
# =============================================================================

set -euo pipefail

# --- Configuration -----------------------------------------------------------
WINEPREFIX="$HOME/.wine-uond"
LAUNCHER="$HOME/Downloads/NewDawnLauncher.exe"
SHORTCUT="$HOME/Desktop/UO-NewDawn.sh"
LOG="$HOME/uond-setup.log"

# --- Helpers -----------------------------------------------------------------
log()  { echo "[$(date '+%H:%M:%S')] $*" | tee -a "$LOG"; }
die()  { echo -e "\n[ERROR] $*" | tee -a "$LOG"; exit 1; }
step() { echo -e "\n\033[1;36m>>> $*\033[0m" | tee -a "$LOG"; }
ok()   { echo -e "\033[1;32m    ✔ $*\033[0m" | tee -a "$LOG"; }
warn() { echo -e "\033[1;33m    ⚠ $*\033[0m" | tee -a "$LOG"; }

export WINEPREFIX
export WINEARCH=win64
export WINEDEBUG=-all
export DISPLAY="${DISPLAY:-:0}"

# --- Pre-flight checks -------------------------------------------------------
step "Checking prerequisites"

[[ -f "$LAUNCHER" ]] \
    || die "Launcher not found at $LAUNCHER\n       Download NewDawnLauncher.exe from the UO New Dawn portal first."

command -v wine &>/dev/null \
    || die "wine not found. Install Wine Staging from WineHQ before running this script."

command -v winetricks &>/dev/null \
    || die "winetricks not found. Install it with:\n       sudo wget -O /usr/local/bin/winetricks https://raw.githubusercontent.com/Winetricks/winetricks/master/src/winetricks && sudo chmod +x /usr/local/bin/winetricks"

WINE_VER=$(wine --version 2>/dev/null)
ok "Wine found: $WINE_VER"

if [[ -d "$WINEPREFIX" ]]; then
    warn "Existing prefix found at $WINEPREFIX"
    read -rp "    Delete it and start fresh? [y/N]: " CONFIRM
    [[ "${CONFIRM,,}" == "y" ]] || die "Aborting. Remove or rename $WINEPREFIX manually and re-run."
    rm -rf "$WINEPREFIX"
    ok "Old prefix removed"
fi

# --- Phase 1: Initialize prefix ----------------------------------------------
step "Initialising Wine prefix (win64, Windows 10)"

wineboot --init 2>>"$LOG"

wine reg add "HKEY_LOCAL_MACHINE\\Software\\Microsoft\\Windows NT\\CurrentVersion" \
    /v "CurrentVersion" /t REG_SZ /d "10.0" /f >>"$LOG" 2>&1
wine reg add "HKEY_LOCAL_MACHINE\\Software\\Microsoft\\Windows NT\\CurrentVersion" \
    /v "CurrentBuildNumber" /t REG_SZ /d "19041" /f >>"$LOG" 2>&1

ok "Prefix initialised"

# --- Phase 2: Install .NET Framework (This will take a few minutes) ---

step "Install .NET Framework (This will take a few minutes)"
winetricks -q dotnet48 >>"$LOG" 2>&1 && ok ".NET 4.8 installed" \
    || warn ".NET 4.8 reported errors (usually safe to continue)"

# --- Phase 3: Supporting components ------------------------------------------
step "Installing supporting components (fonts, gdiplus, vcrun2019)"
winetricks -q corefonts gdiplus vcrun2019 >>"$LOG" 2>&1 \
    && ok "Supporting components installed" \
    || warn "Some components reported errors — check $LOG if game has issues"

# --- Phase 4: Set necessary registry keys ------------------------------------
step "Optimizing Wine registry keys"
wine reg add "HKEY_CURRENT_USER\\Software\\Wine\\DllOverrides" \
    /v "dfshim" /t REG_SZ /d "native" /f >>"$LOG" 2>&1

wine reg add "HKEY_CURRENT_USER\\Software\\Wine\\DllOverrides" \
    /v winemenubuilder.exe /d '' /f >>"$LOG" 2>&1

wine reg add "HKEY_CURRENT_USER\\Software\\Microsoft\Avalon.Graphics" \
    /v "DisableHWAcceleration" /t REG_DWORD /d 1 /f >>"$LOG" 2>&1
ok "Registry keys applied"

# --- Phase 7: Create desktop shortcut ----------------------------------------
step "Creating desktop shortcut"

# Runnable shell wrapper on the Desktop
cat > "$SHORTCUT" << EOF
#!/bin/bash
# UO New Dawn — launches NewDawnLauncher.exe via Wine on every run.
# The launcher handles updates to itself and the game client automatically.
export WINEPREFIX="$WINEPREFIX"
export WINEDEBUG=-all
export DISPLAY="\${DISPLAY:-:0}"
wine "$LAUNCHER"
EOF
chmod +x "$SHORTCUT"
ok "Desktop shortcut created at $SHORTCUT"

# .desktop entry for the app menu
mkdir -p "$HOME/.local/share/applications"
cat > "$HOME/.local/share/applications/uonewdawn.desktop" << EOF
[Desktop Entry]
Name=UO New Dawn
Comment=Ultima Online New Dawn
Exec=$SHORTCUT
Type=Application
Categories=Game;
StartupNotify=true
EOF
ok "App menu entry created"

# --- Done --------------------------------------------------------------------
echo ""
echo -e "\033[1;32m============================================\033[0m"
echo -e "\033[1;32m  Setup complete!\033[0m"
echo -e "\033[1;32m============================================\033[0m"
echo ""
echo "  Prefix location : $WINEPREFIX"
echo "  Launcher        : $LAUNCHER"
echo "  Desktop shortcut: $SHORTCUT"
echo "  Setup log       : $LOG"
echo ""
echo "  To play: double-click 'UO-NewDawn.sh' on your desktop."
echo ""
```

!!! note "Special Thanks"
    Thanks to raajaton for putting these scripts together