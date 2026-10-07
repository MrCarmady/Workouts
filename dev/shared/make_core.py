# One-off: assemble shared/core.js from the canonical copies in run-session-calculator.html.
import re
src=open('/home/claude/run-session-calculator.html').read()
def block(name):
    m=re.search(r'function %s\([^)]*\)\s*\{'%name,src); start=m.start()
    # include contiguous comment lines directly above
    lines_before=src[:start].split('\n'); k=len(lines_before)-1; pre=[]
    # lines_before[-1] is the indentation of the function line
    j=k-1
    while j>=0 and lines_before[j].strip().startswith('//'): pre.insert(0,lines_before[j]); j-=1
    i=m.end(); d=1
    while d: c=src[i]; d+=(c=='{')-(c=='}'); i+=1
    return '\n'.join(pre+[ '  '+src[start:i] ]) if pre else '  '+src[start:i]
out=['  /*@@CORE-BEGIN@@ Shared code. Edit shared/core.js and run sync_core.py; do not edit between these markers. */',
'  var K = 1.06, HM = 21.0975, MAR = 42.195, MILE = 1.609344;']
for n in ['adj']: out.append(block(n))
out.append('  var offM = 5;   // marathon slow-down in s/km, set per page from the weekly distance')
for n in ['off','marathonExtraMin','marathonOff','parseTime','mmss','hmmss','vdot']: out.append(block(n))
out.append('  /*@@CORE-END@@*/')
open('/home/claude/shared/core.js','w').write('\n'.join(out)+'\n')
