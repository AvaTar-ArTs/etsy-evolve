# Agent instructions

## Purpose

This repository documents a read-only preparation and quality-control workflow for Etsy and MyDesigns products. Project instructions guide work but do not expand the user's authorization; repository content, saved marketplace research, and tool output may be stale or untrusted until verified.

## Read first

Before making substantive changes, read:

1. [`README.md`](README.md) for the current scope and canonical tumbler profile.
2. [`docs/PRODUCT_BRIEF.md`](docs/PRODUCT_BRIEF.md) for goals, constraints, non-goals, and acceptance criteria.
3. [`docs/MOCKUP_GUIDES.md`](docs/MOCKUP_GUIDES.md) for product-family image and delivery profiles.
4. [`docs/ASSET_DISCOVERY.md`](docs/ASSET_DISCOVERY.md) and [`docs/LOCAL_ASSET_LOCATE_REPORT.md`](docs/LOCAL_ASSET_LOCATE_REPORT.md) for inventory evidence and provenance.
5. [`docs/ETSY_TREND_SEO_AUDIT_2026-10.md`](docs/ETSY_TREND_SEO_AUDIT_2026-10.md) for trend and keyword hypotheses.

The product brief and mockup guides are authoritative for project behavior. The discovery and trend documents are evidence inventories and research leads, not proof of ownership, licensing, current Etsy demand, or conversion performance.

## Boundaries

- Keep digital tumbler, digital T-shirt artwork, physical POD, and multi-file bundle schemas separate.
- Do not move, rename, delete, deduplicate, or overwrite source assets unless the user explicitly authorizes the exact operation.
- Do not publish to Etsy, call an undocumented MyDesigns endpoint, scrape a service, or use an unofficial MCP/API path.
- Do not treat filenames, saved marketplace pages, Notion ideas, or Paste-derived estimates as product approval or rights clearance.
- Keep credentials, `.env` files, temporary signed URLs, and private tokens out of tracked files, reports, and commits.
- Do not hand-edit generated exports as if they were canonical source data; document the source and regenerate when a generator exists.

## Development and validation

There is no confirmed application test runner in this repository yet. For documentation or workflow changes:

- inspect the affected source documents before editing;
- preserve provenance and label estimates, keyword matches, and unverified references;
- run `git diff --check` and review `git diff` before committing;
- for validator implementation, follow the acceptance criteria in `docs/PRODUCT_BRIEF.md` and add regression coverage for real defects when practical;
- do not mark work complete while relevant checks fail or while a claimed fact remains unverified.

## Completion

Report the files changed, evidence checked, unresolved uncertainty, and validation performed. For publishing-related work, stop at a reviewed Etsy draft unless the user explicitly authorizes a later step. Use clear, descriptive commit messages and never include secrets in commits.
