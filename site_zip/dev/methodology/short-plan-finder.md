# Short-Distance Plan Finder: methodology

Tests the six 5K to 10K plans on Short-Distance Plan Viewer against your starting CTL and ATL, and says which fit. It does not rank plans by how good they are for you. It is the Marathon Plan Finder's page applied to the plans of the Short-Distance Plan Viewer, so the test, inputs, join rule, race-date ramp and CTL estimate work as described on that page. This page lists what differs.

### Plans

| Plan | Weeks | Settings fixed here |
|---|---|---|
| Daniels 40-50 mi | 18 | Middle of the weekly distance range, 10km race in week 18, H pace same as I pace, shortened threshold reps on |
| Daniels 60-70 mi | 18 | As above |
| Davis Full-Spectrum | 16 | As written |
| Pfitzinger 30-42 mi | 12 | 10km goal race, average of the book's early and latter long-run pace |
| Pfitzinger 45-57 mi | 12 | As above |
| Pfitzinger 60-76 mi | 12 | As above |

These are the Short-Distance Plan Viewer's defaults. Plan code is a copy of that page's; tests/check_plans_sync.py fails the build if they differ. Easy pace basis and the easy pace setting are inputs here, as on the Marathon Plan Finder.

### Test

- Each plan's daily TSS is run through CTL (42-day) and ATL (7-day) from your start values.
- Form is CTL minus ATL at the end of each day. The ratio is ATL divided by CTL.
- A plan fits if form never goes below the lowest form allowed (default -20) and the ratio never goes above the limit (default 1.3).
- The test stops at race morning, the last full day before the race. The race and the days after it are not scored. Daniels' and Davis's race is on the last Saturday and Pfitzinger's on the Saturday of week 12, so Pfitzinger's race week is cut after Friday and Daniels' and Davis's at the day before the race. Pfitzinger's post-race recovery week is not included.
- The defaults come from the same sources as on the Marathon Plan Finder: TrainerPlan's ATL to CTL bands (0.8 to 1.3 sweet spot, above 1.3 caution) and a -20 form floor that is my choice for running, not a research threshold.

### Race date

With a race date, the plan stops at race morning, so it starts as many days before race day as its weeks hold up to the day before the race (the Marathon Plan Finder uses 7 x weeks - 1, because the marathon is on the last day of the week). Everything else about the ramp is as described on the Marathon Plan Finder.

### Intensity mix

The Marathon Plan Finder places each run by its session label. The short plans use different labels in each plan, so this page places each run by its pace as a share of your 5km speed:

| Zone | % of 5km speed |
|---|---|
| Easy | under 80 |
| Steady | 80 to 89.5 |
| Threshold | 89.5 to 98 |
| 5k pace and faster | 98 and over |

- The two upper cutoffs are the Marathon Plan Finder's rule for races (98% and 89.5%). The 80% cutoff is my choice, between easy running (60 to 76% in these plans) and marathon-type effort.
- Rows are read from each plan's own detail table, so the mix matches the Viewer. Each row's time is split equally across the paces listed in it.
- Race day and the days after it are left out. A tune-up race counts at its own pace.
- Walked recoveries have no pace, so they are not counted. Davis's walk and walk/jog recoveries are therefore missing from its mix.
- Pfitzinger's endurance runs (about 76% of 5km speed) fall in Easy at the default settings.

### Changes made to Short-Distance Plan Viewer for this page

- Daniels and Davis builders now mark the race day in the last week (`raceIdx`), as Pfitzinger's already did.
- Race morning CTL and ATL on the Viewer for Daniels and Davis are now taken before the race day. They were taken after it, with the race day counted as a zero-TSS day, which lowered race-morning ATL by about 13% and CTL by about 2%. "After the race" is now worked from the race-morning values.
- The Viewer accepts a plan id in the link (for example short-plans.html#pf2) so the Finder can open a plan.
