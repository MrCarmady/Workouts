"""Theme switch used on every tool page and the site pages: one small icon button, top right.
apply_theme.py writes this into the pages; build_site.py uses it for the index and method pages."""
CSS = """.themes { display: inline-grid; place-items: center; flex: none; width: 32px; height: 32px; padding: 0; border: 1px solid var(--line); border-radius: 2px; background: var(--surface); color: var(--muted); cursor: pointer; }
.themes:hover { color: var(--fg); }
.themes:focus-visible { outline: 2px solid var(--accent); outline-offset: 2px; }
.themes svg { display: none; width: 18px; height: 18px; fill: none; stroke: currentColor; stroke-width: 1.8; stroke-linecap: round; stroke-linejoin: round; }
.themes[data-mode="system"] .i-system, .themes[data-mode="light"] .i-light, .themes[data-mode="dark"] .i-dark { display: block; }
.themes .i-system path { fill: currentColor; }"""
HTML = """<button type="button" class="themes" id="themebtn" data-mode="system" aria-label="Theme: auto. Click to change." title="Theme: auto">
      <svg class="i-system" viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="8"/><path d="M12 4a8 8 0 0 1 0 16z"/></svg>
      <svg class="i-light" viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/></svg>
      <svg class="i-dark" viewBox="0 0 24 24" aria-hidden="true"><path d="M21 12.8A9 9 0 1 1 11.2 3a7 7 0 0 0 9.8 9.8z"/></svg>
    </button>"""
JS = """(function () {
  var btn = document.getElementById("themebtn"), order = ["system", "light", "dark"], names = { system: "auto", light: "light", dark: "dark" };
  function apply(t) {
    if (t === "light" || t === "dark") document.documentElement.setAttribute("data-theme", t);
    else document.documentElement.removeAttribute("data-theme");
    btn.setAttribute("data-mode", t);
    btn.setAttribute("aria-label", "Theme: " + names[t] + ". Click to change.");
    btn.title = "Theme: " + names[t];
  }
  var saved = "system";
  try { saved = localStorage.getItem("theme-pref") || "system"; } catch (e) {}
  if (order.indexOf(saved) < 0) saved = "system";
  apply(saved);
  btn.addEventListener("click", function () {
    var t = order[(order.indexOf(btn.getAttribute("data-mode")) + 1) % order.length];
    apply(t);
    try { localStorage.setItem("theme-pref", t); } catch (e) {}
  });
})();"""
