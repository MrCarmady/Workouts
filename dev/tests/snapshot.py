"""Snapshot test: drives each page with fixed inputs and records the visible output.
Usage: python3 snapshot.py write|check [pages_dir]"""
import sys, json, os
from playwright.sync_api import sync_playwright
HERE=os.path.dirname(os.path.abspath(__file__)); SNAP=os.path.join(HERE,'snapshot.json')
PAGES_SRC=sys.argv[2] if len(sys.argv)>2 else os.path.dirname(HERE)
import tempfile, glob
PAGES=tempfile.mkdtemp()   # copies with a charset tag, as the publish wrapper adds one
for _f in glob.glob(os.path.join(PAGES_SRC,'*.html')):
    open(os.path.join(PAGES,os.path.basename(_f)),'w',encoding='utf-8').write('<!doctype html><meta charset="utf-8">'+open(_f,encoding='utf-8').read())
RACES=[('5','18:54','70','mi'),('3','10:44.80','45','mi'),('10','39:10','','mi'),('21.0975','1:25:00','100','km')]
def fill(pg,id,v):
    if pg.query_selector('#'+id):
        el=pg.query_selector('#'+id)
        try:
            if el.evaluate('e=>e.tagName')=='SELECT': el.select_option(v,timeout=500)
            else: el.fill(v,timeout=500)
        except Exception: pass
def main_text(pg): return pg.inner_text('main')
def scenarios():
    out=[]
    for page in ['race-prediction-calculator','plan-builder','run-session-calculator','classic-session-generator']:
        for r in RACES: out.append((page,'race '+'|'.join(r),lambda pg,r=r:[fill(pg,'dist',r[0]),fill(pg,'time',r[1]),fill(pg,'week',r[2]),fill(pg,'wunit',r[3])]))
    out.append(('run-session-calculator','10 min reps',lambda pg:[fill(pg,'dist','5'),fill(pg,'time','18:54'),fill(pg,'unit','min'),fill(pg,'rep','10')]))
    out.append(('run-session-calculator','1000m reps',lambda pg:[fill(pg,'dist','5'),fill(pg,'time','18:54'),fill(pg,'unit','m'),fill(pg,'rep','1000')]))
    out.append(('run-session-calculator','3 min reps',lambda pg:[fill(pg,'dist','3'),fill(pg,'time','10:44.80'),fill(pg,'unit','min'),fill(pg,'rep','3')]))
    out.append(('plan-builder','block 4 days',lambda pg:[fill(pg,'dist','5'),fill(pg,'time','18:54'),fill(pg,'week','60'),fill(pg,'wunit','mi'),fill(pg,'days','4'),fill(pg,'ctl','50'),fill(pg,'weeks','10')]))
    out.append(('plan-builder','block 6 days taper',lambda pg:[fill(pg,'dist','10'),fill(pg,'time','39:10'),fill(pg,'week','50'),fill(pg,'wunit','mi'),fill(pg,'days','6'),fill(pg,'weeks','8'),fill(pg,'taper','14')]))
    for page in ['run-tss-calculator','run-tss-planner']:
        out.append((page,'race mode',lambda pg:[fill(pg,'mode','race'),fill(pg,'thr','3:58'),fill(pg,'dist','5'),fill(pg,'time','18:54'),fill(pg,'wmin','30'),fill(pg,'wpace','4:00'),fill(pg,'target','60'),fill(pg,'emin','20'),fill(pg,'epace','5:00')]))
    out.append(('hard-workout-predictor','6x1k',lambda pg:[fill(pg,'rep','1000'),fill(pg,'splits','3:38, 3:32, 3:33, 3:31, 3:34, 3:35')]))
    out.append(('hard-workout-predictor','6x800',lambda pg:[fill(pg,'rep','800'),fill(pg,'rest','90'),fill(pg,'splits','2:39, 2:39, 2:39, 2:40, 2:38, 2:36')]))
    out.append(('hard-workout-predictor','5x5km marathon',lambda pg:[fill(pg,'unit','km'),fill(pg,'rep','5'),fill(pg,'reps','5'),fill(pg,'target','42.195'),fill(pg,'splits','3:20/km')]))
    for n in ['1','2','4','5','6']:
        out.append(('hard-workout-predictor','3km x '+n,lambda pg,n=n:[fill(pg,'rep','3000'),fill(pg,'reps',n),fill(pg,'target','10'),fill(pg,'splits','3:25/km')]))
    for rep,u,n,rest,sp,tg in [('400','m','5','60','80,80,80,80,80','1.609344'),('400','m','18','60','3:10/km','1.609344'),('2000','m','2','120','7:15/km','10'),('1.2','km','10','90','3:45/km','10'),('1000','m','50','60','3:34','5'),('5','km','3','180','3:20/km','42.195'),('5','km','6','180','3:20/km','42.195')]:
        out.append(('hard-workout-predictor','slide %sx%s%s'%(n,rep,u),lambda pg,rep=rep,u=u,n=n,rest=rest,sp=sp,tg=tg:[fill(pg,'unit',u),fill(pg,'rep',rep),fill(pg,'rest',rest),fill(pg,'reps',n),fill(pg,'target',tg),fill(pg,'splits',sp)]))
    return out
