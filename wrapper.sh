#!/usr/bin/bash

# Path to discord canary binary
DISCORD_BIN=$(dirname $(readlink -f $0))/discord-canary

# Run python script to disable check updates
/usr/lib64/discord-canary/disable-breaking-updates.py

# Launch discord
exec "$DISCORD_BIN" "$@"
