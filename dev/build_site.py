import re, shutil, markdown, os, html, subprocess, sys
# Stop the build if the shared block is out of sync or any test fails.
if subprocess.call([os.path.join(os.path.dirname(os.path.abspath(__file__)),'tests','run_tests.sh')])!=0: sys.exit('Tests failed: build stopped')
HERE=os.path.dirname(os.path.abspath(__file__)); SRC=HERE
OUT=os.environ.get('SITE_OUT') or (os.path.dirname(HERE) if os.path.basename(HERE)=='dev' else os.path.join(HERE,'site'))
os.makedirs(OUT+'/methods',exist_ok=True)
tools=[ # (src file, out file, title, desc, method md, method slug, group)
 ("run-session-calculator.html","run-session-generator.html","Sub-Threshold Session Generator","Rep pace, recovery, rep count and TSS for a session, from a race result and a rep length.","run-session-calculator.md","run-session-generator","Sessions"),
 ("race-prediction-calculator.html","race-prediction-calculator.html","Race Prediction Calculator","Predicted times for 1500m to the marathon from one race result.","race-prediction-calculator.md","race-prediction-calculator","Race and pace"),
 ("classic-session-generator.html","classic-session-generator.html","Classic Session Generator","Paces for tempo runs, ladders, Aussie quarters, Mona fartlek, Yasso and Rosario 800s and more, from a race result.","classic-session-generator.md","classic-session-generator","Sessions"),
 ("sub-t-trend-tracker.html","sub-t-trend-tracker.html","Sub-Threshold Trend Tracker","Log classic sub-threshold sessions and track the implied threshold pace over time.","sub-t-trend-tracker.md","sub-t-trend-tracker","Sessions"),
("hard-workout-predictor.html","hard-workout-predictor.html","Hard Workout Predictor","Predict a race from a hard interval session, using rep length, rest and RPE.","hard-workout-predictor.md","hard-workout-predictor","Race and pace"),
("plan-builder.html","plan-builder.html","Plan Builder","Weekly distance, quality sessions and easy running for a block, from a race result, run days and a target CTL ramp.","plan-builder.md","plan-builder","Planning and load"),
 ("run-load-planner.html","run-load-planner.html","Run Load Planner","Fitness, fatigue and form (CTL, ATL, TSB) from a planned week, or the TSS needed for a target.","run-load-planner.md","run-load-planner","Planning and load"),
 ("run-tss-calculator.html","run-tss-calculator.html","Run TSS Calculator","Training stress score for a run, from your threshold pace and what you ran.","run-tss-calculator.md","run-tss-calculator","Planning and load"),
 ("run-tss-planner.html","run-tss-planner.html","Run TSS Planner","The workout pace that hits a target TSS.","run-tss-planner.md","run-tss-planner","Sessions"),
 ("treadmill-acsm-widget.html","treadmill-flat-equivalent.html","Treadmill Flat Equivalent","Flat-ground pace for a treadmill belt speed and incline.","treadmill-flat-equivalent.md","treadmill-flat-equivalent","Race and pace"),
 ("lift-scheme-calculator.html","lift-scheme-calculator.html","Lift Scheme Calculator","Estimated 1RM and working weights for common set and rep schemes, from one set.","lift-scheme-calculator.md","lift-scheme-calculator","Lifting"),
]
HEAD='<!doctype html>\n<html lang="en">\n<meta charset="utf-8">\n<meta name="viewport" content="width=device-width, initial-scale=1">\n<style>body{margin:0}[hidden]{display:none!important}img{max-width:100%}.sitenav{font-size:.85rem;font-weight:600;letter-spacing:.04em;text-transform:uppercase;margin:0}.sitenav a{color:var(--accent);text-decoration:none}.sitenav a:hover{text-decoration:underline}</style>\n'
for src,out,title,desc,md,slug,grp in tools:
    s=open(f'{SRC}/{src}').read()
    assert s.lstrip().startswith('<title>'), src
    assert s.count('<main class="wrap">')==1, src
    s=s.replace('<main class="wrap">','<main class="wrap">\n  <p class="sitenav"><a href="index.html">&larr; All tools</a></p>',1)
    if src in ('run-session-calculator.html','classic-session-generator.html'):
        assert s.count('var SITE = false;')==1
        s=s.replace('var SITE = false;','var SITE = true; ')
    assert s.count('</main>')==1, src
    s=s.replace('</main>','  <p class="sitenav"><a href="methods/'+slug+'.html">How it works &rarr;</a></p>\n</main>',1)
    open(f'{OUT}/{out}','w').write(HEAD+s)
