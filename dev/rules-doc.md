# Plan Builder, Trend Tracker and Hard Predictor: rules (updated 2026-10-08)

Status: prototypes built (Plan Builder, Sub-Threshold Trend Tracker, Hard Workout Predictor). (P) = Pavel's rule. (D) = Daniels cap, checked by Pavel. Placeholders are listed in the page's methodology.

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
- Threshold race(16). Intervals race(4). R is the predicted mile pace. Easy is 65% of 5km speed (a cap, not a target), editable.

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

## 8. Sub-Threshold Trend Tracker
- Only sessions that ended at RPE 7 or lower are logged (P). RPE is logged in the table but does not change the estimate.
- Excluded if peak HR (last minute or two of the last rep) is above 90% of max (P).
- Excluded if whole-session average HR (warm-up and cool-down included) is above 82% of max (P said about 81 to 82%; 82 is my placeholder).
- Threshold = race(16) (P). Each rep length maps to a race pace through the Sub-Threshold Session Generator table, run backwards.
- Estimate: median of the last 6 counted sessions within the past 6 weeks (P: 2 to 3 sessions a week expected). With fewer than 3 in that window it falls back to the last 6 counted sessions and is flagged stale (my choice).
- Confidence by counted sessions in the last 6 weeks: under 3 stale, 3 to 5 low, 6 to 9 moderate, 10+ good (my placeholders).
- Trend: straight-line fit to counted sessions within the past 12 weeks (P), shown from 4 sessions spanning at least 14 days (my choice). Older sessions stay visible, faded.
- Open: a "Recalculate all" button, to recompute stored implied thresholds from raw inputs after a model change.

## 9. Hard Workout Predictor
- Anchors (P): 400m with 60s rest = mile pace (8 to 10 reps); 800m, 90s = 3k; 1000m, 60s = 5k; 1600m, 2 min = 8k (4x1600m); 3000m, 3 min = 10k; 5000m, 3 min = marathon pace to 2% faster. Placeholders: 600m = 2k, 1200m = 5k, 2000m = 8k.
- Anchors apply at RPE 8 and standard rest (P).
- Rep count must change the answer (P). Short-distance predictors carry more volume than the race, long ones less; the crossover is about 5 to 10km. Equivalent race = anchor race x (reps / typical reps)^1.25 above the typical count, ^0.8 below. Exponents and typical counts are my placeholders, fitted to P's examples.
- Show the nearest common race distance, preferring the shorter, rounder one (P). The 5% round-up and the distance list are mine.
- Limits (placeholders): 25km of work; equivalent race under 400m refused; beyond the marathon capped at marathon pace.
- RPE moves the estimate (P): pace used = pace x (1 + 0.01 x (RPE - 8)). The 1% is a placeholder.
- Continuous mode (tempo or time trial, 1.5 to 30km): pace x (1 + 0.01 x (RPE - 10)) x (1 - 0.025). The 2.5% race-day effect is P's conservative pick from a recalled 2.3 to 4% range. Cross-checks: 5k pace = solo 3.25 to 3.75km pace implies 2.7 to 4.0%; 5k time = solo 4800m time implies 4.4%. Published evidence is mixed (one running study about 4% over 3km, some cycling studies show no effect).
- Pfitzinger 18-mile run with 14 miles at marathon pace fits continuous mode: 22.5km at marathon pace at RPE 7 predicts about 0.6% faster than that pace.
- Race model reliability (my judgement, untested): the 5km to half marathon relationship holds best for intermediate runners on moderate mileage. It may be less reliable for beginners and low mileage.
- Check case: 6x800 averaging 2:38.5 gives a 5k of 17:22 (17:12 to 17:32); the poster ran 17:07. One case, not a calibration.

## Simulation notes
- 100 to 109 km, extra 9 km easy: TSB about -3. Extra 9 km sub-T: about -4 to -5.
- 40 to 45 km, extra 5 km easy: about -2.
- Repeated +10% weeks from 100 km: TSB -3, -8, -12, -17 over weeks 2 to 5.
- Repeated +10% weeks from 40 km: TSB -1, -3, -5, -7.
- 10-week block to CTL 60 and TSB +10 from CTL 41 (constant build TSS, one taper week): build about 494 TSS a week, taper about 266. The 1.9 ramp cap and -10 TSB limit stop this, so it is not reachable.

## Open questions
- Hard Workout Predictor: confirm the RPE slope, the 1% band, typical rep counts, exponents, the 2000m anchor (reads about 5k for 2 reps; P earlier said 6 to 8k).
- Goal race and phases: race date, phase-specific focus.
- Graded taper shape (not built).
- Whether TSB misses structural load from big km jumps at high mileage.
- Low mileage and beginner handling (easy pace, very short weeks).
- Feedback loop (logging what was run) and sync across devices.
- Lifting load: measure (session RPE x minutes), conversion to TSS-equivalent (needs an anchor chosen by P), and whether lifting counts in full toward the TSB limits.

