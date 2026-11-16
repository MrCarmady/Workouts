"""Write the shared theme switch into every tool page, or with --check fail if a page differs."""
import re, glob, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import theme
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
check = '--check' in sys.argv
bad = 0
for f in sorted(glob.glob(os.path.join(R, '*.html'))):
    s = open(f).read()
    if 'data-theme-set' not in s and 'id="themebtn"' not in s:
        continue
    o = s
    s = re.sub(r'<div class="themes" role="group" aria-label="Theme">.*?</div>', lambda m: theme.HTML, s, count=1, flags=re.S)
    s = re.sub(r'<button type="button" class="themes" id="themebtn".*?</button>', lambda m: theme.HTML, s, count=1, flags=re.S)
    lines = s.split('\n'); out = []; done = False
    for l in lines:
        if l.startswith('.themes'):
            if not done: out.append(theme.CSS); done = True
            continue
        out.append(l)
    s = '\n'.join(out)
    # CSS block already new: lines start with .themes too, so the replace above is idempotent
    s = re.sub(r'(\(function \(\) \{\s*var btns = document\.querySelectorAll\("\[data-theme-set\]"\).*?\}\)\(\);)|(\(function \(\) \{\s*var btn = document\.getElementById\("themebtn"\).*?\}\)\(\);)', lambda m: theme.JS, s, count=1, flags=re.S)
    s = re.sub(r'(\.head \{ display: flex; )flex-wrap: wrap;', r'\1flex-wrap: nowrap;', s, count=1)
    if '.head > div:first-child' not in s:
        s = s.replace('.head { display: flex;', '.head > div:first-child { min-width: 0; }\n.head { display: flex;', 1)
    ok = all(x in s for x in (theme.HTML, theme.JS, theme.CSS)) and 'data-theme-set' not in s
    if not ok: print('FAILED', os.path.basename(f)); bad += 1
    if check:
        if s != o: print('differs:', os.path.basename(f)); bad += 1
    elif s != o:
        open(f, 'w').write(s)
if bad: sys.exit('theme block problem')
print('theme block in sync' if check else 'theme block written')
