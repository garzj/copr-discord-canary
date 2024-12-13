#!/usr/bin/env bash
cd "$(dirname "$0")"

git pull origin master --ff-only && ./check_new_version.py -u && git push --follow-tags
