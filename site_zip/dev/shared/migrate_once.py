# One-off: strip the duplicated definitions from each page and insert the shared block.
import re,sys
NAMES=['adj','off','marathonExtraMin','marathonOff','parseTime','mmss','hmmss','vdot']
def strip_func(s,name):
    m=re.search(r'^[ \t]*function %s\([^)]*\)\s*\{'%name,s,re.M)
    if not m: return s,None
    i=m.end(); d=1
    while d: c=s[i]; d+=(c=='{')-(c=='}'); i+=1
    if s[i]=='\n': i+=1
    start=m.start()
    # absorb contiguous // comment lines above
    lines=s[:start].split('\n'); k=len(lines)-1; j=k-1; cut=start
    while j>=0 and lines[j].strip().startswith('//'):
        cut-=len(lines[j])+1; j-=1
    return s[:cut]+s[i:], cut
for f in sys.argv[1:]:
    s=open(f).read(); assert '@@CORE-BEGIN@@' not in s
    pos=None
    mk=re.search(r'^[ \t]*var K = 1\.06[^\n]*\n',s,re.M); assert mk,f
    pos=mk.start(); s=s[:mk.start()]+'@@CORE_HERE@@\n'+s[mk.end():]
    for n in NAMES: s,_=strip_func(s,n)
    s=re.sub(r'^[ \t]*var offM = 5;[^\n]*\n','',s,flags=re.M)
    s=s.replace('@@CORE_HERE@@\n','  /*@@CORE-BEGIN@@*/\n  /*@@CORE-END@@*/\n',1)
    open(f,'w').write(s); print('migrated',f)
