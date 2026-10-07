  /*@@CORE-BEGIN@@ Shared code. Edit shared/core.js and run sync_core.py; do not edit between these markers. */
  var K = 1.06, HM = 21.0975, MAR = 42.195, MILE = 1.609344;
  // Slowing applied to the 5km equivalent when the input race is shorter than 5km, in s/km (my estimate).
  function adj(km) { return km < 5 ? 8 * Math.log(5 / km) : 0; }
  var offM = 5;   // marathon slow-down in s/km, set per page from the weekly distance
  function off(km) { return km <= HM ? 0 : offM * (Math.min(km, MAR) - HM) / (MAR - HM); }
  function marathonExtraMin(weekKm) {
    var mi = weekKm / 1.609344;
    var P = [[80, 7], [70, 10], [60, 13], [50, 17], [35, 25]];   // [miles per week, minutes added to 2 x half marathon]
    if (mi >= P[0][0]) return P[0][1];
    for (var i = 1; i < P.length; i++) {
      if (mi >= P[i][0]) { var f = (P[i - 1][0] - mi) / (P[i - 1][0] - P[i][0]); return P[i - 1][1] + f * (P[i][1] - P[i - 1][1]); }
    }
    return P[P.length - 1][1];
  }
  // p5r = 5km-equivalent pace from Riegel (s/km). Returns the marathon slow-down in s/km.
  function marathonOff(p5r, weekKm) {
    if (weekKm === null) weekKm = 70 * 1.609344;
    var H0 = p5r * Math.pow(HM / 5, K - 1) * HM, M0 = p5r * Math.pow(MAR / 5, K - 1) * MAR;
    return Math.max(0, (marathonExtraMin(weekKm) * 60 - (M0 - 2 * H0)) / MAR);
  }
  function parseTime(str) {
    str = (str || "").trim();
    if (!str) return null;
    if (/^\d{3,6}$/.test(str)) {                                       // digits only: read from the right
      var sec = str.slice(-2), rest = str.slice(0, -2);
      if (Number(sec) >= 60) return null;
      if (rest.length > 2) { if (Number(rest.slice(-2)) >= 60) return null; str = rest.slice(0, -2) + ":" + rest.slice(-2) + ":" + sec; }
      else str = rest + ":" + sec;
    }
    var parts = str.split(":");
    if (parts.length > 3) return null;
    var nums = parts.map(function (p) { return p === "" ? NaN : Number(p); });
    if (nums.some(function (x) { return isNaN(x) || x < 0; })) return null;
    if (parts.length === 1) return nums[0] * 60;                       // plain number = minutes
    if (parts.length === 2) return nums[0] * 60 + nums[1];
    return nums[0] * 3600 + nums[1] * 60 + nums[2];
  }
  function mmss(sec) {
    sec = Math.round(sec);
    var m = Math.floor(sec / 60), s = sec % 60;
    return m + ":" + (s < 10 ? "0" : "") + s;
  }
  function hmmss(sec) {
    sec = Math.round(sec);
    var h = Math.floor(sec / 3600), r = sec - h * 3600;
    return h > 0 ? h + ":" + (Math.floor(r / 60) < 10 ? "0" : "") + mmss(r) : mmss(r);
  }
  // Daniels-Gilbert VDOT for a race of `min` minutes over `m` metres.
  function vdot(min, m) {
    var v = m / min;
    var vo2 = -4.60 + 0.182258 * v + 0.000104 * v * v;
    var pct = 0.8 + 0.1894393 * Math.exp(-0.012778 * min) + 0.2989558 * Math.exp(-0.1932605 * min);
    return vo2 / pct;
  }
  /*@@CORE-END@@*/
