# Bike Session Generator: methodology

Bike sessions in watts from a bike FTP. Added 2026-10-30. Built to the author's brief (power-based, FTP input; sweet spot, threshold, VO2max, over-unders and endurance).

## What is standard and what is a choice

| Item | Status |
|---|---|
| TSS = hours x (power / FTP)^2 x 100, per block at the middle of its power range | Standard (Coggan) formula, applied to block averages, so variable blocks come out a little below a normalised-power figure |
| Endurance 56 to 75%, threshold 91 to 105%, VO2max 106 to 120% of FTP | Coggan's power levels as I recall them; not checked against the source in this session |
| Sweet spot 88 to 94% | Common coaching convention, not a Coggan level |
| Ranges used per set (threshold 98 to 105% for 10-minute reps, 95 to 102% for 15, 95 to 100% for 20; VO2max 112 to 120% for 3-minute, 108 to 115% for 4, 106 to 112% for 5) | My choice, placeholders |
| Set sizes (3 x 10, 3 x 15, 2 x 20, 3 x 20 min sweet spot, and so on) | My selection of common sets; not from a specific book or plan |
| Recoveries at 55% FTP: about a third of the rep or block length, rounded to a whole minute, for sweet spot, threshold and over-unders (10 min reps 3 min, 15 min 5, 20 min 7); equal to the work at 50% FTP for VO2max. Changed 2026-10-30 from a flat 5 minutes, at the author's request: 5 minutes after 10-minute reps felt too generous against running, where 10-minute reps get 90 to 120 s | My placeholder ratio; the author's running comparison would suggest a shorter rest for the 10-minute reps |
| Over-unders: 3 x 12 min blocks of (3 min at 95% + 1 min at 105%), or 2 x 20 min of (4 min at 95% + 1 min at 105%) | My choice |
| Default warm-up 10 min at 55 to 65% and cool-down 5 min at 45 to 55% | My choice; both can be changed |
| Counted towards CTL: 80% of TSS | Author's rule, as in Cross-Training TSS (Copeland: cycling needs 20 to 30% more time than running for similar aerobic benefit) |

FTP must be 50 to 600 W. Not adjusted for heat, hills, fatigue, cadence or indoor versus outdoor. FTP is saved in this browser only (key `bsg`).
