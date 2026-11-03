# Sahara v2 – before going live

Structure mirrors empress-balinese-massage.com (price list, category + treatment pages, guided booking, vouchers, packages, bridal, FAQ, areas, therapists, reviews). Sahara dark-gold brand, real Sahara prices. No Empress text, photos, reviews or prices copied.

## Placeholders to replace (search the repo for each)
| Item | Current value | Where |
|---|---|---|
| WhatsApp / phone | +971 50 123 4567 | `_generator/data.py` (PHONE), then rebuild |
| Fresha URL | https://www.fresha.com/sahara-balinese | data.py (FRESHA) |
| Email | info@saharabalinesespa.com | data.py (EMAIL) |
| Domain | realplannet.github.io/Sahara | data.py (BASE) → canonical, OG, sitemap, robots; add CNAME for custom domain |
| Reviews | none shown (flagged on reviews page) | add real Google reviews + review link |
| Therapists | Neny T., Wayan S., Putu A., Made K. – no photos | confirm names, add photos |
| Areas served | draft list | confirm coverage |
| Terms / Privacy | draft | legal review |
| Package I | "two-hour ritual" vs 150 min | align wording |

## Rebuild
`cd _generator && python3 build.py` (outputs to the site root). Delete `_generator` before deploy if you prefer a clean repo.

## Deploy
Copy contents (not the folder) over repo `main`, commit, push. Live v1 (`sahara-site-ready`) is untouched.
