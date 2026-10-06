# Notion XEO / SEO research synthesis

Read-only synthesis of existing Notion pages fetched on 2026-10-06. No Notion
pages, databases, comments, or verification states were changed.

## Source pages

| Page | Contribution | Confidence |
|---|---|---|
| [AVATARARTS XEO Operations Manual](https://app.notion.com/p/c45a378e33144a44883543a4199b5f6d) | Canonical operating vocabulary, proof vault, publishing cadence, domain routing | Fetched source |
| [AI Gallery SEO/Search Spec](https://app.notion.com/p/bd12f6ba3e7242e78fe2051dc1c36e6a) | Manifest, item pages, collections, facets, sitemaps, JSON-LD | Fetched source |
| [AI Automation Alchemist blueprint](https://app.notion.com/p/87b42735bc8241da91e69feebb1fb55e) | Asset-to-offer mapping and automation inventory context | Fetched source |
| [Suno Profile Optimization](https://app.notion.com/p/2f836221d8b28122a4a6e83d43264ffa) | Music discovery, keyword experiments, cross-domain routing | Fetched source |
| [Content Enhancement Audit](https://app.notion.com/p/2f836221d8b281a8b398c0f2cf39d603) | Known content, catalog, cross-linking, and migration gaps | Fetched source |
| [AI Directory Quick Start](https://app.notion.com/p/2d336221d8b281d1b42fdca2d587d069) | Directory-submission strategy for the three brands | Fetched source; costs/traffic require recheck |

Search results for exact acronyms were keyword matches and were not treated as
proof of a formal Notion taxonomy. Growth percentages and traffic claims in the
source pages remain hypotheses until independently rechecked against a current
first-party or platform source.

## Reconciled operating model

The XEO manual is the best organizing layer. For Etsy-evolve, the layers become
quality gates rather than promises about how a search engine ranks:

1. **SEO** — product-first title, relevant tags, useful description, metadata.
2. **AEO** — answer buyer questions directly: files, size, use, delivery, limits.
3. **GEO** — publish source-backed explanations and demonstrations that can be
   understood and cited; never promise an AI citation.
4. **REO** — earn recommendations through useful products, proof, and honest
   community participation; no automated promotional replies.
5. **DEO** — make thumbnails, cards, pages, and video readable across devices.
6. **EEO** — reduce confusion and friction with clear navigation, previews, and
   accurate download expectations.
7. **PEO** — use owned manifests, email/lead magnets, and first-party analytics
   where appropriate.
8. **LEO** — rights, trademark, privacy, disclosure, and platform compliance.
9. **OEO** — evidence ledger: source, date, scope, confidence, reviewer, result.
10. **KEO/TKEO** — use motion and freshness only when they improve the product
    explanation; do not manufacture publishing volume.

## What this adds to Etsy-evolve

### 1. One canonical product manifest

The Gallery SEO/Search Spec recommends a generated manifest rather than many
unconnected CSVs. The Etsy adaptation should be a normalized audit manifest,
not a replacement for MyDesigns exports:

```json
{
  "id": "stable-hash",
  "product_family": "tumbler-digital",
  "source_path": "absolute-local-path",
  "delivery_files": [],
  "mockup_files": [],
  "video_file": null,
  "title": null,
  "tags": [],
  "description_status": "missing",
  "rights_status": "unknown",
  "marketplace_ready": false,
  "evidence": [],
  "last_checked": "2026-10-06"
}
```

The manifest must be generated from local sources, preserve source paths, and
never silently convert a research reference into a publishable listing.

### 2. Proof vault before promotion

Every product family should have at least one proof record containing:

- input files and source path;
- rendered mockup or before/after image;
- delivery-file inventory;
- dimensions, formats, and size checks;
- rights/provenance note;
- validator output and date;
- the exact listing profile used.

This is the practical bridge between Notion's “proof vault” and the Etsy
repository's draft-only quality-control goal.

### 3. Domain routing

| Surface | Role in this repository |
|---|---|
| AvatarArts | Creative examples, visual/audio work, finished product proof |
| QuantumForgeLabs | Validators, automation architecture, metadata, technical docs |
| IchoTAKU Etsy | Product-facing shop identity and listing destination |
| Etsy-evolve repo | Local preparation, evidence, schemas, and pre-publish QA |

Cross-links should explain the relationship. They should not blur physical POD,
digital downloads, creative experiments, and technical services into one listing.

## Gaps located in Notion

The January content audit identifies these unresolved areas:

- brand taxonomy pages need body content and links;
- discography HTML has placeholder/local paths;
- prompt vault migration is incomplete;
- the music catalog is smaller than the stated archive;
- the n8n workflow arsenal needs cataloging and ROI proof;
- visual assets and music tracks lack complete cross-links;
- keyword fields exist but are not consistently deployed in content.

These are content-system gaps, not reasons to alter Etsy listings blindly. The
first Etsy-relevant fixes are the manifest, proof records, product-family
profiles, and one reviewed draft row.

## Safe execution order

1. Generate the local normalized manifest.
2. Validate one complete tumbler row and one non-tumbler product family.
3. Attach proof and rights status.
4. Render static/indexable product documentation only for approved records.
5. Draft titles/tags/descriptions from verified fields.
6. Review one MyDesigns/Etsy draft manually.
7. Scale only after the draft passes.

## Explicit non-actions

- Do not create another Notion page merely to duplicate this synthesis.
- Do not mark keyword-growth figures as current without a live source.
- Do not use unofficial MyDesigns endpoints or the stored web token.
- Do not auto-post promotional replies into communities.
- Do not treat a directory submission as proof of ranking or sales.
