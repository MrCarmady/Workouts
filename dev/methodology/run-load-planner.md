# Run Load Planner: methodology

Starts from your current CTL and ATL and either:

1. Projects CTL, ATL and TSB day by day for up to 14 days of planned TSS, or
2. Solves for the build and taper TSS needed to reach a target CTL and a target TSB on the last day, in a chosen number of weeks (1 to 16).

## Definitions

- **ATL** (acute training load, "fatigue"): exponentially weighted average of daily TSS with a 7-day time constant.
- **CTL** (chronic training load, "fitness"): the same with a 42-day time constant.
- **TSB** (training stress balance, "form"): CTL minus ATL. Positive means fresher, negative means carrying fatigue.

The difference between CTL and ATL is TSB. It measures freshness, not training effect.

## What is standard and what is a choice

| Part | Status |
|---|---|
| Exponential weighting with 7 and 42 day constants | Common convention for performance-management charts |
| TSB = CTL − ATL, using end-of-day values | Chosen here. Some platforms compute TSB from the previous day's values, so results can differ by a day |
| Daily TSS cap of 300 (forward mode) and average cap of 150 per day | **Author's choices** to reject unrealistic input |
| Same TSS every day for the target solver | A simplification. With rest days, training days need a higher TSS to reach the same total, and an uneven spread changes the result slightly |

## Daily update

```
dA = exp(-1/7)
dC = exp(-1/42)

ATL_new = ATL * dA + TSS * (1 - dA)
CTL_new = CTL * dC + TSS * (1 - dC)
TSB     = CTL_new - ATL_new
```

Rest days use TSS = 0. This is the same as `new = old + (TSS − old) × (1 − e^(−1/τ))`.

Worked example: ATL 52, CTL 48, then TSS 55 on day 1.
- ATL = 52 × 0.8669 + 55 × 0.1331 = 52.4
- CTL = 48 × 0.9764 + 55 × 0.0236 = 48.2
- TSB = 48.2 − 52.4 = −4.2

## Forward mode

Apply the daily update for each planned day. The page shows CTL, ATL and TSB after every day, the total TSS, and the TSS in the first 7 days when the plan is longer than a week.

The user picks the weekday the plan starts on (default: today). Day `d` is labelled `Mon…Sun` as `(start + d − 1) mod 7`. The labels are cosmetic and do not change the calculation.

## Target mode: build, then taper

The user sets a target CTL and a target TSB for the last day, a number of weeks `W`, and a taper length of `k` days (7, 10, 14 or 21). Train at a constant daily TSS `T` for the build phase (`B = 7W − k` days), then at a constant daily TSS `S` for the `k` taper days.

A constant load alone cannot be used for a TSB target: CTL and ATL both converge on the daily load, so TSB drifts towards 0. A positive TSB such as +10 needs a taper.

Let `cB = dC^B`, `aB = dA^B`, `ck = dC^k`, `ak = dA^k`. The end values are:

```
CTL_N = CTL0*cB*ck + T*(1 - cB)*ck + S*(1 - ck)
ATL_N = ATL0*aB*ak + T*(1 - aB)*ak + S*(1 - ak)
```

The targets give `CTL_N = Ct` and `ATL_N = Ct - Bt` (since TSB = CTL − ATL). That is two linear equations in `T` and `S`:

```
p1*T + q1*S = r1      p1 = (1 - cB)*ck    q1 = 1 - ck    r1 = Ct - CTL0*cB*ck
p2*T + q2*S = r2      p2 = (1 - aB)*ak    q2 = 1 - ak    r2 = (Ct - Bt) - ATL0*aB*ak

det = p1*q2 - p2*q1
T = (r1*q2 - r2*q1) / det
S = (p1*r2 - p2*r1) / det
```

The page leads with the build TSS per week (7 × T) and gives the taper TSS per day and per week (7 × S).

Worked example: CTL 48, ATL 52, target CTL 55 and TSB +10 in 4 weeks with a 7-day taper.
- T ≈ 79 TSS a day for 21 days (about 554 per week), then S ≈ 26 a day for 7 days (about 181 per week).
- Simulating the 28 days day by day gives CTL 55.0 and TSB +10.0.

The taper length is a choice, not a standard. The solver returns whatever `T` and `S` satisfy both targets, so a target pair that needs a negative value is rejected.

## TSB zones

TSB is colour-coded, rounded to one decimal. The bands follow the intervals.icu convention, with two changes made for running (the larger injury risk led to a narrower optimal band and an earlier red).

| TSB | intervals.icu | This tool |
|---|---|---|
| above +20 | Transition (yellow) | De-training (yellow) |
| +5 to +20 | Fresh (blue) | Fresh (blue) |
| +5 to −10 | Grey zone | Optimal (grey) |
| −10 to −20 (−30 in intervals.icu) | Optimal (green) | Heavy (green) |
| below −20 | −30 and below: High risk (red) | High risk (red) |

The zone names are in text as well as colour. The thresholds are a judgement call, not a validated standard.

## Input limits

Nothing is shown when:

- ATL or CTL is outside 0 to 300.
- A planned day in forward mode is outside 0 to 400, or above 300, or the plan averages more than 150 per day.
- The taper leaves less than 7 days of build.
- The solved build or taper TSS is negative, so the two targets cannot both be reached in that time.
- The solved build or taper TSS is above 150 per day (1,050 per week).

## Limits

- ATL and CTL depend on how your platform computes TSS. Use TSS from the same source.
- Target mode treats every day as equal, which hides hard-easy structure. Forward mode shows a real weekly pattern, so use it to check a plan.
- The model is a simple smoothing of past load. It does not predict performance or injury.

## Session from the generator

If the page is opened from the Sub-Threshold Session Generator's link, it shows a panel with the session's TSS. You choose the day and press Add. The TSS is added to that day's entry (summed if the day already has TSS), the plan switches to "See the effect of a plan", and the address is cleaned. Dismiss closes the panel without changing the plan. The page accepts TSS values from 1 to 300 only, the same one-day limit as the plan.
