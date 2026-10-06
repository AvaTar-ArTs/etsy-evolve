# Bestseller / hot / rising SEO signal search

Generated from a bounded `rg` + `fzf` pass across `/Users/steven/Pictures/etsy-evolve`, `/Users/steven/Documents`, and `/Users/steven/Pictures/etSy`.

## Search method

Regex families used:

```text
best[ -]?sell | top[ -]?sell | bestseller | hot | rising | trending |
trend | seo | keyword | tag | ranking | high[ -]?demand | popular
```

The pass produced **3,707 candidate files**. The candidate list is preserved at:

`/Users/steven/Pictures/etSy/recon_output/seo_signal_candidates.txt`

## Highest-value local signal sources

### Direct marketplace and listing data

- `/Users/steven/Documents/CsV/EtsyBlackTopListingsNov2024  EtsyBlackTop.csv`
- `/Users/steven/Documents/CsV/EtsyListingsSep2025  EtsyListingsMerge.csv`
- `/Users/steven/Documents/CsV/Etsy_Product_Listings_Database.csv`
- `/Users/steven/Documents/CsV/printify_bestsellers_updated.csv`
- `/Users/steven/Documents/CsV/market_trends_merged.csv`
- `/Users/steven/Documents/CsV/market_trends_merged_dedup.csv`
- `/Users/steven/Documents/CsV/Merged_Trends__preview_.csv`

These are the first files to inspect for measurable product, listing, or trend fields. They should be validated for date, source, duplicate rows, and whether “bestseller” is a label or measured sales evidence.

### Existing trend and SEO packs

- `/Users/steven/Pictures/etSy/top-trend-seo-packs/back_to_school_2025/`
- `/Users/steven/Pictures/etSy/top-trend-seo-packs/chateaucore_castlecore/`
- `/Users/steven/Pictures/etSy/top-trend-seo-packs/cherry_coded/`
- `/Users/steven/Pictures/etSy/top-trend-seo-packs/halloween_2025/`
- `/Users/steven/Pictures/etsy-evolve/docs/KEYWORD_POSTING_MATRIX.csv`
- `/Users/steven/Pictures/etsy-evolve/docs/POD_SIGNAL_LEDGER_TEMPLATE.csv`

These are ready to feed into the draft listing workflow, but should remain hypotheses until matched to an actual product asset and current marketplace evidence.

### Research and strategy references

- BubbleSpider HTML/Markdown captures under `~/Documents/HTML/organized_intelligent/`.
- `bestseller-trending-products-data-format*.html` and `bestseller-val-tiktok.html`.
- `trending_seo_keywords_2024_2025.html`.
- `deep-analysis-seo-improvements.html`.
- `etsy-csv-file-analysis-and-recommendations.html`.

## Setup recommendation

Use a three-tier signal model:

1. **Observed:** current listing/product data with source and date.
2. **Supported:** repeated marketplace pattern plus matching local assets.
3. **Hypothesis:** trend-pack or historical SEO language not yet rechecked.

Only `Observed` and `Supported` signals should drive a first draft listing. `Hypothesis` signals can generate experiments, not claims of bestseller status.

## Next structured outputs

- Normalize the direct Etsy CSVs into a comparison table.
- Deduplicate trend-pack keywords.
- Join product families to available image aspect ratios and delivery formats.
- Generate a scored draft queue with evidence status, not an automatic publish queue.
