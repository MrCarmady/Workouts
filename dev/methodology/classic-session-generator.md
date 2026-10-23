# Classic Session Generator: methodology

Gives paces for traditional workouts from one race result. The Sub-Threshold Session Generator is built around sub-threshold reps. This page covers the more traditional sessions, most of which run at or above threshold.

## What is standard and what is a choice

| Item | Status |
|---|---|
| Pace model (Riegel 1.06, short-race adjustment, marathon slow-down by weekly distance) | Same as the Race Prediction Calculator. See [its methodology](race-prediction-calculator.html) for sources and status |
| VDOT (Daniels-Gilbert) and the 15 to 85 plausibility check | Published formula, range chosen here |
| Mona fartlek structure (2×90s, 4×60s, 4×30s, 4×15s, equal recoveries) and effort guidance (about 5k effort for the 90s, faster as the reps shorten) | As described by Nate Jenkins in his 2015 blog post on the Moneghetti fartlek |
| Mona effort paces and float pace (85% of 5km speed) | Set by the author |
| All other session structures and every pace choice below | Set by the author from his own descriptions, not published prescriptions |
| TSS = hours × (threshold pace ÷ pace)² × 100 | The same method as the other tools |

In this document, race(x) is the predicted race pace over x km, from the Race Prediction Calculator model with the weekly distance applied. Threshold pace is race(16). On the page these appear as pace names: race(5) is 5k pace, race(1.5) is 1500m pace, the mile is mile pace, and marathon pace is M pace. Race(4.5) is shown as 4.5k pace.

## Pace choices

