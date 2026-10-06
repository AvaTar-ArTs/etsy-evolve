# Etsy Evolve

Local preparation and quality control for Etsy digital-product listings created through MyDesigns.

## First release

- Keep tumbler, T-shirt, physical POD, and bundle schemas separate.
- Validate one listing row before any bulk workflow.
- Check delivery files, mockup slots, listing copy, digital-download disclosure, and video metadata.
- Keep MyDesigns automation behind the official web workflow until a documented public API or MCP exists.

## Canonical tumbler profile

1. Hero tumbler thumbnail
2. Full flat wrap
3. 180-degree or alternate view
4. Straight/tapered comparison
5. Close-up detail
6. Lifestyle image
7. Included-files graphic
8. Digital-download disclaimer
9. Bundle overview when applicable
10. Optional alternate view
11. Short rotating video after the stills

The first implementation milestone is a read-only validator for one complete tumbler row. It must not publish, move assets, or call undocumented MyDesigns endpoints.

## Project documentation

- [Product brief](docs/PRODUCT_BRIEF.md)
- [Product mockup guides](docs/MOCKUP_GUIDES.md)
