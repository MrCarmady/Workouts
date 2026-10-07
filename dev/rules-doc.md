# Plan Builder: rules (updated 2026-10-07)

Status: prototype built (Plan Builder page). (P) = Pavel's rule. (D) = Daniels cap, checked by Pavel. Placeholders are listed in the page's methodology.

## 1. Quality sessions per week
- Set by run days, not by an 80/20 split.
- 3 days: 1. 4 days: 2 (P). 5 days: 2 (proposed). 6 days: 3 (P). 7 days: 3 (proposed).
- Mile-paced (I/R-type) sessions: maximum 2 a week at any frequency (P).

## 2. Per-session caps
- T: not more than 10% of weekly mileage (D).
- I: lesser of 10 km or 8% of weekly mileage; reps of 3 to 5 min (D).
- R: lesser of 5 miles or 5% of weekly mileage; bouts up to 2 min (D).
- Marathon pace: 110 min per session (D).
- Sub-T: 12% of weekly distance (P). Daniels' 10% for threshold, raised a little because sub-T sessions are easier (lower lactate).
- Applied per session (P).

## 3. Weekly volume caps by pace type (P)
- R 10%, I 16%, T 20%, sub-T 30%, M 40% of weekly volume.
- Mixed weeks: shared budget (agreed, P). Each km of a type uses 1 / cap of a budget of 1.
- No quality dose setting (P): every session takes its full share of the weekly limit. TSB and the caps do the restraining. To be tested for being too hard.
- Gentlest possible mix still leaves at least 60% easy.
- No minimum quality volume needed (P).
- Easy means truly easy, under 70% max HR.

## 4. Paces
- Sub-T pace is race(21) (P): the average of sub-T paces, since longer reps run a little slower and shorter reps a little quicker. About 1.7% slower than threshold (race(16)). The earlier placeholder of 1.04 x threshold was about race(31), too slow.
- Threshold race(16). Intervals race(4). R is the predicted mile pace. Easy is 62.5% of 5km speed, editable.

## 5. Load progression (P)
- Replaces the 10% mileage rule. Target weekly TSS, simulate daily CTL, ATL, TSB.
- TSB at -10 or above where possible (too keen). Never -20 (no go).
- Ramp rate: CTL change per week, target 1, allowed band 0.1 to 1.9 (agreed). No separate maximum input: the target input is capped at 2 (P, 2026-10-07).
- TSS stays as IF squared (decided). Cubing IF would change every page.
- CTL and ATL use the exponential constants (42 and 7 days). TSB is read at the end of each day, the same as the Run Load Planner (P: either convention, but both pages must match).
- Week 1 jump accepted (P): most users have just entered a race and want to push volume.
- A step-back week after a -10 TSB week is accepted (P): tight TSB control is there to avoid unplanned down weeks.
- No absolute km cap for now.

## 6. Taper and race day
- Race-day TSB target: default +10, maximum +10 (P). Anything higher is overkill.
- Race-day TSB means the morning of race day (end of the day before).
- Headline CTL is the peak at the end of the last build week, not the lower race-day value (P). Race-day CTL is shown beside it.
- 14-day option: the penultimate week holds CTL (ramp 0), the last week is the taper. 7-day option: race week only.
- Race week is solved for the TSB target but kept between 50% and 80% of the peak week's distance (P's expectation; the exact bounds are my placeholders). If the 50% floor stops the target being reached, the page flags it and shows the TSB reached.
- Race day replaces the long run.
- Example (10 km 39:30, 65 km a week, 6 days, CTL 41): 14-day taper, target +10, race week 35.3 km (50%), race-day TSB +4.1. Target 0 gives 45.4 km (64%).
- Reaching +10 with a 50 to 80% race week would need a lower build TSB (for example a lower ramp target). Targets of 0 to +5 fit this shape better.

## 7. Week structure
- Quality days: warm-up and cool-down 20 to 40 min together, so a quality day is about 80% of an easy day's time (my choice, accepted).
- Long run: capped at 35% of weekly distance (P; Daniels' 25% is too low for 3 and 4 run days) and 150 min. No easy run longer than the long run.
- Time first (P): tables lead with time. Easy running is done by minutes, which reduces the temptation to push easy days. Distance follows from the easy pace entered.

## Simulation notes
- 100 to 109 km, extra 9 km easy: TSB about -3. Extra 9 km sub-T: about -4 to -5.
- 40 to 45 km, extra 5 km easy: about -2.
- Repeated +10% weeks from 100 km: TSB -3, -8, -12, -17 over weeks 2 to 5.
- Repeated +10% weeks from 40 km: TSB -1, -3, -5, -7.
- 10-week block to CTL 60 and TSB +10 from CTL 41 (constant build TSS, one taper week): build about 494 TSS a week, taper about 266. The 1.9 ramp cap and -10 TSB limit stop this, so it is not reachable.

## Open questions
- Goal race and phases: race date, phase-specific focus.
- Graded taper shape (not built).
- Whether TSB misses structural load from big km jumps at high mileage.
- Low mileage and beginner handling (easy pace, very short weeks).
- Feedback loop (logging what was run) and sync across devices.
- Lifting load: measure (session RPE x minutes), conversion to TSS-equivalent (needs an anchor chosen by P), and whether lifting counts in full toward the TSB limits.
