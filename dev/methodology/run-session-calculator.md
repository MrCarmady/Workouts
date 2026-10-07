# Sub-Threshold Session Generator: methodology

Takes a recent race result and a rep length (a time or a distance) and returns the rep pace, recovery and suggested rep count, with an optional treadmill-incline adjustment.

## What is published and what is an estimate

| Part | Status |
|---|---|
| Riegel race-time formula (exponent 1.06) | Published |
| ACSM running equation (treadmill mode) | Published |
| Rep length → race-pace distance mapping at 3, 6 and 10 minutes | Copeland's book, **as relayed to the author; not checked against the book**. The book revises his earlier online guidance, which the "Source check" compares with the page (the page's fast ends are faster) |
| 8, 12, 15, 20 minute anchors | **Interpolated or extrapolated** from the three above |
| 200m, 300m and 400m pace rules, 15km tempo rule | **Author's estimates** |
| Slow-downs for short-race inputs and for marathon pace | **Author's estimates** |
| Interpolation between anchors (linear in rep time) | **Chosen here** |
| Recoveries at the anchors | Rules given by the author |
| Suggested rep counts | **Author's estimates**, not sourced |

Treat every pace as a starting point and check it against heart rate or feel.

## Step 1: 5km pace from the race result

```
riegel5 = time * (5 / distance_km) ^ 1.06 / 5          // s per km at 5km
adj(km) = 8 * ln(5 / km)  for km < 5, else 0           // s/km
p5      = riegel5 + adj(input distance)
```

The `adj` slows 5km equivalents that come from short races, because the formula is too optimistic from there. It is the same adjustment as in the Race Prediction Calculator. The coefficient (8) is an estimate.

## VDOT display

The result shows the VDOT of the 5km equivalent (`p5 * 5` seconds over 5000m), using the Daniels–Gilbert formulas. `v` is speed in m/min and `t` is time in minutes:

```
VO2   = -4.60 + 0.182258 * v + 0.000104 * v^2
%VO2  = 0.8 + 0.1894393 * e^(-0.012778 * t) + 0.2989558 * e^(-0.1932605 * t)
VDOT  = VO2 / %VO2
```

A 20:00 5km gives 49.8, which matches the published value. It is display-only: paces come from Riegel, not VDOT tables. For a 5km, 10km or half marathon input it equals the standard VDOT of that result. For a mile or 3km input it is lower than the VDOT of the raw race, because the 5km equivalent includes the short-race adjustment.

## Plausibility check

The page rejects a result whose Daniels–Gilbert VDOT (of the raw race result) is below 15 or above 85. The bounds are my choice: the best performances on record are around 80 to 85. This catches a distance and time that don't belong together, such as a 3km time entered against 5km.

## Step 2: pace for any race distance

```
racePace(km) = p5 * (km / 5) ^ 0.06 + off(km) - off(input distance)

off(km) = 0                                              for km <= 21.0975
        = 5 * (min(km, 42.195) - 21.0975) / (42.195 - 21.0975)   above that
```

`off` slows paces beyond the half marathon, rising linearly to `offM` s/km at the marathon. `offM` is set so the marathon equals twice the half marathon plus 7 min at 80 miles (129km) a week or more, plus 10 min at 70 miles (113km), 13 at 60, 17 at 50, and 25 at 35 miles (56km) or less, in straight lines between those points (never negative). With no weekly distance, 70 miles is assumed. This is the same rule as the Race Prediction Calculator, whose methodology gives the formula and its status as my estimate. It changes the marathon pace anchor and the long tempo paces. Subtracting `off(input distance)` makes a 10km or half marathon input reproduce itself.

## Step 3: anchor reps

Each anchor has a fast and a slow pace in s/km, a duration, a recovery and a total-work range. The fast end uses the shorter race distance.

