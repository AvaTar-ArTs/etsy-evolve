# Home-directory examples audit

Read-only bounded scan completed 2026-10-06 with `rg --files` and `fzf` over
`/Users/steven`, excluding caches, `node_modules`, and Git metadata where
possible. The scan produced 500 candidate paths before filtering. No assets
were moved, renamed, deleted, uploaded, or treated as automatically publishable.

## Evidence hierarchy

| Level | Meaning | Example |
|---|---|---|
| A | Local asset or structured export inspected directly | `etsy-launch-queue.md`, trend-pack CSVs |
| B | Local strategy/reference document | keyword guides, SEO notes |
| C | Saved historical claim requiring current validation | forecast traffic, growth, ranking time |
| D | Filename-only candidate | a path found by keyword search but not inspected |

## Strongest local examples

### Launch queue

`/Users/steven/etsy-launch-queue.md` reports 2,144 candidate assets:

- 1,306 PNG;
- 784 JPG;
- 36 SVG;
- 5 PDF;
- 3 PSD;
- 3 AI;
- smaller GIF/JPEG/WEBP groups.

The largest roots are Downloads (1,621) and AVATARARTS (387). This is an
inventory lead, not a product catalog. Every candidate still needs product
family, rights, dimensions, delivery, and mockup review.

### Trend-pack CSVs

Directly inspected local examples:

```text
/Users/steven/Pictures/etSy/top-trend-seo-packs/back_to_school_2025/titles_tags_descriptions.csv
/Users/steven/Pictures/etSy/top-trend-seo-packs/chateaucore_castlecore/titles_tags_descriptions.csv
/Users/steven/Pictures/etSy/top-trend-seo-packs/cherry_coded/titles_tags_descriptions.csv
/Users/steven/Pictures/etSy/top-trend-seo-packs/halloween_2025/titles_tags_descriptions.csv
/Users/steven/Pictures/etSy/top-trend-seo-packs/stl_printables/titles_tags_descriptions.csv
```

They provide useful title/tag/description shapes, including product-first
phrases such as `Castlecore Wall Art Set`, `Cherry Martini Poster`, `Matching
Family Halloween Shirts`, and `Moon Lamp STL`. They also contain generic tag
padding (`aesthetic`, `gift idea`, `modern`, `retro`) that should not be copied
unless the listing actually supports those terms.

### IchoTAKU examples

The existing repo treatment and local paths identify IchoTAKU visual anchors:

```text
/Users/steven/Pictures/IchoTaku.png
/Users/steven/Pictures/IchoTakuBird.png
/Users/steven/Pictures/IchoTakuRadio.png
/Users/steven/eso-play/ichoTaku-current-image-batch-2026-08-16/
```

These support original world-building, nocturnal broadcast, blue-bird, and
signalwave positioning. They do not prove Etsy availability, sales, licensing,
or commercial rights for every asset.

## Prior-self comparison

### Corrected conclusions

1. An empty `Pictures/etSy/mockups_templates` subtree does not mean the whole
   design library is empty; the primary libraries are on `2T-Xx` and
   `DeVonDaTa`.
2. `etsylisting0mydesign.CSV` is the tumbler-specific layout; the similarly
   shaped `mydesigns-export (3).CSV` is a wrong-product 10-mockup reference.
3. The later canonical image order is hero → flat wrap → 180° view. The flat
   wrap belongs early because the buyer is purchasing the artwork file.
4. LightUnicorn and saved title guides are inspiration only. Their prices,
   traffic, growth, and conversion claims are not portable proof for IchoTAKU.
5. XEO/KEO/DEO labels are internal planning vocabulary, not guaranteed
   platform ranking factors.

## What remains unresolved

- exact rights status for each launch candidate;
- rendered mockup quality and crop safety;
- current Etsy category, tag, and image limits at publish time;
- one complete canonical tumbler row with live delivery files;
- current performance after a controlled Etsy draft test.

The next safe step is a single product-family posting pack and evidence review,
not a bulk publish.
