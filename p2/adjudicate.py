"""Mechanical adjudication worksheet per rubric v14 s9 order of operations.
Reads lane-ektar/*.json and lane-grok/*.json (parsed sheets), then:
 (1) lists both lanes' raw cells,
 (2) D1 flag merge: union; single-lane flags are listed for manual
     re-examination (determinations fed back via determinations.json:
     {"<slug>": {"dropped_flags": [...], "cell_overrides": {"D2": value-or-"UNVERIFIED", ...},
                 "range_cells": {"D3": [lo, hi], ...}}}),
 (3) gate binding of lane values against the merged (post-drop) flag set,
 (4) per-cell point adjudication: |d|<=1 -> mean; |d|>1 -> NEEDS-REEXAM;
     UNVERIFIED-vs-number -> NEEDS-REEXAM,
 (5) UNVERIFIED propagation from adjudicated D1 to D2/D3 values in [2,3],
 (6) ordinal sum (UNVERIFIED=0, range=lower bound, mean as-is).
D5 adjudicated for display only (reported, not ranked).
Outputs adjudication-worksheet.json; unresolved cells stay marked until
determinations are supplied and the script is re-run."""
import json, os, sys

P2 = os.path.dirname(os.path.abspath(__file__))
SLUGS = ['langchain','deer-flow','hermes-agent','autogpt','metagpt','deepseek-harness',
         'gemini-cli','openhands','ruflo','openclaw']
DIMS = ['D1','D2','D3','D4','D5']

def load(lane_dir, slug):
    return json.load(open(os.path.join(P2, lane_dir, slug + '.json')))

det = {}
if os.path.exists(os.path.join(P2, 'determinations.json')):
    det = json.load(open(os.path.join(P2, 'determinations.json')))

out = {}
for slug in SLUGS:
    a = load('lane-ektar', slug)['dimensions']
    b = load('lane-grok', slug)['dimensions']
    d = det.get(slug, {})
    # --- step 2: flag merge
    fa = set(a['D1'].get('flag_set', []))
    fb = set(b['D1'].get('flag_set', []))
    union = fa | fb
    dropped = set(d.get('dropped_flags', []))
    merged_flags = sorted(union - dropped)
    single_lane_flags = sorted(union - (fa & fb))
    # --- gate binding on each lane's values
    def bind(lane_dims):
        v = {k: lane_dims[k]['score'] for k in DIMS}
        if merged_flags:  # any standing loss flag
            if isinstance(v['D1'], (int, float)) and v['D1'] >= 2:
                v['D1'] = 1
        if 'set_loss' in merged_flags:
            for k in ('D2', 'D3'):
                if isinstance(v[k], (int, float)) and v[k] >= 2:
                    v[k] = 0
        return v
    va, vb = bind(a), bind(b)
    # --- step 3: point adjudication
    cells = {}
    for k in DIMS:
        x, y = va[k], vb[k]
        override = d.get('cell_overrides', {}).get(k)
        rng = d.get('range_cells', {}).get(k)
        if override is not None:
            cells[k] = {'value': override, 'how': 're-examination override'}
        elif rng is not None:
            cells[k] = {'value': rng[0], 'range': rng, 'how': 'unresolved >1 disagreement -> range at lower bound'}
        elif x == 'UNVERIFIED' and y == 'UNVERIFIED':
            cells[k] = {'value': 'UNVERIFIED', 'how': 'both lanes UNVERIFIED'}
        elif x == 'UNVERIFIED' or y == 'UNVERIFIED':
            cells[k] = {'value': 'NEEDS-REEXAM', 'lanes': [x, y], 'how': 'UNVERIFIED vs number'}
        elif abs(x - y) <= 1:
            cells[k] = {'value': (x + y) / 2, 'lanes': [x, y], 'how': 'mean of <=1 disagreement'}
        else:
            cells[k] = {'value': 'NEEDS-REEXAM', 'lanes': [x, y], 'how': '>1 disagreement'}
    # --- step 4: UNVERIFIED propagation
    if cells['D1']['value'] == 'UNVERIFIED':
        for k in ('D2', 'D3'):
            v = cells[k].get('value')
            if isinstance(v, (int, float)) and v >= 2:
                cells[k] = {'value': 'UNVERIFIED', 'how': 's2 UNVERIFIED-propagation from D1'}
            elif 'range' in cells[k] and cells[k]['range'][1] >= 2:
                cells[k] = {'value': 'UNVERIFIED', 'how': 's2 UNVERIFIED-propagation (range touched [2,3])'}
    # --- step 5: ordinal
    total = 0
    for k in ('D1', 'D2', 'D3', 'D4'):
        v = cells[k]['value']
        if isinstance(v, (int, float)):
            total += v
    out[slug] = {'merged_flags': merged_flags, 'single_lane_flags': single_lane_flags,
                 'lane_a_bound': va, 'lane_b_bound': vb, 'cells': cells,
                 'ordinal_total': total,
                 'unresolved': [k for k in DIMS if cells[k]['value'] == 'NEEDS-REEXAM']}
json.dump(out, open(os.path.join(P2, 'adjudication-worksheet.json'), 'w'), indent=2)
for slug, r in out.items():
    print(f"{slug:18s} flags={r['merged_flags']} total={r['ordinal_total']} unresolved={r['unresolved']}")
print('worksheet written')
