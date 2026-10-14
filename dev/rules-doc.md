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
- Race week (P, 2026-10-14): quality sessions on Friday or Saturday become easy runs, so there are at least 2 easy days before the race (P said 2, maybe 3; constant RACE_EASY = 2). Easy-run caps (P, 2026-10-14): race-week easy runs are capped at 40 min the day before the race and 70 min otherwise (RACE_SHAKE_MIN, RACE_EASY_MAX_MIN; P's numbers). Distance above the caps is dropped, not moved, so the week can fall below the 50% floor; the note says so. The 50 to 80% distance target is solved before the caps. Fixes 3 and 4 run days (before: 3 days a 2:17 easy run on Thursday, 4 days a 1:11 run on Saturday).
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
- Anchors (P): 400m with 60s rest = mile pace (8 to 10 reps); 800m, 90s = 3k; 1000m, 60s = 5k; 1600m, 2 min = 8k (4x1600m); 3000m, 3 min = 10k; 5000m, 3 min = marathon pace to 2% faster. 2000m, 2 min = 8k confirmed (P, 2026-10-13: 3x2000m at RPE 8 is a light 10k session; 6k would be extra cautious). Placeholders: 600m = 2k, 1200m = 5k.
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
- Hard Workout Predictor: confirm the RPE slope, the 1% band, typical rep counts, exponents (2000m anchor settled at 8k; 2 reps still read about 5.8k by the volume slide).
- Goal race and phases: race date, phase-specific focus.
- Graded taper shape (not built).
- Whether TSB misses structural load from big km jumps at high mileage.
- Low mileage and beginner handling (easy pace, very short weeks).
- Feedback loop (logging what was run) and sync across devices.
- Lifting load: measure (session RPE x minutes), conversion to TSS-equivalent (needs an anchor chosen by P), and whether lifting counts in full toward the TSB limits.

## Lifting Programme Planner (lifting)
- Cycle (as given by the author, not checked against the book): W1 3-5x5 @70%, W2 3-5x5 @80%, W3 3-4x3 @90%, W4 3-5x5 @75%, W5 3-5x3 @85%, W6 3-4x1-2 @95%.
- High-rep mode (P): 10 reps in W1, W2, W4; 8 in W3, W5; 6 in W6. Reps in reserve kept from the standard week (Epley and Brzycki averaged), percentage re-derived. Week 6 uses 1.5 reps for the reps in reserve.
- Fighter: 2 days a week, 2-3 days between, days identical. W1 3-5x5 @75%, W2 3-5x5 @80%, W3 3-5x3 @90%, W4-6 repeat W1-3.
- Training max (author): % of 1RM, default 100%; the author uses 90% for deadlifts and 95% for weighted pull-ups from high-rep estimates.
- Zulu: 4 days a week, A/B/rest/A/B/rest/rest, 1-2 lifts per day. 3x5 @70% then 75% (W1), 3x5 @80% both (W2), 3x3 @90% both (W3), W4-6 repeat W1-3.
- Deadlift (all programmes): 1-3 sets a day on 1-2 days a week (max 6 sets a week); default 3 sets on 1 day.
- Other programmes (from thefitness.wiki; wiki pages, not a book): r/Fitness Basic Beginner, GZCLP stage 1, 5/3/1 for Beginners, 6-day linear progression PPL (Metallicdpa), Dumbbell Stopgap, Dumbbell PPL. Summarised in our own words, source link under each table, no licence stated on the wiki.
- Linear tables project weight by the routine's per-session step if every session is completed; stage changes and deloads are listed as rules, not projected. Dumbbell routines are a workout sheet only (progression is by rule).
- Pounds converted to kg: 2.5 lb = 1.25 kg, 5 lb = 2.5 kg, 10 lb = 5 kg. Example start weights are placeholders.
- 5/3/1 for Beginners: training max = 90% of the estimated 1RM; +2.5 kg (upper) or +5 kg (lower) per three-week cycle; the wiki applies 3 core sets plus 5 x 5 to every appearance of a lift.
- nSuns LP (4-day, 5-day, 6-day deadlift focus, 6-day squat focus): from the spreadsheet bundle P supplied. One week set by set; TM = 90% of 1RM rounded up to the step (or typed in); progression by the 1+ set (0-1 none, 2-3 +5 lb, 4-5 +5-10 lb, over 5 +10-15 lb), not projected. The sheet's 6-day press TM uses the wrong 1RM; the page uses the press 1RM.
- Backlog: other external programmes once P sends them (BBB, Monolith, Westside for Skinny Bastards, PHAT etc. were listed, none requested yet).
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
- 2QD (71-85 mi) added. Backlog: none open for Daniels.
### Copeland Marathon Plan
- 15-week marathon add-on, weekly layout as printed in the book. Reps set by time at current fitness: 1000m = 3 min at 60-min race pace, 1600m = 6 min at 90-min, 2000m = 8 min at 120-min, 3000m = 10 min at 150-min and 3200m = 12 min at 180-min race pace (changed 2026-10-14 from distance anchors race(16/21/30/32); the 60/90/150 anchors fit Copeland's pace table within 2 s/km, slightly slower; 120 and 180 are my extension), 5000m = 15-18 min (default 16.5) at MP, 1.5% faster. Recoveries 60/75/90/90/120/180 s, walked at 6 km/h (TSS and time, not distance).
- Warm-up and cooldown 10 min each; 5km/10km races 20 min warm-up with 2 x 2 min at HM pace and 4 strides. Week 14 Tue progressive 92/93/100% of MP speed; week 14 Thu typo read as 8 x 1000m.
- Marathon pace = site prediction at 70 mi a week, no goal input. Easy = 65% of 5km speed (cap). Load as other plan pages; race day not scored; start CTL = week 1 TSS / 7 if blank (high, no ramp-in).


### Copeland Base (running)
- Ramp from a start CTL to week 1 of the Copeland marathon add-on (Tue 3x12, Thu 6x6, Sat 10x3, Sun 110, other days 60). No taper, no goal race.
- Run days: 7, or 6 with Friday dropped (P, 2026-10-13); 5 days not built. Plan row keeps Friday.
- Week: Mon/Wed/Fri easy, Tue long, Thu medium, Sat short sub-T, Sun long easy (about 25% of the week). Sub-T work at or under 25% of running time (recoveries excluded).
- Ladder (P): min 2x10, 2x6, 4x3; basic 3x10, 5x6, 10x3; extend long (3x11, 3x12, 4x10), then medium (7x5, 5x7, 6x6), then short (8x4, 10x3.5, 9x4, 10x4 only over 8 h). Scale down in reverse: short, medium, long.
- Ramp: largest weekly time (1 min steps, floor 4 h) with CTL ramp at or under target (default 1, input 0.1 to 2). Start ATL = CTL.
- My choices, not confirmed: interpolated rep pace and recovery for 3.5, 4, 5, 7, 9, 11 min; 120-min (8 min reps) and 180-min (12 min reps) anchors (the 60, 90, 150 anchors fit the book table); ladder minimums; 30 min easy-run floor; plan week 1 is not a ladder rung.

### Marathon Plan Recommender (running)
- Load chart (P, 2026-10-14): click a plan row (default: the most demanding plan that fits, else the first) to chart daily CTL, ATL and form (CTL - ATL) from the start values, through the last day of the plan, including held weeks before the join. Dashed lines: form floor and the join week. Hover or arrow keys give CTL, ATL, form and ATL/CTL for a day; table view lists end-of-week values. One axis (all in TSS/day). Colours from the dataviz palette (blue, orange, aqua). ATL/CTL limit is not drawn (a ratio does not share the axis); it is in the tooltip and table.
- Separate page (P, 2026-10-13). Inputs: race, start CTL, start ATL (blank = CTL), lowest form (default -20), highest ATL/CTL (default 1.3).
- Runs all 13 plans from the start values; fits if form never below the floor and ratio never above the limit. Reports week 1 TSS/day, peak 4-week TSS/day, lowest form, highest ratio, with weeks.
- Join late (my choice, default 85%): skips leading plan weeks below that % of 7 x CTL, holds current load until then. 0 = week 1. Added 2026-10-14 after Hansons Beginner (week 1 far below load) failed while Advanced passed at 38:43 10k, CTL 50. Adds "Joins" column and "Never reaches your load" flag.
- Time columns (P, 2026-10-14): average and peak running time per week, join week to the week before race week (race week excluded). Peak = longest single week, not a 4-week average.
- CTL estimate (my design, 2026-10-14): avg hours/week x TSS/hour / 7, TSS/hour from easy at 65% of 5k speed plus a typed share of time at threshold (100 TSS/h; blank 15%, max 50%, P asked for a text input over a dropdown); ATL weights the last 7 days at 0.632. Optional average easy pace replaces the 65% default (P's suggestion: most people who don't know their CTL run easy too fast); cross-checked against race(16) and 5k speed. Assumes steady training. Fills start CTL/ATL on button press.
- Plan settings fixed at Marathon Plans defaults (Daniels at band top, 6 days). Plan code is a copy of Marathon Plans'; tests/check_plans_sync.py fails the build if they differ.
- Floor -20 chosen by P for running (not a research threshold). Ratio 1.3 from TrainerPlan's sweet-spot band.
- Not built: tests from actual recent weeks, a ranking, a lower ratio bound (0.8).

### Pfitzinger Marathon Plan
- 18/85 and 12/85 (70-85 mi) added; marathon pace at 85 mi/week; 12/85 week 7 (recovery) days sum to 74, book prints 70, built as printed. 18/55, 12/55, 18/70 and 12/70 ("up to 55" and "55 to 70 miles per week"), distances as printed, not scaled; weeks labelled by weeks to goal. 12/70 week 7 days sum to 62, the book prints 59: days used.
- Paces: recovery 60% and GA 70% of 5km speed; medium-long and long = 85% of MP speed (input, 80-90%); LT = race(21); V reps = race(5) with jogs of 70% of rep time at recovery pace; MP = site prediction at the plan's weekly mileage (70 or 55), no goal input.
- Rest of a day's distance (not LT, MP or reps) split evenly into warm-up and cooldown at GA pace. Tune-up races: chosen distance (8/10/15 km, week 2 max 10) at race pace, rest of the mid-range total as WU/CD.
- Weekly table lists key sessions only (LT, MP run, V, long run, races) plus any other single run over 1:45 with its time; full detail in the week view.
- Strides and hills not scored (about +3-4 TSS per 8-10 strides).
- Optional 5-week recovery block (separate tables for the 55 and 70 plans); when on, the marathon is scored at MP so the recovery load starts correctly. Otherwise as the other plan pages.

### Site index
- Landing page is Start here plus a link to tools.html (P, 2026-10-14). tools.html groups Running (planning and load, sessions, race and pace) and Lifting. Hybrid group to come with a lifting TSS tool.
- Theme switch: one 32 px icon button, top right (auto half-circle, sun, moon; click cycles). Same block on every page via shared/apply_theme.py; the build fails if a page differs.
- "Start here" list at the top of the index (P, 2026-10-14): 8 plain-language questions, each linking to one tool. Questions and the tool picked for each are my choices; the build fails if a linked tool title is not in the tool list.

### Hybrid Load Planner (running and lifting)
- Separate page (P, 2026-10-14): one week of runs and lifts, repeated up to 12 weeks, giving CTL, ATL, TSB, ATL:CTL and CTL ramp.
- Lift score = max(10, 100 x lower 1 / upper 0.33 x compound 1 / isolation 0.5 x (1 - 0.12 x reps left on last set) x sqrt(sets / 3)). All factors are estimates fitted to P's anchors (squat to failure 100, OHP to failure about 33, light curls about 10, Tactical Barbell style about 60). Reps left is for the last set; 3 sets is standard. Sets curve: P agreed it must be concave.
- Several lifts in a day: pool sets within each type; day total = largest type + 0.5 x the others (my estimate; 3 squat sets plus 3 sets leg curls at 2 reps left = 119, looks high).
- Lifting counts in full for ATL and at an adjustable weight for CTL, default 0.75 (my guess; P wanted ATL weighted above CTL). A common discount on both was rejected as the same as lowering the anchors. Weight below 1 means steady lifters show lower form by design (running 50 + lifting 30 per day: form -7.5 at 0.75, -15 at 0.5).
- Same-day hit like running TSS (P: DOMS depends on exercise familiarity; same logic as a hard run). New or returning exercises not modelled.
- Ramp is CTL-based, with an i button splitting it into running/existing versus lifting (exact, since CTL is a linear sum).
