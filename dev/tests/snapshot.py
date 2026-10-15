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
    LASTWK="e=>{var s=document.querySelector('#wk');s.selectedIndex=s.options.length-1;s.dispatchEvent(new Event('change',{bubbles:true}))}"
    out.append(('plan-builder','race week 7 days sub-T',lambda pg:[fill(pg,'dist','5'),fill(pg,'time','18:45'),fill(pg,'week','60'),fill(pg,'wunit','mi'),fill(pg,'days','7'),fill(pg,'ctl','45'),fill(pg,'weeks','16'),fill(pg,'rt','1.2'),fill(pg,'focus','subT'),fill(pg,'taper','7'),pg.eval_on_selector('#wk',LASTWK)]))
    out.append(('plan-builder','race week 6 days sub-T + intervals',lambda pg:[fill(pg,'dist','5'),fill(pg,'time','18:45'),fill(pg,'week','60'),fill(pg,'wunit','mi'),fill(pg,'days','6'),fill(pg,'ctl','45'),fill(pg,'weeks','12'),fill(pg,'focus','subTI'),fill(pg,'taper','14'),pg.eval_on_selector('#wk',LASTWK)]))
    out.append(('plan-builder','race week 3 days easy cap',lambda pg:[fill(pg,'dist','5'),fill(pg,'time','18:45'),fill(pg,'week','40'),fill(pg,'wunit','mi'),fill(pg,'days','3'),fill(pg,'ctl','35'),fill(pg,'weeks','12'),fill(pg,'rt','1.2'),fill(pg,'focus','subT'),fill(pg,'taper','7'),pg.eval_on_selector('#wk',LASTWK)]))
    out.append(('plan-builder','race week 4 days easy cap',lambda pg:[fill(pg,'dist','5'),fill(pg,'time','18:45'),fill(pg,'week','40'),fill(pg,'wunit','mi'),fill(pg,'days','4'),fill(pg,'ctl','35'),fill(pg,'weeks','12'),fill(pg,'rt','1.2'),fill(pg,'focus','subT'),fill(pg,'taper','7'),pg.eval_on_selector('#wk',LASTWK)]))
    out.append(('plan-builder','block 6 days taper',lambda pg:[fill(pg,'dist','10'),fill(pg,'time','39:10'),fill(pg,'week','50'),fill(pg,'wunit','mi'),fill(pg,'days','6'),fill(pg,'weeks','8'),fill(pg,'taper','14')]))
    out.append(('hybrid-load-planner','defaults',lambda pg:None))
    out.append(('hybrid-load-planner','equal weight',lambda pg:[fill(pg,'cw','1')]))
    out.append(('hybrid-load-planner','weight 0',lambda pg:[fill(pg,'cw','0')]))
    out.append(('hybrid-load-planner','no lifting',lambda pg:[pg.click('[data-rm="0,0"]'),pg.click('[data-rm="3,0"]')]))
    out.append(('hybrid-load-planner','squat plus deadlift pooled',lambda pg:[pg.click('[data-rm="3,0"]'),pg.click('[data-rm="0,0"]'),pg.click('[data-add="1"]'),pg.click('[data-add="1"]'),pg.fill('[data-s="1,0"]','1'),pg.fill('[data-r="1,0"]','0'),pg.fill('[data-s="1,1"]','1'),pg.fill('[data-r="1,1"]','0')]))
    out.append(('hybrid-load-planner','curls and leg curls',lambda pg:[pg.click('[data-add="2"]'),pg.select_option('[data-t="2,0"]','ui'),pg.fill('[data-r="2,0"]','3'),pg.click('[data-add="2"]'),pg.select_option('[data-t="2,1"]','li'),pg.fill('[data-r="2,1"]','2')]))
    out.append(('hybrid-load-planner','ctl 70 atl 80 12 weeks',lambda pg:[fill(pg,'ctl','70'),fill(pg,'atl','80'),fill(pg,'wk','12')]))
    out.append(('hybrid-load-planner','bad weight',lambda pg:[fill(pg,'cw','2')]))
    out.append(('hybrid-load-planner','bad sets',lambda pg:[pg.fill('[data-s="0,0"]','0')]))
    out.append(('lifting-programme-planner','defaults',lambda pg:None))
    out.append(('lifting-programme-planner','fighter',lambda pg:[pg.select_option('#prog','fighter')]))
    out.append(('lifting-programme-planner','zulu',lambda pg:[pg.select_option('#prog','zulu')]))
    out.append(('lifting-programme-planner','bulgarian high-rep',lambda pg:[pg.click('#add'),pg.select_option('#lifts > section:nth-of-type(4) select[data-f=lift]','bss')]))
    for pr in ['rbeg','gzclp','w531','ppl6','dbs','dbppl','nsuns4','nsuns5','nsuns6d','nsuns6s']:
        out.append(('lifting-programme-planner','other '+pr,lambda pg,pr=pr:[pg.select_option('#prog',pr)]))
    out.append(('lifting-programme-planner','other w531 12 weeks 1.25',lambda pg:[pg.select_option('#prog','w531'),pg.select_option('[data-o=weeks]','12'),pg.select_option('[data-o=step]','1.25')]))
    out.append(('lifting-programme-planner','other rbeg 12 weeks',lambda pg:[pg.select_option('#prog','rbeg'),pg.select_option('[data-o=weeks]','12')]))
    out.append(('lifting-programme-planner','other back to operator',lambda pg:[pg.select_option('#prog','gzclp'),pg.select_option('#prog','operator')]))
    out.append(('lift-scheme-calculator','incline dumbbell bench',lambda pg:[pg.select_option('#lift','incdb')]))
    out.append(('lift-scheme-calculator','bulgarian split squat',lambda pg:[pg.select_option('#lift','bss')]))
    for page in ['run-tss-calculator','run-tss-planner']:
        out.append((page,'race mode',lambda pg:[fill(pg,'mode','race'),fill(pg,'thr','3:58'),fill(pg,'dist','5'),fill(pg,'time','18:54'),fill(pg,'wmin','30'),fill(pg,'wpace','4:00'),fill(pg,'target','60'),fill(pg,'emin','20'),fill(pg,'epace','5:00')]))
    out.append(('classic-session-generator','ladder fixed jog tail 3',lambda pg:[fill(pg,'dist','5'),fill(pg,'time','18:45'),fill(pg,'workout','ladder'),fill(pg,'opt_jogmode','fixed'),fill(pg,'opt_tail','3')]))
    out.append(('classic-session-generator','ladder half jog tail 3',lambda pg:[fill(pg,'dist','5'),fill(pg,'time','18:45'),fill(pg,'workout','ladder'),fill(pg,'opt_tail','3')]))
    out.append(('classic-session-generator','ladder up half jog',lambda pg:[fill(pg,'dist','5'),fill(pg,'time','18:45'),fill(pg,'workout','ladder'),fill(pg,'opt_order','up'),fill(pg,'opt_tail','2')]))
    out.append(('classic-session-generator','pre 20 pairs',lambda pg:[fill(pg,'dist','5'),fill(pg,'time','18:45'),fill(pg,'workout','pre'),fill(pg,'opt_pairs','20')]))
    out.append(('classic-session-generator','pre bad pairs',lambda pg:[fill(pg,'dist','5'),fill(pg,'time','18:45'),fill(pg,'workout','pre'),fill(pg,'opt_pairs','2')]))
    out.append(('hard-workout-predictor','aussie 8 x 1:29',lambda pg:[fill(pg,'mode','aussie'),fill(pg,'splits','1:29, 1:29, 1:28, 1:29, 1:30, 1:29, 1:30, 1:29'),fill(pg,'float','52, 51, 52, 52, 52, 51, 52, 52')]))
    out.append(('hard-workout-predictor','aussie avg jog floats',lambda pg:[fill(pg,'mode','aussie'),fill(pg,'splits','1:29'),fill(pg,'float','75')]))
    out.append(('hard-workout-predictor','aussie 6 times error',lambda pg:[fill(pg,'mode','aussie'),fill(pg,'splits','1:29, 1:29, 1:28, 1:29, 1:30, 1:29'),fill(pg,'float','52')]))
    out.append(('hard-workout-predictor','aussie no float',lambda pg:[fill(pg,'mode','aussie'),fill(pg,'splits','1:29')]))
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
    out.append(('copeland-base','defaults',lambda pg:None))
    out.append(('copeland-base','18:45 ctl 40',lambda pg:[fill(pg,'dist','5'),fill(pg,'time','18:45'),fill(pg,'ctl','40')]))
    out.append(('copeland-base','18:45 ctl 30 km week 5',lambda pg:[fill(pg,'dist','5'),fill(pg,'time','18:45'),fill(pg,'ctl','30'),fill(pg,'wunit','km'),fill(pg,'wk','5')]))
    out.append(('copeland-base','18:45 ctl 20 minimum',lambda pg:[fill(pg,'dist','5'),fill(pg,'time','18:45'),fill(pg,'ctl','20')]))
    out.append(('copeland-base','18:45 ctl 55 ramp 1.5',lambda pg:[fill(pg,'dist','5'),fill(pg,'time','18:45'),fill(pg,'ctl','55'),fill(pg,'ramp','1.5')]))
    out.append(('copeland-base','18:45 ctl 70 plan only',lambda pg:[fill(pg,'dist','5'),fill(pg,'time','18:45'),fill(pg,'ctl','70')]))
    out.append(('copeland-base','39:10 10k ctl 45 plan week',lambda pg:[fill(pg,'dist','10'),fill(pg,'time','39:10'),fill(pg,'ctl','45'),fill(pg,'wk','99')]))
    out.append(('copeland-base','6 days ctl 45',lambda pg:[fill(pg,'dist','5'),fill(pg,'time','18:45'),fill(pg,'ctl','45'),fill(pg,'days','6')]))
    out.append(('copeland-base','6 days ctl 30 week 3',lambda pg:[fill(pg,'dist','5'),fill(pg,'time','18:45'),fill(pg,'ctl','30'),fill(pg,'days','6'),fill(pg,'wk','3')]))
    out.append(('copeland-base','easy 60 buffer 3',lambda pg:[fill(pg,'dist','5'),fill(pg,'time','18:45'),fill(pg,'ctl','40'),fill(pg,'ezp','60'),fill(pg,'sbf','3')]))
    out.append(('copeland-base','bad easy pct',lambda pg:[fill(pg,'ezp','40')]))
    out.append(('plan-builder','easy 60 buffer 3',lambda pg:[fill(pg,'dist','5'),fill(pg,'time','18:45'),fill(pg,'week','40'),fill(pg,'wunit','mi'),fill(pg,'ctl','40'),fill(pg,'ezp','60'),fill(pg,'sbf','3')]))
    out.append(('plan-builder','bad buffer',lambda pg:[fill(pg,'dist','5'),fill(pg,'time','18:45'),fill(pg,'week','40'),fill(pg,'wunit','mi'),fill(pg,'ctl','40'),fill(pg,'sbf','20')]))
    out.append(('marathon-plans','copeland easy 60 buffer 3',lambda pg:[fill(pg,'author','copeland'),fill(pg,'dist','5'),fill(pg,'time','18:45'),fill(pg,'ezp','60'),fill(pg,'sbf','3')]))
    out.append(('marathon-plans','daniels easy 60',lambda pg:[fill(pg,'dist','5'),fill(pg,'time','18:45'),fill(pg,'ezp','60')]))
    out.append(('marathon-plan-recommender','easy 60 buffer 3 ctl 50',lambda pg:[fill(pg,'dist','5'),fill(pg,'time','18:45'),fill(pg,'ctl','50'),fill(pg,'ezp','60'),fill(pg,'sbf','3')]))
    out.append(('copeland-base','bad ramp',lambda pg:[fill(pg,'ramp','3')]))
    out.append(('marathon-plan-recommender','chart hansons beginner table',lambda pg:[fill(pg,'dist','10'),fill(pg,'time','38:43'),fill(pg,'ctl','50'),pg.click('#rows tr[data-n="Hansons Beginner"]'),pg.click('#cbtn')]))
    out.append(('marathon-plan-recommender','defaults',lambda pg:None))
    out.append(('marathon-plan-recommender','18:45 ctl 50',lambda pg:[fill(pg,'dist','5'),fill(pg,'time','18:45'),fill(pg,'ctl','50')]))
    out.append(('marathon-plan-recommender','18:45 ctl 70 atl 80',lambda pg:[fill(pg,'dist','5'),fill(pg,'time','18:45'),fill(pg,'ctl','70'),fill(pg,'atl','80')]))
    out.append(('marathon-plan-recommender','39:10 10k ctl 35 floor -30',lambda pg:[fill(pg,'dist','10'),fill(pg,'time','39:10'),fill(pg,'ctl','35'),fill(pg,'floor','-30')]))
    out.append(('marathon-plan-recommender','38:43 10k ctl 50',lambda pg:[fill(pg,'dist','10'),fill(pg,'time','38:43'),fill(pg,'ctl','50')]))
    out.append(('marathon-plan-recommender','38:43 10k ctl 50 join 0',lambda pg:[fill(pg,'dist','10'),fill(pg,'time','38:43'),fill(pg,'ctl','50'),fill(pg,'join','0')]))
    out.append(('marathon-plan-recommender','estimate 8 h 9 h 25%',lambda pg:[fill(pg,'dist','10'),fill(pg,'time','38:30'),fill(pg,'eh','8'),fill(pg,'el','9:00'),fill(pg,'emix','25')]))
    out.append(('marathon-plan-recommender','estimate easy 5:15/km',lambda pg:[fill(pg,'dist','10'),fill(pg,'time','38:30'),fill(pg,'eh','8'),fill(pg,'ep','5:15')]))
    out.append(('marathon-plan-recommender','estimate easy bad pace',lambda pg:[fill(pg,'eh','8'),fill(pg,'ep','x')]))
    out.append(('marathon-plan-recommender','estimate bad share',lambda pg:[fill(pg,'eh','8'),fill(pg,'emix','70')]))
    out.append(('marathon-plan-recommender','estimate bad hours',lambda pg:[fill(pg,'eh','50')]))
    out.append(('marathon-plan-recommender','bad floor',lambda pg:[fill(pg,'floor','5')]))
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
