# `~/Documents` Markdown and HTML reference audit

Scanned `/Users/steven/Documents` for Markdown and HTML references. Originals were not moved or edited.

## Inventory snapshot

- 6,043 files total with `.md`, `.markdown`, `.html`, or `.htm` extensions.
- 1,609 Markdown files.
- 45 `.markdown` files.
- 4,389 HTML files.

## Highest-value references for Etsy evolution

### Etsy and listing workflows

- `HTML/organized_intelligent/Development_and_Code/etsy-csv-file-analysis-and-recommendations.html`
- `HTML/organized_intelligent/Visual_Arts_and_Design/Optimize_Listings_for_Etsy_1.html`
- `HTML/organized_intelligent/Visual_Arts_and_Design/Etsy_Product_Prompt_Creation.html`
- `Codex/2026-09-10/lets-x20-c/.codex-history/2026-09-10_025639_Create-ichoTaku-Etsy-CSV_01a089f3.md`

These should be treated as historical reference material and compared against the current draft CSV schemas before reuse.

### Tumbler, mug, and mockup references

The organized visual-design archive contains at least 33 tumbler-related files and 8 files explicitly named as mockups. Strong candidates include:

- `HTML/organized_intelligent/Visual_Arts_and_Design/ChatGPT-MyDesigns_PSD_Mockup_Guide.html`
- `HTML/organized_intelligent/Visual_Arts_and_Design/Family_Photo_Tumbler_Sublimation...html`
- `HTML/organized_intelligent/Visual_Arts_and_Design/Inflated_Christmas_Tumbler_Bundle...html`
- `HTML/organized_intelligent/Visual_Arts_and_Design/3D_Lil_Mister_Grinch_Mug...html`
- `HTML/organized_intelligent/Visual_Arts_and_Design/Mugs_Print_on_Demand_Product_Category_MyDesigns...html`
- `HTML/organized_intelligent/Visual_Arts_and_Design/Mega_Mockup_Bundle...html`

Use these to improve mockup roles and product-family separation, not to copy marketplace descriptions or images.

### SEO and trend research

- `HTML/deep-analysis-seo-improvements.html`
- `HTML/organized_intelligent/Business_and_Strategy/professional_seo.html`
- `HTML/organized_intelligent/Business_and_Strategy/top_2_5_analytics_2.html`
- `HTML/organized_intelligent/Visual_Arts_and_Design/Bubblespider_*.html`
- `ObsidianVault/xEo/seo.md`
- `markD/programming/redditVideoGenerator-seoREADME.md`

These are useful as historical strategy inputs. Current claims should remain marked as hypotheses until rechecked against live Etsy or platform evidence.

### Shirt and printable product references

- 14 shirt-related HTML/Markdown references were found.
- 9 journal-related references were found, including digital tarot and junk-journal examples.
- 10 Printify-related references were found, including product matching and ornament workflows.

These support separate listing families for physical apparel, digital shirt artwork, journals, and Printify/POD products.

## Recommended integration

The current `etsy-evolve` setup should use this document tree as a read-only reference layer:

1. Extract reusable field patterns into `PRODUCT_LISTINGS_DRAFT.csv` only after checking the actual asset.
2. Add confirmed aspect-ratio or mockup guidance to `MOCKUP_GUIDES.md`.
3. Keep historical SEO claims separate from current Etsy comparisons.
4. Link each new listing draft to a local source path and a verification gate.
5. Do not bulk-import historical CSV examples without schema validation.

## Search commands for future review

```bash
rg -l -i '(etsy|mydesign|tumbler|mockup|seo|aspect ratio|printify)' \
  /Users/steven/Documents --glob '*.md' --glob '*.html'
```

This audit is a locator and triage layer; it does not declare all 6,043 files relevant to Etsy.
