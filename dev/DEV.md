# Working notes (dev folder)

The `dev` folder holds the sources and tools that build the site. GitHub Pages also serves it, which is harmless.

- **Pages:** the `*.html` files here are the source pages. `python3 build_site.py` builds the site (pages with a site header and "How it works" link, methodology pages, index) into the folder above `dev`.
- **Shared code:** the race model, time parsing and formatting, and VDOT live in `shared/core.js`. Each page carries a copy between `CORE-BEGIN` and `CORE-END` markers. Edit `core.js`, then run `python3 shared/sync_core.py`.
- **Tests:** `tests/run_tests.sh` checks the copies are in sync, runs the unit tests (`tests/core.test.js`) and the page snapshots (`tests/snapshot.py check`, 49 scenarios). The build stops if any fail.
- **After an intended output change:** run `python3 tests/snapshot.py write` to accept the new outputs.
- **Needs:** Python 3 with `markdown` and `playwright` (plus its Chromium), and Node.
