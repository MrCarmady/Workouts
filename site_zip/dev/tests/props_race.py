import os
import re, itertools
from playwright.sync_api import sync_playwright
def secs(s):
    p=[float(x) for x in s.split(':')]; t=0
    for x in p: t=t*60+x
    return t
def rows(pg):
    out=[]
    for tr in pg.query_selector_all('#rows tr'):
        tds=tr.query_selector_all('td'); 
        out.append((tds[0].inner_text().split('\n')[0], secs(tds[1].inner_text().split('\n')[0]), secs(tds[2].inner_text())))
    return out
DN=["1500m","Mile","3km","5km","10km","10 miles","Half marathon","Marathon"]
KM=[1.5,1.609344,3,5,10,16.09344,21.0975,42.195]
fails=[]
def F(m): 
    if len(fails)<40: fails.append(m)
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page()
    pg.goto('file://'+os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+'/race-prediction-calculator.html'); pg.evaluate('localStorage.clear()'); pg.reload()
    def set1(d,t,week='',unit='mi'):
        pg.select_option('#dist2',''); pg.select_option('#dist',str(d)); pg.fill('#time',t); pg.fill('#week',week); pg.select_option('#wunit',unit)
    # candidate times: per-km pace from 3:00 to 6:30 at 5k-ish scaled
    def fmt(sec):
        sec=round(sec); h=sec//3600; m=sec%3600//60; s=sec%60
        return f"{h}:{m:02d}:{s:02d}" if h else f"{m}:{s:02d}"
    n=0
    for d in range(8):
        for pace in (190,215,240,270,300,340):
            t=pace*KM[d]*(KM[d]/5)**0.06
            ts=fmt(t); set1(d,ts)
            if pg.is_visible('#err'): continue
            r=rows(pg); n+=1
            # self reproduction
            if abs(r[d][1]-secs(ts))>1: F(f"self {DN[d]} {ts} -> {r[d][1]}")
            # monotone times with distance
            for i in range(7):
                if r[i+1][1]<=r[i][1]: F(f"time not increasing {DN[d]} {ts} at {DN[i]}")
                if r[i+1][2]<r[i][2]-0.6: F(f"pace not nondecreasing {DN[d]} {ts} at {DN[i]}->{DN[i+1]} {r[i][2]} {r[i+1][2]}")
            # slower input => slower everywhere
            set1(d,fmt(t*1.02)); r2=rows(pg)
            for i in range(8):
                if r2[i][1]<r[i][1]: F(f"not monotone in input {DN[d]} {ts} at {DN[i]}")
            # weekly mileage affects only beyond HM
            set1(d,ts,'25'); r3=rows(pg); set1(d,ts,'90'); r4=rows(pg)
            for i in range(7):
                if d<7 and abs(r3[i][1]-r4[i][1])>1 and i<6: F(f"week changes {DN[i]} for {DN[d]} {ts}")
            if r3[7][1]<r4[7][1]-1: F(f"low mileage marathon faster {DN[d]} {ts}")
            # km vs mi units equal
            set1(d,ts,'80','mi'); a=rows(pg)[7][1]; set1(d,ts,str(80*1.609344),'km'); c=rows(pg)[7][1]
            if abs(a-c)>1: F(f"unit mismatch {DN[d]} {ts}")
    print("single cases",n)
    # blend
    m=0
    for d1,d2 in itertools.permutations(range(8),2):
        for p1,p2 in ((215,225),(215,260),(260,215)):
            t1=fmt(p1*KM[d1]*(KM[d1]/5)**0.06); t2=fmt(p2*KM[d2]*(KM[d2]/5)**0.06)
            set1(d1,t1); r1=rows(pg); set1(d2,t2); r2=rows(pg)
            set1(d1,t1); pg.select_option('#dist2',str(d2)); pg.fill('#time2',t2)
            if pg.is_visible('#err'): continue
            rb=rows(pg); m+=1
            for i in range(8):
                lo=min(r1[i][1],r2[i][1])-1.5; hi=max(r1[i][1],r2[i][1])+1.5
                if not(lo<=rb[i][1]<=hi): F(f"blend outside {DN[d1]} {t1} + {DN[d2]} {t2} at {DN[i]}: {rb[i][1]} not in [{lo},{hi}]")
            if abs(rb[d1][1]-secs(t1))>1.5: F(f"blend loses input1 {DN[d1]} {t1}")
            if abs(rb[d2][1]-secs(t2))>1.5: F(f"blend loses input2 {DN[d2]} {t2}")
            # swapping order gives same result
            set1(d2,t2); pg.select_option('#dist2',str(d1)); pg.fill('#time2',t1); rs=rows(pg)
            for i in range(8):
                if abs(rs[i][1]-rb[i][1])>1.5: F(f"blend order dependent {DN[d1]} {DN[d2]} at {DN[i]}")
    print("blend cases",m)
    print("\n".join(fails) if fails else "no property failures")
