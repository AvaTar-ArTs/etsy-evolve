# Design System: Etsy Evolve Research Console

## 1. Visual Theme & Atmosphere

A premium editorial research console for turning scattered Etsy assets into
verified product opportunities. The mood is midnight archive meets precision
studio: deep charcoal surfaces, quiet steel structure, one restrained signal
accent, and generous negative space around dense evidence.

Density: 6/10. The interface can hold inventories, keyword matrices, source
records, and QA findings without becoming a cockpit. Variance: 8/10. Use
asymmetric editorial splits, offset evidence rails, and irregular but deliberate
image proportions. Motion: 6/10. Use weighty spring transitions, staggered
source reveals, and restrained signal pulses for active research states.

The product should feel like a working archive, not a generic SaaS dashboard.
Evidence is visually privileged over decoration. Every trend claim carries a
source, date, confidence, and next action.

## 2. Color Palette & Roles

- **Archive Charcoal** (#17191C) — primary canvas and deep navigation surface
- **Graphite Surface** (#22262A) — elevated panels and research workspaces
- **Paper Mist** (#F2F0EA) — primary light reading surface and document cards
- **Ink** (#202326) — high-contrast text on Paper Mist
- **Muted Steel** (#8D959D) — metadata, secondary descriptions, timestamps
- **Whisper Line** (rgba(242,240,234,0.16)) — structural borders on dark surfaces
- **Signal Ochre** (#C6A15B) — the single accent for active states, primary CTAs,
  confidence markers, and focus rings

Do not introduce purple, electric blue, neon gradients, or competing accent
colors. Keep saturation restrained. Never use pure black; Archive Charcoal is
the darkest value.

## 3. Typography Rules

- **Display:** Cabinet Grotesk — track-tight, controlled, editorial; use
  `clamp(2.75rem, 6vw, 6.25rem)` for hero headlines.
- **Body:** Geist — relaxed leading, 65ch maximum line length, minimum 16px.
- **Mono:** Geist Mono — source IDs, file paths, timestamps, confidence scores,
  CSV fields, and technical status values.
- **Hierarchy:** establish importance through weight, spacing, and Ink/Muted
  Steel contrast before increasing font size.
- **Headlines:** never create narrow six-line walls. Keep display headlines to
  two or three lines with a 72rem maximum container.
- **Dashboard numbers:** use Geist Mono for dense metrics and evidence values.

Inter and generic serif fonts are banned. Do not use Times New Roman, Georgia,
Garamond, or Palatino. Use a distinctive modern serif only for a campaign or
editorial cover, never for the research console itself.

## 4. Component Stylings

### Navigation

Use a compact floating dark navigation rail with a thin Signal Ochre active
indicator. Primary routes: Inventory, Evidence, Keywords, Mockups, Posting
Packs. On mobile, collapse into a full-width menu with 44px touch targets.

### Buttons

Primary actions use Signal Ochre fill with Ink text. Secondary actions use a
transparent Graphite Surface with Whisper Line border and Paper Mist text.
Active state translates down 1px with a short spring response. No outer glow,
gradient fill, or invisible text. Button labels should describe an action:
`Review evidence`, `Open posting pack`, `Mark blocked`.

### Evidence rows

Prefer border-top dividers and generous vertical rhythm over card piles. Every
row shows source, observation date, confidence, and next test. Use a narrow
Signal Ochre rule for high-confidence evidence and a muted dashed rule for
unverified research leads.

### Cards

Use cards only when elevation communicates hierarchy: featured product proof,
rendered mockup, or a selected posting pack. Corners are generous but not
playful: 1.5rem radius, diffused shadow tinted toward Archive Charcoal, and
subtle image crop behavior on hover.

### Inputs and filters

Labels sit above inputs. Helper text sits below. Filters use compact rectangular
controls rather than pill clouds. Active filters use Signal Ochre text and a
single border, not a saturated fill. Errors are inline and specific.

### Loading, empty, and error states

Use skeletal loaders matching the eventual inventory-row geometry. Never use a
generic circular spinner. Empty states should show an illustrated evidence
folder, an example source path, and one clear action. Errors must name the
source or field that failed and provide a recovery action.

## 5. Layout Principles

- Use a 12-column CSS Grid inside a 1400px maximum container.
- Hero and overview screens use an asymmetric 7/5 split: editorial statement
  and selected product proof on the left, evidence summary on the right.
- Research screens use a 8/4 split: dense result table plus pinned source rail.
- Avoid the generic three-equal-card row. Use a zig-zag two-column layout,
  horizontal evidence rail, or one dominant feature with supporting records.
- Use large chapter spacing: `clamp(4rem, 10vw, 10rem)` between major sections.
- Use `min-h-[100dvh]`, never `h-screen`.
- Use CSS Grid for layout math. Avoid percentage `calc()` positioning hacks.
- No absolute-positioned content that overlaps another content zone.
- Mobile-first collapse below 768px. Every multi-column region becomes a single
  readable column without horizontal overflow.
- Product images preserve their actual ratio and include explicit crop-safe
  padding. Never let a research thumbnail masquerade as a delivery file.

## 6. Screen Architecture

### Research home

Begin with a wide statement such as “Find the signal worth testing.” Pair it
with one selected proof image and a concise evidence count. Follow with a dense
asymmetric index of product families: tumbler, apparel, wall art, journals,
STL, and stickers.

### Product family view

Place the family title and exact product mode at the top. Show the posting pack,
keyword matrix, evidence ledger, and mockup guide as separate spatial zones.
The primary action is `Review evidence`, not `Publish`.

### Evidence detail

Use a pinned source rail with source URL/local path, observed date, confidence,
rights state, and next test. The main column shows the actual claim and the
artifact it supports.

### Posting pack view

Show title, tags, description opening, image order, delivery files, and policy
checks in one editorial document layout. Keep the physical/digital mode
visible in the header and repeat it before the description.

## 7. Motion & Interaction

- Default spring: stiffness 100, damping 20.
- Animate only `transform` and `opacity`; avoid layout-property animation.
- Stagger inventory rows into view with 40–70ms cascade delays.
- Let evidence rows softly brighten when their source is selected.
- Use a restrained perpetual pulse on the current review target, never on every
  element at once.
- Product images scale from 0.985 to 1.0 on hover inside an overflow-hidden
  frame; never use an aggressive zoom.
- Source rails may pin during desktop evidence review, but unpin naturally on
  mobile.
- Motion must clarify state: loading, selected, verified, blocked, or ready.
- Respect reduced-motion preferences by removing perpetual loops and replacing
  them with opacity changes.

## 8. Responsive Rules

- Below 768px, collapse every grid to one column and preserve source context
  above the claim.
- Keep body text at least 16px and interactive targets at least 44px.
- Inline visual accents move below the headline on mobile rather than squeezing
  the heading.
- Tables become stacked evidence records with field labels.
- Do not require horizontal scrolling to understand a title, tag, or delivery
  file.
- Use `clamp(3rem, 8vw, 6rem)` for section spacing and `clamp()` for display
  typography.

## 9. Anti-Patterns

Never use:

- emojis in interface copy, code, or design documentation;
- Inter or generic serif fonts;
- pure black, neon purple/blue, or glowing gradient buttons;
- three equal cards in a row;
- centered hero layouts for this high-variance console;
- overlapping text and images;
- fake metrics, invented sales, or round performance claims;
- generic names such as “Nexus,” “Acme,” or “John Doe”;
- AI clichés such as “Elevate,” “Seamless,” “Unleash,” or “Next-Gen”;
- filler prompts such as “Scroll to explore” or bouncing arrows;
- competitor tag copying, automated promotional replies, or shadow-ban claims;
- a physical mockup in a digital delivery slot;
- unverified marketplace data presented as current performance proof.
