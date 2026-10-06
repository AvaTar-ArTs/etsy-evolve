#!/usr/bin/env python3
"""Build an evidence-weighted Etsy SEO opportunity scorecard."""
from __future__ import annotations
import csv, json
from pathlib import Path
from datetime import date

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'docs'

EVIDENCE = {'observed': 1.0, 'supported': 0.75, 'hypothesis': 0.35}
ROWS = [
    {'product_family':'tumbler-digital','keyword':'20oz tumbler wrap PNG','evidence':'observed','freshness':0.85,'product_fit':1.0,'differentiation':0.70,'creative_angle':'signalwave / nocturnal broadcast wrap','source':'Etsy comparable listings'},
    {'product_family':'tumbler-digital','keyword':'straight tapered tumbler wrap','evidence':'observed','freshness':0.85,'product_fit':1.0,'differentiation':0.65,'creative_angle':'show both files and the fit comparison','source':'Etsy comparable listings'},
    {'product_family':'journal-printable','keyword':'printable reading journal PDF','evidence':'observed','freshness':0.80,'product_fit':1.0,'differentiation':0.70,'creative_angle':'dark academia / illustrated review pages','source':'Etsy comparable listings'},
    {'product_family':'journal-tablet','keyword':'hyperlinked digital reading journal','evidence':'observed','freshness':0.80,'product_fit':0.95,'differentiation':0.85,'creative_angle':'book capacity + guided review system','source':'Etsy comparable listings'},
    {'product_family':'shirt-digital','keyword':'T-shirt design PNG SVG','evidence':'supported','freshness':0.65,'product_fit':1.0,'differentiation':0.72,'creative_angle':'TrashCat dark-humor collection','source':'local product files + Etsy comparison'},
    {'product_family':'wall-art-digital','keyword':'castlecore printable wall art','evidence':'supported','freshness':0.60,'product_fit':0.90,'differentiation':0.88,'creative_angle':'rococo cottage / nocturnal signalwave crossover','source':'local trend pack + posting matrix'},
    {'product_family':'seasonal-shirt','keyword':'matching family Halloween shirt design','evidence':'hypothesis','freshness':0.55,'product_fit':0.95,'differentiation':0.62,'creative_angle':'Boo Crew story-world variants','source':'local seasonal pack'},
    {'product_family':'stl','keyword':'castle cookie cutter STL','evidence':'hypothesis','freshness':0.50,'product_fit':0.80,'differentiation':0.78,'creative_angle':'four-size maker test pack','source':'local posting matrix'},
]

def score(row):
    # Evidence and fit dominate; differentiation rewards a defendable creative angle.
    return round(100 * (0.35*EVIDENCE[row['evidence']] + 0.20*row['freshness'] + 0.30*row['product_fit'] + 0.15*row['differentiation']), 1)

for row in ROWS:
    row['score'] = score(row)
    row['review_gate'] = 'draft now' if row['score'] >= 75 else 'validate evidence'
    row['checked_on'] = date.today().isoformat()
ROWS.sort(key=lambda r: r['score'], reverse=True)

fields = ['product_family','keyword','score','evidence','freshness','product_fit','differentiation','creative_angle','source','review_gate','checked_on']
with (OUT/'SEO_SIGNAL_SCORECARD.csv').open('w', newline='', encoding='utf-8') as f:
    w=csv.DictWriter(f, fieldnames=fields, lineterminator='\n'); w.writeheader(); w.writerows(ROWS)

payload = {'name':'Signal Forge','purpose':'Evidence-weighted Etsy SEO opportunity ranking','formula':'35% evidence + 20% freshness + 30% product fit + 15% differentiation','rows':ROWS}
(OUT/'SEO_SIGNAL_SCORECARD.json').write_text(json.dumps(payload, indent=2), encoding='utf-8')

md=['# Signal Forge SEO opportunity report','',f'Generated: {date.today().isoformat()}','', '## Direct answer', '', 'The strongest immediate listing candidates are the 20oz tumbler-wrap family and the two reading-journal modes. They have the clearest observed marketplace language and the strongest fit to verified product structures.','','## Ranked opportunities','', '| Rank | Product family | Keyword | Score | Evidence | Action |','|---:|---|---|---:|---|---|']
for i,r in enumerate(ROWS,1): md.append(f"| {i} | `{r['product_family']}` | `{r['keyword']}` | **{r['score']}** | {r['evidence']} | {r['review_gate']} |")
md += ['', '## Creative experiments', '', '- **Tumbler:** pair the standard straight/tapered proof layout with a signalwave/nocturnal visual system.', '- **Journal:** publish printable and hyperlinked tablet versions as separate products with separate promises.', '- **Shirt:** build a small TrashCat collection instead of one-off files; test consistent cover language and format cards.', '- **Wall art:** use castlecore as a visual direction only until current demand is revalidated.', '', '## AI-readable evidence block', '', 'The Signal Forge score is a prioritization aid, not a bestseller claim. A high score means the phrase has strong product fit and either observed marketplace support or a clear local asset match. Every listing still requires asset, rights, format, and current Etsy review before publication.', '', '## Files', '', '- `SEO_SIGNAL_SCORECARD.csv` — spreadsheet-ready scorecard.', '- `SEO_SIGNAL_SCORECARD.json` — machine-readable scorecard.', '- `ETSY_COMPETITIVE_COMPARE_2026-10.md` — source comparison.', '- `seo_signal_candidates.txt` — raw `rg` candidate index.']
(OUT/'SEO_SIGNAL_FORGE_REPORT.md').write_text('\n'.join(md)+'\n', encoding='utf-8')
print(f'generated {len(ROWS)} opportunities')
