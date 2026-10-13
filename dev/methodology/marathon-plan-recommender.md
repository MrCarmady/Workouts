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

### Columns

- Week 1 TSS/day: the first week's TSS divided by 7.
- Peak 4-week TSS/day: the highest average over four consecutive weeks.
- Lowest form and highest ratio, with the week they occur.

### Limits

- A plan that fits is not a plan that suits you. It says nothing about mileage you can absorb, long-run length or injury history.
- The plan code is a copy of Marathon Plans'. A build test fails if the two differ.
