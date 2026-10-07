# Sub-Threshold Trend Tracker: methodology

Logs classic sub-threshold sessions and turns each into an implied threshold pace. It is a prototype. Every numeric choice below is marked.

| Item | Status |
|---|---|
| Rep length to race-pace table (3 min race(14–16) … 20 min race(40–42.195)) | Same as the Sub-Threshold Session Generator, run backwards |
| Race model (Riegel 1.06). Weekly distance is not an input; the marathon offset assumes 70 miles a week, which does not affect threshold | Same as the other tools; my estimates |
| Threshold = race(16) | Author's definition |
| The user logs only sessions ending at RPE 7 or lower (RPE is logged in the table for reference but does not change the result) | Author's guardrail |
| Excluded if peak HR (last minute or two of the last rep) is above 90% of max | Author's guardrail |
| Excluded if whole-session average HR (warm-up and cool-down included) is above 82% of max | Author said about 81–82%; 82 is my placeholder |
| Implied threshold range: fast to slow end of the table for that rep length | Follows from the table |
| Estimate = median of the last 6 counted sessions | My choice |
| Confidence: <3 indicative, 3–5 low, 6–9 moderate, 10+ good | My placeholders, not validated. Author to set n |
| Trend: straight-line fit, shown from 4 sessions spanning 14 days, in s/km per 4 weeks | My choice |

Not corrected for: heat, hills, wind, fatigue, pacing errors. Data is stored in the browser only (key `stt`).
