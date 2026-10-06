# Product-family SEO and evidence crosswalk

This is the implementation bridge between `MOCKUP_GUIDES.md`, the local asset
locate reports, Paste research, and the fetched Notion XEO material.

## Product families

| Family | Buyer decision | Primary proof | Delivery model | Main risk |
|---|---|---|---|---|
| Digital tumbler wrap | Will this fit and what files arrive? | flat wrap + straight/taper comparison | up to five digital files | confusing physical mockup with digital file |
| Physical POD T-shirt | What will fit, feel, and ship? | model, placement, size/material cards | fulfilled physical item | using digital-download language |
| Digital T-shirt design | Can I print/use this artwork? | transparent art + format/license card | PNG/SVG/EPS/ZIP as promised | mockup mistaken for delivery file |
| Book/journal | What is inside and what format is it? | cover + legible interior pages | physical or printable, never mixed | unreadable collage or unclear edition |
| Digital wall art | What ratio and files do I receive? | clean art + ratio/size card | printable files | framed scene hides actual file |
| Physical sticker/label | How many, what size, what finish? | sheet + scale/material detail | physical shipment | tiny bundle grid as hero |
| Music/creative bundle | What is included and how is it used? | inventory + preview + license | digital bundle | unsupported rights or usage claims |

## Search-to-proof mapping

| Layer | Listing implementation | Evidence required |
|---|---|---|
| SEO | product-first title, relevant tags, readable description | current product fields and platform limits |
| AEO | “what you receive,” sizing, delivery, FAQ blocks | actual file manifest |
| GEO | tutorial or case study explaining the workflow | source links, dated run log, rendered proof |
| DEO | mobile-readable hero, cards, alt text, responsive page | crop check at thumbnail size |
| KEO | rotation or product-use video only where useful | verified codec, duration, dimensions |
| LEO | rights, trademark, license, disclosure checks | rights status and reviewer decision |
| OEO | confidence and claim ledger | source, date, scope, limitation |

## Recommended stable asset IDs

Use a deterministic ID based on normalized source path and product family. Do
not use a mutable title as the primary key.

```text
<family>:<sha256(normalized-source-path)>[:12]
```

Example:

```text
tumbler-digital:8f2d2d1f4f73
```

## Listing copy skeletons

### Digital tumbler

```text
[Theme] 20oz Tumbler Wrap PNG — Straight and Tapered Sublimation Design

WHAT YOU RECEIVE
- Straight 20oz PNG
- Tapered 20oz PNG
- [additional files only if present]

DIGITAL DOWNLOAD ONLY
No physical tumbler is shipped. Measure your blank before printing.
```

### Digital T-shirt artwork

```text
[Theme] Graphic T-Shirt Design PNG/SVG — Instant Digital Download

Includes: [exact formats]. No physical shirt is included. Review the license
and confirm the artwork is suitable for your intended production method.
```

### Physical T-shirt

```text
[Theme] Graphic T-Shirt — [fit/material/garment]

Physical product. Include size chart, garment color, print placement, care,
shipping, and any personalization rules. Do not describe it as a download.
```

## Evidence gates before a listing becomes bulk-ready

- [ ] Product family is selected.
- [ ] Main delivery files exist and match the family.
- [ ] Mockups show the exact product and variant.
- [ ] Title uses product language before motif language.
- [ ] Tags are relevant and not copied from another product family.
- [ ] Description states what is included and excluded.
- [ ] Rights status is known or explicitly blocked.
- [ ] Hero survives mobile crop.
- [ ] Video metadata is verified when present.
- [ ] One draft has been manually reviewed.

Saved trend claims, Notion growth figures, and marketplace examples are leads;
they cannot clear these gates by themselves.
