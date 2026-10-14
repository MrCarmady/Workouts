# Marathon Plan Recommender: methodology

Tests all 13 marathon plans on Marathon Plans against your starting CTL and ATL, and says which fit. It does not rank plans by how good they are for you.

### Test

- Each plan's daily TSS is run through CTL (42-day) and ATL (7-day) from your start values.
- Form is CTL minus ATL at the end of each day. The ratio is ATL divided by CTL.
- A plan fits if form never goes below the lowest form allowed (default -20) and the ratio never goes above the limit (default 1.3).
- The test covers the plan up to the last full day before the marathon. The marathon is not scored.

### Where the defaults come from

- TrainerPlan's ATL to CTL bands: 0.8 to 1.3 is the sweet spot, above 1.3 is caution, above 1.5 is the highest risk. Its alerts sit at form -10 and -20, and it treats below -30 as high strain.
- The -20 floor is chosen by the user for running, which is higher impact than cycling. It is not a research threshold.
- ATL below 0.8 times CTL (undertraining) is not tested.

### Start values

- CTL 5 to 200. ATL blank means the same as CTL (a flat start).
- A start ATL above CTL, as after a hard week, makes early weeks fit worse.

### Plan settings

These are Marathon Plans' defaults, fixed here:

| Setting | Value |
|---|---|
| Daniels | Top of each plan's band (40, 55, 70, 85 mi), 6 run days, short threshold reps on |
| Pfitzinger | Long runs at 85% of marathon speed, 10km tune-up, no recovery weeks |
| Copeland | 5km reps 16.5 min |
| Hansons | As on Marathon Plans |

### Joining late

- Input "Join plan once load is (% of yours)", default 85 (my choice, not confirmed). Leading weeks whose TSS is below that share of your current weekly load (7 x CTL) are skipped. Your current load is held until the join week, then the plan runs.
- Reason: a light early week would otherwise let CTL decay, so later weeks look harder than they are. A runner at CTL 50 would not start Hansons Beginner at week 1.
- 0 = start at week 1, no skipping. "Never reaches your load" is flagged if no week gets there.
- Peak 4-week TSS/day is taken from the join week on.

### Estimating CTL from recent hours

- Inputs: average hours per week over the last 6 weeks, hours in the last 7 days (blank = same as average), and a rough percentage of running time at threshold or harder (blank = 15, limit 0 to 50, my limit).
- TSS per hour = (1 - q) x 100 x (race(16) pace / easy pace)^2 + q x 100, with easy pace = race(5) / 0.65 (the engine's easy cap) and threshold work scored at 100 TSS/hour. About 49, 56 and 61 TSS/hour for 0, 15 and 25%.
- CTL = average hours x TSS/hour / 7, which assumes steady training. ATL = (last-7-days x 0.632 + average x 0.368) x TSS/hour / 7, which is the 7-day time constant on a steady week followed by one different week.
- Optional average easy pace (per km or per mile) replaces the 65% default: easy TSS/hour = 100 x (race(16) pace / easy pace)^2. The page shows the pace as a percentage of 5km speed and flags values under 50% or over 80% (my limits, to catch unit mistakes), and rejects paces at or faster than threshold pace or outside 2:30 to 10:00 per km. Slower real easy running than the default lowers TSS and faster raises it. The 15% mix and 25% mix are my choices, not tested against real logs.
- "Use these" copies the numbers into start CTL and ATL. Nothing is saved.

### Columns

- Joins: the week the plan is entered (1 = no skipping).
- Avg and peak time/week: running time (warm-up, cooldown and walked recoveries included) from the join week to the week before race week. Average = mean of those weeks; peak = longest single week. Race week excluded so the marathon does not inflate it.
- Week 1 TSS/day: the first week's TSS divided by 7.
- Peak 4-week TSS/day: the highest average over four consecutive weeks.
- Lowest form and highest ratio, with the week they occur.

### Limits

- A plan that fits is not a plan that suits you. It says nothing about mileage you can absorb, long-run length or injury history.
- The plan code is a copy of Marathon Plans'. A build test fails if the two differ.