| Session | Hard part | Easy part |
|---|---|---|
| Continuous tempo | 20 min at threshold. Longer tempos slow by 4.9% × ln(minutes ÷ 20), capped at marathon pace, up to 60 min | None |
| Ladder 5-4-3-2-1 min | 5 min at race(10), 4 at race(5), 3 at race(3), 2 at race(2), 1 at race(1.5). The paces are the author's: the Outside article on ladders gives effort, not paces | Jog after each rep of half its length by default (150, 120, 90 and 60 s), as in the article's ladder (the article's example is 5:00, 4:00, 3:00, 2:00, then repeats of 1:00 hard and 1:00 easy). Option: a fixed jog (90 s default). Option: 0 to 8 extra repeats of 1 min easy and 1 min at race(1.5) after the 1-min rep, 5-4-3-2-1 order only. The article's research ladder (3-2-1-0.75-0.5 min, jogs of two-thirds of the rep) is not built in |
| Aussie quarters | 400m at race(4) | 200m float from marathon pace to 3% faster, continuous. Float marathon pace ignores weekly distance (70-mile default). Always 8 reps (4.8km), optional 200m float first (5km) (author's decision, 2026-10-15) |
| Pre's 200s | Fast 200m from mile pace to 2% slower (race(1.609), my reading of "slightly slower than mile pace") | Float 200m (P, 2026-10-22: "float" rather than "recovery", which suggests an easy pace), 33⅓% slower than the fast ones (the article's figure), continuous with no standing rest. 12 pairs by default (4.8km, about the article's 3 miles), 4 to 30 pairs. From the Outside article on Pre's 200s, which credits Bill Bowerman; the article suggests using it before the final taper. The 2% upper end and the default pair count are mine |
| Mona fartlek structure (2×90s, 4×60s, 4×30s, 4×15s, equal recoveries) and effort guidance (about 5k effort for the 90s, faster as the reps shorten) | As described by Nate Jenkins in his 2015 blog post on the Moneghetti fartlek |
| Mona effort paces and float pace (85% of 5km speed) | Set by the author |
| All other session structures and every pace choice below | Set by the author from his own descriptions, not published prescriptions |
| TSS = hours × (threshold pace ÷ pace)² × 100 | The same method as the other tools |

In this document, race(x) is the predicted race pace over x km, from the Race Prediction Calculator model with the weekly distance applied. Threshold pace is race(16). On the page these appear as pace names: race(5) is 5k pace, race(1.5) is 1500m pace, the mile is mile pace, and marathon pace is M pace. Race(4.5) is shown as 4.5k pace.

## Pace choices

| Session | Hard part | Easy part |
|---|---|---|
| Continuous tempo | 20 min at threshold. Longer tempos slow by 4.9% × ln(minutes ÷ 20), capped at marathon pace, up to 60 min | None |
| Ladder 5-4-3-2-1 min | 5 min at race(10), 4 at race(5), 3 at race(3), 2 at race(2), 1 at race(1.5) | 90s jog (adjustable), 4 jogs |
| Aussie quarters | 400m at race(4) | 200m float from marathon pace to 3% faster, continuous. Float marathon pace ignores weekly distance (70-mile default). 8 reps by default (4.8km), optional 200m float first (5km) |
| Mona fartlek | 90s at race(5), 60s at race(4), 30s at race(3), 15s at race(1.6) | Float of the same duration after every effort, at 85% of 5km speed (my choice; the article calls it a quick jog), so the total is 20 min (10 + 10) |
| Yasso 800s | 800m at race(5) | Jog for the same time as the rep, at the warm-up pace. 10 reps by default |
| Rosario 800s | 800m at race(5) | 800m float at race(5) + 25s per 800m (31.25s/km). 4 reps by default, a float after every rep |
| 1km repeats | 1km at race(4.5) | Jog, 105s by default |
| Mile repeats | 1 mile at race(10) | Jog, 135s by default |
| 30/30 | 30s at race(3) | 30s jog |
| Marathon-pace long run | Chosen distance at marathon pace (12km by default) | Easy running first (12km by default) |

Race(1.5) is the shortest distance the pace model is fitted to. Nothing here goes faster than it.

## Tempo scale

A tempo longer than 20 minutes at threshold pace is closer to a time trial, so the pace slides towards marathon pace as the run gets longer. The slide is `pace(T) = threshold × (1 + 0.049 × ln(T / 20))`, never slower than marathon pace, for T from 20 to 60 minutes.

The 0.049 comes from a least-squares fit to a table the author supplied and described as Daniels' method. It listed, for 20 to 60 minutes in 5-minute steps, paces of 4:07, 4:10, 4:12, 4:14, 4:16, 4:17, 4:18, 4:19 and 4:20 per km. That is +1.2% at 25 minutes and +5.3% at 60 minutes against the 20-minute pace, and the fit stays within about 1s/km of every entry. I have not seen where the table comes from and have not checked it against Daniels' books. The fit uses percentages, so it is applied to your threshold pace, not to the runner in the table. The cap at marathon pace stops the slide from passing it when the gap between threshold and marathon pace is small, for example at high weekly mileage.

## Marathon pace and weekly distance

Marathon pace is race(42.195), which depends on the weekly distance field. The marathon is set to 2.10 times the half marathon at 70 miles a week or more, 2.13 at 60, 2.17 at 50 and 2.25 at 35 or less, in straight lines between those points. Blank means 70 miles. The Race Prediction Calculator methodology gives the formula and says these numbers are my estimates.

## Yasso 800s and the marathon

The traditional rule reads the average 800m time in minutes:seconds as the marathon time in hours:minutes. This page runs the 800s at race(5) and shows the rule's marathon time beside the model's predicted marathon, with the difference. At about 75 miles a week the model was 1 min 35s slower than the rule for an 18:54 5k. At lower weekly distances the model's marathon is slower, so the rule would overestimate. This is shown for comparison. The rule is a folk rule, and 5km-paced 800s are a fitness check more than a predictor.

## Rosario 800s

The float pace is race(5) + 25s per 800m. The page shows how far that float is from the predicted marathon pace. The intention, as described by the author, is that the floats approximate marathon pace when the weekly volume is adequate. I have not checked that against a published source.

## Session load

- Warm-up and cool-down default to 10 + 10 min at 65% of 5km speed, a cap rather than a target (see the Sub-Threshold Session Generator methodology). The pace is editable and also sets the jog pace.
- Hard parts use their stated paces. Floats use the mid-point of their range.
- The marathon-pace long run has no separate warm-up or cool-down.
- TSS = hours × (threshold pace ÷ pace)² × 100, summed over every part.

## Results table layout
Columns: Part, Reps, Distance, Time, Pace /km. Every row fills both Distance and Time. The prescribed one is exact (distance reps: metres; timed reps and jogs: the time); the other is derived from the pace, with "ca." on a distance worked out from a time. Distance reps show a time range (e.g. 41–42s) because coaches give short reps as times. Jogs between reps use the same two columns, so figures line up with the rep above. The warm-up and cool-down row has no rep count. Labels do not repeat the length.
