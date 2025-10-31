# Zeo — Links Micro‑Site (GitHub Pages / Netlify)

This is a single‑file landing page for all your social links. You’ll point a QR code to this page.

## Edit
1. Open `index.html` and replace:
   - Display name (“Zeo”)
   - Social URLs (`yourhandle`)
   - Email and phone
2. Keep `?utm_source=qr` at the end of each link for analytics.

## Deploy (GitHub Pages)
1. Create a new repo (public). Name it anything, e.g. `links`.
2. Upload `index.html` to the root of the repo.
3. Go to **Settings → Pages**.
4. **Source:** `Deploy from a branch` → **Branch:** `main` → `/ (root)` → Save.
5. Pages URL becomes `https://<your-username>.github.io/<repo>/` (copy this).

## Deploy (Netlify drag‑and‑drop)
1. Go to Netlify → **Add new site** → **Deploy manually**.
2. Drag `index.html` in. It’ll publish at a random subdomain you can rename.
3. Copy the site URL.

## Optional: Custom domain
- Point a domain/subdomain (e.g., `links.yourdomain.com`) to GitHub Pages or Netlify by following their DNS instructions.
- Once the domain is live, use that for the QR.

## Create a short URL
Use a shortener (Bitly/Rebrandly) or your own short‑domain (`go.yourdomain.com`):
- Target URL = your live page URL (custom domain if you set it).
- Short URL example: `go.yourdomain.com/links`.
- Print this short URL under the QR as a fallback.

## QR code spec (for print)
- **Content:** the short URL (NOT the long one).
- **Error Correction:** **H** (30%).
- **Format:** **SVG** (preferred) and **PNG** ≥ 1000×1000 px.
- **Quiet zone:** ≥ 4 modules.
- **Contrast:** dark code on light background (not inverted).
- **Size rule:** QR side ≈ viewing distance / 10 (e.g., 5 m → 50 cm).

## Test
- Scan on iOS and Android from the real distance and under event lighting.
- Test with mobile data (Wi‑Fi off).

