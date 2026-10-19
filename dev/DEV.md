# Working notes (dev folder)

The `dev` folder holds the sources and tools that build the site. GitHub Pages also serves it, which is harmless.

- **Pages:** the `*.html` files here are the source pages. `python3 build_site.py` builds the site (pages with a site header and "How it works" link, methodology pages, index) into the folder above `dev`.
- **Shared code:** the race model, time parsing and formatting, and VDOT live in `shared/core.js`. Each page carries a copy between `CORE-BEGIN` and `CORE-END` markers. Edit `core.js`, then run `python3 shared/sync_core.py`.
- **Tests:** `tests/run_tests.sh` checks the copies are in sync, runs the unit tests (`tests/core.test.js`) and the page snapshots (`tests/snapshot.py check`, 49 scenarios). The build stops if any fail.
- **After an intended output change:** run `python3 tests/snapshot.py write` to accept the new outputs.
- **Needs:** Python 3 with `markdown` and `playwright` (plus its Chromium), and Node.

## Parkrun Converter
Course scores live in data/parkrun-sss.txt (name | SSS). After editing that file or data/parkrun-converter.tpl, run make_parkrun.py to rebuild parkrun-converter.html, then run python3 shared/apply_theme.py (the template does not carry the shared theme block).

## Stress tests (added 2026-10-19)
Not part of run_tests.sh because they take minutes. Run when changing inputs, parsing or models.
- `python3 tests/fuzz.py full [page-name-fragment]`: feeds every input on every page junk values (letters, huge, negative, "18:75", "Infinity", unicode), random combinations, button clicks, corrupt localStorage and blocked storage. Reports JS errors, NaN/Infinity/undefined text, impossible numbers and horizontal overflow at 390px. Known false positives: negative differences in the comparison column and "-0" inside "-0.6".
- `python3 tests/seqfuzz.py 25 40`: 25 seeds x 40 random actions per page, to catch crashes that depend on order (late change events, stale panels).
- `python3 tests/props_race.py`: Race Prediction Calculator properties (input reproduced, times and paces rise with distance, slower input slows everything, mileage only moves the marathon, blend stays between the two predictions and does not depend on result order).
