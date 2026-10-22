# 1RM and Scheme Calculator: methodology (page file: lift-scheme-calculator)

Takes one set (lift, bodyweight, weight, reps, optional reps in reserve) and returns:

1. An estimated 1RM.
2. The weights for common set × rep schemes (3×3, 5×5, 3×10 and so on), as a % of 1RM.
3. Single-set rep maxes (1RM to 12RM).

## What is published and what is an estimate

| Part | Status |
|---|---|
| Epley and Brzycki 1RM formulas | Published, widely used |
| Averaging the two formulas | A choice made here |
| Per-set fatigue values by rep range | **Estimates, not published figures** |
| Rest multipliers (1.25 / 1.1 / 1 / 0.8) | **Estimates.** Only the 1 min value rests on one data point (50 kg bench, 5×5, 60s rest, about 0.5 RIR on the last set) |
| 1.15× fatigue for squat, deadlift and Bulgarian split squat | **Estimate.** Applying it to the split squat is my choice, as a lower-body lift |

The fatigue values are the part to calibrate against your own training logs.

## Step 1: estimate the 1RM

Let `reps` be the reps completed and `RIR` the reps left in reserve (0 if the set was to failure).

```
n = reps + RIR            // reps the set could have reached
Brzycki:  fraction(n) = (37 - n) / 36
Epley:    fraction(n) = 1 / (1 + n / 30)    // see the single-rep note below
pct(n)    = average of the two fractions
e1RM      = load / pct(n)
```

Single-rep fix: raw Epley gives a fraction of 0.968 at n = 1, so a true 1RM attempt would read about 3% above the weight lifted (100 kg × 1 gave 101.6 kg). The Epley fraction is therefore set to 1 at n ≤ 1 and interpolated linearly to its normal value at n = 2. Brzycki already gives 1 at n = 1. From n = 2 upward nothing changes. This is a patch for the single-rep case, not a published adjustment.

`load` is the weight on the bar. For weighted pull-ups and dips it is bodyweight + added weight.

The page also shows the two single-formula estimates (`load / brzycki(n)` and `load / epley(n)`) as a range. Brzycki is undefined at 37 or more reps. Both formulas get less reliable above about 10 reps, so the page warns above that and refuses n ≥ 36.

Worked example: bench 60 kg × 5, RIR 0.
- Brzycki fraction 0.8889, Epley 0.8571, average 0.8730.
- e1RM = 60 / 0.8730 = 68.7 kg (range 67.5 to 70.0).

## Entering a whole session (added 2026-10-16)

The page has a toggle, "One set" or "Whole session". The session mode works backwards from a session of identical sets (same weight, same reps).

```
f     = baseFatigue(reps) * restMultiplier * (lowerBody ? 1.15 : 1)
lost  = f * (sets - 1)              // reps of capacity lost before the last set
n     = reps + RIR + lost           // reps the first set could have reached
e1RM  = load / pct(n)
```

`RIR` is the reps in reserve after the last set. `baseFatigue` is read in a straight line between the scheme values in Step 2: 3 reps 0.75, 5 and 6 reps 1.0, 8 reps 1.2, 10 reps 1.5, 12 reps 1.6 (the straight-line join and the 1.5 at 10 reps are choices made here; the 10-rep schemes use 1.35 or 1.6). Rest options are 1 min (×1.25), 2 min (×1.1) and 3 min or more (×1).

Caveats:
- The fatigue values and rest multipliers are estimates, so a session gives a less certain 1RM than a fresh single set. The page shows the 1RM if the loss per set is 25% lower or higher.
- Sets of different reps (such as 9, 7, 6 to failure) are not supported. Enter the last set alone as a single set instead.
- One test found no difference in rep loss between 80% and 50% of 1RM (bench, five sets), so the rise in fatigue with set length is an assumption.
- Checks: 3 sets of 6 bodyweight pull-ups, 2 min rest, 2 reps in reserve at 76 kg gives about 102 kg total (about +26 kg added) and a fresh set of about 10 reps.

## Step 2: weights for set × rep schemes

The idea: if the last set must finish with a given number of reps in reserve, and each earlier set costs some reps of capacity, then fresh capacity on set 1 is bigger than the reps written on the plan. Convert that capacity back to a % of 1RM.

