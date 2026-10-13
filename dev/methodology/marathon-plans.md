# Marathon Plans: methodology

One page, four authors. Choose the author, then the plan. The race, time, units and starting CTL are shared. Load (TSS, CTL, ATL, ramp) is calculated the same way for all authors; each section below covers what is specific to that author.

---

## Copeland Marathon Plan

Lays out the 15-week Copeland marathon add-on ("My Marathon Build") from a race result, with paces, recoveries and load. The weekly layout was transcribed from the book's table.

### Plan

| Item | Status |
|---|---|
| Weekly sessions, weeks 1 to 15 | As printed in the book |
| Week 14 Thursday | Printed as a different session; read as 8 x 1000m, as confirmed by the author |
| Week 14 Tuesday | 3 x 27.5 min progressive at 92%, 93% and 100% of marathon speed, as given |
| Distance-based easy runs ("8 km E") | Converted to time at the easy pace |

### Paces

| Rep | Time | Pace | Recovery |
|---|---|---|---|
| 1000m | 3 min | race(16) | 60 s |
| 1600m | 6 min | race(21) | 75 s |
| 2000m | 8 min | race(30) | 90 s |
| 3000m | 10 min | race(32) | 90 s |
| 3200m | 12 min | race(32) | 120 s |
| 5000m | 15 to 18 min (default 16.5) | marathon pace, 1.5% faster | 180 s |

- Reps are set by time at current fitness, with the book's rep counts. The 2000m pace is slightly slower than half marathon pace, by the author's choice.
- Marathon pace: the Race Prediction Calculator's marathon, assuming 70 miles a week.
- Easy and long runs: 65% of 5km speed, a cap.
- Warm-up and cooldown: 10 min each at the easy pace. 5km and 10km races use a 20 min warm-up (easy, 2 x 2 min at half marathon pace, 4 strides of 17 s at mile pace).

### Load

- Recoveries are walked at 6 km/h. They count for time and TSS, not distance.
- TSS per segment = hours x (threshold pace / pace)^2 x 100, threshold = race(16).
- Races are scored at race pace. The marathon on the last Sunday is not scored.
- CTL has a 42-day and ATL a 7-day time constant. Starting CTL is entered, or estimated as week 1's TSS divided by 7. The plan has no ramp-in, so the estimate is high; enter your own CTL to see the real ramp and form.

### Limits

- Only the marathon add-on is built, not the base NSA weeks.
- The page does not adapt to what you actually ran.

---

## Daniels 2Q Plan

Lays out the 18-week 2QA plan from a race result. Two quality sessions a week (Q1, Q2), the rest easy. The week-by-week sessions and fractions of peak are as given by the author, not checked against the book.

### Plan

| Item | Status |
|---|---|
| Session contents and fraction of peak for weeks 1 to 17, and the day-by-day race week | As given by the author |
| Long runs count as quality sessions and are run at easy pace | Author's rule |
| Numbers before E, M and T are miles | Daniels' notation |
| I and R reps are timed; distance follows from pace | Daniels' notation |
| Jogs and easy segments count towards distance; standing rests do not | My choice |
| Run days 5 to 7, so 3 to 5 easy days | Author's rule |

### Paces

- Easy: 65% of 5km speed. This is a cap rather than a target.
- Marathon: plain Riegel prediction (exponent 1.06), with no extra slowdown for weekly distance. The Race Prediction Calculator's marathon pace is slower.
- Threshold: race(17).
- Intervals: race(4).
- Repetition: race(1.7).

The short-race slowdown is the one in the Race Prediction Calculator.

### Weekly distance

Weekly total = peak weekly distance × the week's fraction of peak. Easy days share what remains after Q1 and Q2 equally. If the quality sessions alone exceed the total, the total is raised to match and the page says so. Week 18 has no fraction; it is listed by day, counting down to the race, and easy days there are by time.

### Slower runners

Daniels: 5 to 6 min of threshold counts as 1 mile, 10 to 15 min as 2 miles, 16 to 20 min as 3 miles. With the option on, a threshold segment of 1, 2 or 3 miles is cut to 6, 15 or 20 min if the runner's pace would take longer. Segments of other lengths, and the 800m reps in race week, are not changed. Shortened segments are starred.

### Load

- TSS per segment = hours × (threshold pace ÷ pace)² × 100, the same as the Run TSS Calculator. Threshold is race(16). Standing rests score 0. Jogs between reps count at easy pace.
- CTL uses a 42-day and ATL a 7-day time constant. Ramp is the change in CTL over the week.
- Q2 is on Wednesday, Q1 on Sunday, easy days fill the other run days, and rest days come first in the week. This is my placeholder; the order affects ATL slightly.
- Steady runs given as a range use the midpoint for TSS.
- Starting CTL is entered, or estimated as week 1's TSS divided by 7.
- Week 18 covers the seven days before the race. Race day is not scored, so CTL and ATL are for the morning of the race.

### Limits

- Only the 2QA plan is built. 
- Time-based easy runs are converted to distance at the easy cap, so the distance is the shortest likely.
- The page does not adapt to what you actually ran.

---

## Hansons Advanced Plan

