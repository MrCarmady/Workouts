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
| 2000m, 2 min rest: 8k pace | Confirmed by the author: 3 × 2000m at RPE 8 is a light 10k session, so 8k is reasonable (6k would be extra cautious). Same volume as 4×1600m |
| 3000m, 3 min rest: 10k pace | Author's anchor (3×3000m is closer to 10k than HM pace) |
| 5000m, 3 min rest: marathon pace to 2% faster | Author's anchor |
| Aussie quarters (400m hard, 200m float, continuous): always 8 reps. The whole session time, floats included, for 8 reps (4800m) is read as the 5k time; the real race is quicker, by up to 15 s. Range: that total to 15 s off it | Author's rule of thumb (Pavel, 2026-10-15): 4800m in about the time of the 5k, and most people can go a bit quicker in the race. The 15 s is the author's. The rep count is fixed at 8 because it is a classic session (author's decision). The RPE adjustment (applied to the total) is mine. Not validated against real sessions |
| Aussie float handling: floats count towards the total, so float times are required | Author's decision. The tool warns if the floats were as fast as the hard 400s (inputs swapped) or more than 10% slower than marathon pace (a jog); the 10% is my placeholder. M pace is from the race model at 70 miles a week |
| Typical rep counts: 400m 9 (author: 8–10), 600m 6, 800m 6, 1000m 5 (author, 2026-10-29: 5×1k is the classic 5k predictor; was 6), 1200m 4, 1600m 4, 2000m 3, 3000m 3, 5000m 5 (3×5km is too little volume for a marathon prediction); interpolated for other rep lengths | 400m and 1000m from the author; the rest are my placeholders |
| Volume slide (changed 2026-10-29): the race the reps equal is the anchor race distance × g(r), where r is reps ÷ typical reps. Below the typical count g = r^0.8. From 1 to 1.6 times it, g = r (8×1k is about 8k). Beyond 1.6 times, g = r × (r ÷ 1.6)^0.93, so pace holds up less well with volume. Examples at standard rest: 5×400m ≈ 1.0k pace, 18×400m ≈ 4.0k, 2×2000m ≈ 5.8k, 10×1.2km ≈ 18.9k, 3×5km ≈ 28k, 12×1k ≈ 17.5k | The 1.6 knee and the 0.93 are fitted to the author's 1k examples (5×1k = 5k, 8×1k about 8k, 12×1k at 60s = 17.5k). Earlier version: ^1.25 above the typical count, which read 12×1k as 12k |
| Rest (added 2026-10-29): the anchors assume the standard rest. The equivalent race is multiplied by (standard rest ÷ rest)^0.38, with the ratio limited to between 0.4 and 2.5 and rest under 15s treated as 15s. Longer rest means an easier session, so the same pace reads as a shorter race. 12×1k at 90s = 15k against 17.5k at 60s; 6×1k at 90s ≈ 5.1k, about the same as 5×1k at 60s | The author's judgement: extra rest roughly offsets an extra rep (6×1k at 90s ≈ 5×1k at 60s), and 12×1k is 17.5k at 60s and 15k at 90s. The 0.38 is fitted to the second pair and checks against the first. The standard rest is the anchor rest, interpolated by rep length; it does not itself grow with volume, since the volume slide carries that. Not validated against real sessions |
| The equivalent race is shown as the largest common distance at or below the computed one, or the next one up if the computed one is within 5% of it: 400m, 600m, 800m, 1000m, 1200m, 1500m, mile, 2k, 3k, 4k, 5k, 8k, 10k, 12k, 15k, 10 mile, half marathon, 30k, 20 mile, marathon. The prediction itself uses the unrounded distance | Author's preference for round, common distances, rounding down when in doubt; the list (real race distances; 8k kept because it is the 1600m anchor) and the 5% are mine |
| Limits: total work up to 25km (refused above), an equivalent race under 400m (refused), and an equivalent race beyond the marathon (capped at marathon pace, with a note) | My placeholders |
| Anchors apply at RPE 8 and standard rest | Author's assumption |
| Pace used = pace × (1 + 0.01 × (RPE − 8)) | My placeholder |
| RPE accepted: 6 to 10 only (changed 2026-10-29); below 6 shows an error. Below 7 warns that the session is too easy for a meaningful prediction; above 9 warns not to leave the race in training (recovery may be excessive). Reps below 0.6 or above 2 times the typical count for the rep length give the same two warnings (all four limits are placeholders, 2026-10-29). The Session equals box (what the reps and rest equal) does not depend on RPE; the first tile shows the RPE-adjusted pace | The author's call: at low RPE the pace says almost nothing about race fitness (easy running is about 65% of 5k speed, so a 5% adjustment would be far too small), and the 1% per point was never fitted away from RPE 8. A proper RPE-to-race-pace model is open (the Sub-Threshold Trend Tracker uses RPE 7 or lower only as a gate, not as a conversion) |
| Continuous mode: pace × (1 + 0.01 × (RPE − 10)) × (1 − 0.025), then the race model | My placeholders. No source for the 2.5% race-day effect |
| Band of 1% in pace around each anchor (5000m: marathon pace to 2% faster) | My placeholder |
| Pace for other rep lengths: linear interpolation between anchors by rep distance | My choice |
| Race model: Riegel 1.06, adjustment below 5km, marathon offset at 70 miles a week | My estimates, not validated |

Continuous mode accepts 1.5 to 30km (a solo effort longer than that is not supported).

The 2.5% race-day effect is a placeholder. It is the author's conservative pick from a recalled 2.3 to 4% range. Published evidence is mixed: one running study found about 4% over 3km, and some cycling studies found little or no effect. Cross-checks against the 3.25 to 3.75km solo pace and 4800m solo time rules of thumb imply roughly 2.7 to 4.4%.

Not adjusted: heat, surface, wind, hills. The tool notes how much the equivalent race changed when rest differs from standard by more than 10%, warns when rest is under 20s or more than 2.5 times standard, when RPE is below 6 or above 9.5, and when the second half of the reps differs from the first by more than 2%.

Check against posted cases: 6×800 averaging 2:38.5 gives a 5k of 17:22 (range 17:12–17:32); the poster ran 17:07. One case, not a calibration.

Display (2026-10-30): the Session equals box shows the actual race distance (for example 6.9k) unless it is within 5% of a standard distance, when it shows that name. It used to round down to the next standard distance, so 6.9k read as 5k. The box includes the rest adjustment; RPE is not applied to it. The rest note compares the session with the same session at standard rest.
