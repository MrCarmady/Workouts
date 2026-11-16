"""Fail if the plan code copied into marathon-plan-recommender.html differs from marathon-plans.html, or the code copied into short-plan-finder.html differs from short-plans.html."""
import os, sys
R=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
mp=open(os.path.join(R,'marathon-plans.html')).read()
rc=open(os.path.join(R,'marathon-plan-recommender.html')).read()
a=mp[mp.index('  var U = "mi";'):mp.index('  // ---------- Engine ----------')].rstrip()+'\n'
b=rc[rc.index('/*@@PLANS-BEGIN@@'):rc.index('  /*@@PLANS-END@@*/')]
b=b[b.index('\n')+1:]
if a!=b: sys.exit('Plan code in marathon-plan-recommender.html differs from marathon-plans.html: recopy it.')
print('plan code in sync')
sp=open(os.path.join(R,'short-plans.html')).read()
sf=open(os.path.join(R,'short-plan-finder.html')).read()
a=sp[sp.index('  var U = "km";'):sp.index('  // ---------- Engine ----------')].rstrip()+'\n'
b=sf[sf.index('/*@@PLANS-BEGIN@@'):sf.index('  /*@@PLANS-END@@*/')]
b=b[b.index('\n')+1:]
if a!=b: sys.exit('Plan code in short-plan-finder.html differs from short-plans.html: recopy it.')
print('short plan code in sync')
