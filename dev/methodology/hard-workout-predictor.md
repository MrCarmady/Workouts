# Hard Workout Predictor: methodology

Predicts a race from a hard interval session. It is a prototype. The anchors are the author's, from experience, not from a published source.

| Item | Status |
|---|---|
| 400m, 60s rest: mile pace (8–10 reps) | Author's anchor |
| 600m, 75s rest: 2k pace | My midpoint between mile and 3k pace, to be confirmed |
| 800m, 90s rest: 3k pace | Author's anchor |
| 1000m, 60s rest: 5k pace | Author's anchor |
| 1200m, 90s rest: 5k pace | My placeholder |
| 1600m and 2000m, 2 min rest: 10k pace | My placeholder |
| 3000m, 3 min rest: 10k pace | Author's anchor (3×3000m is closer to 10k than HM pace) |
| 5000m, 3 min rest: marathon pace to 2% faster | Author's anchor |
| Typical rep counts: 400m 9 (author: 8–10), 600m 6, 800m 6, 1000m 6, 1200m 4, 1600m 4, 2000m 3, 3000m 3, 5000m 5 (3×5km is too little volume for a marathon prediction); interpolated for other rep lengths | 400m from the author; the rest are my placeholders |
| Volume slide: the race the reps equal is the anchor race distance × (reps / typical reps)^1.25 above the typical count and ^0.8 below it. Examples: 5×400m ≈ 1.0k pace, 18×400m ≈ 3.8k, 2×2000m ≈ 7.2k, 10×1.2km ≈ 15.7k, 3×5km ≈ 28k | Exponents are my choice, fitted to the author's examples (5×400m closer to 1000–1200m pace than 800m, 18×400m at 3–5k, 2×2000m at 6–8k, 10×1.2km at 15k to HM). Where two distances fit, the shorter, rounder one was preferred so the tool does not over-predict |
| Limits: total work up to 25km, and an equivalent race between 400m and the marathon | My placeholders; replace the per-rep-length rep ranges of the first version |
| Anchors apply at RPE 8–8.5 and standard rest | Author's assumption |
| Band of 1% in pace around each anchor (5000m: marathon pace to 2% faster) | My placeholder |
| Pace for other rep lengths: linear interpolation between anchors by rep distance | My choice |
| Race model: Riegel 1.06, adjustment below 5km, marathon offset at 70 miles a week | My estimates, not validated |

Not adjusted: rest, RPE, heat, surface, wind, hills. The tool warns when rest is more than 20% shorter or 25% longer than standard, when RPE is below 7 or above 9, and when the second half of the reps differs from the first by more than 2%.

Check against posted cases: 6×800 averaging 2:38.5 gives a 5k of 17:22 (range 17:12–17:32); the poster ran 17:07. One case, not a calibration.
