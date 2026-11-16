// Unit tests for shared/core.js. Run: node core.test.js
const fs = require("fs"), vm = require("vm"), path = require("path"), assert = require("assert");
const src = fs.readFileSync(path.join(__dirname, "..", "shared", "core.js"), "utf8");
const ctx = {}; vm.createContext(ctx);
vm.runInContext(src + "\nthis.api = { K, HM, MAR, MILE, adj, off, marathonFactor, marathonOff, parseTime, mmss, hmmss, vdot, setOff: function (v) { offM = v; } };", ctx);
const a = ctx.api; let n = 0;
function t(name, fn) { fn(); n++; }
const near = (x, y, e, m) => assert.ok(Math.abs(x - y) <= e, (m || "") + " got " + x + " expected " + y);

t("constants", () => { assert.strictEqual(a.K, 1.06); near(a.HM, 21.0975, 0); near(a.MAR, 42.195, 0); near(a.MILE, 1.609344, 0); });
t("parseTime: digits read from the right", () => {
  assert.strictEqual(a.parseTime("1854"), 18 * 60 + 54); assert.strictEqual(a.parseTime("18:54"), 1134);
  assert.strictEqual(a.parseTime("13200"), 1 * 3600 + 32 * 60 + 0); assert.strictEqual(a.parseTime("1:32:10"), 5530);
  assert.strictEqual(a.parseTime("90"), 5400);            // plain number = minutes
  assert.strictEqual(a.parseTime("10:44.80"), 644.8);
});
t("parseTime: rejects bad input", () => { ["", "abc", "1:2:3:4", "1875", "-5:00"].forEach(x => assert.strictEqual(a.parseTime(x), null, x)); });
t("parseTime: strict forms (2026-10-19)", () => {
  ["59:99", "1:75", "0:90", "12:60", "1:60:00", "1:00:75", "0x10", "1e2", "1e2:30", "Infinity", "+5:00", "5:+30", "18:.5", "18.5:30", "18:5", "18:054", "18 : 54", "18:54.", "1854.5", "9999999", "1_000", "٣", "NaN"].forEach(x => assert.strictEqual(a.parseTime(x), null, x));
  assert.strictEqual(a.parseTime(" 18:54 "), 1134); assert.strictEqual(a.parseTime("18:54.5"), 1134.5); assert.strictEqual(a.parseTime("1.5"), 90);
  assert.strictEqual(a.parseTime("0:59"), 59); assert.strictEqual(a.parseTime("120:00"), 7200); assert.strictEqual(a.parseTime("1:59:59"), 7199);
});
t("mmss and hmmss", () => {
  assert.strictEqual(a.mmss(65), "1:05"); assert.strictEqual(a.mmss(59.6), "1:00"); assert.strictEqual(a.mmss(1134), "18:54");
  assert.strictEqual(a.hmmss(5530), "1:32:10"); assert.strictEqual(a.hmmss(1134), "18:54"); assert.strictEqual(a.hmmss(3600), "1:00:00");
});
t("adj: short-race slowing is 6.5 ln(5/km) below 5km, zero above", () => {
  near(a.adj(5), 0, 0); near(a.adj(10), 0, 0); near(a.adj(3), 6.5 * Math.log(5 / 3), 1e-12); near(a.adj(1.5), 6.5 * Math.log(5 / 1.5), 1e-12);
});
t("marathonFactor: points, flat outside, linear between", () => {
  const mi = x => x * 1.609344;
  [[70, 2.10], [60, 2.13], [50, 2.17], [35, 2.25]].forEach(p => near(a.marathonFactor(mi(p[0])), p[1], 1e-9, "at " + p[0]));
  near(a.marathonFactor(mi(150)), 2.10, 1e-9); near(a.marathonFactor(mi(20)), 2.25, 1e-9);
  near(a.marathonFactor(mi(65)), 2.115, 1e-9); near(a.marathonFactor(mi(40)), 2.25 - 5 / 15 * 0.08, 1e-9);
});
t("marathonOff: the marathon is the factor times the half marathon, never below Riegel", () => {
  const p5 = 1125 / 5, H0 = p5 * Math.pow(a.HM / 5, a.K - 1) * a.HM;
  a.setOff(a.marathonOff(p5, 50 * 1.609344));
  const pm = p5 * Math.pow(a.MAR / 5, a.K - 1) + a.off(a.MAR);
  near(pm * a.MAR / H0, 2.17, 1e-9);
  a.setOff(a.marathonOff(p5, 130 * 1.609344));
  near((p5 * Math.pow(a.MAR / 5, a.K - 1) + a.off(a.MAR)) * a.MAR / H0, 2.10, 1e-9);
});
t("marathonOff: null assumes 70 miles, never negative, falls with more mileage", () => {
  const p5 = 226.8;   // 18:54 5k
  near(a.marathonOff(p5, null), a.marathonOff(p5, 70 * 1.609344), 1e-12);
  assert.ok(a.marathonOff(p5, 130) >= 0);
  assert.ok(a.marathonOff(p5, 40 * 1.609344) > a.marathonOff(p5, 80 * 1.609344));
});
t("off: zero up to the half marathon, offM at the marathon, flat beyond", () => {
  a.setOff(6); near(a.off(10), 0, 0); near(a.off(a.HM), 0, 1e-12); near(a.off(a.MAR), 6, 1e-12); near(a.off(50), 6, 1e-12);
  near(a.off((a.HM + a.MAR) / 2), 3, 1e-12);
});
t("vdot: regression pins (Daniels-Gilbert formula as coded)", () => {
  near(a.vdot(18 + 54 / 60, 5000), 53.2, 0.05);     // 18:54 5k, pinned to the current output
  assert.ok(a.vdot(17, 5000) > a.vdot(18, 5000) && a.vdot(18, 5000) > a.vdot(19, 5000));
});
console.log(n + " core tests passed");