Lays out the 18-week Hansons Marathon Method Advanced program (Table 4.4) from a race result. Distances and weekly totals are the book's, not scaled to your own mileage. The session list was transcribed from the book's table.

### Plan

| Item | Status |
|---|---|
| Daily sessions and weekly totals, weeks 1 to 18 | As printed in the book |
| Weekly totals include a 1.5-mile warm-up and cooldown on speed, strength and tempo days | As stated in the book |
| Tuesdays are speed work in weeks 2 to 10 and strength work in weeks 11 to 17 | As given by the author |
| Thursday tempo runs are at marathon pace | Hansons' rule, confirmed by the author |
| Strength is 10 s per mile faster than marathon pace | Hansons' rule, confirmed by the author |
| Speed reps run at 5km pace | Author's reading of the book's pace chart; the book's rep paces vary by about 2 s per 400m depending on rep length, which the page ignores |
| Easy running and recovery jogs at 65% of 5km speed | Author's choice, a cap rather than a target |

### Paces

- Marathon pace: the Race Prediction Calculator's marathon, assuming 70 miles a week (2 × half marathon + 10 min). There is no goal-time input: every session is set from current fitness, so tempo and strength cannot come out faster than speed work. The book quotes 3:00:21 for an 18:30 5km; the page gives 3:00:12 for the same result.
- Tempo: marathon pace. Strength: marathon pace minus 10 s per mile. Speed: race(5).
- Easy, long runs and recoveries: the 5km pace divided by 0.65.

### Load

- TSS per segment = hours × (threshold pace ÷ pace)² × 100, with threshold as race(16), as in the Run TSS Calculator.
- CTL has a 42-day and ATL a 7-day time constant. Ramp is the change in CTL over the week.
- Daily sessions are as in the book, Monday to Sunday, so day order is not assumed.
- Starting CTL is entered, or estimated as week 1's TSS divided by 7. Because week 1 is only 26 miles, the estimate is low and the first weeks show large ramps.
- The marathon on the last Sunday is not scored, so week 18 covers Monday to Saturday and CTL and ATL are for the morning of the race.

### Limits

- Only the Advanced program is built. The Beginner program is in the same book.
- Easy and long runs are listed by distance, as the book gives them; the time follows from the easy cap.
- The page does not adapt to what you actually ran.

---

## Pfitzinger Marathon Plan

Lays out Pfitzinger's 18-week and 12-week "up to 55 miles per week" and "55 to 70 miles per week" marathon plans (18/55, 12/55, 18/70, 12/70) from a race result, with paces and load. Sessions were transcribed from the book's tables. The higher-mileage plans are not built.

### Plan

| Item | Status |
|---|---|
| Daily sessions and distances, both plans | As printed in the book; not scaled |
| Weekly totals | Checked against the book's printed totals; every week of every plan matches except 12/70 week 7 |
| 12/70 week 7 | The days sum to 62 miles; the book prints 59. The days are used, as agreed with the author |
| Tune-up races | The book gives a range of total miles; the page uses the middle |
| Recovery block | Optional, five weeks, from the book's recovery tables: 15 to 41 miles for the 70 plans, 13 to 35 miles for the 55 plans |

### Paces

| Session | Pace | Status |
|---|---|---|
| Recovery | 60% of 5km speed | Author's choice |
| General aerobic, warm-up, cooldown | 70% of 5km speed | Author's choice |
| Medium-long and long runs | 85% of marathon-pace speed (input, 80 to 90%) | Book's 80 to 90% range, author's reading; applied to medium-long runs as well |
| LT | race(21) | Author's choice; the book gives 15K to half marathon pace |
| 5K reps | race(5) | Book; jogs of 70% of rep time at recovery pace (book says 50 to 90%) |
| Marathon pace | Race Prediction Calculator at the plan's weekly mileage: 70 for the 70 plans, 55 for the 55 plans (about 11 s per mile slower at 18:45) | Extends the Hansons and Copeland approach; no goal-time input |

- The distance not used by LT, marathon-pace or rep work is split evenly into warm-up and cooldown at general aerobic pace. Rep jogs count towards the day's distance.
- A tune-up race at the chosen distance (8, 10 or 15 km; week 2 capped at 10 km) is scored at race pace, with easy warm-up and cooldown making up the middle of the range.
- Strides and hill sprints are counted as easy running. At 18:45, 8 to 10 strides at mile pace would add roughly 3 to 4 TSS, and 6 hill sprints of 10 s about 1.

### Display

- The weekly table lists only key sessions (LT, marathon-pace runs, 5K reps, long runs, races) and any other single run over 1:45, shown with its time. Other runs appear in the week-by-week detail and in the totals.

### Load

- TSS per segment = hours x (threshold pace / pace)^2 x 100, threshold = race(16).
- CTL has a 42-day and ATL a 7-day time constant. Starting CTL is entered, or estimated as week 1's TSS divided by 7; the plans have no ramp-in, so the estimate is high.
- The marathon is not scored. With the recovery block added it is scored at marathon pace so that the recovery weeks start from the right load.

### Limits

- The page does not adapt to what you actually ran.