| Anchor | Pace basis | Recovery | Total work (min) |
|---|---|---|---|
| 200m | 0.91 × p5 to 0.96 × p5 | 90s | 12–15 |
| 300m | p5 − 2 to p5 + 2s/km | 45s | 17–22 |
| 400m | racePace(8) to racePace(10) | 45s | 20–26 |
| 3 min | racePace(14) to racePace(16) | 60s | 24–30 |
| 6 min | racePace(20) to racePace(21) | 60s | 24–36 |
| 8 min | racePace(23) to racePace(26) | 82.5s | 24–32 |
| 10 min | racePace(25) to racePace(30) | 82.5s | 20–40 |
| 12 min | racePace(30) to racePace(35) | 120s | 24–48 |
| 15 min | racePace(35) to racePace(40) | 195s | 30–60 |
| 20 min | racePace(40) to racePace(42.195) | 195s | 40–80 |
| 15km tempo | marathon pace × 1.03 to × 1.06 | none | one continuous run |
| 20km tempo | marathon pace × 1.03 to × 1.06 | none | one continuous run |

The duration of a distance anchor is its distance times its mid pace. The tempo duration is 15km times its mid pace. The recovery values for 8 to 20 minutes are the midpoints of the ranges given by the author (75–90s, 150–240s) and are rounded to 5s in the output.

## Step 4: any rep length

