# Treadmill Flat Equivalent: methodology

Takes a treadmill belt speed and incline and returns the flat-ground pace with the same estimated oxygen cost. The calculation is one multiplication, so the page is mainly a unit converter.

## What is standard and what is a choice

| Item | Status |
|---|---|
| ACSM running equation | Published |
| Flat equivalent from setting the oxygen costs equal | Derived here from the equation |
| No wind or treadmill offset | Chosen here |
| Display error default of 1.7% | One measurement, my treadmill against a Stryd footpod |
| Input limits (5 to 25km/h, 0 to 20% incline) | Chosen here, not taken from ACSM |

## The equation

The ACSM running equation estimates oxygen cost from speed and grade. `S` is speed in m/min and `G` is grade as a fraction (0.06 for 6%):

```
VO2 = 0.2 * S + 0.9 * S * G + 3.5      (ml/kg/min)
```

On the flat (`G = 0`), the cost of running at speed `S_flat` is `0.2 * S_flat + 3.5`. Setting the two costs equal and solving for `S_flat`:

```
0.2 * S_flat = 0.2 * S + 0.9 * S * G
S_flat = S * (1 + 4.5 * G)
```

So each 1% of incline adds 4.5% to the flat-equivalent speed, independent of speed. In pace terms:

```
flat pace = belt pace / (1 + 4.5 * G)
```

## Conversions

- Speed in mph is converted to km/h by multiplying by 1.609344.
- Pace in seconds per km is `3600 / speed in km/h`.
- Pace per mile is the per-km pace multiplied by 1.609344.

## Worked example: 10.9km/h at 6%

- Factor: 1 + 4.5 × 0.06 = 1.27.
- Flat speed: 10.9 × 1.27 = 13.84km/h.
- Flat pace: 3600 / 13.84 = 260s/km, which is 4:20/km or about 6:59/mile.
- The belt pace is 3600 / 10.9 = 330s/km, or 5:30/km.

To go the other way, use `belt pace = flat pace × (1 + 4.5 × G)`. For a 4:20/km flat equivalent at 6%, the belt pace is 260 × 1.27 = 330s/km, or 5:30/km. This matches the example above.

## Input limits

The page shows an error and no result when:

- belt speed is outside 5 to 25km/h (3.1 to 15.5 mph), or
- incline is outside 0 to 20%.

These bounds are a sanity check I chose. They are not limits stated by ACSM.

## Choices and limits

- **Wind and treadmill effect:** the equation has no term for air resistance. Some treadmill conversion tables add an offset because treadmill running at 0% is easier than the same pace outdoors. This page does not. The choice is to err on the easy side, which is safer for sub-threshold work.
- **Display error:** the page has a "Display reads fast by (%)" input, default 1.7. That figure is one measurement of my treadmill against a Stryd footpod, not a general value. True belt speed = displayed speed / (1 + error). The flat equivalent uses the true speed. Set it to 0 if your display is accurate. The value is stored in the browser and shared with the Sub-Threshold Session Generator when both pages are on the same site.
- **Incline:** the displayed incline is assumed to be accurate.
- **Steady state:** the equation is for steady-state running. It says nothing about fatigue, heat or the mental load of treadmill running.
- **Accuracy:** this is an estimate for training, not a lab measurement.

## How it compares with other approaches

These comparisons come from calculations I ran over belt speeds of about 5 to 12 mph and inclines of 1 to 10%.

- **Hillrunner treadmill table (hillrunner.com):** an empirical lookup table. Its author says it is built from 1980s and 1990s studies, is not based on a formula, and has thin data at fast speeds and steep inclines. Across 671 cells it was slower than this equation in about 97% of them, by about 24s/mile on average. The gap is roughly constant at about 4% on the flat, and it widens with speed and incline.
- **Mental-maths heuristic (1m of climb per km is worth 1s/km, so 10s/km per 1% of incline):**
  - At 11 to 13km/h and up to about 6% it stays within about 10s/km of this equation, always slower.
  - At slower belt speeds it understates the incline credit by more. The gap reaches about 63s/mile at 5 mph and 10%.
  - At faster speeds and steeper inclines the sign flips and it overstates the credit, for example by 16s/km at 14km/h and 9%.
  - It has no published source. Check results against the equation.

## Hold the flat-equivalent pace

With the box ticked, you enter the flat pace you want. Changing the incline sets the belt speed, and changing the belt speed sets the incline:

```
true belt speed = flat speed / (1 + 4.5 * grade)
display speed   = true belt speed * (1 + display error)
```

Speeds are rounded to 0.1 and inclines to 0.1, so the flat pace shown in the result can differ from the target by a second or two. A belt speed faster than the flat pace, or one needing more than 20% incline, is refused.
