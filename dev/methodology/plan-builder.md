# Plan Builder: methodology

Builds a block of weeks from a race result, current weekly distance, run days and a target rate of fitness gain. It is a prototype. The rules come from the author's guidelines. The constants and week layouts are my placeholders, marked below.

## What is a rule and what is a choice

| Item | Status |
|---|---|
| Quality sessions by run days: 3 days 1, 4 days 2, 6 days 3 | Author's rule |
| 5 days 2, 7 days 3 | My interpolation |
| Weekly limits by pace type: mile pace 10%, intervals 16%, threshold 20%, sub-threshold 30%, marathon pace 40% | Author's rule |
| Shared quality budget across pace types | Author's rule |
| Ramp target 1 CTL point per week, band 0.1 to 1.9. The target input is capped at 2; there is no separate maximum box | Author's rule |
| TSB at or above -10 where possible, never -20 | Author's rule |
| Daniels per-session limits | As read from secondary summaries, not checked against the book |
| Sub-threshold per-session limit of 12% of weekly distance | Author's figure: Daniels' 10% for threshold, raised to 12% because sub-threshold is easier (lower lactate) |
| Sub-threshold pace is race(21) | Author's figure: the average of sub-threshold paces, as longer reps run a little slower and shorter reps a little quicker |
| Long run weighted 1.6 times an easy day, capped at 35% of weekly distance and 150 minutes | 35% is the author's rule (Daniels' 25% is too low for 3 and 4 run days). The 1.6 is my choice. The 150 minutes is Daniels' long-run limit as summarised in a secondary source |
| No quality dose setting: every session gets its full share of the weekly limit | Author's choice, to be tested: TSB and the caps restrain the load |
| Warm-up and cool-down: 20 minutes together at least, up to 40, so a quality day takes about 80% of an easy day's time | My choice, to avoid a long easy run one day and a short quality day the next |
| Week layouts | Placeholder |

## Paces

Same model as the Race Prediction Calculator, with marathon pace set by the weekly distance entered.

- Easy: 62.5% of 5km speed, or your own pace.
- Sub-threshold: race(21), about 1.7% slower than threshold (the 16km pace).
- Threshold: the predicted 16km pace.
- Intervals: race(4).
- Mile pace: the predicted mile pace.
- Marathon pace: the predicted marathon pace.

## Quality sessions

The number of quality sessions per week comes from run days. The focus picks their types. Intervals, mile pace or marathon pace each add one session as the last quality session of the week, and the rest are sub-threshold or threshold.

Each session gets an equal share of the week's budget:

```
km = min(cap[type] * V / n, per-session cap[type])
```

`V` is weekly distance and `n` the number of quality sessions. Per-session caps, as read from secondary summaries ([notes on Daniels chapter 4](https://cdbaca.github.io/ssg/reading-daniels-running-formula-chapter-4.html), [Coach Ray's summary](https://www.coachray.nz/2023/05/03/jack-daniels-running-intensity/)):

- Threshold: 10% of V.
- Intervals: the lesser of 10 km or 8% of V.
- Repetition (mile pace): the lesser of 5 miles or 5% of V.
- Marathon pace: 110 minutes.
- Sub-threshold: 12% of V (author's figure: Daniels' 10% for threshold, raised because sub-threshold is easier).

The weekly limits and the shared budget are the author's: each km of a type uses 1 ÷ its limit of a budget of 1. There is no dose setting: each session takes its full share of the budget. TSB and the caps restrain the load. At least 60% of every week is easy.

## Easy and long runs

Each quality day includes the warm-up and cool-down, counted as easy. Together they last at least 20 minutes and grow up to 40 minutes, so the quality day takes about 80% of an easy day's time. The remaining distance goes to easy days and one long run, which counts 1.6 times an easy day. The long run stops at 35% of weekly distance or 150 minutes, whichever is lower, and the excess goes to the easy days. No easy run is longer than the long run. If the week cannot fit in the run days under those limits, the distance falls short of the target and the page says so. The page flags easy days under 20 minutes or over 2 hours.

## Load

TSS per km at pace `p` follows from the TSS definition used on the other pages:

```
TSS per km = (p / 3600) * (threshold / p)^2 * 100 = threshold^2 / (36 * p)
```

CTL and ATL are daily exponential averages:

```
CTL += (TSS - CTL) / 42
ATL += (TSS - ATL) / 7
TSB = CTL - ATL at the end of each day, the same convention and exponential constants as the Run Load Planner
```

Starting CTL is entered, or estimated as the TSS of the current weekly distance run as this plan's week, divided by 7.

## Solving each week

For each week the weekly distance is found by bisection so that CTL at the end of the week rises by the target. Three other distances are found the same way: the one that gives a ramp of 0.1, the one that keeps the lowest TSB at -10, and the one that keeps it at -20. The week uses:

```
V = min(V_target, max(V_tsb10, V_ramp_min))
V = min(V, V_tsb20)
```

So the -10 limit holds the ramp back, but not below 0.1. The -20 limit always wins. The weekly table says when a week was held back, when the lowest TSB is under -10, or when the ramp is under 0.1.

## Behaviour to know about

- Week 1 is the first step above the current load. The author accepts this: most users are runners who have just entered a race and want to push volume. A ramp of 1 from a steady state needs about 45 TSS more in the week, so week 1 shows the largest increase. In test runs this was +10% at 76 km a week, +19% at 40 km and +29% at 30 km.
- A sustained ramp of 1 pushes the lowest TSB to about -10 within three or four weeks. The week after, the solver holds the load back, then lets it rise again, so some blocks show a step-back week followed by a rise. The author accepts this: the aim of tight TSB control is to avoid unplanned down weeks, so one after a -10 week is reasonable.
- Runners with 3 run days and a high weekly distance get large days and low TSB. The flags show this.

## Taper

A taper of 7 or 14 days is optional. With 14 days, the penultimate week holds CTL (ramp 0) and the last week is the taper proper. With 7 days, only the last week is the taper. Race day replaces the long run.

The race week is solved so TSB on the morning of race day (end of the day before) equals the target. The target defaults to +10 and is capped at +10, since more is overkill (author's view). The race week is kept between 50% and 80% of the peak week's distance (author's expectation: about 50 to 80% of normal; the exact bounds are my placeholders). If the 50% floor stops the target being reached, the table says so and shows the TSB reached.

The headline CTL is the peak, at the end of the last build week, not the lower value on race day. The peak is the fitness you take into the race; the CTL model's taper decay overstates how much of it is lost (author's view). Race-day CTL is shown beside it.

The Run Load Planner holds daily TSS constant in the taper. Plan Builder does not. TSB and the CTL/ATL constants follow the same convention in both.

## Time first

The page leads with time for each run and each week, with distance second. Easy and long runs are best done by time, which removes the temptation to push easy days. Distance is derived from the easy pace entered, so an error in that pace changes the km, not the minutes.

## Limits

- It does not adapt to what was actually run.
- TSB does not capture the structural load of big jumps in weekly km. This was left open on purpose.
- Week layouts and the pace and distance placeholders are mine.
- No injury, hills, heat or race calendar inputs.