- **Rep given as a time:** find the two anchors either side of it and interpolate the fast pace, slow pace, recovery and total work linearly in time.
- **Rep given as a distance `d`:** find the time `t` where `t = d × midpace(t)` by bisection, then proceed as above.
- **Range:** from the 200m anchor (about 45s at a 20:00 5km) to a 20km continuous run. Between 15 and 20km the pace stays at the tempo range. Outside this the page shows an error rather than extrapolating.
- **Output distance (time input):** `t / midpace`, rounded to 50m under 4 minutes and 100m above, shown as "ca.".
- **Output time (distance input):** distance times the fast and slow paces.
- **Suggested reps:** total work low and high, divided by rep time and rounded, at least 1. The high end is also capped so that reps × rep distance is at most 25km of flat distance (**author's rule**), so a 12km rep shows 1, and a 4.8km rep still shows up to 4. When the high end is 1, the page shows "1 (continuous)" and no recovery.
- **Recovery:** interpolated, rounded to 5s.
- **Beyond the 20 minute anchor:** total work (40–80 min) stays at the 20 minute value. The tempo anchors only set pace. Recovery rises linearly from 195s at 20 minutes to 300s at 40 minutes, then stays at 300s (**author's estimate, not sourced**). A 58 minute rep shows "1 (continuous)" with no recovery. A 38 minute rep shows 1–2 reps with 5:00 recovery.

## Session limits and weekly distance cap

**Absolute session limits** (apply with or without a weekly distance, and are the author's adaptation of Daniels):

| Rep length | Intensity | Limit |
|---|---|---|
| 200m | mile pace | 5km of work (Daniels says 5 miles; the page uses 5km as the more conservative choice) |
| 300m | 5km pace | 10km of work (Daniels: lesser of 10km and 8% of weekly distance) |
| 400m | 8–10km pace | 10km of work (the author's cap) |
| 3 up to 12 minutes | sub-threshold | one hour of work (the author's cap) |
| 15 minutes and longer, up to the 20km run | marathon pace | two hours of work |

All are further capped at 25km of total session distance. A single rep can still be up to 20km.

**Weekly distance cap (optional).** If a weekly distance is entered (km or miles, between 30 and 300km), the top of the suggested rep range also cannot exceed Daniels' maximum share of it:

| Rep length | Share of weekly distance |
|---|---|
| 200m | 5% |
| 300m | 8% |
| 400m | 10% |
| 3 up to 12 minutes | 12% (**author's change**: Daniels' 10% is for T-pace, and most of these sessions are below T) |
| 15 minutes and longer | 20% |

The percentages and distance limits were checked against secondary sources quoting Daniels (see "Source check"), not against the book. Daniels gives 20% for marathon-paced work, and the page uses it. Where he gives a distance, the page's limit can differ (see the table below the check).

**Low-mileage floor:** the weekly limit never drops below 2km of mile-paced work, 4km of 5km-paced work or 6km of slower work (**author's judgement**, set so that low-mileage runners still get a usable session).

```
weeklyMaxKm = max(weeklyKm * share, floorKm)      // floorKm: 2 (200m), 4 (300m), 6 (400m and longer)
topReps     = min(floor(weeklyMaxKm / repDistance), floor(absolute limit / rep size), floor(25km / repDistance))
bottom      = the unchanged estimate from total work, never above the top
```

Weekly distance below 30km (19 miles) or above 300km (186 miles) is rejected (author's limits). When even one rep exceeds the weekly limit, the page shows 1 rep with a short warning under the rep count. With no weekly distance entered, only the absolute limits apply.

## Session load (TSS)

The page estimates the running TSS of the generated session. It uses the same definition as the Run TSS Calculator:

```
TSS_part  = (minutes / 60) * (thresholdPace / pace)^2 * 100
TSS       = round(warm-up and cool-down) + round(reps) + round(recoveries)
```

| Part | Time | Pace |
|---|---|---|
| Warm-up and cool-down | minutes entered (default 10 + 10) | the pace entered, or by default 62.5% of 5km speed, the middle of 55–70% (**author's rule**); the page shows the default as the placeholder. On a treadmill, enter the flat-equivalent pace |
| Reps | reps × rep time | middle of the rep pace range; the flat-equivalent pace on a treadmill |
| Recoveries | (reps − 1) × recovery time | walking at 6km/h, which is 600s/km (**author's rule**) |

- **Threshold pace** is `racePace(16)`, the predicted pace at about 16km, from the race result. This is the same rule of thumb as in the TSS calculator.
- **Warm-up and cool-down pace** accepts 2:00 to 15:00 per km; blank uses the default.
- **Reps** default to the middle of the suggested range, rounded. A number entered overrides it, from 1 to 100. The page notes when the number is outside the suggested range, above or below.
- **Total time** is warm-up + cool-down + reps + recoveries.
- The recovery time per rep is the one shown in the recovery tile, which stays at its 20-minute value above 20 minutes of rep length plus the extension described above.

Worked example at a 20:00 5km, 6 minute reps, 5 reps, 10 + 10 minutes of warm-up and cool-down: threshold 4:17, warm-up and cool-down 15, reps 49, recoveries 1, total 65 TSS in 54:00.

## Source check (5 October 2026)

None of these is the primary text. All are web pages quoting the guidance.

**Daniels weekly limits** (VDOT O2 training definitions, a Daniels' Running Formula chapter 4 reading note, the Hillrunner "Basics of Speed Training" page, and Coach Ray's summary):

| Pace | What the sources say | What the page does |
|---|---|---|
| Threshold (T) | About 10% of weekly mileage per session; one source states it per week | 10% for 400m, 12% for 3 to 12 minute reps (**author's change**) |
| Interval (I) | Lesser of 10km and 8% of weekly mileage | 8% share and a 10km cap for 300m reps. The 10km cap is also applied to 400m |
| Repetition (R) | Lesser of 5 miles and 5% of weekly mileage | 5% share and a 5km cap (more conservative than 5 miles, **author's choice**) |
| Marathon (M) | Lesser of 20% of weekly mileage and 18 miles; or a single run of 110 minutes (1:50) or 18 miles | 20% share, a 2 hour cap (**author's choice; Daniels' figure is 110 minutes**) and a 25km session cap (Daniels' 18 miles is about 29km) |

- The "15–20%" figure for marathon-paced work was not found in any of these sources. They say 20%.
- One source adds that a single repetition-pace bout should not exceed 2 minutes.

**Rep length to race pace** (a web archive of the best posts from the LetsRun Norwegian Singles thread; the page does not name an author, so the link to James Copeland is not confirmed):

| Source | Page anchor |
|---|---|
| 3 to 4 minute reps at 10 mile to 15km pace, 60s rest | 3 min at 14–16km pace, 60s rest |
| 6 to 8 minute reps at half marathon pace, 60s rest | 6 min at 20–21km, 8 min at 23–26km, 60s and 75–90s rest |
| 10 to 12 minute reps at 30km pace, 60s rest | 10 min at 25–30km, 75–90s rest |
| 1km reps (usually 8 to 12) at 10 mile to 15km pace, 60s rest | not an anchor |
| 400m or 1 minute reps at 10km pace, 30s rest | 400m at 8–10km pace, 45s rest |

- The 6 minute anchor is close to the source. The 3 and 10 minute anchors reach faster than the source at their fast end (12km against 15km, and 25km against 30km).
- The source gives 60s rest across 3 to 12 minute reps. The page's recoveries for 8 minutes and longer are longer, and are author's estimates.
- The source also says sub-threshold work should be 20–25% (maybe 30%) of weekly running time, and easy runs no higher than 65% of MAS. The page does not use either.
- A third-party Norwegian Singles calculator uses a different convention (3 min reps 5–7s/km faster than threshold, 6 min at threshold, 10 min 5–7s/km slower). It does not name Copeland either.
- I could not read James Copeland's book, so the original wording is unchecked. The author keeps the page's anchors because the book revises these earlier online figures. The author found 12km pace too fast for 3 minute reps; the range was left unchanged.

## Treadmill mode

Uses the ACSM running equation, with `S` in m/min and `G` as grade (0.035 for 3.5%):

```
VO2 = 0.2 * S + 0.9 * S * G + 3.5
belt speed = flat speed / (1 + 4.5 * G)
belt pace  = flat pace  * (1 + 4.5 * G)
```

At 3.5% incline the factor is 1.1575, so belt speed is 86% of flat speed. Rep times stay the same as flat. A time input shows the belt distance with the flat equivalent underneath. A distance input is the flat distance and shows the belt distance underneath.

No offset is added for the lower air resistance of treadmill running, by design. See the Treadmill Flat Equivalent methodology for the comparison with the Hillrunner table. The choice is to take the equation as is and err on the easy side, because for sub-threshold work running too easy costs less than running too hard. The equation ignores your treadmill's calibration, heat and the mental load of treadmill running. The Treadmill Flat Equivalent page has a display error input; this page does not.

## What changed from the earlier version

- The fixed table of rows is replaced by a single rep-length input.
- The short-race adjustment changed from fixed 5/5/2s/km to `8 × ln(5/km)`.
- The reference-paces panel (5km, 10km, half marathon, marathon paces) is removed. A VDOT tile (of the 5km equivalent) is shown with the result.
- The anchors, paces and rep counts at the original rep lengths are unchanged.

## Worked example: 20:00 5km, flat

- p5 = 240s/km (4:00).
- 400m: racePace(8) = 4:07, racePace(10) = 4:10, so 4:07–4:10 and 99–100s per rep.
- 3 min: 4:15–4:17, ca. 700m, 8–10 reps, 60s recovery.
- 4.5 min (between the 3 and 6 minute anchors): 4:17–4:19, ca. 1.0km, 5–7 reps.
- 15km tempo: marathon pace is 4:38, so 4:46–4:54 and 72–74 min.

## Shared race result

This page shares its race distance and time with the Sub-Threshold Session Generator, the Race Prediction Calculator, the Run TSS Calculator and the Run TSS Planner. The values are kept in the browser's local storage under one key. The last page you edited sets the value for the others. It applies only on the hosted site, where the pages share an origin, and only in the same browser on the same device. It does not sync between devices. If a stored distance is missing from a page's list (the 10 miles and marathon options exist only on the predictor), that page keeps its own distance.

## Hand-off to the Run Load Planner

On the hosted site, the session load has an "Add to Run Load Planner" link. It opens the planner with the session's TSS and a short label in the address (`run-load-planner.html?tss=65&name=5x 6 min`). Nothing is stored. The link is hidden in the standalone artifact, where the planner page is not next to it.
