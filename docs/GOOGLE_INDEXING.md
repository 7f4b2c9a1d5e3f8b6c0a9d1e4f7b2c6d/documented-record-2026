# Google accessibility checklist

## Live crawlable URLs (GitHub Pages)

- Home: https://7f4b2c9a1d5e3f8b6c0a9d1e4f7b2c6d.github.io/documented-record-2026/
- Academic: https://7f4b2c9a1d5e3f8b6c0a9d1e4f7b2c6d.github.io/documented-record-2026/academic.html
- Proclamations: https://7f4b2c9a1d5e3f8b6c0a9d1e4f7b2c6d.github.io/documented-record-2026/proclamations.html
- Sitemap: https://7f4b2c9a1d5e3f8b6c0a9d1e4f7b2c6d.github.io/documented-record-2026/sitemap.xml
- robots.txt: https://7f4b2c9a1d5e3f8b6c0a9d1e4f7b2c6d.github.io/documented-record-2026/robots.txt
- llms.txt: https://7f4b2c9a1d5e3f8b6c0a9d1e4f7b2c6d.github.io/documented-record-2026/llms.txt

## What was done (2026-08-26)

1. Public GitHub repo + GitHub Pages (/docs) enabled
2. `academic.html` with ScholarlyArticle JSON-LD for Volume I
3. Expanded `sitemap.xml` + home page links to academic packages
4. `robots.txt` allows all crawlers and points to sitemap

## What YOU should do once in Search Console (2 minutes)

Google no longer accepts the old /ping sitemap endpoint. Use Search Console:

1. Open https://search.google.com/search-console
2. Add property: `https://7f4b2c9a1d5e3f8b6c0a9d1e4f7b2c6d.github.io/` (URL-prefix) or the documented-record-2026 path
3. Verify (HTML tag or DNS — GitHub Pages often uses URL-prefix verification via google-site-verification meta if you paste it into docs/index.html)
4. Sitemaps → submit: `https://7f4b2c9a1d5e3f8b6c0a9d1e4f7b2c6d.github.io/documented-record-2026/sitemap.xml`
5. URL Inspection → request indexing for:
   - `.../documented-record-2026/`
   - `.../documented-record-2026/academic.html`

## Google Doc for Volume I

Open the manuscript Doc → Share → **Anyone with the link** → Viewer
so the Drive URL in the JCS email and academic page is publicly readable.

Doc: https://docs.google.com/document/d/1EgXw6P-9FdvF-nno-O6ntHu8xBqIC0Ql5tCv7YcoZR8/edit

## Expected timeline

New pages often appear in Google within days after Search Console request; organic ranking for branded queries (`Garth Murray Substrate-Independence`) usually follows once indexed.
