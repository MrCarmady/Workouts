# Random Session Generator: methodology

Picks one session at random from the Classic Session Generator and the Sub-Threshold Session Generator, fitted to a 5k time and the time available. Built for "I just want something" (P, 2026-11-20), in the spirit of the sessions a training app might hand out. It adds no sessions and no paces of its own.

## What is standard and what is a choice

| Item | Status |
|---|---|
| Paces, structures, recoveries and TSS for every session | Copied from the two generators; `tests/check_lucky_sync.py` compares total time, TSS and distance for each session type at four 5k times, and the sub-threshold rep ranges |
| Pace model | Same as the Race Prediction Calculator, from the 5k time. Marathon pace assumes 70 miles a week |
| Inputs: 5k time and time available (30, 45, 60, 90 or 120 min; 120 added 2026-11-23 so the long Daniels session can appear) | P's choice, 2026-11-20. No weekly distance, race distance, heat or treadmill inputs |
| No filter on the pool, no TSS cap, no knowledge of recent training | P's choice, 2026-11-20 |
| Everything below about the draw and the fit | My choices, placeholders |

## The draw

1. A coin flip picks the family: Classic or Sub-Threshold.
2. Within the family, every session type that has at least one version fitting the time has the same chance.
3. Within the type, one version is picked at random.

Weekly distance (added 2026-11-23, P: the tool should ask for it): optional, miles or km, saved in the shared profile. It sets marathon pace (blank = 70 miles a week), applies the Sub-Threshold Session Generator's weekly cap to sub-threshold and short-rep volume (12%, 20%, 5%, 8% or 10% of weekly distance by rep type, with a floor for low mileage), and selects Daniels rep counts by band (up to 40 miles, 41 to 70 and blank, over 70; my reading of Tables 4.2 to 4.4). Unlike the Sub-Threshold Session Generator, weekly distance here only lowers the top of the rep range, never raises it, so 90 miles a week does not give 20 × 3 min. Aussie float pace ignores weekly distance, as on the Classic page.

Pre's 200s is capped at 7% of weekly distance (P, 2026-11-23: 8% is too aggressive for a hard session; 6 to 7%, 7% is my pick within that), never below 8 pairs, so 70 km a week gives at most 12 pairs (4.8 km). With a blank weekly distance the pool stays at 8 to 16 pairs. The Classic page still allows 4 to 30 pairs.

Classic types: continuous tempo (20 to 60 min in 5 min steps), Rowland Tempo (2 to 5 blocks), ladder (down or up), Aussie quarters (with or without the opening float), 1 min I / 1 min MP (6 to 16 reps), Pre's 200s (8 to 16 pairs), Mona fartlek, Moose fartlek (3 to 5 sets), Yasso 800s (4 to 10), Rosario 800s (3 to 8), 1km repeats (4 to 8), mile repeats (3 to 6), 30/30 (12 to 24) the marathon-pace long run (12 to 26km, half at marathon pace) and six Daniels sessions (cruise intervals, descending T, timed hard reps, R repeats, R sets and MP with T surges; see the Classic Session Generator methodology). Other options use the Classic Session Generator's defaults.

Sub-Threshold types: reps of 200, 300 and 400m (added 2026-11-20 at P's request; faster than sub-threshold, so the page names them by distance) and 3, 6, 8, 10, 12, 15 and 20 minutes. Distance reps are timed by the Sub-Threshold Session Generator's own method: the rep time at which time equals distance × pace. Rep count runs from half the usual low end (at least 2) up to the usual high end. Recoveries are the Sub-Threshold Session Generator's and are walked at 10:00/km for TSS.

Because the coin flip is first, Sub-Threshold sessions come up about half the time even though they are ten of about twenty-three types. The page keeps the same draw when the inputs change, so the session refits instead of jumping.

## Fitting the time

- The full session, warm-up and cool-down included, must be at most the time available and at least 70% of it.
- Warm-up and cool-down: 10 + 10 min for 60, 90 and 120 minutes, 8 + 8 for 45, 5 + 5 for 30, at the Classic Session Generator's easy pace (65% of 5km speed). The marathon-pace long run has none.
- Short sessions (2026-11-23, P: shorter workouts are the intense ones, so a longer warm-up suits them): a session that would run under 70% of the slot gets a longer warm-up and cool-down, each up to 20 min, aiming for 90% of the slot (the same FILL as above, my choice). It is not used if the session still does not fit. Sessions with no warm-up (marathon pace long run, MP with T surges) are never extended. Applies to sub-threshold and Classic sessions alike. This lets Pre's 200s (12 pairs under the 7% cap) appear in a 60 minute slot, with about 17 + 17 min.
- Within a session type, only versions that fill the slot are drawn: those within 90% of the longest version that fits (added 2026-11-20, P: a 60 minute slot should give 9 or 10 × 3 min, not 6 × 3 min). A type with a fixed length, like the Mona fartlek, still appears if it fits at 70% or more.
- If no session in the picked family fits, the other family is used. If none fits at all, the page says so.

## Known limits

- Short slots drop sessions that need more time (mile repeats and 1km repeats do not fit 30 minutes; a 10 × 3 min sub-T does not fit 45).
- Without a weekly distance, the sub-threshold rep ranges use only the generator's absolute limits, not a share of weekly mileage. The Classic Session Generator applies no weekly-volume limits either.
- A random pick can be a hard day after a hard day. Nothing here knows what you did yesterday.

## Treadmill incline (P, 2026-11-23)

Same optional incline box as the Classic Session Generator (belt pace, belt distance and belt speed; see its methodology). Does not change which session is drawn, its times or its TSS.

## Units (P, 2026-11-24)

Same as the Classic Session Generator: the unit box also sets pace, distance and belt speed display. Does not affect the draw.
