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
    out.append(('tactical-barbell-planner','defaults',lambda pg:None))
    out.append(('tactical-barbell-planner','fighter',lambda pg:[pg.select_option('#prog','fighter')]))
    out.append(('tactical-barbell-planner','zulu',lambda pg:[pg.select_option('#prog','zulu')]))
    out.append(('tactical-barbell-planner','bulgarian high-rep',lambda pg:[pg.click('#add'),pg.select_option('#lifts > section:nth-of-type(4) select[data-f=lift]','bss')]))
    for page in ['run-tss-calculator','run-tss-planner']:
        out.append((page,'race mode',lambda pg:[fill(pg,'mode','race'),fill(pg,'thr','3:58'),fill(pg,'dist','5'),fill(pg,'time','18:54'),fill(pg,'wmin','30'),fill(pg,'wpace','4:00'),fill(pg,'target','60'),fill(pg,'emin','20'),fill(pg,'epace','5:00')]))
    out.append(('hard-workout-predictor','6x1k',lambda pg:[fill(pg,'rep','1000'),fill(pg,'splits','3:38, 3:32, 3:33, 3:31, 3:34, 3:35')]))
    out.append(('hard-workout-predictor','6x800',lambda pg:[fill(pg,'rep','800'),fill(pg,'rest','90'),fill(pg,'splits','2:39, 2:39, 2:39, 2:40, 2:38, 2:36')]))
    out.append(('hard-workout-predictor','5x5km marathon',lambda pg:[fill(pg,'unit','km'),fill(pg,'rep','5'),fill(pg,'reps','5'),fill(pg,'target','42.195'),fill(pg,'splits','3:20/km')]))
    for n in ['1','2','4','5','6']:
        out.append(('hard-workout-predictor','3km x '+n,lambda pg,n=n:[fill(pg,'rep','3000'),fill(pg,'reps',n),fill(pg,'target','10'),fill(pg,'splits','3:25/km')]))
    for rep,u,n,rest,sp,tg in [('400','m','5','60','80,80,80,80,80','1.609344'),('400','m','18','60','3:10/km','1.609344'),('2000','m','2','120','7:15/km','10'),('1.2','km','10','90','3:45/km','10'),('1000','m','50','60','3:34','5'),('5','km','3','180','3:20/km','42.195'),('5','km','6','180','3:20/km','42.195')]:
        out.append(('hard-workout-predictor','slide %sx%s%s'%(n,rep,u),lambda pg,rep=rep,u=u,n=n,rest=rest,sp=sp,tg=tg:[fill(pg,'unit',u),fill(pg,'rep',rep),fill(pg,'rest',rest),fill(pg,'reps',n),fill(pg,'target',tg),fill(pg,'splits',sp)]))
    for lab,u,d,tm,rp,tg in [('5k TT 20:00 RPE10','km','5','20:00','10','5'),('8k tempo 4:50/km RPE7','km','8','4:50/km','7','10'),('HM 1:20:00 RPE10 to M','km','21.0975','1:20:00','10','42.195')]:
        out.append(('hard-workout-predictor','continuous '+lab,lambda pg,u=u,d=d,tm=tm,rp=rp,tg=tg:[fill(pg,'mode','cont'),fill(pg,'unit',u),fill(pg,'rep',d),fill(pg,'rpe',rp),fill(pg,'target',tg),fill(pg,'splits',tm)]))
    out.append(('marathon-plans','daniels week 1 mi',lambda pg:[fill(pg,'author','daniels'),fill(pg,'plan','2qa'),fill(pg,'dist','5'),fill(pg,'time','18:54'),fill(pg,'week','50'),fill(pg,'wunit','mi')]))
    out.append(('marathon-plans','daniels week 7 km slower',lambda pg:[fill(pg,'author','daniels'),fill(pg,'plan','2qa'),fill(pg,'dist','5'),fill(pg,'time','24:00'),fill(pg,'week','80'),fill(pg,'wunit','km'),fill(pg,'days','5'),fill(pg,'wk','7')]))
    out.append(('marathon-plans','daniels race week',lambda pg:[fill(pg,'author','daniels'),fill(pg,'plan','2qa'),fill(pg,'dist','10'),fill(pg,'time','39:10'),fill(pg,'week','45'),fill(pg,'wk','18')]))
    out.append(('marathon-plans','hansons beginner week 11',lambda pg:[fill(pg,'author','hansons'),fill(pg,'plan','beg'),fill(pg,'dist','5'),fill(pg,'time','18:45'),fill(pg,'wk','11')]))
    out.append(('marathon-plans','hansons beginner km race week',lambda pg:[fill(pg,'author','hansons'),fill(pg,'plan','beg'),fill(pg,'dist','10'),fill(pg,'time','39:10'),fill(pg,'wunit','km'),fill(pg,'wk','18')]))
    out.append(('marathon-plans','daniels 2QB week 12',lambda pg:[fill(pg,'author','daniels'),fill(pg,'plan','2qb'),fill(pg,'dist','5'),fill(pg,'time','18:45'),fill(pg,'week','50'),fill(pg,'wk','12')]))
    out.append(('marathon-plans','daniels 2QB km race week',lambda pg:[fill(pg,'author','daniels'),fill(pg,'plan','2qb'),fill(pg,'dist','10'),fill(pg,'time','39:10'),fill(pg,'week','80'),fill(pg,'wunit','km'),fill(pg,'wk','18')]))
    out.append(('marathon-plans','daniels 2QC week 7 lesser',lambda pg:[fill(pg,'author','daniels'),fill(pg,'plan','2qc'),fill(pg,'dist','5'),fill(pg,'time','18:45'),fill(pg,'week','65'),fill(pg,'wk','13')]))
    out.append(('marathon-plans','daniels 2QC week 3 reps',lambda pg:[fill(pg,'author','daniels'),fill(pg,'plan','2qc'),fill(pg,'dist','5'),fill(pg,'time','18:45'),fill(pg,'week','65'),fill(pg,'wk','3')]))
    out.append(('marathon-plans','daniels 2QC race week',lambda pg:[fill(pg,'author','daniels'),fill(pg,'plan','2qc'),fill(pg,'dist','5'),fill(pg,'time','18:45'),fill(pg,'week','65'),fill(pg,'wk','18')]))
    out.append(('marathon-plans','daniels 2QD week 13',lambda pg:[fill(pg,'author','daniels'),fill(pg,'plan','2qd'),fill(pg,'dist','5'),fill(pg,'time','18:45'),fill(pg,'week','75'),fill(pg,'wk','13')]))
    out.append(('marathon-plans','daniels 2QD race week km',lambda pg:[fill(pg,'author','daniels'),fill(pg,'plan','2qd'),fill(pg,'dist','10'),fill(pg,'time','39:10'),fill(pg,'week','120'),fill(pg,'wunit','km'),fill(pg,'wk','18')]))
    out.append(('marathon-plans','pfitz 18/85 week 11',lambda pg:[fill(pg,'author','pfitzinger'),fill(pg,'plan','18/85'),fill(pg,'dist','5'),fill(pg,'time','18:45'),fill(pg,'wk','11')]))
    out.append(('marathon-plans','pfitz 12/85 recovery',lambda pg:[fill(pg,'author','pfitzinger'),fill(pg,'plan','12/85'),fill(pg,'dist','5'),fill(pg,'time','18:45'),pg.check('#rec'),fill(pg,'wk','14')]))
    out.append(('marathon-plans','hansons 18:30 week 1',lambda pg:[fill(pg,'author','hansons'),fill(pg,'plan','adv'),fill(pg,'dist','5'),fill(pg,'time','18:30')]))
    out.append(('marathon-plans','hansons week 7 km',lambda pg:[fill(pg,'author','hansons'),fill(pg,'plan','adv'),fill(pg,'dist','5'),fill(pg,'time','18:30'),fill(pg,'wunit','km'),fill(pg,'wk','7')]))
    out.append(('marathon-plans','hansons week 11 strength',lambda pg:[fill(pg,'author','hansons'),fill(pg,'plan','adv'),fill(pg,'dist','10'),fill(pg,'time','39:10'),fill(pg,'wk','11')]))
    out.append(('marathon-plans','hansons race week',lambda pg:[fill(pg,'author','hansons'),fill(pg,'plan','adv'),fill(pg,'dist','5'),fill(pg,'time','20:00'),fill(pg,'wk','18')]))
    out.append(('marathon-plans','copeland 18:45 week 1',lambda pg:[fill(pg,'author','copeland'),fill(pg,'dist','5'),fill(pg,'time','18:45')]))
    out.append(('marathon-plans','copeland week 14 mi',lambda pg:[fill(pg,'author','copeland'),fill(pg,'dist','5'),fill(pg,'time','18:45'),fill(pg,'wunit','mi'),fill(pg,'wk','14')]))
    out.append(('marathon-plans','copeland week 13 rep5 18',lambda pg:[fill(pg,'author','copeland'),fill(pg,'dist','5'),fill(pg,'time','18:45'),fill(pg,'rep5','18'),fill(pg,'wk','13')]))
    out.append(('marathon-plans','copeland race week ctl 45',lambda pg:[fill(pg,'author','copeland'),fill(pg,'dist','10'),fill(pg,'time','39:10'),fill(pg,'ctl','45'),fill(pg,'wk','15')]))
    out.append(('marathon-plans','pfitz 18/70 18:45',lambda pg:[fill(pg,'author','pfitzinger'),fill(pg,'dist','5'),fill(pg,'time','18:45')]))
    out.append(('marathon-plans','pfitz 12/70 km',lambda pg:[fill(pg,'author','pfitzinger'),fill(pg,'dist','5'),fill(pg,'time','18:45'),fill(pg,'plan','12/70'),fill(pg,'wunit','km'),fill(pg,'wk','5')]))
    out.append(('marathon-plans','pfitz long pace 80 tune-up 15',lambda pg:[fill(pg,'author','pfitzinger'),fill(pg,'dist','10'),fill(pg,'time','39:10'),fill(pg,'lp','80'),fill(pg,'rd','15'),fill(pg,'wk','12')]))
    out.append(('marathon-plans','pfitz recovery ctl 50',lambda pg:[fill(pg,'author','pfitzinger'),fill(pg,'dist','5'),fill(pg,'time','18:45'),fill(pg,'ctl','50'),pg.check('#rec'),fill(pg,'wk','20')]))
    out.append(('marathon-plans','pfitz 18/55',lambda pg:[fill(pg,'author','pfitzinger'),fill(pg,'dist','5'),fill(pg,'time','18:45'),fill(pg,'plan','18/55'),fill(pg,'wk','11')]))
    out.append(('marathon-plans','pfitz 12/55 km race week recovery',lambda pg:[fill(pg,'author','pfitzinger'),fill(pg,'dist','10'),fill(pg,'time','39:10'),fill(pg,'plan','12/55'),fill(pg,'wunit','km'),pg.check('#rec'),fill(pg,'wk','13')]))
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
