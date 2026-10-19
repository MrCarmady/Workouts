import sys, re, json, glob, os, random, time
from playwright.sync_api import sync_playwright
SRC=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
JUNK=["18:75","18:5","0:0","00:00:00","1:00:00","999:59:59","-0","0.0","1e-9","12345678901234567890","1.2.3","  5  ","5 5","+7","7+","５","0 0","1:30:00.5",".5","5.","", " ", "0", "-5", "1e9", "99999999", "abc", "1:2:3:4", "::", "0:00", "59:99", "-1:30", "1,5", "٣", "🏃", "<img src=x onerror=alert(1)>", "9"*30, "0.0000001", "NaN", "Infinity", "1:00:00:00", "00:00:01", "3:00:00", "100000", "0.5", "-0"]
BAD=re.compile(r'NaN|Infinity|undefined|\[object|\bnull\b|Invalid|(?:^|\t)-\d+:\d\d|:60\b|\d:\d\d:\d\d:\d\d|\b\d+\.\d{5,}|-0\b(?!\d)',re.M)
def pages():
    return sorted(f for f in glob.glob(SRC+'/*.html') if 'style-options' not in f)
def vis_text(pg):
    try: return pg.inner_text('body')
    except Exception: return ''
def check(pg, errs, ctx, issues):
    t=vis_text(pg)
    for m in BAD.finditer(t):
        s=max(0,m.start()-40); issues.setdefault(('text',m.group(0)),(ctx,t[s:m.end()+40].replace('\n',' | ')))
    try:
        ov=pg.evaluate('document.documentElement.scrollWidth - window.innerWidth')
        if ov>2: issues.setdefault(('overflow',),(ctx,'scrollWidth exceeds viewport by %d'%ov))
    except Exception: pass
    while errs:
        e=errs.pop(0); issues.setdefault(('js',e[:80]),(ctx,e[:300]))
def run_page(br,path,mode):
    name=os.path.basename(path); issues={}
    ctx=br.new_context(viewport={'width':390,'height':800})
    pg=ctx.new_page(); errs=[]
    pg.on('pageerror',lambda e:errs.append('pageerror: '+str(e)))
    pg.on('dialog',lambda d:(errs.append('DIALOG: '+d.message),d.dismiss()))
    pg.on('console',lambda m:errs.append('console: '+m.text) if (m.type=='error' and 'ERR_TUNNEL' not in m.text and 'Failed to load resource' not in m.text) else None)
    html='<!doctype html><meta charset="utf-8">'+open(path,encoding='utf-8').read()
    tmp='/tmp/fz_'+name; open(tmp,'w',encoding='utf-8').write(html)
    pg.goto('file://'+tmp); pg.wait_for_timeout(200)
    check(pg,errs,'load',issues)
    sel='input:not([type=hidden]):not([type=file]):not([type=checkbox]):not([type=radio]), select, textarea'
    n=len(pg.query_selector_all(sel))
    n=min(n,60)
    for i in range(n):
        els=pg.query_selector_all(sel)
        if i>=len(els): break
        el=els[i]
        try:
            if not el.is_visible(): continue
            tag=el.evaluate('e=>e.tagName'); eid=el.evaluate('e=>e.id||e.getAttribute("data-f")||e.getAttribute("data-o")||e.name||""')
            orig=el.evaluate('e=>e.value')
        except Exception: continue
        label='%s#%s[%d]'%(tag,eid,i)
        if tag=='SELECT':
            opts=el.evaluate('e=>Array.from(e.options).map(o=>o.value)')
            for v in opts:
                try: el.select_option(v,timeout=500)
                except Exception: continue
                check(pg,errs,'%s=%s'%(label,v),issues)
            try: el.select_option(orig,timeout=500)
            except Exception: pass
        else:
            for v in JUNK:
                try: el.fill(v,timeout=500)
                except Exception: continue
                try: el.dispatch_event('change')
                except Exception: pass
                check(pg,errs,'%s=%r'%(label,v[:20]),issues)
            try: el.fill(orig,timeout=500)
            except Exception: pass
    # random combos
    random.seed(7)
    for rnd in range(150 if mode=='full' else 10):
        els=pg.query_selector_all(sel)
        for el in random.sample(els,min(len(els),6)):
            try:
                if not el.is_visible(): continue
                tag=el.evaluate('e=>e.tagName')
                if tag=='SELECT':
                    opts=el.evaluate('e=>Array.from(e.options).map(o=>o.value)'); el.select_option(random.choice(opts),timeout=300)
                else: el.fill(random.choice(JUNK),timeout=300)
            except Exception: pass
        check(pg,errs,'random round %d'%rnd,issues)
    # buttons: click each visible button once
    btns=pg.query_selector_all('button')
    for i,b in enumerate(btns[:40]):
        try:
            if b.is_visible(): b.click(timeout=300)
        except Exception: pass
        check(pg,errs,'button %d'%i,issues)
    # corrupt storage
    keys=pg.evaluate('Object.keys(localStorage)')
    for variant in ['{','null','"x"','[]','{"time":123,"dist":"zz","km":"x","cmp":5}','\x00','9'*5000]:
        pg.evaluate('([k,v])=>{k.forEach(x=>localStorage.setItem(x,v))}',[keys,variant])
        pg.goto('file://'+tmp); pg.wait_for_timeout(100)
        check(pg,errs,'storage=%r'%variant[:15],issues)
    # storage throws
    pg2=ctx.new_page(); e2=[]
    pg2.on('pageerror',lambda e:e2.append('pageerror: '+str(e)))
    pg2.add_init_script("Storage.prototype.getItem=function(){throw new Error('blocked')};Storage.prototype.setItem=function(){throw new Error('blocked')}")
    pg2.goto('file://'+tmp); pg2.wait_for_timeout(200)
    check(pg2,e2,'storage blocked',issues)
    ctx.close()
    return issues
if __name__=='__main__':
    mode=sys.argv[1] if len(sys.argv)>1 else 'full'
    only=sys.argv[2:] 
    out={}
    with sync_playwright() as p:
        br=p.chromium.launch()
        for path in pages():
            if only and not any(o in path for o in only): continue
            t=time.time()
            try: iss=run_page(br,path,mode)
            except Exception as e: iss={('crash',):('harness',str(e)[:200])}
            print('==',os.path.basename(path),'%.0fs'%(time.time()-t),len(iss),'issue types',flush=True)
            for k,(c,d) in iss.items(): print('  ',k,'|',c,'|',d[:220],flush=True)
