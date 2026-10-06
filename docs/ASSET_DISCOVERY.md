# Etsy/product asset discovery

Read-only inventory pass: 2026-10-06.

## Method

- Searched bounded product roots with `rg --files`: `Pictures`, `Downloads`, `Documents`, `Desktop`, and `Movies`.
- Filtered paths with product terms using ripgrep.
- Used `fzf --filter` to narrow the candidate list for review.
- Excluded `.git`, `node_modules`, and cache directories where practical.
- No files were moved, renamed, deleted, or modified by the scan.

The wider home directory contains substantial skill, corpus, cache, and archive noise. Do not treat a filename match as a sellable product or an approved asset.

## Highest-value Etsy data and listing references

```text
/Users/steven/Documents/CsV/etsylisting0mydesign.CSV
/Users/steven/Documents/CsV/etsylisting0mydesign (1).CSV
/Users/steven/Documents/CsV/EtsyListingsDownload.csv
/Users/steven/Documents/CsV/EtsyListingsSep2025  EtsyListingsMerge.csv
/Users/steven/Documents/CsV/Etsy_Product_Listings_Database.csv
/Users/steven/Documents/Codex/2026-09-10/lets-x20-c/outputs/ichotaku-etsy.csv
/Users/steven/Documents/Codex/2026-09-10/dee/outputs/ichotaku-etsy.csv
/Users/steven/Documents/Codex/2026-09-10/dee/outputs/ichotaku-etsy-banner.png
```

These are data/reference sources. Validate headers, dates, ownership, and whether a row is a listing, a research export, or a generated draft before use.

## Product clusters

### Tumbler and mug wraps

The Documents HTML archive contains a large research/reference cluster, including:

- 20 oz stainless-steel tumbler references;
- 12 oz wine tumbler references;
- 250-design 3D tumbler bundles;
- Christmas, Halloween, Valentine, animal, book, and character mug-wrap references;
- MyDesigns black mug, color-changing mug, and mug-category pages.

Useful examples include:

```text
/Users/steven/Documents/HTML/organized_intelligent/Development_and_Code/20_oz_Stainless_Steel_Tumbler_*.html
/Users/steven/Documents/HTML/organized_intelligent/Development_and_Code/250_MEGA_Bundle_3D_Tumblers_Wraps_*.html
/Users/steven/Documents/HTML/organized_intelligent/Development_and_Code/Books_in_Cave_Tumbler_Wrap_*.html
/Users/steven/Documents/HTML/organized_intelligent/Visual_Arts_and_Design/3D_*Mug_Wrap_*.html
```

### T-shirts and apparel

```text
/Users/steven/Documents/CsV/t-shirt-feb.CSV
/Users/steven/Pictures/Best-Trendy-Christmas-TShirt-Bundle-21186978-1/
/Users/steven/Documents/HTML/organized_intelligent/Visual_Arts_and_Design/Christmas_T-Shirt_*.html
/Users/steven/Documents/HTML/organized_intelligent/Visual_Arts_and_Design/*Hoodie*.html
```

The Christmas bundle contains AI/EPS source files and should be treated as a source library, not as a ready-to-publish Etsy catalog. Physical apparel and digital shirt artwork need separate mockup and delivery profiles.

### Books, journals, and planners

```text
/Users/steven/Documents/HTML/organized_intelligent/Development_and_Code/Black_Cat_Reading_Book_*.html
/Users/steven/Documents/HTML/organized_intelligent/Development_and_Code/Digital_Tarot_Journal_for_IPad_Canva_Kdp_*.html
/Users/steven/Pictures/storybook/
/Users/steven/Pictures/ideoGram/jpg/ReadBooks.jpeg
```

The `storybook` tree is potentially important for a book/journal film route, but it needs a separate rights and product-status review before being represented as an Etsy product.

### Stickers and decals

```text
/Users/steven/Documents/HTML/organized_intelligent/Development_and_Code/Halloween_Labels_Halloween_Stickers_*.html
/Users/steven/Documents/HTML/organized_intelligent/Development_and_Code/Kiss-Cut_Sticker_Sheet_Printful_*.html
/Users/steven/Documents/HTML/organized_intelligent/Visual_Arts_and_Design/Cute_Unicorn_Printable_Sticker_PNG_*.html
```

These references support a sticker/label mockup guide, but the local CapCut `upload-sticker` matches are application cache and should be ignored for product planning.

### Posters, prints, and wall art

Poster and print results are mixed with general website/gallery imagery. Keep only files tied to an identified listing or approved artwork set. The generic Leonardo poster mockups remain reference assets, not IchoTAKU product proof.

## IchoTAKU brand assets

```text
/Users/steven/Pictures/IchoTaku.png
/Users/steven/Pictures/IchoTakuBird.png
/Users/steven/Pictures/IchoTakuRadio.png
/Users/steven/Pictures/IchoTAKU-*.png
/Users/steven/Downloads/IchoTakuArt-*.png
```

Observed visual language:

- midnight black city fields;
- electric blue bird, signal, and interface traces;
- red moon, alerts, and broadcast interruptions;
- anime-inspired broadcaster figure;
- English/Japanese signal vocabulary;
- archive, transmission, frequency, and “Bird of Blue” mythology.

These assets support the launch-film treatment in [`ICHOTAKU_LAUNCH_FILM_TREATMENT.md`](ICHOTAKU_LAUNCH_FILM_TREATMENT.md). They do not, by themselves, prove product ownership, licensing, Etsy availability, or commercial-use rights.

## Noise boundaries

Do not use these as product evidence without separate verification:

- CapCut cache files;
- generic automation scripts;
- HTML research pages with no matching local source asset;
- generic poster mockups;
- skill/agent corpora;
- duplicate archive paths;
- third-party marketplace references;
- files whose names contain a product keyword only because they describe a tool or tutorial.

## Next inventory step

Choose one product family at a time and create a verified manifest with:

```text
asset path
product family
physical or digital
source or finished mockup
license/rights status
listing or draft URL
intended mockup slot
approval state
```

