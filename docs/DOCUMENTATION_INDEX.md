# Documentation Index

This index maps the repository artifacts to their job in the Etsy preparation
workflow. The repository is a local research, preparation, and quality-control
layer; it is not an Etsy publishing bot.

## Start here

- `README.md` — project purpose, canonical tumbler layout, and links.
- `PRODUCT_BRIEF.md` — product scope and operating boundaries.
- `PRODUCT_LISTING_GENERATION_NOTES.md` — required review gates before upload.
- `CHANGELOG.md` — dated project changes and safety boundaries.

## Asset and source discovery

- `ASSET_DISCOVERY.md` — primary local asset locations.
- `LOCAL_ASSET_LOCATE_REPORT.md` — broader home and volume locate results.
- `LOCAL_FINDINGS_INDEX.csv` — machine-readable local findings index.
- `DEVONDATA_ASSET_LOCATE.md` — DeVonDaTa source and mockup roots.
- `DOCUMENTS_REFERENCE_AUDIT.md` — Markdown/HTML references under Documents.
- `HOME_EXAMPLES_AUDIT.md` — examples found under the home/Pictures ecosystem.
- `HTML_REFERENCE_REVIEW.md` — HTML reference review.

## Product and mockup preparation

- `MOCKUP_GUIDES.md` — product-family mockup layouts.
- `ETSY_POSTING_PACKS.md` — reusable posting structures.
- `PRODUCT_LISTINGS_DRAFT.csv` — cross-family listing drafts.
- `MYDESIGNS_DRAFT_QUEUE.csv` — MyDesigns preparation queue.
- `ETSY_COMPARISON_MATRIX.csv` — product-family comparison matrix.
- `ETSY_COMPETITIVE_COMPARE_2026-10.md` — observable Etsy examples and
  implementation rules.
- `PRODUCT_SEO_CROSSWALK.md` — product-to-keyword-to-asset mapping.

## SEO, trend, and competitive research

- `ETSY_TREND_SEO_AUDIT_2026-10.md` — trend and SEO audit.
- `KEYWORD_POSTING_MATRIX.csv` — keyword and posting matrix.
- `POD_SIGNAL_LEDGER_TEMPLATE.csv` — reusable signal-capture schema.
- `SEO_SIGNAL_SEARCH_REPORT.md` — local `rg`/`fzf` candidate-search method.
- `SEO_SIGNAL_FORGE_REPORT.md` — ranked evidence-weighted opportunities.
- `SEO_SIGNAL_SCORECARD.csv` — spreadsheet-ready scorecard.
- `SEO_SIGNAL_SCORECARD.json` — machine-readable scorecard.
- `BUBBLESPIDER_COMPETITIVE_AUDIT.md` — competitor capability comparison.
- `PASTE_XEO_SEO_RESEARCH.md` — Paste/XEO research synthesis.
- `NOTION_XEO_RESEARCH.md` — Notion/XEO research synthesis.

## Design and presentation

- `DESIGN.md` — Stitch-inspired design system for the research console.
- `ICHOTAKU_LAUNCH_FILM_TREATMENT.md` — launch-film creative treatment.
- `site/` — static research-console pages.

## Reproducible generation

```bash
python3 scripts/build_signal_forge.py
```

The generator updates the Signal Forge CSV, JSON, and Markdown report. Review
the resulting diff before committing.

## Evidence-first evolution gate

- `.cursor/hooks.json` — project hook configuration for the creation gate.
- `.cursor/hooks/evidence-first-evolver.sh` — prompts a host agent to inspect
  existing capability before creating new machinery.
- `.cursor/agents/evidence-first-evolver.md` — reusable reasoning contract for
  locate → comprehend → reuse/adapt/create → verify.

The files are configured in this repository; host-level hook activation still
requires verification in the editor's Hooks output/settings surface.

## Publication boundary

Every product row remains `draft_review` or `prepare_only` until its local
delivery files, rights, dimensions, formats, mockups, title, tags, price, and
digital/physical status are verified. The first live operation should be one
manually reviewed Etsy draft, never a blind bulk publish.
