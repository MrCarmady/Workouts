"""Fail if the plan code copied into marathon-plan-recommender.html differs from marathon-plans.html."""
import os, sys
R=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
mp=open(os.path.join(R,'marathon-plans.html')).read()
rc=open(os.path.join(R,'marathon-plan-recommender.html')).read()
a=mp[mp.index('  var U = "mi";'):mp.index('  // ---------- Engine ----------')].rstrip()+'\n'
b=rc[rc.index('/*@@PLANS-BEGIN@@'):rc.index('  /*@@PLANS-END@@*/')]
b=b[b.index('\n')+1:]
if a!=b: sys.exit('Plan code in marathon-plan-recommender.html differs from marathon-plans.html: recopy it.')
print('plan code in sync')