## Tactical Barbell Planner (lifting)
- Cycle (as given by the author, not checked against the book): W1 3-5x5 @70%, W2 3-5x5 @80%, W3 3-4x3 @90%, W4 3-5x5 @75%, W5 3-5x3 @85%, W6 3-4x1-2 @95%.
- High-rep mode (P): 10 reps in W1, W2, W4; 8 in W3, W5; 6 in W6. Reps in reserve kept from the standard week (Epley and Brzycki averaged), percentage re-derived. Week 6 uses 1.5 reps for the reps in reserve.
- Fighter: 2 days a week, 2-3 days between, days identical. W1 3-5x5 @75%, W2 3-5x5 @80%, W3 3-5x3 @90%, W4-6 repeat W1-3.
- Training max (author): % of 1RM, default 100%; the author uses 90% for deadlifts and 95% for weighted pull-ups from high-rep estimates.
- Zulu: 4 days a week, A/B/rest/A/B/rest/rest, 1-2 lifts per day. 3x5 @70% then 75% (W1), 3x5 @80% both (W2), 3x3 @90% both (W3), W4-6 repeat W1-3.
- Deadlift (all programmes): 1-3 sets a day on 1-2 days a week (max 6 sets a week); default 3 sets on 1 day.
## Marathon Plans (running)
One page with an author selector (Copeland, Daniels, Hansons, Pfitzinger), then a plan selector. Race, time, units and starting CTL are shared; author-specific fields show only for that author. The weekly table has a uniform Sessions column (key sessions only). Load rules are identical across authors. The marathon is scored at marathon pace (same TSS formula) and added to the race week's TSS, time and distance; CTL/ATL stay at race morning, with the post-marathon values in the table note. Replaces the four separate plan pages.

### Daniels 2Q Plans
- 2QA up to 40 mi, 2QB 41-55 mi, 2QC 56-70 mi; peak distance is always an input, the band only selects the sessions.
- 18 weeks, 2 quality sessions (Q1, Q2) plus 3-5 easy days (5-7 run days). Sessions and fraction of peak as given by the author, not checked against the book. Long runs are Q sessions at easy pace. Plan name 2QA; 2QB, 2QC etc. to follow.
- Paces: M = plain Riegel (no weekly-distance slowdown), T = race(17), I = race(4), R = race(1.7), E = 65% of 5km speed (cap).
- Weekly total = peak x fraction of peak; easy days share the remainder after Q1 and Q2. Race week (18) is by day.
- Load: TSS from pace vs race(16) threshold (same as Run TSS Calculator), CTL 42d / ATL 7d, Q2 Wed and Q1 Sun (placeholder), start CTL = week 1 TSS / 7 if blank, race day not scored.
- Slower runners (Daniels): 5-6 min T = 1 mile, 10-15 min = 2 miles, 16-20 min = 3 miles; page caps 1, 2, 3-mile T segments at 6, 15, 20 min (option).
### Hansons Plans (Beginner, Advanced)
- Beginner (Table 4.3): same pace rules as Advanced; warm-up/cooldown 1 mile (the book's note, and it fits the totals), Advanced 1.5. Marathon pace at 55 mi/week for Beginner (choice), 70 for Advanced.
- Book's Advanced program (Table 4.4), 18 weeks, 6 days a week, mileage as printed (26 to 63 mi), not scaled. Tue: speed weeks 2-10, strength weeks 11-17. Thu: tempo. Sun: long run every other week from week 3. Totals include 1.5 mi warm-up and cooldown on speed, strength and tempo days.
- Paces: marathon = predicted from the race result (70 mi a week; the book's 18:30 -> 3:00:21, page gives 3:00:12), no goal-time input because sessions run at current fitness, not goal pace (P), tempo = MP, strength = MP - 10 s/mi, speed = 5km pace, easy and recoveries = 65% of 5km speed.
- Load: same TSS rule as the Daniels page; race day not scored; start CTL = week 1 TSS / 7 if blank.
- Backlog: Daniels 2QD.
### Copeland Marathon Plan
- 15-week marathon add-on, weekly layout as printed in the book. Reps set by time at current fitness: 1000m = 3 min at race(16), 1600m = 6 min at race(21), 2000m = 8 min at race(30), 3000m = 10 min and 3200m = 12 min at race(32), 5000m = 15-18 min (default 16.5) at MP, 1.5% faster. Recoveries 60/75/90/90/120/180 s, walked at 6 km/h (TSS and time, not distance).
- Warm-up and cooldown 10 min each; 5km/10km races 20 min warm-up with 2 x 2 min at HM pace and 4 strides. Week 14 Tue progressive 92/93/100% of MP speed; week 14 Thu typo read as 8 x 1000m.
- Marathon pace = site prediction at 70 mi a week, no goal input. Easy = 65% of 5km speed (cap). Load as other plan pages; race day not scored; start CTL = week 1 TSS / 7 if blank (high, no ramp-in).


### Pfitzinger Marathon Plan
- 18/55, 12/55, 18/70 and 12/70 ("up to 55" and "55 to 70 miles per week"), distances as printed, not scaled; weeks labelled by weeks to goal. 12/70 week 7 days sum to 62, the book prints 59: days used.
- Paces: recovery 60% and GA 70% of 5km speed; medium-long and long = 85% of MP speed (input, 80-90%); LT = race(21); V reps = race(5) with jogs of 70% of rep time at recovery pace; MP = site prediction at the plan's weekly mileage (70 or 55), no goal input.
- Rest of a day's distance (not LT, MP or reps) split evenly into warm-up and cooldown at GA pace. Tune-up races: chosen distance (8/10/15 km, week 2 max 10) at race pace, rest of the mid-range total as WU/CD.
- Weekly table lists key sessions only (LT, MP run, V, long run, races) plus any other single run over 1:45 with its time; full detail in the week view.
- Strides and hills not scored (about +3-4 TSS per 8-10 strides).
- Optional 5-week recovery block (separate tables for the 55 and 70 plans); when on, the marathon is scored at MP so the recovery load starts correctly. Otherwise as the other plan pages.
