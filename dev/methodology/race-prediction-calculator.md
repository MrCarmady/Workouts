# Race Prediction Calculator: methodology

Takes one race result (distance and time) and predicts times, paces per km and paces per mile for 1500m, mile, 3km, 5km, 10km, 10 miles, half marathon and marathon.

## What is standard and what is a choice

| Item | Status |
|---|---|
| Riegel formula, exponent 1.06 | Published, widely used |
| Slowing the 5km equivalent from a result shorter than 5km by 6.5 × ln(5 / km) s/km | My estimate. The coefficient was lowered from 10.6 to 8 because the 5km PB it was first set from is thought to be soft, then to 6.5 as a halfway point between 8 and what the Daniels-Gilbert (VDOT) equations imply, which is about 3 to 6 s/km depending on distance and fitness (see below) |
| No adjustment between 5km and the half marathon | Chosen here |
| Marathon = 2.10 × half marathon at 70+ miles a week, 2.13 at 60, 2.17 at 50, 2.25 at 35 or less; 70 miles assumed when blank | 2.10 is the author's; the rest are placeholders. Not fitted to data |
| Distances offered | Chosen here |

The adjustments were set by judgement. The short-race one rests on a single runner's untrained mile, so it is weak evidence. Treat them as starting points.

## Step 1: Riegel base

For a result of time `t` over `D` km, the Riegel pace at 5km is:

```
riegel5 = t * (5 / D) ^ 1.06 / 5       (s/km)
```

## Step 2: short-race adjustment

Riegel from a short race is optimistic about the 5km, so the 5km equivalent is slowed:

```
adj(km) = 6.5 * ln(5 / km)   for km < 5      adj(km) = 0   otherwise
(1500m: 7.8s/km, mile: 7.4, 3km: 3.3)
p5 = riegel5 + adj(D)

Where 6.5 comes from: plain Riegel gives a 5km that is too fast from a mile or 3km, so the 5km equivalent is slowed. For a runner with a VDOT of about 55, the Daniels-Gilbert equations imply a coefficient of about 6 from a mile or 1500m, 5 from 2km and 3 from 3km (about 5 to 6 at 800m and 1000m, and falling at 4km and with lower fitness). The earlier value of 8 was slower than VDOT at every distance. The author asked for a value halfway between 8 and VDOT, and 6.5 sits within about 1 s/km of that halfway point at 1500m to 3km. For an 18:54 5km runner entering a mile of 5:23.4, the predicted 5km is now 18:32 (VDOT 18:29, previously 18:41). From a 3k of 10:44.80 it is 18:45 (VDOT 18:35, previously 18:49). A single logarithmic coefficient cannot follow VDOT's curve at all distances.
```

## Step 3: beyond the half marathon

Paces beyond the half marathon get an extra slowing that is 0 at the half marathon (21.0975km) and rises linearly to `offM` s/km at the marathon (42.195km):

```
off(km) = 0                                                for km <= 21.0975
off(km) = offM * (min(km, 42.195) - 21.0975) / 21.0975     otherwise
```

`offM` is set from the weekly distance. With the field blank, 70 miles a week is assumed.

The marathon is set to `F` times the half marathon, where `F` is a straight line through these points (weekly distance in miles). Changed 2026-10-15 from "twice the half marathon plus 7 to 25 minutes" to a percentage, so the adjustment scales with the runner.

| Weekly distance | F |
|---|---|
| 70 or more | 2.10 |
| 60 | 2.13 |
| 50 | 2.17 |
| 35 or less | 2.25 |

```
H0 = half marathon time and M0 = marathon time from Riegel with no offset, both from the input race
offM = max(0, (F * H0 - M0) / 42.195)     (s/km)
```

Riegel with exponent 1.06 already puts the marathon at 2.085 times the half marathon. The mileage term adds only the remainder up to `F`. It is never negative, so a runner whose Riegel result is already above `F` keeps it.

