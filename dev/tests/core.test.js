// Unit tests for shared/core.js. Run: node core.test.js
const fs = require("fs"), vm = require("vm"), path = require("path"), assert = require("assert");
const src = fs.readFileSync(path.join(__dirname, "..", "shared", "core.js"), "utf8");
const ctx = {}; vm.createContext(ctx);
vm.runInContext(src + "\nthis.api = { K, HM, MAR, MILE, adj, off, marathonExtraMin, marathonOff, parseTime, mmss, hmmss, vdot, setOff: function (v) { offM = v; } };", ctx);
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
t("mmss and hmmss", () => {
  assert.strictEqual(a.mmss(65), "1:05"); assert.strictEqual(a.mmss(59.6), "1:00"); assert.strictEqual(a.mmss(1134), "18:54");
  assert.strictEqual(a.hmmss(5530), "1:32:10"); assert.strictEqual(a.hmmss(1134), "18:54"); assert.strictEqual(a.hmmss(3600), "1:00:00");
});
t("adj: short-race slowing is 8 ln(5/km) below 5km, zero above", () => {
  near(a.adj(5), 0, 0); near(a.adj(10), 0, 0); near(a.adj(3), 8 * Math.log(5 / 3), 1e-12); near(a.adj(1.5), 8 * Math.log(5 / 1.5), 1e-12);
});
t("marathonExtraMin: author's points, flat outside, linear between", () => {
  const mi = x => x * 1.609344;
  [[80, 7], [70, 10], [60, 13], [50, 17], [35, 25]].forEach(p => near(a.marathonExtraMin(mi(p[0])), p[1], 1e-9, "at " + p[0]));
  near(a.marathonExtraMin(mi(120)), 7, 1e-9); near(a.marathonExtraMin(mi(20)), 25, 1e-9);
  near(a.marathonExtraMin(mi(65)), 11.5, 1e-9); near(a.marathonExtraMin(mi(42.5)), 21, 1e-9);
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
