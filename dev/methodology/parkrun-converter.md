# Parkrun Converter: methodology

Converts a parkrun time from one course to another.

| Item | Status |
|---|---|
| Course scores (SSS, 0 to 12, 835 UK parkruns) | The Running Channel, list dated 29 April 2026, from Tim Grose and Power of 10 data |
| 30 seconds per point | The Running Channel: median finish times in average conditions |
| The same 30 seconds for every runner | Simplification. The real effect varies with ability, weather and surface |

Predicted time = your time + 30s × (SSS of the new course − SSS of the old one).

Not adjusted: weather and ground on the day, crowding, and your own strengths on hills, turns or surfaces. The tool warns when the courses are 2 or more points apart.

Names are as listed on the source page. Seasonal courses appear as separate entries, for example Bromley (Winter) and Bromley (Summer).