Where the numbers come from:
- 2.10 at 70 miles or more is the author's figure (a 1:40 half converts to 3:30 on 70-mile weeks). One cross-check, not a fit: Kejelcha's half of 56:51 and marathon of 1:59:41 (as given by the author, not verified by me) is a ratio of 2.105, so there is no separate band above 70 miles. Elites at 130+ miles a week have about the same ratio. The old 80+ band (twice the half plus 7 min, ratio about 2.07 for a 1:40 half) would have been too fast for him.
- 2.13, 2.17 and 2.25 keep the shape of the old table (+13, +17 and +25 min) converted to factors at a 100-minute half. They are placeholders, not fitted. The author's two low-mileage marathons (1:39 half, 4:05 marathon and 1:29 half, 3:31 marathon, both blow-ups, ratios 2.48 and 2.37) suggest the low end may be too optimistic, but weekly distance for those blocks is not known.
- The old points came from the Vickers & Vertosick figures below and the 42cal article's reading of them. I could not read the model equations, so they are not used here. The slide between points is linear by choice.

The closest published work is Vickers & Vertosick (2016, BMC Sports Science, Medicine and Rehabilitation, 2,303 recreational runners). There, Riegel with k = 1.07 predicted marathon times 10 minutes or more too fast for about half of runners, and models that add typical weekly mileage cut that to about 25%. Below 35 miles a week the adjustment stops at 2.25 and the page says so.

## Step 4: prediction for a target distance `T`

```
pace(T) = (p5 - adj(T)) * (T / 5) ^ 0.06 + off(T) - off(D)       (s/km)
time(T) = pace(T) * T
```

- `(T/5)^0.06` is the pace form of Riegel: exponent 1.06 on time becomes 0.06 on pace.
- `adj(T)` is subtracted for short targets, so the same adjustment works in both directions. A 5km runner's 1500m is predicted 7.8s/km faster (before the distance scaling) than plain Riegel would give.
- `- off(D)` removes the long-distance slowing already in the input when the input is a marathon.
- The input race always reproduces its own time exactly.

## Worked example: 20:00 5km

- `riegel5` = 240s/km, `adj` = 0, so `p5` = 240.
- Half marathon: 240 × (21.0975 / 5) ^ 0.06 = 262s/km, which is 4:22/km and 1:32:00.
- Marathon: 240 × (42.195 / 5) ^ 0.06 + 5 = 278s/km, which is 4:38/km and 3:15:20.
- 1500m: (240 − 7.8) × (1.5 / 5) ^ 0.06 = 216.0s/km, which is a time of 5:24.

## Plausibility check

The page rejects a result whose Daniels–Gilbert VDOT (of the raw race result) is below 15 or above 85. The bounds are my choice: the best performances on record are around 80 to 85. This catches a distance and time that don't belong together, such as a 3km time entered against 5km.

## Input limits

The page shows an error when the time can't be read, when the VDOT check above fails, or when the time over the chosen distance gives a pace outside 2:00 to 12:00 per km. These are sanity limits I chose.

## Limits

- Riegel and these adjustments are rules of thumb for a trained runner with a comparable preparation for each distance. They do not account for course, weather, pacing or distance-specific training.
- Predictions are most reliable close to the input distance, and least reliable at the extremes (for example 1500m from a marathon time).
- The 5km to half marathon relationship is most reliable for intermediate runners on moderate mileage. It may be less reliable for beginners and for runners on low mileage. This is the author's judgement, not tested here. Vickers & Vertosick (2016) found Riegel reasonable up to the half marathon in a mostly recreational sample (median 30 miles a week), but the main text does not report that by runner type.
- The marathon adjustment is small and is a guess. Long runs, fuelling and heat dominate real marathon outcomes.

## Shared race result

This page shares its race distance and time with the Sub-Threshold Session Generator, the Race Prediction Calculator, the Run TSS Calculator and the Run TSS Planner. The values are kept in the browser's local storage under one key. The last page you edited sets the value for the others. It applies only on the hosted site, where the pages share an origin, and only in the same browser on the same device. It does not sync between devices. If a stored distance is missing from a page's list (the 10 miles and marathon options exist only on the predictor), that page keeps its own distance.
