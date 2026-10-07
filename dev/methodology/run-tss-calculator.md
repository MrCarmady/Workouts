# Run TSS Calculator: methodology

Takes a threshold pace (or a race result to estimate one), plus the minutes and average pace of warm-up/cool-down and of workout efforts. Returns one training stress score (TSS) for the session.

## What is published and what is an estimate

| Part | Status |
|---|---|
| Running TSS formula (hours × intensity² × 100) | Standard definition, simplified here to use pace |
| Riegel formula for estimating threshold from a race | Published |
| "Threshold is about 16km race pace" | A rule of thumb used by the author |
| Slow-down for short-race inputs (8 × ln(5 / km) s/km below 5km, the same rule as in the Race Prediction Calculator) | **Author's estimate** |
| Input limits and the 120 TSS per hour cap | **Author's choices** |

## The formula

For each part of the session:

```
intensity = thresholdPace / averagePace          // speed relative to threshold
TSS_part  = (minutes / 60) * intensity^2 * 100
TSS       = round(TSS_warmup) + round(TSS_efforts)
```

One hour at threshold pace scores 100. A longer session can score more. The total is the sum of the rounded parts so the breakdown line adds up.

Pace is used as the intensity measure with no grade or terrain correction. Recoveries between reps are not counted. To include them, add their minutes to the warm-up/cool-down line with a combined average pace.

## Estimating threshold from a race

```
riegel5 = time * (5 / distance_km) ^ 1.06 / 5          // s per km at 5km
adj     = 8 * ln(5 / distance_km)  for distance < 5km, else 0   // s/km
p5      = riegel5 + adj
threshold pace = p5 * (16 / 5) ^ 0.06                  // pace at about 16km
```

## Input limits

Results are not shown when any of these fail:

- Threshold pace outside 2:30 to 8:00 per km.
- Warm-up or effort pace outside 2:00 to 15:00 per km.
- Minutes outside 0 to 480.
- No minutes entered for either part.
- The whole session works out to more than **120 TSS per hour of total time** (`TSS / ((warm-up minutes + effort minutes) / 60)`). This catches impossible combinations such as nearly an hour at a pace far faster than threshold. A short all-out effort with no warm-up can hit the cap.

## Worked example

Threshold 4:15 (255s/km). Warm-up and cool-down 20 min at 6:30 (390s/km). Efforts 30 min at 4:25 (265s/km).

- Warm-up: (20/60) × (255/390)² × 100 = 14.3, shown as 14.
- Efforts: (30/60) × (255/265)² × 100 = 46.3, shown as 46.
- TSS = 14 + 46 = 60.

## Shared race result

This page shares its race distance and time with the Sub-Threshold Session Generator, the Race Prediction Calculator, the Run TSS Calculator and the Run TSS Planner. The values are kept in the browser's local storage under one key. The last page you edited sets the value for the others. It applies only on the hosted site, where the pages share an origin, and only in the same browser on the same device. It does not sync between devices. If a stored distance is missing from a page's list (the 10 miles and marathon options exist only on the predictor), that page keeps its own distance.
