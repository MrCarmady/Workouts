# Builds parkrun-converter.html from data/parkrun-converter.tpl and data/parkrun-sss.txt. Run after editing either.
import json, os
H = os.path.dirname(os.path.abspath(__file__))
rows = [l.rsplit(' | ', 1) for l in open(f'{H}/data/parkrun-sss.txt', encoding='utf-8').read().splitlines() if l.strip()]
data = json.dumps([[a, float(b)] for a, b in rows], ensure_ascii=False, separators=(',', ':'))
t = open(f'{H}/data/parkrun-converter.tpl', encoding='utf-8').read()
assert t.count('/*@@DATA@@*/') == 1
open(f'{H}/parkrun-converter.html', 'w', encoding='utf-8').write(t.replace('/*@@DATA@@*/', data))
print(len(rows), 'courses')
