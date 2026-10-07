# Run TSS Planner: methodology

The reverse of the Run TSS Calculator. Takes a threshold, a target TSS, the minutes of workout efforts, and the minutes and pace of warm-up/cool-down. Returns the pace to run the efforts at.

## Why the warm-up pace is an input

One target TSS cannot fix two unknown paces. The warm-up and cool-down score is worked out from the pace you enter. Whatever is left of the target is assigned to the efforts, and their pace is solved from that.

## What is published and what is an estimate

Same as the TSS calculator: the TSS formula and Riegel formula are standard, while the threshold rule of thumb (about 16km pace), the short-race slow-down (8 × ln(5 / km) s/km below 5km) and the 120 TSS per hour cap are the author's choices.

## The algebra

```
TSS_warmup = (wMin / 60) * (thr / wPace)^2 * 100       // 0 if wMin = 0
rest       = target - TSS_warmup                       // what the efforts must supply

// TSS_efforts = (eMin / 60) * q^2 * 100, where q = thr / effortPace
q          = sqrt(rest * 60 / (eMin * 100))
effortPace = thr / q
```

`q` is effort speed as a fraction of threshold speed, and the page shows it as a percentage. Speed in km/h is `3600 / effortPace`.

## Estimating threshold from a race

```
riegel5 = time * (5 / distance_km) ^ 1.06 / 5          // s per km at 5km
adj     = 8 * ln(5 / distance_km)  for distance < 5km, else 0   // s/km
p5      = riegel5 + adj
thr     = p5 * (16 / 5) ^ 0.06                         // pace at about 16km
```

## Input limits

Nothing is shown, and an error explains why, when:

- Threshold pace is outside 2:30 to 8:00 per km.
- Target is outside 1 to 600 TSS.
- Effort minutes are outside 1 to 480, or warm-up minutes outside 0 to 480.
- Warm-up pace is outside 2:00 to 15:00 per km.
- Target divided by total hours is above **120 TSS per hour**.
- The warm-up and cool-down alone already reach the target (`rest <= 0`).
- The solved effort pace is outside 2:00 to 15:00 per km.

Efforts minutes should exclude recoveries between reps.

## Worked example

Threshold 4:15 (255s/km). Target 60 TSS. Efforts 30 min. Warm-up and cool-down 20 min at 6:30 (390s/km).

- Warm-up score: (20/60) × (255/390)² × 100 = 14.3.
- Remainder: 60 − 14.3 = 45.7.
- q = sqrt(45.7 × 60 / (30 × 100)) = 0.957, which is 96% of threshold speed.
- Effort pace = 255 / 0.957 = 266.6s/km, shown as 4:27.
- Check: the TSS calculator gives 60 for those inputs.

## Shared race result

This page shares its race distance and time with the Sub-Threshold Session Generator, the Race Prediction Calculator, the Run TSS Calculator and the Run TSS Planner. The values are kept in the browser's local storage under one key. The last page you edited sets the value for the others. It applies only on the hosted site, where the pages share an origin, and only in the same browser on the same device. It does not sync between devices. If a stored distance is missing from a page's list (the 10 miles and marathon options exist only on the predictor), that page keeps its own distance.
