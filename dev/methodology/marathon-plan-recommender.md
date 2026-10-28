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

### Race date and ramp

Optional. With a race date, the page plans the calendar as well as the load. Blank = the behaviour above, unchanged.

- Plan placement: the plan's last day is race day, so a plan of L weeks starts 7 x L - 1 days before it. Days between today and that start are spare.
- Ramp (Pavel's choices, 2026-10-26): the page finds, for each plan, the lowest CTL at which the plan passes the fit test when it starts. It reaches that CTL by the slowest ramp: a straight rise in CTL spread over all the spare days. The rise may not exceed the weekly cap (default 1.0 CTL per week, Pavel's choice; input limit 0.1 to 10 is mine).
- Daily load for the ramp comes from CTL's own update rule: TSS = CTL(yesterday) + (CTL(today) - CTL(yesterday)) / k, with k = 1 - exp(-1/42). ATL is run on the same daily loads, so ATL at the plan start is real. After a ramp it sits above CTL, by about 5 points for every 1.0 CTL a week of ramp.
- The plan's fit test then starts from the ramp's end CTL and ATL. The ramp's own form is not tested.
- If the plan fits with no ramp, the current load is held until it starts, so ATL settles to CTL. A tired start ATL therefore recovers during the spare days.
- If the plan does not fit even at the cap, the table says how many more weeks of ramp it needs (found by search, up to 52 weeks; "does not fit at this rate" beyond that).
- If there are fewer weeks than the plan has, the plan is joined part-way at the next week boundary, holding the current load until then. Spare days of fewer than a week are held. A race less than one plan-week away shows "Race is too soon".
- Join percentage is not used when a race date is set (the input is disabled). A ramp makes the load-based skip unnecessary.
- Columns change: Result moves next to the plan name; Plan starts and Ramp to CTL replace Joins week.
- Limits: the cap applies to the ramp only. The plans themselves raise CTL faster than that once they start (Copeland add-on at CTL 42 rises about 3 CTL a week in its first weeks). Session content for the ramp weeks is not planned.

### Estimating CTL from recent hours

- Inputs: average hours per week over the last 6 weeks, hours in the last 7 days (blank = same as average), and a rough percentage of running time at threshold or harder (blank = 15, limit 0 to 50, my limit).
- TSS per hour = (1 - q) x 100 x (race(16) pace / easy pace)^2 + q x 100, with easy pace = race(5) / 0.65 (the engine's easy cap) and threshold work scored at 100 TSS/hour. About 49, 56 and 61 TSS/hour for 0, 15 and 25%.
- CTL = average hours x TSS/hour / 7, which assumes steady training. ATL = (last-7-days x 0.632 + average x 0.368) x TSS/hour / 7, which is the 7-day time constant on a steady week followed by one different week.
- Optional average easy pace (per km or per mile) replaces the easy percentage (65% by default) used for the load estimate. The plans use the same easy percentage and sub-threshold buffer inputs as Marathon Plans: easy TSS/hour = 100 x (race(16) pace / easy pace)^2. The page shows the pace as a percentage of 5km speed and flags values under 50% or over 80% (my limits, to catch unit mistakes), and rejects paces at or faster than threshold pace or outside 2:30 to 10:00 per km. Slower real easy running than the default lowers TSS and faster raises it. The 15% mix and 25% mix are my choices, not tested against real logs.
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

### Load chart

- Click a plan row to chart it. By default the chart shows the most demanding plan that fits, or the first plan if none fits.
- The lines are daily CTL, ATL and form (CTL minus ATL), from your start CTL and ATL. The held weeks before the join week are included (flat at your current load). Values are at the end of each day.
- The dashed horizontal line is the lowest form allowed. The dashed vertical line marks the join week.
- All three lines are in TSS per day on one axis. The ATL/CTL ratio is not drawn: it has a different scale. Hover (or the arrow keys) shows it with the other values, and the table view lists end-of-week CTL, ATL, form and ratio.

## Sub-threshold buffer box
The buffer only changes the Copeland add-on, so its input is shown only while the Copeland row is selected, or while its value is invalid (so it can be fixed). A hidden buffer still applies to the Copeland row in the table. An invalid easy % or buffer now shows an error instead of an empty table.

### Intensity mix (2026-10-28)

A stacked bar per plan (all 13) showing the share of running time or distance in each zone, over the whole plan from week 1 to race week with marathon day left out. A Time / Distance toggle, a table view, and click-to-select a plan (same selection as the load chart). It does not depend on CTL, ATL or the join week.

- Zones follow each plan's own session labels, not a speed cutoff. A cutoff on % of 5km speed misplaces plans: marathon pace depends on the plan's weekly mileage (about 85% of 5km speed for the 55-mile plans, 87% at 70 or more), so Pfitzinger's 55-mile long runs fell under any common "steady" cutoff.
- Recovery: Pfitzinger recovery runs only. Easy: Daniels E, Copeland easy, Hansons Easy A and B, Pfitzinger general aerobic. Long and steady: Hansons long runs, Pfitzinger long pace (long and medium-long runs, 85% of marathon speed), Copeland's 92% and 93% of marathon speed blocks. Marathon pace: each plan's own. Faster than marathon pace: Hansons strength (MP minus 10 s) and Copeland's 150, 120 and 90 minute reps. Threshold: Daniels T, Pfitzinger LT, Copeland's 60 minute reps. 5k pace and faster, races: Daniels I and R, Hansons speed, Pfitzinger 5K and races, Copeland races.
- Daniels and Copeland easy pace is the 65% of 5km speed assumption, not their books' paces, so their large easy blocks come from that assumption. Hansons easy uses Table 3.5, Pfitzinger recovery and GA use his 60% and 70%.
- Warm-ups, cooldowns and recoveries count at their own pace. Distance shares divide each row's time by its pace. The mix is read from each plan's detail rows, so it matches the plan pages. Copeland rows with mixed paces and no time (about 2%) are left out.
- Example at an 18:52 5km, time share: Daniels 2QC 70 is 84% easy, 7% marathon pace, 7% threshold; Hansons Advanced is 69% easy, 11% long, 12% marathon pace, 5% faster than marathon pace; Pfitzinger 18/70 is 28% recovery, 18% easy, 45% long and steady.
