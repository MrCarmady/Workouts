# Hybrid Load Planner: how it works

The page projects CTL, ATL and TSB from one week of running and lifting, repeated for up to 12 weeks. Lifting is scored in TSS-like points so both sit on one scale.

## Running

You enter each day's running TSS. CTL uses a 42-day time constant and ATL a 7-day one, read at the end of each day. TSB is CTL minus ATL. The week starts on Monday morning from your start CTL and ATL.

## Scoring a lift

Each lift scores:

`max(10, 100 x lower-or-upper x compound-or-isolation x (1 - 0.12 x reps left on the last set) x sqrt(sets / 3))`

| Factor | Values |
|---|---|
| Lower or upper | lower 1, upper 0.33 |
| Compound or isolation | compound 1, isolation 0.5 |
| Reps left on the last set | 0 to 5; each rep left removes 12% |
| Sets | three sets is standard; the effect grows with the square root |

Examples: three sets of a lower-body compound lift with the last set to failure score 100. Three sets of an upper-body compound lift to failure score 33. Three sets of light biceps curls with 3 reps left score about 11. A lower-body compound lift with 3 reps left scores about 64.

## Several lifts in a day

Sets and reps left are pooled within each of the four lift types. The day's lifting total is the largest type's score plus half of the rest. One set of squats and one set of deadlifts, both to failure, pool to two lower-compound sets and score about 82.

## Where the numbers come from

They are the author's estimates, fitted to a few anchors: squat to failure 100, overhead press to failure about 33, light curls about 10, and a Tactical Barbell style session with reps left about 60. The 0.33 upper-body factor, the 0.5 isolation factor, the 12% per rep left, the square-root sets curve, the 10-point floor and the half-weight for combining lift types are all estimates. None is a research value. Reps left is self-reported and easy to misjudge.

## Weights in CTL and ATL

Lifting counts in full for ATL. For CTL it counts at a weight you set, 0.75 by default, because a stronger squat transfers less to running fitness than running does. Because the weights differ, a steady lifter shows lower form than a runner with the same total load. That is intended.

Example: running 50 TSS a day plus lifting 30 TSS a day. With equal weights CTL and ATL are both 80. With a CTL weight of 0.75, CTL is about 72 and ATL 80, so form is about -8 and ATL:CTL about 1.10. At 0.5 form is about -15.

## CTL ramp breakdown

CTL is the sum of a running (and existing load) part and a lifting part, so the weekly change splits exactly between them. The i button on each row shows the two parts.

## Limits

- Lifting is treated as a same-day hit, like running TSS.
- A new or returning exercise can leave you much sorer than its score suggests. The model does not capture that.
- If your start CTL already includes lifting, for example from a watch, lifting is counted twice.
- Only four lift types are scored. Exercise choice within a type is ignored.

## Cross-training (2026-10-22)

Each day has a cross-training TSS box (raw TSS from the Cross-Training TSS page). It is multiplied by one weight (80% by default, a placeholder shared with the Run Load Planner) and counts the same for CTL and ATL, in its own running average beside running and lifting. The table gets a cross-training column when any day has a value. The ramp breakdown adds a cross-training term. Running plus counted cross-training in one day is limited to 300 TSS. Each day is 0 to 400 raw, weight 0 to 150%.
