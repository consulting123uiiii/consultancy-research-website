# Consultancy Research International — website

Static marketing site for the outreach brand **Consultancy Research International (CRI)**.
No framework, no build dependency, no runtime. Plain HTML/CSS/JS served as files.

**Live:** https://consultancyresearch.com (once DNS is pointed)

---

## Structure

```
index.html            hand-maintained homepage
build.py              generates every other page from shared header/footer templates
capabilities.html     generated
sectors.html          generated
insights.html         generated
about.html            generated
contact.html          generated
privacy.html          generated — required for cold-outreach compliance
terms.html            generated
404.html              generated
assets/css/site.css   single stylesheet
assets/js/site.js     nav, scroll reveal, counters, mailto contact form
assets/img/           favicon
CNAME                 GitHub Pages custom domain
robots.txt sitemap.xml
```

## Editing

- **Homepage:** edit `index.html` directly.
- **Every other page:** edit the `PAGES` dict in `build.py`, then run:

```bash
python3 build.py
```

Header, footer and `<head>` live once in `build.py`. If you change them there, also mirror
the change into `index.html`.

## Local preview

```bash
python3 -m http.server 8000
# open http://localhost:8000
```

## Deployment

GitHub Pages, served from the `main` branch root.
Settings → Pages → Source: `Deploy from a branch` → `main` / `/ (root)`.

`CNAME` contains the custom domain. DNS records required at the registrar:

| Type  | Name  | Value                                                          |
|-------|-------|----------------------------------------------------------------|
| A     | @     | 185.199.108.153                                                |
| A     | @     | 185.199.109.153                                                |
| A     | @     | 185.199.110.153                                                |
| A     | @     | 185.199.111.153                                                |
| CNAME | www   | `<github-user>.github.io.`                                     |

Enable **Enforce HTTPS** in Settings → Pages once the certificate provisions (usually
under an hour).

## Before this goes live for outreach

- [ ] Register the domain and point DNS.
- [ ] Create the mailboxes referenced on the site: `research@`, `privacy@`.
- [ ] Publish SPF, DKIM and DMARC for the sending domain.
- [ ] Send outreach from a **separate** domain (e.g. `consultancyresearch.co`) redirecting
      to the primary, so deliverability problems never burn the main brand domain.
- [ ] Warm the sending domain for 2–3 weeks before volume.
- [ ] Replace the placeholder statistics in `index.html` and `about.html` with figures the
      firm can stand behind.
