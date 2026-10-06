# BubbleSpider competitive and trend-research audit

Updated: 2026-10-06

## Sources reviewed

- Live public site: <https://bubblespider.com/>
- Live public best-seller page: <https://bubblespider.com/amazon/best-sellers>
- Local SiteSucker mirror:
  `/Volumes/2T-Xx/us.sitesucker.mac.sitesucker-pro/bubblespider.com/`
- User-provided BubbleSpider competitive notes.

The local mirror is historical and contains captured data with dates through
February 2025. It is useful for product-surface analysis, not current market
validation.

## Confirmed product surface

The live homepage positions BubbleSpider as “Intelligent tools & up-to-date
analytics” for print-on-demand sales and links to Amazon Best Sellers. The live
best-seller page describes itself as a small teaser of approximately the top
2,000 Amazon T-shirt best sellers, with a fuller filtered tool planned.

The mirror additionally exposes:

- Amazon Best Sellers navigation;
- Keyword Research navigation;
- BSR, review, rating, category, publication-date, and change indicators;
- historical product snapshots and trend percentages;
- Supabase session/cookie policy references;
- affiliate-style Amazon product links in captured product cards.

The pasted claims about Chrome extensions, Redbubble tag copying, shadow-ban
detection, and tag-spam indicators remain user-provided leads. They should not
be represented as independently confirmed by the captured homepage alone.

## Competitive interpretation

BubbleSpider's observable strength is **market-signal compression**: it puts
best-seller, BSR, reviews, dates, and change signals into a product-research
surface. The valuable idea to borrow is the evidence table, not scraping or
copying competitor tags.

| BubbleSpider signal | Etsy-evolve equivalent |
|---|---|
| BSR / movement | platform-specific demand signal with source date |
| Reviews / rating | competitive moat indicator, not demand proof alone |
| Product date | freshness and lifecycle context |
| Keyword research | local keyword matrix with product-family validation |
| Tag analysis | gap analysis without copying protected or irrelevant terms |
| Trending design | hypothesis requiring asset, rights, and buyer-fit checks |
| Cross-platform view | separate schemas and platform rules, never one universal tag list |

## Safe opportunity for Etsy-evolve

Build a **POD evidence ledger**, not a BubbleSpider scraper. Each signal should
contain:

```text
signal_id
platform
query_or_category
source_url_or_local_path
observed_at
source_last_updated
product_family
signal_type
value
confidence
rights_or_policy_note
next_test
```

Recommended signal types:

- `demand_snapshot`
- `review_moat`
- `freshness`
- `keyword_candidate`
- `visual_pattern`
- `seasonality`
- `policy_risk`

## Trend score for internal prioritization

Use a transparent, non-predictive score only to decide what to inspect next:

```text
priority =
  0.25 * evidence_recency
  + 0.20 * product_fit
  + 0.20 * rights_confidence
  + 0.15 * delivery_readiness
  + 0.10 * keyword_specificity
  + 0.10 * visual_distinctiveness
```

Each component is scored 0–5 by a reviewer. A high score means “inspect/test
first,” not “will sell.” Missing rights or product evidence caps the priority
at 2 regardless of trend signals.

## BubbleSpider-inspired keyword workflow

1. Start with a product-family seed: `20oz tumbler wrap PNG`, `graphic T-shirt`,
   `printable wall art`, `STL 3D printable file`, or `reading journal PDF`.
2. Add one visual/style phrase only when visible: `signalwave`, `castlecore`,
   `cherry red`, `gothic`, `blue bird`.
3. Add one audience/occasion phrase only when true: `music lover`, `Halloween`,
   `book lover`, `teacher`, or `maker`.
4. Remove generic padding and unsupported superlatives.
5. Check product mode: physical, digital, printable, or STL.
6. Record source and date in the keyword matrix.
7. Draft one listing and compare hero/copy variants only after the evidence gate.

## Platform separation

Do not reuse one generated tag list across platforms:

- Etsy requires product-relevant listing language and clear digital/physical
  disclosure.
- Redbubble and Amazon have different title, tag, and backend-search behavior.
- A BubbleSpider-style Amazon BSR signal cannot be treated as an Etsy demand
  measurement.
- A competitor tag is not automatically safe, relevant, or legally usable.

## Explicit exclusions

- No automated tag copying from competitor listings.
- No scraping behind authentication or rate-limit bypasses.
- No “shadow-ban detector” claims without a documented, authorized signal.
- No auto-posting, auto-uploading, or cross-platform scheduling in this repo.
- No political or news-cycle trend listing without a separate rights, safety,
  and policy review.

## Current conclusion

BubbleSpider is a useful competitive reference for how to present marketplace
signals, but the captured evidence does not prove its entire feature list or
current data freshness. Etsy-evolve should differentiate through provenance,
product-family validation, mockup QA, rights checks, and draft review rather
than promising prediction or automated marketplace manipulation.
