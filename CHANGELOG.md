# Changelog

All notable changes to Etsy Evolve are recorded here.

## 2026-10-06

### Added

- Added cross-family product listing drafts for tumblers, journals, shirts,
  wall art, and STL products.
- Added a MyDesigns preparation queue with explicit draft-only status,
  personalization controls, mockup slots, and delivery-file fields.
- Added comparable Etsy product research and a product-family comparison matrix.
- Added evidence-weighted Signal Forge SEO scorecards in CSV and JSON formats.
- Added deterministic scorecard/report generation at
  `scripts/build_signal_forge.py`.
- Added asset-location reports for Etsy, DeVonDaTa, Documents, and backup
  libraries.
- Added documentation for listing generation gates, rights checks, dimensions,
  delivery formats, mockup order, and one-draft validation.

### Changed

- Expanded the README into the project documentation map.
- Kept product schemas separate: tumbler digital, journal, shirt digital,
  physical POD, bundle, and STL.
- Kept SEO opportunity scores explicitly separate from bestseller claims.
- Corrected generated CSV output to use repository-safe LF line endings.

### Safety and scope

- No Etsy listings were published.
- No undocumented MyDesigns API or MCP endpoint was called.
- No source assets were moved or copied.
- Prices and quantities in draft CSVs remain planning hypotheses until reviewed.

## Earlier history

- `3feb382` — Evolve Etsy product signals and listing workflow.
- `e2b3296` — Expand Etsy signal atlas and keyword lab.
- `d064ee4` — Add static Etsy research console pages.
- `d7822b0` — Add Stitch design system for research console.
- `52c6dad` — Normalize signal ledger evidence date.
- `a1a7a64` — Add BubbleSpider competitive research ledger.
- `7f1df37` — Add home evidence audit and Etsy posting packs.
- `dda7a59` — Add Notion XEO research and product SEO crosswalk.
