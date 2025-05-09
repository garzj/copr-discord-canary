#!/usr/bin/python3
"""
Disable breaking updates which will prompt users to download a deb or tar file
and lock them out of Discord making the program unusable.

This will dramatically improve the experience :

 1) The maintainer doesn't need to be worried at all times of an update which will break Discord.
 2) People will not be locked out of the program while the maintainer runs to update it.

"""

import json
import os
from pathlib import Path

XDG_CONFIG_HOME = os.environ.get("XDG_CONFIG_HOME") or os.path.join(
    os.path.expanduser("~"), ".config"
)

settings_path = Path(f"{XDG_CONFIG_HOME}/discordcanary/settings.json")
settings_path_temp = Path(f"{XDG_CONFIG_HOME}/discordcanary/settings.json.tmp")
try:
    with settings_path.open() as settings_file:
        settings = json.load(settings_file)
except (IOError, json.decoder.JSONDecodeError):
    settings_path.parent.mkdir(parents=True, exist_ok=True)
    settings = {}

if settings.get("SKIP_HOST_UPDATE"):
    print("Disabling updates already done")
else:
    skip_host_update = {"SKIP_HOST_UPDATE":True}
    settings.update(skip_host_update)

    with settings_path_temp.open('w') as settings_file_temp:
        json.dump(settings, settings_file_temp, indent=2)

    settings_path_temp.rename(settings_path)
    print("Disabled updates")
