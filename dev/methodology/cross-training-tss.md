# Cross-Training TSS: methodology

Training stress for non-running sessions, with the share that counts towards CTL. Added 2026-10-19.

## What is standard and what is a choice

| Item | Status |
|---|---|
| TSS = hours x IF^2 x 100 | Standard (Coggan), as used for running on the other pages |
| Bike IF = average power / FTP | Standard |
| Concept2 watts = 2.80 / (seconds per metre)^3 | Concept2's published pace-to-watts formula |
| Rower threshold = 2k split + 15 s per 500m | Author's use of Paul's law (see below); a rule of thumb, not checked against data |
| Heart-rate intensity from heart rate reserve | My formula, a placeholder, not validated |
| Treadmill walking via the ACSM walking equation | Published equation; the TSS step is derived here |
| 80% counts towards CTL, for every activity | Copeland's rough guide for the bike; a placeholder for the others |
| Over 40% of weekly time as cross-training is flagged | Copeland's rough guide (one friend's experience); the check uses plain hours |
| IF above 1.5 is rejected | My sanity limit |

## Bike

```
IF = average power / FTP
TSS = hours * IF^2 * 100
```

Gym bike power displays can be inaccurate. TSS is relative to your own FTP on the same bike, so use one bike consistently. Average power underestimates the stress of very uneven sessions (normalised power would be higher).

## Rower

```
watts = 2.80 / (split / 500)^3          split in seconds per 500m
threshold split = 2k time / 4 + 15 s    (or enter threshold watts)
IF = session watts / threshold watts
```

Paul's law (author's description, a rowing rule of thumb): for every doubling of distance, add 5 seconds to the 500m split. From a 2k that gives 4k + 5, 8k + 10, 16k + 15. A 16k at 2k + 15 takes about an hour for typical 2k splits (checked: 2k split 1:45 gives about 60 min; 2:00 gives about 61 min), so 2k + 15 is used as the one-hour, FTP-like power. For a 1:45 2k split that is 202 W against 302 W for the 2k, about 67%.

Power is used, not speed, because boat speed rises with the cube root of power. 50% of 2k power is a realistic easy split (the 2k split x 1.26); 50% of 2k speed is not.

## Heart rate (elliptical, Stairmaster and others)

```
intensity = (average HR - resting HR) / (threshold HR - resting HR)
TSS = hours * intensity^2 * 100
```

Dividing by threshold HR alone would score easy sessions too high. Placeholder. Heart rate lags effort and drifts with heat and fatigue, so steady sessions suit it best.

## Treadmill walking

ACSM walking equation, VO2 = 0.1 S + 1.8 S G + 3.5. The flat-run speed with the same oxygen cost is S x (0.5 + 9 G). IF = threshold pace / flat-equivalent pace. Limits 2 to 8 km/h, 0 to 20%; the page warns above 6.4 km/h. Blank threshold uses the race result saved by the other pages (race(16)).

## Counts towards CTL

Counted TSS = raw TSS x percentage (default 80). Source: Copeland, Norwegian Singles Method, pp. 174 to 175: cycling should be extended by 20 to 30% compared with running time for similar aerobic benefit, which is 1 / 1.2 to 1 / 1.3 = 77 to 83%. He gives no figure for other activities; 80% is used for all as the author's choice. The raw TSS is shown beside the counted figure.

## Weekly balance

Copeland's anecdote: a friend who moved to about 60% running and 40% cycling held running performance, and it fell once cycling dominated. Treated as a rough flag, not a limit. The page flags cross-training above 40% of weekly hours. It is not yet part of the load planners.

## Hand-off

The counted TSS can be sent to the Run Load Planner through the same link format as the session generators (tss and name in the address).
