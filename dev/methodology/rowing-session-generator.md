# Rowing Session Generator: methodology

Erg sessions as splits and watts from a 2k time. Added 2026-11-02. Built to the author's brief (2k time input; steady state, threshold, race-pace intervals, 5k-pace intervals and pyramids; output as on the Bike Session Generator).

## What is standard and what is a choice

| Item | Status |
|---|---|
| Watts = 2.80 / (split in seconds per metre)^3 | Concept2's published pace-to-watts formula |
| Threshold split = 2k split + 15 s | Author's use of Paul's law (5 s per 500m per doubling of distance; 16k is 2k + 15), as in Cross-Training TSS; a rule of thumb, not checked against data |
| TSS = hours x (watts / threshold watts)^2 x 100, per block at the middle of its split range | Standard (Coggan) form, as in Cross-Training TSS, with watts as the intensity measure |
| Offsets from the 2k split: steady state +22 to +28 s; threshold +13 to +16 s (10 min reps), +14 to +17 (15 min), +15 to +18 (20 min); race pace -2 to 0 s (500 m), 0 to +2 (750 m), +2 to +4 (1000 m); 5k pace +6 to +7 (1500 m), +7 to +8 (2000 m), +7.5 to +8.5 (3000-2500-2000 m); pyramids +4 to +6 (500-1500 m), +1 to +3 (250-1000 m) | My choice, placeholders; not from a specific programme and not checked against a source |
| Set sizes: steady 40, 60, 90 min; threshold 4 x 10, 3 x 15, 2 x 20 min; race pace 8 x 500, 6 x 750, 4 x 1000 m; 5k pace 5 x 1500, 4 x 2000, 3000-2500-2000 m; two pyramids | My selection of common sets |
| Rests, as light rowing at 2k + 35 s: threshold a third of the rep (3, 5, 7 min); race pace 90 s, 2 min, 3 min; 5k pace 5 min; pyramids half of the preceding rep | My placeholders. The threshold ratio follows the over-unders on the Bike Session Generator; the author's view on rest for threshold is not yet known for the erg |
| Default warm-up 10 min at 2k + 25 to 35 s, cool-down 5 min at 2k + 30 to 40 s | My choice; both can be changed |
| Counted towards CTL: 80% of TSS | Placeholder for all non-running activities, as in Cross-Training TSS |

2k time must be 5:00 to 12:00. Distance for timed blocks is the time divided by the middle split; time for distance blocks is the distance times the middle split. Concept2 ergometer only. Not adjusted for drag factor, stroke rate or fatigue. The 2k time is saved in this browser only (key `rsg`).
