#!/bin/bash
# Run before every build: shared block in sync, unit tests, page snapshots.
set -e
cd "$(dirname "$0")"
python3 ../shared/sync_core.py --check
node core.test.js
python3 snapshot.py check
