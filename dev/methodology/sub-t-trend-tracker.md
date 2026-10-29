# Sub-Threshold Trend Tracker: methodology

Logs classic sub-threshold sessions and turns each into an implied threshold pace. It is a prototype. Every numeric choice below is marked.

| Item | Status |
|---|---|
| Rep length to race-pace table (3 min race(14–16) … 20 min race(40–42.195)) | Same as the Sub-Threshold Session Generator, run backwards |
| Race model (Riegel 1.06) with the short-race adjustment and the marathon slow-down at the 70-mile value (2.10 times the half marathon). Same as the Sub-Threshold Session Generator with its weekly distance left blank, so the table runs backwards consistently. Weekly distance is not an input | Author's judgement |
| Threshold = race(16) | Author's definition |
| The user logs only sessions ending at RPE 7 or lower (RPE is logged in the table for reference but does not change the result) | Author's guardrail |
| Excluded if peak HR (last minute or two of the last rep) is above 90% of max | Author's guardrail |
| Excluded if whole-session average HR (warm-up and cool-down included) is above 82% of max | Author said about 81–82%; 82 is my placeholder |
| Implied threshold range: fast to slow end of the table for that rep length | Follows from the table |
| Estimate = median of the last 6 counted sessions within the past 6 weeks (42 days). With fewer than 3 in that window it uses the last 6 counted sessions regardless of age and is marked stale | Window and minimum of 3 are my placeholders; 6 weeks is the author's (2–3 sessions a week expected) |
| Confidence from counted sessions in the last 6 weeks: <3 stale, 3–5 low, 6–9 moderate, 10+ good | My placeholders, not validated. Author to set n |
| Trend: straight-line fit to counted sessions within the past 12 weeks (84 days), shown from 4 sessions spanning 14 days, in s/km per 4 weeks. Older sessions stay in the table and chart, faded | 12 weeks is the author's; the rest is my choice |

Not corrected for: heat, hills, wind, fatigue, pacing errors. Data is stored in the browser only (key `stt`). "Clear all sessions" deletes every logged session after a second confirmation click; the backup text box can be copied first.

## Race results (added 2026-10-29)

| Item | Status |
|---|---|
| A race time (1500 m, mile, 3 km, 5 km, 10 km, half, marathon) is converted to a 5km pace by solving the same race model; races under 5km get the same short-race slowing. Threshold = race(16) at that 5km pace | Author's model, applied to a real result |
| Comparison: the median of up to the last 6 counted sessions in the 6 weeks up to the race date gives the sub-T threshold and a predicted race time. Gap = race minus predicted (positive = slower than predicted) | My construction; same window as the estimate |
| Races are shown as diamonds on the trend chart and do not change the estimate, the trend or the confidence | Author's decision: tighten the model against reality first |
| Races are stored with the sessions (key `stt`, field `races`) and included in the backup text. "Clear all sessions" does not delete races | My choice |

The race is assumed to be an all-out effort in normal conditions. Heat, hills, wind and tactics are not corrected for.
