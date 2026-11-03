# Sahara Balinese Spa & Salon — Website

Static site, no build step. 10 pages, mobile-responsive, deploys as-is to GitHub Pages.

## Pages
| File | Page |
|---|---|
| index.html | Home — "The Sahara Ritual" |
| services.html | Services & pricing |
| packages.html | Signature packages |
| bridal.html | Bridal packages |
| about.html | About Neny & the team |
| gallery.html | Photo gallery |
| blog.html | Wellness journal |
| contact.html | Contact & booking |
| faq.html | FAQs |
| ar.html | Arabic version |

## Deploy (GitHub Pages)
1. Push this folder's contents to the root of `main` on `github.com/realplannet/Sahara`.
2. Repo → Settings → Pages → Source: `Deploy from a branch` → Branch: `main` / `/(root)`.
3. Site goes live at `https://realplannet.github.io/Sahara/` (or your custom domain if you attach one — the schema.org markup already declares `saharabalinesespa.com`).

## Before going fully live — still using placeholder values
- WhatsApp number: `+971501234567` (used site-wide) — confirm this is the real number.
- Fresha booking link: `https://www.fresha.com/sahara-balinese` — confirm this is the live Fresha profile URL.
- No Google review link is wired in on any page currently.

## What changed from the design export
The original files (`*.dc.html`) were exported from a design tool and wrapped in a proprietary
`<x-dc>`/`<helmet>` format that requires a React-based runtime (`support.js`) to render — they
cannot be hosted directly. Each page was converted to standard HTML5:
- `<helmet>` contents moved into a real `<head>`.
- `<x-dc>` inner markup moved into `<body>`, unchanged.
- The page's interactive JS (scroll reveals, FAQ accordion, nav scroll effect, the gold-dust/petal
  canvas animation on the homepage) was extracted from the component wrapper and now runs on
  `DOMContentLoaded` with no framework dependency.
- All internal links updated from `.dc.html` to `.html`.
- Added `<title>` and favicon tags (none existed before) — no visual/layout change.
No visual design or mobile layout was altered. `mobile.css` (shared breakpoint overrides) is linked
on every subpage exactly as in the source; the homepage keeps its own self-contained responsive
rules as it did originally.

Note on mobile nav: by original design, the top nav's link list is intentionally hidden below 840px
(collapses to logo + Reserve/WhatsApp button only) — full navigation is available in every page's
footer. This was already the case in the source design and has been preserved as-is.
