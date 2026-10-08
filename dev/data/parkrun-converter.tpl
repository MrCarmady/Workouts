<title>Parkrun Converter</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo:wght@400;500;600;700&family=Archivo+Narrow:wght@500;600;700&display=swap">
<style>
:root {
  --bg: #f2f2f1; --surface: #ffffff; --surface-2: #f0f0ee; --fg: #17181a; --muted: #6a6d72; --line: #deded9;
  --accent: #c8372d; --accent-fg: #ffffff; --warn: #a35a00;
  --font-display: "Archivo Narrow", "Arial Narrow", system-ui, sans-serif;
  --font-body: "Archivo", system-ui, -apple-system, "Segoe UI", sans-serif;
}
@media (prefers-color-scheme: dark) {
  :root:not([data-theme="light"]) { --bg: #141416; --surface: #1c1c1f; --surface-2: #25252a; --fg: #ececea; --muted: #9a9ca2; --line: #34343a; --accent: #ef6a5e; --accent-fg: #1a0b09; --warn: #f0a35a; color-scheme: dark; }
}
:root[data-theme="dark"] { --bg: #141416; --surface: #1c1c1f; --surface-2: #25252a; --fg: #ececea; --muted: #9a9ca2; --line: #34343a; --accent: #ef6a5e; --accent-fg: #1a0b09; --warn: #f0a35a; color-scheme: dark; }
body { background: var(--bg); color: var(--fg); font-family: var(--font-body); font-size: 15px; line-height: 1.45; }
.wrap { max-width: 760px; margin: 0 auto; padding-inline: 16px; padding-block: 24px 40px; display: grid; gap: 20px; }
.wrap > * { min-width: 0; }
h1 { font-family: var(--font-display); font-weight: 700; font-size: 2rem; letter-spacing: .02em; text-transform: uppercase; margin: 0; text-wrap: balance; }
h2 { font-family: var(--font-display); font-weight: 600; font-size: 1.15rem; letter-spacing: .06em; text-transform: uppercase; margin: 0; color: var(--muted); }
.head { display: flex; flex-wrap: wrap; align-items: flex-start; justify-content: space-between; gap: 12px; }
.themes { display: inline-flex; border: 1px solid var(--line); border-radius: 2px; overflow: hidden; background: var(--surface); }
.themes button { font: inherit; font-size: .8rem; font-weight: 600; letter-spacing: .05em; text-transform: uppercase; color: var(--muted); background: transparent; border: 0; padding: 7px 12px; cursor: pointer; }
.themes button + button { border-left: 1px solid var(--line); }
.themes button[aria-pressed="true"] { background: var(--accent); color: #fff; }
.themes button:focus-visible { outline: 2px solid var(--accent); outline-offset: -2px; }
.sub { color: var(--muted); margin: 4px 0 0; max-width: 62ch; }
.panel { background: var(--surface); border: 1px solid var(--line); border-radius: 2px; padding: 18px; min-width: 0; display: grid; gap: 14px; align-content: start; }
.fields { display: grid; grid-template-columns: minmax(0, 1fr) minmax(0, 1fr); gap: 14px; align-items: start; }
.fields .full { grid-column: 1 / -1; }
@media (max-width: 600px) { .fields { grid-template-columns: minmax(0, 1fr); } }
label { display: grid; gap: 4px; align-content: start; font-size: .8rem; font-weight: 600; letter-spacing: .05em; text-transform: uppercase; color: var(--muted); }
input { box-sizing: border-box; width: 100%; height: 2.75rem; font: inherit; font-size: 1.05rem; font-weight: 500; letter-spacing: 0; text-transform: none; color: var(--fg); background: var(--bg); border: 1px solid var(--line); border-radius: 2px; padding: 0 10px; }
input:focus-visible { outline: 2px solid var(--accent); outline-offset: 1px; }
small.info { font-size: .8rem; font-weight: 400; letter-spacing: 0; text-transform: none; color: var(--muted); min-height: 1.1em; }
.btn { font: inherit; font-size: .85rem; font-weight: 600; letter-spacing: .05em; text-transform: uppercase; color: var(--muted); background: transparent; border: 1px solid var(--line); border-radius: 2px; height: 2.75rem; padding: 0 18px; cursor: pointer; justify-self: start; }
.btn:focus-visible { outline: 2px solid var(--accent); outline-offset: 2px; }
.note { font-size: .85rem; color: var(--muted); margin: 0; }
.warn { color: var(--warn); font-size: .88rem; margin: 0; }
.res { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 12px; }
@media (max-width: 600px) { .res { grid-template-columns: repeat(2, minmax(0, 1fr)); } .res div:first-child { grid-column: 1 / -1; } }
.res div { background: var(--surface-2); border-radius: 2px; padding: 10px 12px; min-width: 0; }
.res b { display: block; font-family: var(--font-display); font-size: 1.6rem; font-weight: 600; font-variant-numeric: tabular-nums; line-height: 1.2; }
.res b.pace { color: var(--accent); }
.res span { font-size: .75rem; letter-spacing: .05em; text-transform: uppercase; color: var(--muted); }
.res small { display: block; font-size: .78rem; color: var(--muted); margin-top: 2px; }
.method { font-size: .88rem; color: var(--muted); display: grid; gap: 6px; }
.method ul { margin: 0; padding-left: 1.2em; display: grid; gap: 6px; }
.method b { color: var(--fg); font-weight: 600; }
[hidden] { display: none !important; }
</style>

<main class="wrap">
  <header class="head">
    <div>
      <h1>Parkrun Converter</h1>
      <p class="sub">Convert a parkrun time to another course, using course difficulty scores.</p>
    </div>
    <div class="themes" role="group" aria-label="Theme">
      <button type="button" data-theme-set="system" aria-pressed="true">Auto</button>
      <button type="button" data-theme-set="light" aria-pressed="false">Light</button>
      <button type="button" data-theme-set="dark" aria-pressed="false">Dark</button>
    </div>
  </header>

  <section class="panel">
    <h2>Your run</h2>
    <div class="fields">
      <label class="full">Time <input id="t" inputmode="text" autocomplete="off" value="20:00" placeholder="20:00"></label>
      <label>Course you ran <input id="from" list="courses" autocomplete="off" spellcheck="false" value="Gunnersbury" placeholder="Start typing a course"><small class="info" id="fromInfo"></small></label>
      <label>Course to attempt <input id="to" list="courses" autocomplete="off" spellcheck="false" value="Battersea" placeholder="Start typing a course"><small class="info" id="toInfo"></small></label>
      <button type="button" class="btn" id="swap">Swap courses</button>
    </div>
    <datalist id="courses"></datalist>
    <p class="note">Time as mm:ss, or h:mm:ss. Type part of a course name and pick it from the list.</p>
    <p class="warn" id="err" hidden></p>
  </section>

  <section class="panel">
    <h2>Prediction</h2>
    <div class="res" id="res"></div>
    <p class="note" id="flags"></p>
  </section>

  <section class="panel method">
    <h2>How it works</h2>
    <ul>
      <li><b>Scores.</b> Each course has a Standard Scratch Score (SSS) from The Running Channel, built from Tim Grose's work and Power of 10 data (list dated 29 April 2026). 0 is fastest and 12 is slowest.</li>
      <li><b>Conversion.</b> Each point is 30 seconds over 5km, from median finish times in average conditions. Predicted time = your time + 30s × (score of the new course − score of the old one).</li>
      <li><b>Limits.</b> The 30s is fixed for everyone. Weather, surface on the day, crowding and your own strengths are not adjusted for. Treat gaps of 2 points or more with caution.</li>
    </ul>
  </section>
</main>

<script>
(function () {
  var COURSES = /*@@DATA@@*/;
  var SEC_PER_POINT = 30, BIG_GAP = 2;
  var $ = function (id) { return document.getElementById(id); };
  var byName = {};
  COURSES.forEach(function (c) { byName[norm(c[0])] = c; });
  var dl = $("courses");
  COURSES.slice().sort(function (a, b) { return a[0].localeCompare(b[0]); }).forEach(function (c) {
    var o = document.createElement("option"); o.value = c[0]; o.label = "SSS " + c[1].toFixed(1); dl.appendChild(o);
  });
  function norm(s) { return s.toLowerCase().replace(/[’‘]/g, "'").replace(/\s+/g, " ").trim(); }
  // Exact name first, then a single course whose name contains the text.
  function find(q) {
    var n = norm(q); if (!n) return null;
    if (byName[n]) return byName[n];
    var hits = COURSES.filter(function (c) { return norm(c[0]).indexOf(n) >= 0; });
    return hits.length === 1 ? hits[0] : null;
  }
  function parseTime(x) {
    var p = x.trim().split(":");
    if (p.length < 2 || p.length > 3 || p.some(function (v) { return v === "" || isNaN(v); })) return null;
    var s = p.reduce(function (a, v) { return a * 60 + Number(v); }, 0);
    return s > 0 ? s : null;
  }
  function fmt(s) {
    s = Math.round(s);
    var h = Math.floor(s / 3600), m = Math.floor((s % 3600) / 60), r = s % 60;
    return h ? h + ":" + (m < 10 ? "0" : "") + m + ":" + (r < 10 ? "0" : "") + r : m + ":" + (r < 10 ? "0" : "") + r;
  }
  function info(id, q) {
    var c = find(q), el = $(id);
    el.textContent = c ? c[0] + ", SSS " + c[1].toFixed(1) : (q.trim() ? "Not found. Pick a course from the list." : "");
    return c;
  }
  function update() {
    $("err").hidden = true;
    var a = info("fromInfo", $("from").value), b = info("toInfo", $("to").value);
    var t = parseTime($("t").value);
    $("res").innerHTML = ""; $("flags").textContent = "";
    if (t === null) { $("err").hidden = false; $("err").textContent = "Enter the time as mm:ss, for example 20:00."; return; }
    if (!a || !b) { $("err").hidden = false; $("err").textContent = "Pick both courses from the list."; return; }
    var gap = b[1] - a[1], delta = Math.round(gap * SEC_PER_POINT), out = t + delta;
    var chg = delta === 0 ? "No change" : (delta < 0 ? "−" : "+") + Math.abs(delta) + "s";
    $("res").innerHTML =
      "<div><span>Predicted at " + b[0] + "</span><b class=\"pace\">" + fmt(out) + "</b><small>from " + fmt(t) + " at " + a[0] + "</small></div>" +
      "<div><span>Change</span><b>" + chg + "</b><small>" + (delta < 0 ? "faster course" : delta > 0 ? "slower course" : "same score") + "</small></div>" +
      "<div><span>Scores</span><b>" + a[1].toFixed(1) + " → " + b[1].toFixed(1) + "</b><small>" + Math.abs(gap).toFixed(1) + " points apart</small></div>";
    if (Math.abs(gap) >= BIG_GAP) $("flags").textContent = "These courses are " + Math.abs(gap).toFixed(1) + " points apart. Large gaps are less reliable, so treat the estimate with caution.";
  }
  $("swap").addEventListener("click", function () { var f = $("from"), g = $("to"), x = f.value; f.value = g.value; g.value = x; update(); });
  ["t", "from", "to"].forEach(function (id) { $(id).addEventListener("input", update); $(id).addEventListener("change", update); });
  update();
})();

(function () {
  var btns = document.querySelectorAll("[data-theme-set]");
  function apply(t) {
    if (t === "light" || t === "dark") document.documentElement.setAttribute("data-theme", t);
    else document.documentElement.removeAttribute("data-theme");
    btns.forEach(function (b) { b.setAttribute("aria-pressed", b.getAttribute("data-theme-set") === t ? "true" : "false"); });
  }
  var saved = "system";
  try { saved = localStorage.getItem("theme-pref") || "system"; } catch (e) {}
  apply(saved);
  btns.forEach(function (b) { b.addEventListener("click", function () { var t = b.getAttribute("data-theme-set"); apply(t); try { localStorage.setItem("theme-pref", t); } catch (e) {} }); });
})();
</script>
