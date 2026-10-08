# Hard Workout Predictor: methodology

Predicts a race from a hard interval session. It is a prototype. The anchors are the author's, from experience, not from a published source.

| Item | Status |
|---|---|
| 400m, 60s rest: mile pace (8–10 reps) | Author's anchor |
| 600m, 75s rest: 2k pace | My midpoint between mile and 3k pace, to be confirmed |
| 800m, 90s rest: 3k pace | Author's anchor |
| 1000m, 60s rest: 5k pace | Author's anchor |
| 1200m, 90s rest: 5k pace | My placeholder |
| 1600m, 2 min rest: 8k pace (4×1600m is a solid 8k predictor) | Author's anchor |
| 2000m, 2 min rest: 8k pace | My placeholder: about the same volume as 4×1600m |
| 3000m, 3 min rest: 10k pace | Author's anchor (3×3000m is closer to 10k than HM pace) |
| 5000m, 3 min rest: marathon pace to 2% faster | Author's anchor |
| Typical rep counts: 400m 9 (author: 8–10), 600m 6, 800m 6, 1000m 6, 1200m 4, 1600m 4, 2000m 3, 3000m 3, 5000m 5 (3×5km is too little volume for a marathon prediction); interpolated for other rep lengths | 400m from the author; the rest are my placeholders |
| Volume slide: the race the reps equal is the anchor race distance × (reps / typical reps)^1.25 above the typical count and ^0.8 below it. Examples: 5×400m ≈ 1.0k pace, 18×400m ≈ 3.8k, 2×2000m ≈ 5.8k, 10×1.2km ≈ 15.7k, 3×5km ≈ 28k | Exponents are my choice, fitted to the author's examples (5×400m closer to 1000–1200m pace than 800m, 18×400m at 3–5k, 2×2000m at 6–8k, 10×1.2km at 15k to HM). Where two distances fit, the shorter, rounder one was preferred so the tool does not over-predict |
| The equivalent race is shown as the largest common distance at or below the computed one, or the next one up if the computed one is within 5% of it: 400m, 600m, 800m, 1000m, 1200m, 1500m, mile, 2k, 3k, 5k, 8k, 10k, 12k, 15k, 10 mile, half marathon, 30k, 20 mile, marathon. The prediction itself uses the unrounded distance | Author's preference for round, common distances, rounding down when in doubt; the list (real race distances; 8k kept because it is the 1600m anchor) and the 5% are mine |
| Limits: total work up to 25km (refused above), an equivalent race under 400m (refused), and an equivalent race beyond the marathon (capped at marathon pace, with a note) | My placeholders |
| Anchors apply at RPE 8 and standard rest | Author's assumption |
| Pace used = pace × (1 + 0.01 × (RPE − 8)) | My placeholder |
| Continuous mode: pace × (1 + 0.01 × (RPE − 10)) × (1 − 0.025), then the race model | My placeholders. No source for the 2.5% race-day effect |
| Band of 1% in pace around each anchor (5000m: marathon pace to 2% faster) | My placeholder |
| Pace for other rep lengths: linear interpolation between anchors by rep distance | My choice |
| Race model: Riegel 1.06, adjustment below 5km, marathon offset at 70 miles a week | My estimates, not validated |

Continuous mode accepts 1.5 to 30km (a solo effort longer than that is not supported).

The 2.5% race-day effect is a placeholder. It is the author's conservative pick from a recalled 2.3 to 4% range. Published evidence is mixed: one running study found about 4% over 3km, and some cycling studies found little or no effect. Cross-checks against the 3.25 to 3.75km solo pace and 4800m solo time rules of thumb imply roughly 2.7 to 4.4%.

Not adjusted: rest, heat, surface, wind, hills. The tool warns when rest is more than 20% shorter or 25% longer than standard, when RPE is below 6 or above 9.5, and when the second half of the reps differs from the first by more than 2%.

Check against posted cases: 6×800 averaging 2:38.5 gives a 5k of 17:22 (range 17:12–17:32); the poster ran 17:07. One case, not a calibration.
