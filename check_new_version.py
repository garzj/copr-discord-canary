#!/usr/bin/python3

import re
import subprocess
import sys

import requests

spec_file = "discord-canary.spec"

do_update = "-u" in sys.argv

h = requests.head(
    "https://discord.com/api/download/canary?platform=linux&format=tar.gz"
)
dl_location = h.headers.get("location")
if dl_location is None:
    print(f"Request did not redirect to new location.")
    exit(1)
new_version = dl_location.split("/")[5]

spec = open(spec_file).read()
match = re.search(r"Version:\s+(.*)", spec)
if match is None:
    print(f"Version field not found in spec:", spec)
    exit(1)
cur_version = match.group(1)

if cur_version == new_version:
    print(f"Version: {cur_version}")
    print("Already updated!")
    exit(1 if do_update else 0)

print(f"Current version: {cur_version}")
print(f"New version: {new_version}")
print()

if not do_update:
    print("Pass -u to update.")
    exit(0)

changelog = f"Update to {new_version}"
cmd = [
    "tito",
    "tag",
    "--use-version",
    new_version,
    "--changelog",
    changelog,
    "--accept-auto-changelog",
]
print("+", " ".join(cmd))

try:
    subprocess.check_call(cmd, stderr=subprocess.PIPE)
except FileNotFoundError:
    print("Command not found. Is tito installed?")
    exit(1)
except subprocess.CalledProcessError as e:
    print("Command failed:", e)
    exit(1)

print()
print("Updated to version:", new_version)
