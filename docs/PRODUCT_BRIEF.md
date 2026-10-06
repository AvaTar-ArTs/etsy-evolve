# Product brief

## Goal

Turn scattered Etsy and MyDesigns assets into a dependable, reviewable listing-preparation workflow for digital 20 oz tumbler wraps and, later, digital T-shirt designs.

## Users

- Shop owner preparing listings in batches.
- Reviewer checking that a listing is safe before it becomes an Etsy draft.

## First release scope

The first release is a local, read-only audit layer that accepts a prepared listing row and reports:

- missing or mismatched delivery files;
- missing straight/tapered variants;
- wrong-product mockups;
- missing digital-download language;
- missing title, tags, price, or description;
- missing or invalid listing video metadata;
- schema mismatches between the 10-mockup tumbler profile and the 5-mockup bundle template.

## Confirmed constraints

- Ordinary tumbler wraps should have personalization disabled.
- Etsy digital delivery supports five files of up to 20 MB each; larger bundles need an intentional ZIP/PDF delivery design.
- A single tumbler listing uses the proof-first image sequence documented in the README.
- The local 360-degree MP4 is a listing asset, not a thumbnail or delivery file.
- No undocumented API, scraping path, or automatic publishing is part of this release.

## Non-goals

- Publishing directly to Etsy.
- Calling an unofficial MyDesigns API or MCP endpoint.
- Moving, renaming, or deduplicating the design library.
- Automatically deciding whether artwork is commercially licensed.
- Treating marketplace examples as proof of conversion performance.

## Acceptance criteria

1. A validator can inspect one row without modifying source files.
2. Every finding identifies its row, field, and severity.
3. A clean row reports the exact evidence checked.
4. A failed row cannot be treated as bulk-ready.
5. Tests cover a valid row, missing delivery files, wrong mockup product, and missing disclaimer.

## Planned milestones

1. Define a normalized row model and fixture data.
2. Implement read-only validation rules.
3. Add CSV adapters for the tumbler and Digital Bundles schemas.
4. Add rendered-image and video metadata checks.
5. Generate a human-readable audit report.
6. Validate one real candidate row, then decide whether bulk preparation is safe.

