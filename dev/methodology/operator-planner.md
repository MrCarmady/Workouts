# Operator Planner: methodology

Takes up to four lifts, each with a tested 1RM or a set (weight, reps, reps in reserve) that gives an estimated 1RM, and an optional training max percentage, and returns the six-week Tactical Barbell Operator cycle as weights. A second mode keeps the same effort but uses more reps, for single-leg work.

Operator is three lifting days a week, with a day or two off between them. All three days are the same, so the page lists one day's sets and you repeat them. This is the author's description of the programme and I have not checked it against the book.

## What is published and what is an estimate

| Part | Status |
|---|---|
| The Operator cycle (weeks, sets, reps, percentages) below | As given by the author from Tactical Barbell. **Not checked against the book by me** |
| Epley and Brzycki formulas, averaged | Published formulas. The averaging and the single-rep fix are the same as in the Lift Scheme Calculator |
| High-rep mode (10, 8 and 6 reps, matched reps in reserve) | **Author's design.** The reps were set by the author. The percentages follow from them |
| Week 6 reps in reserve worked out at 1.5 reps | **My choice**, the middle of 1–2 |
| Reps in reserve from the formulas | **Estimates.** The formulas are least reliable above about 10 reps |

## The cycle (standard mode)

| Week | Sets × reps | % of 1RM |
|---|---|---|
| 1 | 3–5 × 5 | 70% |
| 2 | 3–5 × 5 | 80% |
| 3 | 3–4 × 3 | 90% |
| 4 | 3–5 × 5 | 75% |
| 5 | 3–5 × 3 | 85% |
| 6 | 3–4 × 1–2 | 95% |

Weight = training max × percentage, rounded to the chosen step (1, 2, 2.5 or 5 kg). With the training max at 100% that is the 1RM × percentage.

## Estimated 1RM

Each lift takes either a tested 1RM or one set, which the page converts to an estimated 1RM. The author describes Tactical Barbell's default recommendation as an estimate from a low-rep set of about 3–5 reps, because it is fairly accurate and easier to do to failure without spotters, with a tested 1RM as a fine alternative. I have not checked this against the book. Both formulas get less reliable as reps rise, which is why the page warns above about 10 reps.

```
n     = reps + RIR
pct(n)= average of Brzycki (37 - n) / 36 and Epley 1 / (1 + n / 30)    // Epley pinned to 1 at n <= 1
e1RM  = load / pct(n)
```

`load` is the weight lifted. For weighted pull-ups and dips it is bodyweight + added weight, and the table shows added weight. For dumbbell lifts (Bulgarian split squat, incline dumbbell bench) it is the weight per hand. A tested 1RM is the same calculation with 1 rep and 0 reps in reserve.

## Training max

The training max is separate from the 1RM. It is a percentage of the 1RM (tested or estimated), and the Operator percentages are applied to it. The author describes it as a guardrail on intensity and fatigue, mainly useful to advanced lifters, for whom 90% of their max is still heavy enough to give a good stimulus while working more sub-maximally than the standard programme. The default is 100%, which means the 1RM is used directly.

The author borrows the idea for estimates from higher-rep sets: an endurance background may make a high-rep set overstate the true 1RM, so the author uses 90% for deadlifts and 95% for weighted pull-ups to standardise the weights without testing low-rep sets to failure. These figures are the author's judgement. The page does not set them for you.

For weighted pull-ups and dips the percentage applies to total load (bodyweight + added weight), and the table shows added weight.

Example: 22 kg per hand for 10 reps to failure. Both formulas give a fraction of 0.75, so the estimated 1RM is 29.3 kg per hand.

## Reps in reserve for each week

At a fraction p of the 1RM, the reps to failure `nFail(p)` solve `pct(n) = p`. The reps in reserve for an Operator week are `nFail(p) - reps`.

| Week | % | Reps to failure | Reps | Reps in reserve |
|---|---|---|---|---|
| 1 | 70% | 12.2 | 5 | 7 |
| 2 | 80% | 7.9 | 5 | 3 |
| 3 | 90% | 4.0 | 3 | 1 |
| 4 | 75% | 10.0 | 5 | 5 |
| 5 | 85% | 5.9 | 3 | 3 |
| 6 | 95% | 2.2 | 1.5 | 1 |

## High-rep mode

The idea is to keep each week's reps in reserve and change the reps, so the effort stays what Operator intends while the set gets longer. This suits single-leg work such as Bulgarian split squats, where balance and set-up make sets of 1–5 awkward.

```
reps (high-rep) = 10 in weeks 1, 2 and 4;  8 in weeks 3 and 5;  6 in week 6
RIR             = nFail(p) - operatorReps
percentage      = pct(highRepReps + RIR)
```

For a 29.3 kg estimated 1RM (22 kg × 10 to failure), with rounding to 2 kg:

| Week | Sets × reps | % of 1RM | Weight per hand |
|---|---|---|---|
| 1 | 3–5 × 10 | 59% | 18 kg |
| 2 | 3–5 × 10 | 68% | 20 kg |
| 3 | 3–4 × 8 | 77% | 22 kg |
| 4 | 3–5 × 10 | 64% | 18 kg |
| 5 | 3–5 × 8 | 73% | 22 kg |
| 6 | 3–4 × 6 | 83% | 24 kg |

The formulas lose accuracy as reps rise, so the percentages are a starting point to adjust against how the sets feel.

## Limits

- **Deadlift schedule.** Deadlifts get a reduced load: either one day a week with the sets listed, or one set on each of the three days. The author considers one set on one day too little to progress. These options are the author's description.
- **Lifts.** Squat, bench press, deadlift, overhead press, weighted pull-up, weighted dip, incline dumbbell bench and Bulgarian split squat. Incline dumbbell bench is an alternative pressing movement and uses the standard cycle per hand.
- Sets (3–5 or 3–4) are the ranges from the plan. The page does not choose a number within them.
- Standard weeks 1–5 assume the formulas hold at 1–12 reps. Week 6 uses a pinned Epley at one rep, so its reps in reserve are rough.
- The formulas assume sets near the stated percentage of a true maximum. A 1RM entered from a tired or untested set will carry through every week.