def tracker(pg):
    for d,reps,rep,u,pace in [('2026-09-01','4','10','min','4:05'),('2026-09-08','6','1','km','3:58'),('2026-09-15','5','8','min','3:55'),('2026-09-29','3','12','min','4:08'),('2026-10-06','4','10','min','4:00')]:
        fill(pg,'date',d);fill(pg,'reps',reps);fill(pg,'rep',rep);fill(pg,'unit',u);fill(pg,'pace',pace);pg.click('#add')
def run():
    res={}
    with sync_playwright() as p:
        b=p.chromium.launch()
        sc=scenarios()+[('sub-t-trend-tracker','5 sessions',tracker)]
        for page,name,fn in sc:
            ctx=b.new_context(viewport={'width':900,'height':900}); pg=ctx.new_page(); errs=[]; pg.on('pageerror',lambda e:errs.append(str(e)))
            pg.goto('file://'+os.path.join(PAGES,page+'.html')); fn(pg); pg.wait_for_timeout(50)
            txt=main_text(pg)
            if page=='classic-session-generator' and pg.query_selector('#workout'):
                pass
            res[page+' :: '+name]={'text':txt,'errors':errs}; ctx.close()
        # classic: every workout option
        ctx=b.new_context(); pg=ctx.new_page(); pg.goto('file://'+os.path.join(PAGES,'classic-session-generator.html'))
        fill(pg,'dist','5');fill(pg,'time','18:54');fill(pg,'week','70');fill(pg,'wunit','mi')
        for o in pg.eval_on_selector_all('#workout option','els=>els.map(e=>e.value)'):
            fill(pg,'workout',o); res['classic-session-generator :: workout '+o]={'text':main_text(pg),'errors':[]}
        b.close()
    return res
if __name__=='__main__':
    mode=sys.argv[1]; res=run()
    if mode=='write':
        json.dump(res,open(SNAP,'w'),indent=1); print('wrote',len(res),'scenarios')
    else:
        old=json.load(open(SNAP)); bad=0
        for k in sorted(set(old)|set(res)):
            if k not in res or k not in old or old[k]!=res[k]:
                bad+=1; print('DIFF',k)
                if k in old and k in res:
                    a,b2=old[k]['text'].split('\n'),res[k]['text'].split('\n')
                    for x,y in zip(a,b2):
                        if x!=y: print('   was:',x[:100]); print('   now:',y[:100]); break
        errs=[k for k,v in res.items() if v['errors']]
        print('checked',len(res),'scenarios;',bad,'differ;',len(errs),'with page errors')
        sys.exit(1 if bad or errs else 0)
