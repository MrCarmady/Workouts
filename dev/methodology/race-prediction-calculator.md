# Race Prediction Calculator: methodology

Takes one race result (distance and time) and predicts times, paces per km and paces per mile for 1500m, mile, 3km, 5km, 10km, 10 miles, half marathon and marathon.

## What is standard and what is a choice

| Item | Status |
|---|---|
| Riegel formula, exponent 1.06 | Published, widely used |
| Slowing the 5km equivalent from a result shorter than 5km by 8 × ln(5 / km) s/km | My estimate. The coefficient was lowered from 10.6 to 8 because the 5km PB it was first set from is thought to be soft |
| No adjustment between 5km and the half marathon | Chosen here |
| Marathon = 2 × half marathon + 7 min at 80+ miles a week, + 10 at 70, + 13 at 60, + 17 at 50, + 25 at 35 or less; 70 miles assumed when blank | My estimate, set by judgement. Not fitted to data |
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
adj(km) = 8 * ln(5 / km)   for km < 5      adj(km) = 0   otherwise
(1500m: 9.7s/km, mile: 9.1, 3km: 4.1)
p5 = riegel5 + adj(D)
```

## Step 3: beyond the half marathon

Paces beyond the half marathon get an extra slowing that is 0 at the half marathon (21.0975km) and rises linearly to `offM` s/km at the marathon (42.195km):

```
off(km) = 0                                                for km <= 21.0975
off(km) = offM * (min(km, 42.195) - 21.0975) / 21.0975     otherwise
```

`offM` is set from the weekly distance. With the field blank, 70 miles a week is assumed.

The marathon is set to twice the half marathon plus `X` minutes, where `X` is a straight line through these points (weekly distance in miles):

| Weekly distance | X |
|---|---|
| 80 or more | 7 min |
| 70 | 10 min |
| 60 | 13 min |
| 50 | 17 min |
| 35 or less | 25 min |

```
X = 7                                   for weekly >= 80
X = 7 + (80 - weekly) / 10 * 3          for 70 <= weekly < 80
X = 10 + (70 - weekly) / 10 * 3         for 60 <= weekly < 70
X = 13 + (60 - weekly) / 10 * 4         for 50 <= weekly < 60
X = 17 + (50 - weekly) / 15 * 8         for 35 < weekly < 50
X = 25                                  for weekly <= 35

H0 = half marathon time and M0 = marathon time from Riegel with no offset, both from the input race
offM = max(0, (X * 60 - (M0 - 2 * H0)) / 42.195)     (s/km)
```

Riegel with exponent 1.06 already puts the marathon about 8.5% above twice the half marathon (6.8 min for an 80-minute half). The mileage term adds only the remainder up to `X`. It is never negative, so a slower runner at high mileage keeps the plain Riegel result, which can be above `X`.

Where the numbers come from: all of them are my judgement, set with the author, not fitted to data. 7 min is for a well-trained club runner (elites lose almost nothing). 10 min at 70 miles was chosen because the author says a common 70-mile Pfitzinger plan assumes about that conversion; I have not checked that against Pfitzinger's books. 25 min at 35 miles is the author's figure for a low-mileage marathon build, raised from 20 because a runner's fuelling capacity and muscular endurance should still grow with mileage. The 60 and 50 mile points (13 and 17 min) were added after comparing with the Vickers & Vertosick figures below: a straight line from 10 at 70 to 25 at 35 gave +16 at 56 miles, where the 42cal article's reading of that study gives about +12 for a 1:45 half marathon. The article reports that at 60 miles Riegel overestimates by about 1 min and at 20 miles by 20+ min; I have not verified its calculation or read the paper. The 13 and 17 min points are a compromise between the two, not a fit. The slide between points is linear by choice.

The closest published work is Vickers & Vertosick (2016, BMC Sports Science, Medicine and Rehabilitation, 2,303 recreational runners). There, Riegel with k = 1.07 predicted marathon times 10 minutes or more too fast for about half of runners, and models that add typical weekly mileage cut that to about 25%. I could not read the model equations, so they are not used here. Below 35 miles a week the adjustment stops at +25 min and the page says so.

## Step 4: prediction for a target distance `T`

```
pace(T) = (p5 - adj(T)) * (T / 5) ^ 0.06 + off(T) - off(D)       (s/km)
time(T) = pace(T) * T
```

- `(T/5)^0.06` is the pace form of Riegel: exponent 1.06 on time becomes 0.06 on pace.
- `adj(T)` is subtracted for short targets, so the same adjustment works in both directions. A 5km runner's 1500m is predicted 9.7s/km faster (before the distance scaling) than plain Riegel would give.
- `- off(D)` removes the long-distance slowing already in the input when the input is a marathon.
- The input race always reproduces its own time exactly.

## Worked example: 20:00 5km

- `riegel5` = 240s/km, `adj` = 0, so `p5` = 240.
- Half marathon: 240 × (21.0975 / 5) ^ 0.06 = 262s/km, which is 4:22/km and 1:32:00.
- Marathon: 240 × (42.195 / 5) ^ 0.06 + 5 = 278s/km, which is 4:38/km and 3:15:20.
- 1500m: (240 − 9.7) × (1.5 / 5) ^ 0.06 = 214.3s/km, which is a time of 5:21.

## Plausibility check

The page rejects a result whose Daniels–Gilbert VDOT (of the raw race result) is below 15 or above 85. The bounds are my choice: the best performances on record are around 80 to 85. This catches a distance and time that don't belong together, such as a 3km time entered against 5km.

## Input limits

The page shows an error when the time can't be read, when the VDOT check above fails, or when the time over the chosen distance gives a pace outside 2:00 to 12:00 per km. These are sanity limits I chose.

## Limits

- Riegel and these adjustments are rules of thumb for a trained runner with a comparable preparation for each distance. They do not account for course, weather, pacing or distance-specific training.
- Predictions are most reliable close to the input distance, and least reliable at the extremes (for example 1500m from a marathon time).
- The marathon adjustment is small and is a guess. Long runs, fuelling and heat dominate real marathon outcomes.

## Shared race result

This page shares its race distance and time with the Sub-Threshold Session Generator, the Race Prediction Calculator, the Run TSS Calculator and the Run TSS Planner. The values are kept in the browser's local storage under one key. The last page you edited sets the value for the others. It applies only on the hosted site, where the pages share an origin, and only in the same browser on the same device. It does not sync between devices. If a stored distance is missing from a page's list (the 10 miles and marathon options exist only on the predictor), that page keeps its own distance.
