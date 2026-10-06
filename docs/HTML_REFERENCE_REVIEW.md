# Local HTML reference review

Reviewed 78,204 HTML paths under `/Users/steven` on 2026-10-06 with `rg
--files`, excluding `Library`, `node_modules`, Git metadata, and cache trees
where practical. The review was bounded by filenames and representative source
roots; it did not render every page.

## Reference families selected

| Family | Representative roots | Reusable pattern |
|---|---|---|
| Gallery | `AVATARARTS/code/sites/*gallery*`, `Documents/HTML/*gallery*` | image-first browsing, collections, indexable item paths |
| Product storefront | `AVATARARTS/business/products/storefront/` | product proof, offer separation, clear CTA |
| SEO dashboards | `AVATARARTS/code/sites/ORGANIZED/html_files/SEO_*.html` | evidence tables, filters, source-oriented status |
| Music/discography | `AVATARARTS/business/content/music-empire/` | archive navigation, metadata, collection grouping |
| Etsy/product research | `Documents/HTML/organized_intelligent/` | saved marketplace references and product-specific notes |

## Design decisions carried forward

- Use a dark editorial archive surface with one restrained ochre signal accent.
- Keep product family, physical/digital mode, evidence, and rights visible.
- Prefer source rails and border dividers over generic card grids.
- Make the first action review-oriented, not publish-oriented.
- Treat gallery imagery as proof and context, not as a substitute for delivery
  files or rights verification.
- Keep static HTML meaningful without JavaScript; progressive enhancement can
  add filtering later.

## Deliberately excluded

- Client and medical pages unrelated to Etsy or creative products.
- Generated dashboards that contain claims without source/date context.
- Duplicated archives and backup copies as separate design authorities.
- Raw HTML copied into the repo; this project uses a small purpose-built surface
  with links back to local provenance.

## Output

The synthesized static surface lives under `site/`:

- `site/index.html` — research console home;
- `site/posting-packs.html` — product-family posting templates;
- `site/source-review.html` — evidence and provenance view;
- `site/styles.css` — shared visual system.

These are local preparation pages. They do not publish to Etsy, call MyDesigns,
or modify Notion.
