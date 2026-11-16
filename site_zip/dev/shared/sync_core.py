"""Copy shared/core.js into every page between the CORE markers. Run after editing core.js."""
import re, glob, os, sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
core=open(os.path.join(ROOT,'shared','core.js')).read().rstrip('\n')
pat=re.compile(r'[ \t]*/\*@@CORE-BEGIN@@.*?/\*@@CORE-END@@\*/',re.S)
n=0; stale=[]
CHECK="--check" in sys.argv
for f in sorted(glob.glob(os.path.join(ROOT,'*.html'))):
    s=open(f).read()
    if '@@CORE-BEGIN@@' in s:
        t=pat.sub(lambda m:core,s,count=1)
        if t!=s:
            stale.append(os.path.basename(f))
            if not CHECK: open(f,'w').write(t); print('updated',os.path.basename(f))
        n+=1
print(n,'pages carry the shared block')
if CHECK and stale: print('OUT OF SYNC:',stale); sys.exit(1)