TOK='''
:root { --bg:#f2f2f1; --surface:#ffffff; --surface-2:#f0f0ee; --fg:#17181a; --muted:#6a6d72; --line:#deded9; --accent:#c8372d; --accent-soft:#f8e3e0;
  --font-display:"Archivo Narrow","Arial Narrow",system-ui,sans-serif; --font-body:"Archivo",system-ui,-apple-system,"Segoe UI",sans-serif; }
@media (prefers-color-scheme: dark) { :root:not([data-theme="light"]) { --bg:#141416; --surface:#1c1c1f; --surface-2:#25252a; --fg:#ececea; --muted:#9a9ca2; --line:#34343a; --accent:#ef6a5e; --accent-soft:#3a1f1c; color-scheme:dark; } }
:root[data-theme="dark"] { --bg:#141416; --surface:#1c1c1f; --surface-2:#25252a; --fg:#ececea; --muted:#9a9ca2; --line:#34343a; --accent:#ef6a5e; --accent-soft:#3a1f1c; color-scheme:dark; }
body { margin:0; background:var(--bg); color:var(--fg); font-family:var(--font-body); font-size:15px; line-height:1.5; }
.wrap { max-width:760px; margin:0 auto; padding-inline:16px; padding-block:24px 48px; display:grid; gap:20px; }
.wrap > * { min-width:0; }
h1 { font-family:var(--font-display); font-weight:700; font-size:2rem; letter-spacing:.02em; text-transform:uppercase; margin:0; text-wrap:balance; }
h2 { font-family:var(--font-display); font-weight:600; font-size:1.15rem; letter-spacing:.06em; text-transform:uppercase; margin:0 0 12px; color:var(--muted); }
a { color:var(--accent); }
.head { display:flex; flex-wrap:wrap; align-items:flex-start; justify-content:space-between; gap:12px; }
.themes { display:inline-flex; border:1px solid var(--line); border-radius:2px; overflow:hidden; background:var(--surface); }
.themes button { font:inherit; font-size:.8rem; font-weight:600; letter-spacing:.05em; text-transform:uppercase; color:var(--muted); background:transparent; border:0; padding:7px 12px; cursor:pointer; }
.themes button + button { border-left:1px solid var(--line); }
.themes button[aria-pressed="true"] { background:var(--accent); color:#fff; }
.themes button:focus-visible, a:focus-visible { outline:2px solid var(--accent); outline-offset:2px; }
.sub { color:var(--muted); margin:6px 0 0; max-width:62ch; }
'''
THEME_JS='''<script>
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
</script>'''
TOGGLE='''<div class="themes" role="group" aria-label="Theme">
      <button type="button" data-theme-set="system" aria-pressed="true">Auto</button>
      <button type="button" data-theme-set="light" aria-pressed="false">Light</button>
      <button type="button" data-theme-set="dark" aria-pressed="false">Dark</button>
    </div>'''
