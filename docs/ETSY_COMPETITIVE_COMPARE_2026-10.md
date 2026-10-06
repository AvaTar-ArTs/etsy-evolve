# Etsy comparable-product review

Reviewed October 6, 2026. This is an observable-market comparison, not a claim that any listing is a bestseller. Prices and listing details can change; recheck them before publishing.

## 1. 20oz tumbler wraps

Comparable listings repeatedly make the same promise clear in the first screen: straight and tapered versions, 300 DPI/high-resolution PNGs, approximately 9.3 × 8.2 inches, instant download, no physical tumbler, usage boundaries, and blank-measurement guidance.

Examples:

- [DigitalPearlDesigns](https://www.etsy.com/listing/1541212914/20-oz-skinny-tumbler-sublimation-wrap) — two PNG files plus a PDF link, straight/tapered delivery, and explicit digital-only language.
- [MountainMistDigital](https://www.etsy.com/listing/1682052424/chef-20-oz-skinny-tumbler-wrap) — two PNGs, PDF link, 300 PPI, dimensions, license restriction, and no-physical-product disclosure.
- [TumblerGraphicsHub](https://www.etsy.com/listing/1594699679/flower-line-art-20oz-tumbler-sublimation) — two PNGs, 300 DPI, dimensions, and commercial-use boundary.
- [TheDragonTattoo](https://www.etsy.com/listing/1634513921/travel-tumbler-wrap-wanderlust-20-oz) — straight/tapered files, dimensions, instant delivery, and physical-product-only usage boundary.

Implementation: use `20oz tumbler wrap PNG` as the primary phrase. Put `straight`, `tapered`, `300 DPI`, `9.3 × 8.2`, `instant download`, and `no physical tumbler` in the first description block. Keep the image order: hero tumbler, flat wrap, 180-degree view, straight/tapered comparison, close-up, info card, disclaimer, video.

## 2. Digital reading journals

Comparable listings compete on specificity and utility: page count or book capacity, hyperlinked navigation, compatible apps, printable-versus-tablet distinction, visible file count, and download method.

Examples:

- [MimiandKi](https://www.etsy.com/listing/1298261134/dark-academia-reading-journal-digital) — eight-page printable journal, PDF, goals, reviews, tracker, and no-physical-product language.
- [TheGirlRocksCo](https://www.etsy.com/listing/1467620463/digital-reading-journal-dark-academia) — hyperlinked portrait journal, 60-book tracker, guide, and tablet-app compatibility.
- [Nestlittledoodle](https://www.etsy.com/listing/4542008431/dark-academia-reading-journal-gothic) — 27-page A4 PDF with illustrated spreads and character prompts.
- [StrigoiStudioDE](https://www.etsy.com/listing/4396741700/dark-academia-digital-reading-journal) — large capacity and hyperlinked functionality as the value proposition.

Implementation: split the product into `printable PDF` and `hyperlinked tablet PDF` modes. Do not claim hyperlinked, editable, or app-compatible until the file has been tested. Show cover, legible interior, multi-page overview, dimensions, device/printed example, file inventory, and digital-only card.

## 3. Digital T-shirt designs

Comparable bundles emphasize format breadth, DTF/DTG/sublimation use, and commercial licensing. Large quantity claims appear in the category, but should not be repeated without a verified inventory count.

Example: [ARTLIIndia bundle](https://www.etsy.com/listing/4325960343/100000-t-shirt-design-bundle-png-svg-eps) — PNG/SVG/EPS/PSD positioning, instant download, and commercial-use framing.

Implementation: describe only actual formats and counts in the delivery folder. Use `T-shirt design PNG SVG` when both are delivered. Keep physical shirts separate; never use `instant download` for a shipped garment.

## Cross-product setup rules

1. Assign `product_family` and `listing_type` before generating copy.
2. State exactly what is delivered and what is not shipped.
3. Classify every mockup as hero, proof, detail, information, or lifestyle.
4. Require local verification for DPI, page count, commercial use, and hyperlinks.
5. Use market observations for structure, not copied titles, descriptions, images, or protected terms.

Related artifacts: `PRODUCT_LISTINGS_DRAFT.csv`, `MYDESIGNS_DRAFT_QUEUE.csv`, and `PRODUCT_LISTING_GENERATION_NOTES.md`.
