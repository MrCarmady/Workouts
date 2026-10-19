import random, glob, os, sys, re
from playwright.sync_api import sync_playwright
JUNK=["", "0", "-5", "1e9", "99999999", "abc", "9"*30, "0.0000001", "NaN", "Infinity", "100", "60","18:54","5:30","1","2","3","10","0.5","-0","18:75"]
BAD=re.compile(r'NaN|Infinity|undefined|\[object|\bnull\b|e\+\d\d')
def main(seeds,acts_n):
    pages=sorted(f for f in glob.glob(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),'*.html')) if 'style-options' not in f)
    with sync_playwright() as p:
        b=p.chromium.launch()
        for path in pages:
            found={}
            for seed in range(seeds):
                pg=b.new_page(viewport={'width':390,'height':800}); errs=[]; acts=[]
                pg.on('pageerror',lambda e:errs.append(str(e)))
                pg.goto('file://'+path)
                random.seed(seed*131+7); sel='input:not([type=hidden]):not([type=file]), select, textarea, button, summary'
                for rnd in range(acts_n):
                    els=pg.query_selector_all(sel)
                    if not els: break
                    el=random.choice(els)
                    try:
                        if not el.is_visible(): continue
                        tag=el.evaluate('e=>e.tagName'); desc=el.evaluate('e=>e.tagName+"#"+e.id+" "+JSON.stringify(e.dataset)+" "+(e.innerText||"").slice(0,12)')
                        if tag=='SELECT':
                            opts=el.evaluate('e=>Array.from(e.options).map(o=>o.value)'); v=random.choice(opts); acts.append((desc,v)); el.select_option(v,timeout=300)
                        elif tag in('BUTTON','SUMMARY'): acts.append((desc,'click')); el.click(timeout=300)
                        else: v=random.choice(JUNK); acts.append((desc,v)); el.fill(v,timeout=300)
                    except Exception: pass
                    if errs:
                        key=errs[0][:90]
                        if key not in found: found[key]=(seed,acts[-6:])
                        break
                    if rnd%5==4:
                        try: t=pg.inner_text('body')
                        except Exception: t=''
                        m=BAD.search(t)
                        if m:
                            key='TEXT '+m.group(0)
                            if key not in found: found[key]=(seed,acts[-6:]+[t[max(0,m.start()-60):m.end()+40].replace('\n',' | ')])
                            break
                pg.close()
            print('==',os.path.basename(path),len(found),flush=True)
            for k,(sd,ac) in found.items():
                print('  ',k,'seed',sd)
                for a in ac: print('      ',a)
main(int(sys.argv[1]),int(sys.argv[2]))