FONTS='<link rel="preconnect" href="https://fonts.googleapis.com">\n<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo:wght@400;500;600;700&family=Archivo+Narrow:wght@500;600;700&display=swap">'
# index
ORDER=['Planning and load','Sessions','Race and pace','Lifting']
cards={}
for src,out,title,desc,md,slug,grp in sorted(tools,key=lambda t:(ORDER.index(t[6]),tools.index(t))):
    cards.setdefault(grp,[]).append(f'''      <li class="card"><div><a class="name" href="{out}">{html.escape(title)}</a><p>{html.escape(desc)}</p></div><a class="meth" href="methods/{slug}.html">How it works</a></li>''')
groups=''.join(f'''    <section>
      <h2>{g}</h2>
      <ul class="cards">
{chr(10).join(v)}
      </ul>
    </section>
''' for g,v in cards.items())
index=f'''<!doctype html>
<html lang="en">
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Training Tools</title>
{FONTS}
<style>{TOK}
.cards {{ list-style:none; margin:0; padding:0; display:grid; gap:10px; }}
.card {{ display:flex; flex-wrap:wrap; align-items:center; justify-content:space-between; gap:10px 16px; background:var(--surface); border:1px solid var(--line); border-radius:2px; padding:14px 16px; }}
.card > div {{ min-width:0; flex:1 1 320px; }}
.card .name {{ font-family:var(--font-display); font-weight:600; font-size:1.25rem; text-decoration:none; }}
.card .name:hover {{ text-decoration:underline; }}
.card p {{ margin:2px 0 0; color:var(--muted); font-size:.92rem; }}
.card .meth {{ font-size:.85rem; font-weight:600; letter-spacing:.04em; text-transform:uppercase; white-space:nowrap; }}
.note {{ color:var(--muted); font-size:.85rem; margin:0; }}
</style>
<main class="wrap">
  <header class="head">
    <div>
      <h1>Training Tools</h1>
      <p class="sub">Calculators for running sessions, race predictions, training load and lifting. Each has a short page on how it is calculated.</p>
    </div>
    {TOGGLE}
  </header>
{groups}  <p class="note">All figures are estimates for training. Check paces against heart rate or feel.</p>
</main>
{THEME_JS}
'''
open(f'{OUT}/index.html','w').write(index)
open(f'{OUT}/.nojekyll','w').write('')
# method pages
mdcss='''
.doc { background:var(--surface); border:1px solid var(--line); border-radius:2px; padding:20px; }
.doc h1 { font-size:1.6rem; margin-bottom:12px; }
.doc h2 { margin:24px 0 8px; }
.doc p, .doc li { max-width:78ch; }
.doc table { border-collapse:collapse; display:block; overflow-x:auto; max-width:100%; font-variant-numeric:tabular-nums; margin:12px 0; }
.doc th, .doc td { text-align:left; padding:7px 12px; border:1px solid var(--line); vertical-align:top; }
.doc th { background:var(--surface-2); font-family:var(--font-display); letter-spacing:.05em; text-transform:uppercase; font-size:.85rem; color:var(--muted); }
.doc pre { background:var(--surface-2); padding:12px; overflow-x:auto; border-radius:2px; max-width:100%; }
.doc code { font-size:.9em; background:var(--surface-2); padding:1px 4px; border-radius:2px; }
.doc pre code { background:none; padding:0; }
.crumbs { font-size:.85rem; display:flex; flex-wrap:wrap; gap:8px 16px; }
@media (max-width:560px) { .doc { padding:14px; } }
'''
for src,out,title,desc,md,slug,grp in tools:
    body=markdown.markdown(open(f'{SRC}/methodology/{md}').read(),extensions=['tables','fenced_code'])
    page=f'''<!doctype html>
<html lang="en">
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}: how it works</title>
{FONTS}
<style>{TOK}{mdcss}</style>
<main class="wrap">
  <header class="head">
    <nav class="crumbs"><a href="../index.html">All tools</a><a href="../{out}">Open {html.escape(title)}</a></nav>
    {TOGGLE}
  </header>
  <article class="doc">
{body}
  </article>
</main>
{THEME_JS}
'''
    open(f'{OUT}/methods/{slug}.html','w').write(page)
print('ok')
