# Copeland Base: methodology

Builds a week-by-week ramp from a starting CTL to week 1 of the Copeland marathon plan. It has no taper and no goal race. Race, time and units are shared with the other running tools.

### Week

7 run days (6 drops Friday; 5 is below).

| Day | Session |
|---|---|
| Mon, Wed, Fri | Easy (Friday is a rest or cross-training day with 6 run days) |
| Tue | Sub-threshold, long |
| Thu | Sub-threshold, medium |
| Sat | Sub-threshold, short |
| Sun | Long easy |

Each sub-threshold day has a 10 min warm-up and cooldown at the easy cap (65% of 5km speed by default, adjustable from 50 to 85). A sub-threshold buffer (percent slower, default 0, up to 10) slows every rep pace. Both inputs are shared with the other plan pages. They are personal margins, not from the book.

### Five run days

Two easy runs, two sub-threshold sessions and one long run (your split; the days and which sessions are mine).

| Day | Session |
|---|---|
| Mon | Rest or cross-train |
| Tue | Sub-threshold, long |
| Wed | Easy |
| Thu | Sub-threshold, medium |
| Fri | Rest or cross-train |
| Sat | Easy |
| Sun | Long easy |

- The short session is dropped, in line with the ladder rule that short is cut first. The ladder climbs the long and medium sessions only (top state 4 x 10 and 6 x 6), so sub-threshold share tops out near 17% in the biggest weeks.
- Easy days share the time left after the sub-threshold days and the long run (about 25% of the week).
- Optional cross-training on the rest days (Mon and Fri with 5 run days, Fri with 6) counts toward CTL and ATL. See Cross-training below.
- Plan week 1 is still the book's seven-day week. The last row is therefore a step from five runs to seven, and at a start CTL of 30 it shows "ramp above target" (+1.1 against 1.0) because five-day weeks carry less load per hour.

### Target

Plan week 1 is the first week of the Copeland marathon add-on: Tue 3 x 12 min, Thu 6 x 6 min, Sat 10 x 3 min, Sun 110 min, other days 60 min. It is the same week as on Marathon Plans (about 7:51 h and 451 TSS at an 18:45 5km). The table stops at this week.

### Ramp

- Each week is the largest total time (steps of 1 min, down to 4 hours) whose end-of-week CTL ramp stays at or under the target.
- Target default 1 CTL per week. The input accepts 0.1 to 2.
- Start ATL is set equal to start CTL.
- The plan row is added as soon as its own ramp from the current CTL is at or under the target.
- If the start CTL already supports plan week 1, only that row is shown.
- Below about 30 CTL the 4 hour floor ramps faster than the target. Those weeks are flagged.

### Time split

- Long easy run: about 25% of the week.
- Sub-threshold days: work, walked recoveries and 20 min of warm-up and cooldown.
- The easy days (three, or two with 6 run days) share the rest equally, at least 30 min each. Runs are rounded to the minute.
- With 6 run days the plan week 1 row still has its Friday run, because it is the book's week.

### Sub-threshold sessions

Sub-threshold work is kept at or under 25% of running time. Walked recoveries are not running time. The session set is the furthest rung of one ladder that meets that rule.

| Step | Long | Medium | Short |
|---|---|---|---|
| Minimum | 2 x 10 | 2 x 6 | 4 x 3 |
| Build to the basic week | 3 x 10 | 3, 4, 5 x 6 | 6, 8, 10 x 3 |
| Extend long | 3 x 11, 3 x 12, 4 x 10 | | |
| Extend medium | | 7 x 5, 5 x 7, 6 x 6 | |
| Extend short | | | 8 x 4, 10 x 3.5, 9 x 4, 10 x 4 |

- The ladder is climbed long first, then medium, then short. Scaling down is the reverse: short is cut first, then medium, then long.
- 10 x 4 needs a week over 8 hours.
- Plan week 1 (3 x 12, 6 x 6, 10 x 3) is not a rung of the ladder. The last base week can have more sub-threshold minutes than it.

### Pace and recovery

| Rep | Pace | Recovery |
|---|---|---|
| 3 min | 60-min race | 60 s |
| 6 min | 90-min race | 75 s |
| 8 min | 120-min race | 90 s |
| 10 min | 150-min race | 90 s |
| 12 min | 180-min race | 120 s |

These are the Copeland plan's values, restated in time (2026-10-14). "60-min race" means the pace of a race lasting 60 minutes, from the race model. The 60, 90 and 150 min anchors fit Copeland's printed 5k-vs-rep-pace table at seven 5k times (15:00 to 28:20) within 2 s/km, always slightly slower than the book. The earlier distance anchors (16, 21, 32 km) drifted with runner speed, so they were the wrong frame. The 120 min (8 min reps) and 180 min (12 min reps) anchors are my extension: the book's table has only 3, 6 and 10 min reps. Other rep lengths are interpolated between anchors, in anchor time and in recovery (rounded to 5 s). The interpolation and the ladder minimums are my choices, not the author's.

### Load

- TSS per segment = hours x (threshold pace / pace)^2 x 100, threshold = race(16).
- Recoveries are walked at 6 km/h (100 m per minute). They count for time, TSS and distance.
- CTL has a 42-day and ATL a 7-day time constant. CTL, ATL and ramp are at the end of each week.
- The race model's 70-mile marathon slow-down applies to long-race paces, as on Marathon Plans.

### Limits

- Does not adapt to what you actually ran.
- Only the first week of the marathon add-on is a target.

### Cross-training (2026-10-22)

- Input: TSS per rest day, as it comes from the Cross-Training TSS page, and a weight (default 80%, a placeholder shared with the Run Load Planner). Counted TSS = TSS x weight, added to that rest day's TSS for CTL and ATL.
- It applies to base weeks only. With 7 run days there are no rest days, so it is off. Plan week 1 is the book's seven-day week with no cross-training.
- The ramp solver includes it, so the running time that fits the ramp target is smaller. Example: start CTL 35, 5 run days, 40 TSS on both rest days: week 1 falls from 4:58 to 4:01 (the minimum week, flagged "ramp above target").
- The weekly TSS column and week detail show running TSS only. The week note gives the counted cross-training TSS.
- Limits: 0 to 300 TSS per rest day, weight 0 to 150%.
