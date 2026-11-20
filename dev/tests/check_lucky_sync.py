"""Fail if the Random Session Generator's numbers differ from the Classic and Sub-Threshold Session Generators
for the same 5k time, options, warm-up and cool-down (total time, TSS, distance, and the sub-threshold rep range)."""
import os, sys
from playwright.sync_api import sync_playwright
R=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
U=lambda f:'file://'+os.path.join(R,f)
CLASSIC=[('tempo',{'min':20}),('tempo',{'min':45}),('prog',{'blocks':3,'brk':120}),('ladder',{'order':'down','jogmode':'half','jog':90,'tail':0}),('ladder',{'order':'up','jogmode':'half','jog':90,'tail':0}),
 ('aussie',{'start':False}),('aussie',{'start':True}),('imp',{'reps':10}),('pre',{'pairs':12}),('mona',{}),('yasso',{'reps':8}),('rosario',{'reps':5}),
 ('k1',{'reps':6,'rest':105}),('mile',{'reps':4,'rest':135}),('thirty',{'reps':16}),('mplr',{'total':20,'mp':10})]
bad=[]
with sync_playwright() as p:
    b=p.chromium.launch(); pr=b.new_page(); pc=b.new_page(); ps=b.new_page()
    pr.goto(U('random-session-generator.html')); pc.goto(U('classic-session-generator.html')); ps.goto(U('run-session-calculator.html'))
    for t5 in ['16:00','18:54','20:00','24:30']:
        pr.fill('#time',t5)
        pc.select_option('#dist','5'); pc.fill('#time',t5); pc.fill('#week','')
        ps.select_option('#dist','5'); ps.fill('#time',t5); ps.fill('#week',''); ps.select_option('#surface','flat'); ps.fill('#temp',''); ps.fill('#dew','')
        for key,o in CLASSIC:
            pc.select_option('#workout',key)
            for k,v in o.items():
                el=pc.query_selector('#opt_'+k)
                if isinstance(v,bool): el.set_checked(v)
                elif el.evaluate('e=>e.tagName')=='SELECT': el.select_option(v)
                else: el.fill(str(v))
            wu=0 if key=='mplr' else 10
            if key!='mplr': pc.fill('#wu','10'); pc.fill('#cd','10')
            got=pr.evaluate('([k,o,w])=>window.__rsg.classic(k,o,w,w)',[key,{**o,'start':o.get('start',False)} if key=='aussie' else o,wu])
            want={'tss':int(pc.inner_text('#o-tss')),'total':pc.inner_text('#o-time'),'dist':pc.inner_text('#o-dist')}
            if got!=want: bad.append((t5,key,o,got,want))
        ps.select_option('#unit','min'); ps.fill('#wu','10'); ps.fill('#cd','10')
        for m,unit in [(200,'m'),(300,'m'),(400,'m'),(3,'min'),(6,'min'),(8,'min'),(10,'min'),(12,'min'),(15,'min'),(20,'min')]:
            ps.select_option('#unit',unit); ps.fill('#rep',str(m)); ps.fill('#reps','')
            rng=ps.inner_text('#o-reps').replace('–','-')
            lo,hi=[int(x) for x in rng.split('-')] if '-' in rng else (int(rng.split()[0]),)*2
            info=pr.evaluate('([m])=>window.__rsg.subt(m,1,10,10,u)',[m,unit]) if False else pr.evaluate('([m,u])=>window.__rsg.subt(m,1,10,10,u)',[m,unit])
            if (info['rl'],info['rh'])!=(lo,hi): bad.append((t5,'subT range',m,(info['rl'],info['rh']),(lo,hi)))
            for n in sorted({lo,hi,max(1,(lo+hi)//2)}):
                ps.fill('#reps',str(n))
                got=pr.evaluate('([m,n,u])=>window.__rsg.subt(m,n,10,10,u)',[m,n,unit])
                want={'tss':int(ps.inner_text('#o-tss')),'total':ps.inner_text('#o-total')}
                if (got['tss'],got['total'])!=(want['tss'],want['total']): bad.append((t5,'subT',m,n,got,want))
if bad:
    for x in bad[:20]: print(x)
    sys.exit('Random Session Generator differs from the Classic or Sub-Threshold generator in %d cases'%len(bad))
print('random session generator in sync with the two generators')