```
f        = baseFatigue(scheme) * restMultiplier * (lowerBody ? 1.15 : 1)
extra    = f * (sets - 1)                 // reps of capacity lost before the last set

// the user picks a last-set RIR band: 0-1, 1-2 or 2-3. Call its lower edge R.
capacityHeavy = reps + R     + extra      // fewer reps in reserve, so heavier
capacityLight = reps + R + 1 + extra

pctHeavy = pct(capacityHeavy)
pctLight = pct(capacityLight)
weight range = e1RM * pctLight  to  e1RM * pctHeavy
set 1 RIR    = R + extra  to  R + 1 + extra   (rounded)
```

Base fatigue per set, at 3 min rest (reps of capacity lost per set):

| Scheme | Base fatigue |
|---|---|
| 3×3, 5×3 | 0.75 |
| 3×5, 5×5, 3×6, 4×6 | 1.0 |
| 3×8 | 1.2 |
| 2×10 | 1.35 |
| 3×10, 3×12 | 1.6 |

Rest multipliers: 1 min ×1.25, 2 min ×1.1, 3 min ×1.0. The default "By rep range" assumes 3 min for sets of 3–5, 2 min for 6–8 and 1 min for 10–12. The 5 min option was removed (not used for higher-rep sets; its 0.8 factor was never calibrated).

Lower-body lifts (squat, deadlift, Bulgarian split squat) multiply fatigue by 1.15.

Worked example: 3×5 at 3 min rest, upper body, 1–2 RIR, e1RM 68.7 kg.
- f = 1.0, extra = 2.0, R = 1.
- Capacities 8 and 9 reps. pct(8) = 0.7975, pct(9) = 0.7735.
- Weights 53.2 to 54.8 kg (77–80%). Set 1 RIR is 3 to 4.

## Step 3: single-set rep maxes

`weight(k) = e1RM * pct(k)` for k in 1, 3, 5, 8, 10, 12. This is a fresh single set to failure, with no fatigue model.

## Display rules

- Weights round to the plate step the user chooses (1, 2.5 or 5 kg).
- For weighted pull-ups and dips the table shows added weight, with "BW" for zero and "assist" for negative.
- Example sets load per lift until the user types their own numbers.

## Limits

- Estimates from rep-based formulas are less accurate at high reps and for lifts you rarely test.
- The fatigue model assumes constant loss per set. Real fatigue depends on the lifter, the lift and the day.
- Rest changes only the fatigue multiplier. Nothing else in the model uses it.

**Dumbbell lifts (incline dumbbell bench, Bulgarian split squat):** the weight entered and shown is per hand, and the 1RM is per hand. The formulas and fatigue model are unchanged. A true single is rarely tested on these lifts, so the estimate rests on a set of 5–10 reps.

## Warm-up (2026-10-20)

The page lists a warm-up ladder for a top set. The top set is the weight for a chosen rep max (1, 3, 5 or 8RM, taken from the 1RM above) or a weight you enter.

```
barbell lifts:   bar x 10, 50% x 5, 70% x 3, 85% x 2, top set
pull-up and dip: bodyweight x 5, then 50%, 70% and 85% of TOTAL load (bodyweight + added), shown as added weight; steps at or below bodyweight are dropped
dumbbell and split squat: lightest dumbbells x 10 (bodyweight x 8 per leg for the split squat),
                 then the same percentages of the per-hand weight
```

Weights are rounded to the page's step. A set that rounds to the same weight as the one before it, or to the top set, is dropped, and a note says so. A top set at or below the bar gets no ladder.

Deadlift: the first set is a "Light pull" of 10 reps at a starting weight you set (default 50 kg, P, 2026-10-22), not the bare bar, because nobody pulls the empty bar and the gym's bumper plates (5 to 25 kg) put the usual start between 30 and 70 kg. Other barbell lifts keep the bar weight.

The ladder is the one P described (10 x bar, 10 x 50%, 5 x 70%, 2 to 3 x 85%), with 5 reps at 50% and 2 at 85% as my trims. It is a common convention, not from research. I know of no evidence that one scheme beats another. The reps and percentages are fixed on the page. A note advises 5 minutes or more of rest before a rep-max set (my suggestion).

Changed 2026-10-22 (P: the old pull-up ladder was too hard). Percentages on the added weight alone made light top sets look like 8 bodyweight reps then three near-top steps. Total-load percentages ramp the real load. A light top set (for example +10 kg on 76 kg bodyweight) gets just 5 bodyweight reps before it.
