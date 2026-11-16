# Bike Session Generator: methodology

Bike sessions in watts from a bike FTP. Added 2026-10-30. Built to the author's brief (power-based, FTP input; sweet spot, threshold, VO2max, over-unders and endurance).

## What is standard and what is a choice

| Item | Status |
|---|---|
| TSS = hours x (power / FTP)^2 x 100, per block at the middle of its power range | Standard (Coggan) formula, applied to block averages, so variable blocks come out a little below a normalised-power figure |
| Endurance 56 to 75%, threshold 91 to 105%, VO2max 106 to 120% of FTP | Coggan's power levels as I recall them; not checked against the source in this session |
| Sweet spot 88 to 94% | Common coaching convention, not a Coggan level |
| Ranges used per set (threshold 98 to 105% for 8 and 10-minute reps, 97 to 103% for 12, 95 to 102% for 15, 95 to 100% for 20; VO2max 112 to 120% for 3-minute, 108 to 115% for 4, 106 to 112% for 5) | My choice, placeholders |
| Set sizes: sweet spot 3 x 10, 3 x 15, 2 x 20, 3 x 20, 2 x 30 min; threshold 4 x 8, 3 x 10, 3 x 12, 2 x 15, 2 x 20 min; VO2max and over-unders as before. Sweet spot carries 20 to 60 min of work, threshold 30 to 40 | My selection of common sets; not from a specific book or plan |
| Recoveries at 55% FTP (50% for VO2max): sweet spot about a quarter of the rep, rounded to whole minutes (10 min reps 3 min, 15 min 4, 20 min 5, 30 min 8); threshold about half (8 min reps 4, 10 min 5, 12 min 6, 15 min 8, 20 min 10); over-unders about a third of the block (12 min 4, 20 min 7); VO2max equals the work. Author's reasoning, 2026-10-30: sweet spot is the volume session, threshold is harder and needs more rest, and 5 minutes after 10-minute reps felt too generous against running (10-minute run reps get 90 to 120 s) | My placeholder ratios, not from a source |
| Over-unders: 3 x 12 min blocks of (3 min at 95% + 1 min at 105%), or 2 x 20 min of (4 min at 95% + 1 min at 105%) | My choice |
| Default warm-up 10 min at 55 to 65% and cool-down 5 min at 45 to 55% | My choice; both can be changed |
| Counted towards CTL: 80% of TSS | Author's rule, as in Cross-Training TSS (Copeland: cycling needs 20 to 30% more time than running for similar aerobic benefit) |

FTP must be 50 to 600 W. Not adjusted for heat, hills, fatigue, cadence or indoor versus outdoor. FTP is saved in this browser only (key `bsg`).
