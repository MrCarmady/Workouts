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
- Threshold race(16). Intervals race(4). R is the predicted mile pace. Easy is 65% of 5km speed (a cap, not a target), editable (pace box or percentage).

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
- Race results (P, 2026-10-29): the tracker takes race results (distance, date, time), converts each to an implied threshold with the same race model, plots them as diamonds, and compares them with the sub-T estimate from the 6 weeks before (median of up to 6 counted sessions): sub-T predicted race time and the gap. The estimate, trend and confidence do not use races. Purpose: tighten the model against reality, so that without racing a recent sub-T block can estimate an all-out race. First data point: 18:52 5k, Sutcliffe parkrun, 17 Oct 2026 (implied threshold about 4:03/km).

## 9. Hard Workout Predictor
- Anchors (P): 400m with 60s rest = mile pace (8 to 10 reps); 800m, 90s = 3k; 1000m, 60s = 5k; 1600m, 2 min = 8k (4x1600m); 3000m, 3 min = 10k; 5000m, 3 min = marathon pace to 2% faster. 2000m, 2 min = 8k confirmed (P, 2026-10-13: 3x2000m at RPE 8 is a light 10k session; 6k would be extra cautious). Placeholders: 600m = 2k, 1200m = 5k.
- Anchors apply at RPE 8 and standard rest (P).
- Rep count must change the answer (P). Volume slide (changed 2026-10-29): equivalent race = anchor race x g(r), r = reps / typical reps; r below 1: r^0.8; 1 to 1.6: r; above 1.6: r x (r/1.6)^0.93. Fitted to P's 1k points (5 reps = 5k, 8 about 8k, 12 = 17.5k at 60 s); typical reps for 1000m now 5. Placeholders.
- Rest (P, 2026-10-29): equivalent race x (standard rest / rest)^0.38, ratio limited to 0.4 to 2.5, rest under 15 s treated as 15 s. More rest = easier session = shorter equivalent race: 12 x 1k is 17.5k at 60 s and 15k at 90 s; 6 x 1k at 90 s about 5.1k (about 5 x 1k at 60 s). P's own example 12 x 1k at 4:00, 60 s, RPE 8: 5k 18:33, 10k 38:41 (was 18:59 and 39:35). Standard rest is the anchor rest, not growing with volume. Placeholders, not validated.
- Show the nearest common race distance, preferring the shorter, rounder one (P). The 5% round-up and the distance list are mine.
- Limits (placeholders): 25km of work; equivalent race under 400m refused; beyond the marathon capped at marathon pace.
- RPE moves the estimate (P): pace used = pace x (1 + 0.01 x (RPE - 8)). The 1% is a placeholder. RPE limited to 6 to 10 (P, 2026-10-29): below 6 is an error, because pace at low effort says almost nothing about race fitness and 1% per point is far too small there (easy is about 65% of 5k speed). Session equals box (2026-10-30): shows the actual distance (6.9k) unless within 5% of a standard distance; includes the rest effect; caption 'pace, at RPE 8 effort, rest included'. Worked example from a run-club friend: 8x1k at 3:17, 90s rest, RPE 8 gives 16:07 5k (6.9k equivalent: 8k at 60s rest x 0.86); the same session at 60s rest gives 15:58. Predicted 5k pace is faster than the session pace because 8 reps is more volume than the 5x1k that equals 5k. Warnings (P, 2026-10-29; limits are my placeholders): RPE below 7 or reps below 0.6 x the typical count: 'too easy for a meaningful prediction, try a harder effort or more reps next time'. RPE above 9 or reps above 2 x typical: 'don't leave the race in training; the prediction is solid, but recovery may be excessive'. Continuous and Aussie modes use the RPE rule only. The box formerly 'Reps equal about' is 'Session equals' (what reps and rest equal at RPE 8, not changed by RPE); the first tile shows the RPE-adjusted pace. Open: a proper RPE to race-pace model (the Sub-Threshold Trend Tracker only uses RPE 7 or lower as an inclusion gate).
- Continuous mode (tempo or time trial, 1.5 to 30km): pace x (1 + 0.01 x (RPE - 10)) x (1 - 0.025). The 2.5% race-day effect is P's conservative pick from a recalled 2.3 to 4% range. Cross-checks: 5k pace = solo 3.25 to 3.75km pace implies 2.7 to 4.0%; 5k time = solo 4800m time implies 4.4%. Published evidence is mixed (one running study about 4% over 3km, some cycling studies show no effect).
- Pfitzinger 18-mile run with 14 miles at marathon pace fits continuous mode: 22.5km at marathon pace at RPE 7 predicts about 0.6% faster than that pace.
- Race model reliability (my judgement, untested): the 5km to half marathon relationship holds best for intermediate runners on moderate mileage. It may be less reliable for beginners and low mileage.
- Aussie quarters (P, 2026-10-14/15): mode in the predictor. Always 8 reps (P: a classic session, no rep input; a list of times must have 8 entries or give one average). Floats count (P): 8 x (400m + 200m float) = 4800m, total time read as the 5k time; the race itself is quicker by up to 15 s (P's rule of thumb), so range = total to total minus 15 s. Float times required. RPE applied to the total (mine). Warnings: floats as fast as the 400s, or more than 10% slower than M pace (10% is mine). 4k added to the common-distance list. Replaced earlier versions (4k anchor; variable rep counts) after P's corrections. Not validated.
- Check case: 6x800 averaging 2:38.5 gives a 5k of 17:22 (17:12 to 17:32); the poster ran 17:07. One case, not a calibration.

## Classic Session Generator changes (P, 2026-10-15)
- Ladder 5-4-3-2-1: jog after each rep defaults to half of that rep (P chose this from the Outside ladders article); fixed jog (90 s) is an option; optional 0 to 8 extra "1 min easy + 1 min hard" repeats after the 1-min rep (down order only), as in the article. Paces are P's own (the article gives effort only).
- Aussie quarters: always 8 reps in the generator too (P).
- Pre's 200s added (P, from the Outside article crediting Bowerman): fast 200 at mile pace to 2% slower (2% is my reading of "slightly slower"), recovery 200 33 1/3% slower, no standing rest, 12 pairs default (about 3 miles), 4 to 30 pairs.

## Simulation notes
- 100 to 109 km, extra 9 km easy: TSB about -3. Extra 9 km sub-T: about -4 to -5.
- 40 to 45 km, extra 5 km easy: about -2.
- Repeated +10% weeks from 100 km: TSB -3, -8, -12, -17 over weeks 2 to 5.
- Repeated +10% weeks from 40 km: TSB -1, -3, -5, -7.
- 10-week block to CTL 60 and TSB +10 from CTL 41 (constant build TSS, one taper week): build about 494 TSS a week, taper about 266. The 1.9 ramp cap and -10 TSB limit stop this, so it is not reachable.

## Open questions
- Unify the Hard Workout Predictor and the Sub-Threshold Trend Tracker (P, 2026-10-29: leave for now, resolve later). They disagree: the tracker maps rep time and pace to a race pace and ignores rep count and rest; the predictor uses rep count, rest and RPE. For the same sessions the implied threshold differs by up to 24 s/km (5x1k at 4:00: tracker 3:59, predictor 4:15; 12x1k: 3:59 vs 3:56; 6x800 at 3:50: 3:51 vs 4:15). They roughly match only for about 10 to 12 reps of 3 to 4 min. Draft shared model (my construction, not built, not validated): predictor engine (volume, rest) with the equivalent race x 1.5 per RPE point below 8 (divided by 1.5 per point above). It reproduces the predictor at RPE 8. The 1.5 is a rough fit to the tracker's table assuming its sessions are RPE 6 (the page default); the table implies 1.3 to 1.7 per point at RPE 6 and much more if its sessions are RPE 7. One RPE point moves the threshold about 6 s/km (2.5%), against 1% per point now. Sample outputs at RPE 7 (threshold, 5k): 10x1k @4:00 60 s 3:58, 18:30; 5x1k 4:11, 19:31; 12x1k 3:53, 18:04; 4x1600 @4:05 4:09, 19:22; 6x6 min @4:07 4:06, 19:05; 3x12 min @4:19 4:19, 20:07; 6x800 @3:50 4:09, 19:21. P's view: tracker predictions are fairly good so far, if anything a little conservative because most sessions are run straight after lifting (the draft model would read slightly slower at RPE 7, untested).
- Calibration plan (P, 2026-10-29): enter the Pymmes parkrun result and have the tracker show something that reflects actual results, so the model can be tightened. Goal: when P goes without racing for a while, estimate his all-out race from recent sub-T sessions. Needs real sessions with dates and RPE, plus race results; FIT files available for sessions. Not designed yet (where the race result sits on the trend chart, how the residual feeds back).
- Low-RPE handling (P, 2026-10-29): the Hard Workout Predictor now accepts RPE 6 to 10 only. A proper RPE to race-pace model replaces the 1% per point placeholder (see unification above).
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
- GZCLP 1RM defaults (P, 2026-10-16): optional 1RM per lift fills T1 and T2 start weights at 77% and 62% of 1RM, rounded to the step (1.25, 2.5 or 5 kg), editable after. Placeholders derived from the 1RM and Scheme model with the last set 3 reps from failure (T1 5x3 gives 77% upper, 76% lower; T2 3x10 gives 62%, 61%). Sources disagree: Set for Set about 81-86% (T1) and 62-72% (T2) of 1RM; Liftosaur 85% of 5RM (about 74%) for T1, and its own sample says T2 35% of 1RM, which contradicts its own 65-85% of a 2-3RM principle line. P noted 5x3 at 77% looks easy; accepted because the progression adds weight each session. Changing the step re-fills lifts that have a 1RM, overwriting hand edits to their T1 and T2 weights.
- Linear tables project weight by the routine's per-session step if every session is completed; stage changes and deloads are listed as rules, not projected. Dumbbell routines are a workout sheet only (progression is by rule).
- Pounds converted to kg: 2.5 lb = 1.25 kg, 5 lb = 2.5 kg, 10 lb = 5 kg. Example start weights are placeholders.
- 5/3/1 for Beginners: training max = 90% of the estimated 1RM; +2.5 kg (upper) or +5 kg (lower) per three-week cycle; the wiki applies 3 core sets plus 5 x 5 to every appearance of a lift.
- nSuns LP (4-day, 5-day, 6-day deadlift focus, 6-day squat focus): from the spreadsheet bundle P supplied. One week set by set; TM = 90% of 1RM rounded up to the step (or typed in); progression by the 1+ set (0-1 none, 2-3 +5 lb, 4-5 +5-10 lb, over 5 +10-15 lb), not projected. The sheet's 6-day press TM uses the wrong 1RM; the page uses the press 1RM.
- Backlog: other external programmes once P sends them (BBB, Monolith, Westside for Skinny Bastards, PHAT etc. were listed, none requested yet).
## Marathon Plan Viewer (running)
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
- Paces: marathon = predicted from the race result (70 mi a week; the book's 18:30 -> 3:00:21, page gives 2:58:43 since the 2026-10-15 factor change, was 3:00:12), no goal-time input because sessions run at current fitness, not goal pace (P), tempo = MP, strength = MP - 10 s/mi, speed = 5km pace. Easy running follows the book's Table 3.5 (audiobook supplement p. 33) by predicted marathon time, interpolated, nearest row outside 2:10-5:00 (P, 2026-10-27: plans follow the books as printed, the load assumes perfect execution): Easy Aerobic A on easy days, warm-ups, cooldowns and rep recoveries; Easy Aerobic B on Saturdays (Table 3.1 note); Moderate Aerobic/Long Run column on long runs. The column-to-day mapping other than Saturday is my reading (supplement does not give it). Recovery column unused. Easy % input does not apply to Hansons. Recommender and Marathon Plan Viewer share the code.
- Load: same TSS rule as the Daniels page; race day not scored; start CTL = week 1 TSS / 7 if blank.
- 2QD (71-85 mi) added. Backlog: none open for Daniels.
### Copeland Marathon Plan
- 15-week marathon add-on, weekly layout as printed in the book. Reps set by time at current fitness: 1000m = 3 min at 60-min race pace, 1600m = 6 min at 90-min, 2000m = 8 min at 120-min, 3000m = 10 min at 150-min and 3200m = 12 min at 180-min race pace (changed 2026-10-14 from distance anchors race(16/21/30/32); the 60/90/150 anchors fit Copeland's pace table within 2 s/km, slightly slower; 120 and 180 are my extension), 5000m = 15-18 min (default 16.5) at MP, 1.5% faster. Recoveries 60/75/90/90/120/180 s, walked at 6 km/h (TSS and time, not distance).
- Warm-up and cooldown 10 min each; 5km/10km races 20 min warm-up with 2 x 2 min at HM pace and 4 strides. Week 14 Tue progressive 92/93/100% of MP speed; week 14 Thu typo read as 8 x 1000m.
- Marathon pace = site prediction at 70 mi a week, no goal input. Easy = 65% of 5km speed (cap). Load as other plan pages; race day not scored; start CTL = week 1 TSS / 7 if blank (high, no ramp-in).


### Copeland Base (running)
- Ramp from a start CTL to week 1 of the Copeland marathon add-on (Tue 3x12, Thu 6x6, Sat 10x3, Sun 110, other days 60). No taper, no goal race.
- Run days: 7, or 6 with Friday dropped (P, 2026-10-13). Plan row keeps all seven days.
- 5 run days (P, 2026-10-16): 2 easy, 2 sub-T, 1 long. Mon rest or cross-train, Tue sub-T long, Wed easy, Thu sub-T medium, Fri rest or cross-train, Sat easy, Sun long easy. Which two sub-T sessions to keep, and the day layout, are my choices (P gave only the 2/2/1 split): short dropped, matching "short is cut first". Ladder climbs L and M only. Cross-training is not counted in TSS or CTL (P: cross-training TSS is a later topic). Plan week 1 stays the book's 7-day week, so the last row is a step from 5 runs to 7 and can show "ramp above target".
- Week: Mon/Wed/Fri easy, Tue long, Thu medium, Sat short sub-T, Sun long easy (about 25% of the week). Sub-T work at or under 25% of running time (recoveries excluded).
- Ladder (P): min 2x10, 2x6, 4x3; basic 3x10, 5x6, 10x3; extend long (3x11, 3x12, 4x10), then medium (7x5, 5x7, 6x6), then short (8x4, 10x3.5, 9x4, 10x4 only over 8 h). Scale down in reverse: short, medium, long.
- Ramp: largest weekly time (1 min steps, floor 4 h) with CTL ramp at or under target (default 1, input 0.1 to 2). Start ATL = CTL.
- My choices, not confirmed: interpolated rep pace and recovery for 3.5, 4, 5, 7, 9, 11 min; 120-min (8 min reps) and 180-min (12 min reps) anchors (the 60, 90, 150 anchors fit the book table); ladder minimums; 30 min easy-run floor; plan week 1 is not a ladder rung.

### Marathon Plan Finder (running)
- Easy pace basis switch (P, 2026-10-29), on Marathon Plan Viewer and Finder, saved in the profile, default 'As written in the book'. As written: Daniels 74% of 5k speed (middle of P's quoted 4:52-5:22/km at 18:52, one point only, Daniels' table not seen), Copeland 70% (Table 2.3 ceiling, 11 rows checked), Hansons Table 3.5, Pfitzinger recovery 60% and GA 70%. 'My easy pace setting' (65% default): the setting replaces easy pace in every plan (Hansons Easy A and B, Pfitzinger GA; Pfitzinger recovery = 60% or the setting if lower; Hansons long run shifts by the same seconds as Easy B (P, 2026-10-29: if easy is slower than the book, long runs should be too); all other paces unchanged; Viewer shows one 'Easy (A and B)' tile when A and B are equal). It drives paces, TSS, CTL/ATL fit and Intensity mix together, so the Easy bucket is no longer split by source. Earlier (2026-10-28) Daniels and Copeland easy were fixed at the setting as P's stand-in for truly easy running (Copeland asks for easy below 70% of max HR); that is now the 'my setting' option.
- Intensity mix walking zone (P, 2026-10-28): Copeland walked rep recoveries are their own Walking zone at 6 km/h (not in the rep zone); 5000m reps (MP+1.5%) stay in Marathon pace.
- Intensity mix (P, 2026-10-28): stacked bars of time or distance share by zone for all 13 plans, zones from each plan's own session labels (Recovery = Pfitzinger recovery only; Easy; Long and steady; Marathon pace; Sub-threshold = Hansons MP-10 and Copeland 150/120/90 min reps; Threshold; 5k and faster; races placed by pace, 98%+ of 5k speed = 5k and faster, 89.5-98% = threshold, so 10k and HM races are threshold). Key shows each zone's % of 5k speed range; values shown on segments of 3% or more. Key shows each zone's range as % of 5k speed and pace, per km unless saved units are miles, one line per zone with a caption under the key (P, 2026-10-28); a colour-chip version for sub-3% zones was tried and dropped. Whole plan, marathon day excluded, not affected by CTL or join week. Daniels and Copeland easy = our 65% assumption. Bubble and cumulative views were tried and dropped.
- Load chart (P, 2026-10-14): click a plan row (default: the most demanding plan that fits, else the first) to chart daily CTL, ATL and form (CTL - ATL) from the start values, through the last day of the plan, including held weeks before the join. Dashed lines: form floor and the join week. Hover or arrow keys give CTL, ATL, form and ATL/CTL for a day; table view lists end-of-week values. One axis (all in TSS/day). Colours from the dataviz palette (blue, orange, aqua). ATL/CTL limit is not drawn (a ratio does not share the axis); it is in the tooltip and table.
- Separate page (P, 2026-10-13). Inputs: race, start CTL, start ATL (blank = CTL), lowest form (default -20), highest ATL/CTL (default 1.3).
- Runs all 13 plans from the start values; fits if form never below the floor and ratio never above the limit. Reports week 1 TSS/day, peak 4-week TSS/day, lowest form, highest ratio, with weeks.
- Join late (my choice, default 85%): skips leading plan weeks below that % of 7 x CTL, holds current load until then. 0 = week 1. Added 2026-10-14 after Hansons Beginner (week 1 far below load) failed while Advanced passed at 38:43 10k, CTL 50. Adds "Joins" column and "Never reaches your load" flag.
- Time columns (P, 2026-10-14): average and peak running time per week, join week to the week before race week (race week excluded). Peak = longest single week, not a 4-week average.
- CTL estimate (my design, 2026-10-14): avg hours/week x TSS/hour / 7, TSS/hour from easy at 65% of 5k speed plus a typed share of time at threshold (100 TSS/h; blank 15%, max 50%, P asked for a text input over a dropdown); ATL weights the last 7 days at 0.632. Optional average easy pace replaces the 65% default (P's suggestion: most people who don't know their CTL run easy too fast); cross-checked against race(16) and 5k speed. Assumes steady training. Fills start CTL/ATL on button press.
- Plan settings fixed at Marathon Plan Viewer defaults (Daniels at band top, 6 days). Plan code is a copy of Marathon Plan Viewer's; tests/check_plans_sync.py fails the build if they differ.
- Floor -20 chosen by P for running (not a research threshold). Ratio 1.3 from TrainerPlan's sweet-spot band.
- Race date and ramp (P, 2026-10-26): optional race date (up to 2 years) places each plan so its last day is race day; spare days before it are a ramp from today. P chose: cap 1.0 CTL per week (default), the ramp target is the lowest start CTL at which the plan passes the fit test, the slowest ramp (a straight rise over all spare days), and ATL and CTL simulated at the start and end of the ramp (ATL at plan start is real, above CTL). Daily ramp TSS from the CTL update rule. Fits as you are = hold current load until the start. Not enough ramp: "Needs N more weeks" (search up to 52). Fewer weeks than the plan: joined part-way. Join percentage is used with a race date (P, 2026-10-27, after seeing 18/55 need more weeks than 18/70): entry week = earliest plan week not lighter than that % of the CTL the ramp reaches; each week skipped adds 7 days to the ramp; 0 = week 1. Fit does not pick the week, so a plan cannot dodge its own spike by joining late (a fit-based pick joined 18/85 at week 16 of 18). "Needs N more weeks" re-picks the entry for each length. No qualifying week: week 1 and the "Never reaches your load" flag. P's reasoning: periodised plans ramp faster than year-round training, so some plans carry their own TSB/A:C spike; the entry rule fixes a start-load mismatch, not that spike. Ramp form is not tested. Cap applies to the ramp only; plans rise faster once started (Copeland add-on from CTL 42: about +3 CTL a week early on). Session content for ramp weeks not planned yet.
- Out-of-limit values (P, 2026-10-27): in the plans table, Lowest TSB below the form floor and Highest A:C above the limit are shown in red bold. Same test as the Result column, on the unrounded values.
- Plans table width (P, 2026-10-27): with a race date the table has 11 columns and must fit its box at 1280 px without a sideways scroll. Cells 0.95rem, headers 0.7rem, Result column narrower, "Needs N more weeks" on its own line. A snapshot scenario checks it. Narrower windows (about 900 px and under) still scroll inside the box.
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


## Personal pace inputs (2026-10-15)
- Easy pace % of 5km speed (default 65, range 50 to 85) and sub-threshold buffer % slower (default 0, range 0 to 10), on Plan Builder, Marathon Plan Viewer, Copeland Base and the Recommender. Saved in the shared browser profile.
- Easy % feeds E paces only when the easy pace basis is 'My easy pace setting' (it always feeds the Recommender load estimate). Buffer slows Plan Builder sub-threshold (race 21) and the Copeland rep paces (3 to 12 min); 5km reps, race paces and the Hansons table paces are unchanged.
- Plan Builder keeps its easy pace box; if filled it overrides the percentage.
- Marathon Plan Viewer (P, 2026-10-29): the buffer box shows only when Copeland is selected or the value is invalid, as in the Recommender, because it changes nothing in the other plans (Plan Builder and Copeland Base use it for sub-threshold pace and keep the box).
- Recommender: the buffer box is hidden unless the Copeland row is selected or the value is invalid; a hidden buffer still applies to the Copeland row. Invalid easy % or buffer shows an error.

## Marathon factor (2026-10-15)
- Marathon = F x half marathon (replaces 2 x half + 7/10/13/17/25 min). F = 2.10 at 70+ mi/week, 2.13 at 60, 2.17 at 50, 2.25 at 35 or less, linear between. 70 mi assumed when blank. Never below plain Riegel (2.085).
- 2.10 is the author's (1:40 half -> 3:30 at 70 mi). Cross-check: Kejelcha 56:51 half, 1:59:41 marathon (author-supplied, unverified) = 2.105, so no separate band above 70 mi.
- 60/50/35 mi factors are placeholders (old table converted at a 100 min half). Author's low-mileage blow-ups (1:39/4:05, 1:29/3:31) suggest the low end may be too optimistic; weekly mileage in those blocks unknown.
- Effect: faster halves get faster marathons (1:20 at 40 mi: 3:02:20 -> 2:57:52), slower halves slower (1:50 at 40 mi: 4:02:20 -> 4:04:34); 1:40 unchanged.

## Compare with (2026-10-15)
- Race Prediction Calculator: optional column for Daniels (VDOT), Hansons or Pfitzinger, one at a time, with difference vs ours.
- Hansons and Pfitzinger are fitted curves/ratios, not the books' tables (public site). No extrapolation; unsupported inputs or distances show a dash plus a note.
- Our VDOT is not tuned to the printed Daniels table (a few seconds apart; author's call).
- At 18:30 5km: Daniels 2:57:08, Hansons 3:00:21 (matches chart), ours 2:58:43 (70 mi default).
- Tinman added (2026-10-16): reverse-engineered from six sample sheets (5k 13:00-29:00). Pure scaling: time = 5k time x factor(d). 400m 0.056878, 800m 0.13338, 1000m 0.17358 added 2026-10-28 from four more sheets (5k 15:00, 17:00, 19:00, 23:00; constant across all), output rows only. d >= 3000m: (d/5000)^1.0579, no marathon fade. Mile 0.29447, 1500m 0.2723. Author accepted a broad fit (his tool's input and output curves differ slightly, e.g. 2400m by 1.26%, mile 0.17%). Range 13:00-29:00 5k equivalent. At 18:30 5k: marathon 2:56:39.
## % of world record (2026-10-16)
- Race Prediction Calculator: '% WR' column on every row, plus a 'Same % of world record' compare option (constant % of WR pace across distances).
- Race Prediction Calculator: 400m, 800m and 1000m rows (P, 2026-10-26), output only, same formula, no comparison-model values; 1000m record 2:11.83 (Wanyonyi, 2026).
- Male WRs (s): 1500m 206.00, mile 222.66 (3:42.66, author), 3km 437.55, 5km 755.36, 10km 1571.00, 10 miles 2664 (44:24 Gebrselassie, ratified; author chose it over a faster time by a sanctioned athlete; a 10km-to-half power law would give 42:55, so % at 10 miles reads high), half 3411 (56:51 Kejelcha, unratified; author's choice, revert to 57:20 Kiplimo if rejected), marathon 7170 (1:59:30 Sawe, London 2026, author-supplied, unverified by me).
- Planned later: women's and masters' records.
- At 18:45 5k our model gives ~67.1% (5k) and 66.0% (marathon).
## 1RM and Scheme Calculator (renamed from Lift Scheme Calculator, 2026-10-16): session input
- Toggle 'One set' / 'Whole session'. File name unchanged (lift-scheme-calculator.html) so links and the artifact URL stay valid.
- New inputs 'Sets done' and 'Rest between sets' (1 / 2 / 3+ min). Reverse of the scheme model: n = reps + last-set RIR + f x (sets - 1), e1RM = load / pct(n). Sets = 1 behaves exactly as before.
- Base fatigue per set for any rep count read by straight-line interpolation (3: 0.75, 5-6: 1.0, 8: 1.2, 10: 1.5, 12: 1.6). Shows 1RM sensitivity at +/-25% loss per set.
- Equal sets only. Heavy-vs-light fatigue difference is an unverified assumption (one bench study found no difference in rep sustainability at 80% vs 50%).
- 3x6 BW pull-ups, 2 min, RIR 2 at 76 kg: e1RM ~102 kg total, fresh set ~10 reps.
## Hard Workout Predictor validation log (started 2026-10-18)
- Pre-race prediction (P, set before the race): central 18:45, range about 18:40-19:05.
- 2026-10-17, Sutcliffe parkrun: 18:52 (+7 s, +0.6% vs central; inside the range). Flat tarmac, fast course, cold, sunny, little wind, no pacer, near-ideal conditions. Even splits by power: 332 W (first ~800 m), 340 W (next ~2 miles), 346 W (last 800 m), 406 W (final 27 s). Normal training week, no extra fatigue. Course has a couple of tight turns and two 180-degree turns. PB before the race was 18:54.
- One data point, not a calibration. Next: Pymmes, about 2 weeks later.

## Race Prediction Calculator: two results (P, 2026-10-19)
- Optional second result. Each result predicts separately; blend per target distance with weights 1 / |ln(target / result distance)| (power 1 chosen by P as a starting point; mine as a form, not fitted). Result at the target distance takes all the weight.
- Comparison column uses the same blend of each model's predictions from each result (P).
- P's reasoning: the mile (5:23.4) is close to a 10/10 effort and shows potential; the 10k (39:43) is the more relevant anchor but was run blind with a strong negative split, so it is slow for his ability. Blend gives 5km 18:51 and half 1:27:06 (22/78); actual 5km 18:52.
- Both results must be at different distances (P, 2026-10-19): same-distance pairs are rejected with a message.
- Two results only (P). Other pages still read result 1 only.

## Cross-training and the stress test (P, 2026-10-19)
- Cross-training should count towards CTL (P). Not yet built into the planners: needs a way to enter cross-training TSS (see open questions in the chat of 2026-10-19) and a decision on which planners get the input.
- Treadmill Flat Equivalent gained a Walking mode (ACSM walking equation) and an optional TSS output (P agreed). The 12/3/30 session is about 13 TSS against about 24 for a 30-minute easy jog.
- Time parsing is now strict everywhere (shared core): plain minutes (1 or 2 digits, decimals), m:ss, h:mm:ss, with seconds and minutes after the first part 00 to 59. Rejected: 18:75, 18:5, 0x10, 1e2, Infinity, signs, spaces inside, 7+ digit numbers. Digits only (3 to 6 digits) are still read from the right.
- Range checks added: Lift Scheme Calculator (bodyweight 30 to 250 kg, weight up to 1000 kg, reps up to 30, RIR 0 to 10); Lifting Programme Planner (bodyweight 30 to 250 kg, weight up to 1000 kg, reps up to 30, numbers outside 0 to 1000 read as blank).
- Fixed crashes in the Lifting Programme Planner from late change events on replaced or hidden fields.

## Cross-Training TSS (P, 2026-10-19)
- New page. Activities: bike, rower, treadmill walking, other (heart rate; elliptical, Stairmaster). Dropdown labels cleaned 2026-10-26 (P).
- Bike: TSS = hours x (power / FTP)^2 x 100 (P: FTP as the anchor).
- Rower: watts, not pace (P). Threshold = 2k split + 15 s per 500m from Paul's law (P: add 5 s per 500m for each doubling; 2k + 15 about an hour). Threshold watts can be entered instead.
- Lift Scheme Calculator warm-up (P, 2026-10-20): section under the scheme tables. Top set from 1/3/5/8RM or own weight. Ladder bar x 10 (bodyweight x 8 for pull-ups and dips; dumbbell lifts start at 50% x 10 then 70% x 3, 85% x 2, no lightest-dumbbell set (P, 2026-10-29); bodyweight x 8 per leg for split squat), 50% x 5, 70% x 3, 85% x 2 of the top set (P's scheme with my trims). Included for bodyweight and dumbbell lifts too (P asked why not). Convention, not research; reps and percentages not adjustable; duplicate steps dropped.
- Load weights for combining sources (P, 2026-10-20, not built yet): each source has a CTL weight (stimulus) and an ATL weight (fatigue). Running 1 / 1. Lifting 0.75 / 1 (built). Cross-training 0.8 / 0.8 (P: ATL below CTL would give odd outcomes; may be lower in practice, to be adjusted later). Fatigue extra from back-to-back and double sessions (adjusted TSS minus TSS): CTL 0.75, ATL 1 (P: matches lifting for now; a few percentage points either way). Steady-state form shift from the extra is -(1 - CTL weight) x average daily extra. All placeholders; adjustable settings, not calibrated.
- Rower inputs (P, 2026-10-20): the two dropdowns (threshold from, session shown as) removed. Split and watts are the same quantity, so every box takes either: colon = time, plain number = watts. Boxes: 2k time or watts, session average split or watts, optional threshold split or watts (overrides 2k + 15 s). Old saved values for the removed controls are ignored.
- Bike checks (P found 60 min at 290 W with FTP 250 accepted, 2026-10-20): rejected at 60 min or longer if more than 5% above FTP; warning from 20 min up if more than 5% above a ceiling through FTP at 60 min and FTP/0.95 at 20 min. My tolerances and interpolation. Heart rate (P, 2026-10-20): rejected at 60 min or longer if the heart-rate-reserve intensity is above 1.05; warning from 20 min up. My tolerance and cut-offs.
- Rower checks (P found 30 min at 205 W accepted with a 200 W 2k): rejected if the session is longer than the 2k and averages more than the 2k watts; warning (not blocked) if more than 5% above the Paul's-law all-out power for that duration. With an entered threshold the 2k is taken as threshold split minus 15 s. The 5% tolerance and the ceiling are my choices.
- Heart rate: heart rate reserve against threshold HR (mine, placeholder; P agreed HR is the way for elliptical and Stairmaster).
- Counts towards CTL: 80% for every activity (P). Source for the bike: Copeland pp. 174 to 175, cycling +20 to 30% time for similar aerobic benefit. Raw TSS shown beside the counted figure.
- Cross-training share above 40% of weekly time is flagged (P: 60/40 running to cross-training, Copeland's anecdote). Weekly balance check only on the new page so far.
- Run Load Planner cross-training (P, 2026-10-21): second row of per-day inputs for raw cross-training TSS, one weight for CTL and ATL (default 80%, placeholder), cross-training column in the table when used, optional weekly run hours and cross-training hours driving the 40% flag. Forward mode only. The Cross-Training TSS page now hands over raw TSS with `xt=1` and its percentage, so the weight is applied once. The planner only takes TSS per day, so the flag needs hours typed separately. Not yet built: cross-training inputs in Copeland Base and the Hybrid Load Planner.
- Run Load Planner fatigue layer, 48 h rule only (P, 2026-10-21): optional (default off) select plus a tick box per day for a hard run. A hard run less than 48 h after the previous hard run gets extra = TSS × w × (0.28 + 0.5 × previous extra fraction), w = 1 − gap/48 h, gap = days × 24 h, cap +25%. Extra counts 1.0 toward ATL and 0.75 toward CTL (decided 2026-10-20). Flag wording agreed with P: "Hard session within 48 h of another hard session: about +15% fatigue." Constants are placeholders from the prototype. Not built: the 20 h double-day rule (needs time of day) and the prototype's intensity and duration terms; the hold-time cap fix (marathon-based limit for slow paces) goes in with those.
- Deadlift warm-up start (P, 2026-10-22): the first warm-up set for the deadlift is a 10-rep "Light pull" at an editable starting weight, default 50 kg, instead of the bar. Reason: bumper plates at P's gym are 5 to 25 kg, so a real start is 30 to 70 kg. Other barbell lifts still start with the bar.
- Pull-up and dip warm-up (P, 2026-10-22): first set 5 bodyweight reps (was 8); 50/70/85% steps are taken on total load (bodyweight + added), not on added weight, and steps at or below bodyweight are dropped. P found the old ladder too hard. Open: a light top set now gets only one bodyweight set before it; P may want more ramp.
- Cross-training in Copeland Base and the Hybrid Load Planner (P, 2026-10-22): Hybrid Load Planner has a cross-training TSS box per day and one weight (80% default, placeholder) counted equally toward CTL and ATL. Copeland Base has TSS per rest day plus the weight, used on 5 and 6 run days only, base weeks only; the ramp solver includes it so running time shrinks. Not built: hand-off from Cross-Training TSS to these two pages, and the fatigue layer in Hybrid Load Planner.
- Copeland Base cross-training days (P, 2026-10-22): P asked to cross-train on top of running 7 days. Replaced the rest-days-only rule with Mon to Sun tick boxes; ticks follow the rest days until the user ticks one. Cross-training on a run day adds to that day's CTL and ATL and shrinks the running time the ramp allows.
- Copeland Base cross-training minutes (P, 2026-10-22): P found Saturday stuck at 4 x 3 for four weeks with 50 TSS cross-training on Fridays (18:52 5k, CTL 41, 6 run days). Cause: cross-training TSS uses ramp room, so running time falls, and the 25% sub-threshold rule then binds. Fix: optional minutes per cross-training day that count as easy time in the 25% denominator. Blank keeps the old behaviour. Open: whether Copeland's 75/25 counts cross-training; a double (easy AM run) is already running time and needs no input.
- Pre's 200s label (P, 2026-10-22): the slow 200 is called "float", not "recovery", because recovery implies an easy pace. Pace unchanged (33 1/3% slower than the fast 200).

## Bike Session Generator (P, 2026-10-30)
- New page. P's brief: power-based (FTP in watts), sessions: sweet spot, threshold, VO2max, over-unders, endurance. P chose the session-generator form over a run-equivalent or weekly plan.
- Output: warm-up, main set with watts, recoveries, cool-down; total time, average power, TSS, counted towards CTL (80%, as Cross-Training TSS).
- Placeholders (mine, listed in the methodology): per-set power ranges, set sizes, recoveries, warm-up 10 min and cool-down 5 min. Zone bands are Coggan's as I recall them, not checked against the source.
- Not built: weekly plan, run-equivalent conversion, heart-rate version, hand-off to the Run Load Planner.

## Page names (P, 2026-10-28)
- Marathon Plans is now Marathon Plan Viewer; Marathon Plan Recommender is now Marathon Plan Finder. File names unchanged. Kept as two pages (P): Viewer = one plan in detail with its own settings; Finder = all 13 plans against CTL/ATL with the load chart and intensity mix. The Finder links the selected plan to the Viewer (#author.plan), the Viewer links to the Finder. Finder uses the Viewer's default plan settings.
