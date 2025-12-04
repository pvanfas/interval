# Interval Education Platform

IntervalEdu is a content-heavy Django 4.2 project that powers Interval's marketing website, academic program catalog, lead funnels, and online assessment tooling. The codebase bundles a traditional CMS-like `web` app for rich storytelling alongside the `smartest` app that curates board-specific mock tests.

## Highlights
- **Composable content models** for programs, courses, testimonials, media features, news, and blogs powered by CKEditor 5 and Taggit.
- **Geography-aware enrollment journey** with countries, locations, and boards exposed via reusable templates and partials.
- **Razorpay-ready checkout flow** for course payments plus honeypot + ratelimit middleware for safer public forms.
- **Operational tooling**: Sentry error monitoring, database-backed caching, WhiteNoise static serving, and `django-extensions` for day-to-day scripts.

## Repository Layout
| Path | Purpose |
| --- | --- |
| `intervaledu/` | Django project settings, URLs, ASGI/WSGI entrypoints. |
| `web/` | Main site models, views, URLs, templates, and context processors. |
| `smartest/` | Subject + board specific mock-test links surfaced to learners. |
| `templates/web/` | Page templates and partials used by both apps. |
| `static/` | Pre-built CSS/JS/assets served via WhiteNoise. |
| `media/` | User-uploaded media (keep out of version control in production). |
| `fixtures/` | JSON fixtures for bootstrapping demo content. |
| `scripts/` | Helper scripts (e.g., automated ingestion) runnable via `python -m scripts.main`. |

## Tech Stack
- Python 3.10 (formatting targets enforced by Black/Ruff).
- Django 4.2 with PostgreSQL (SQLite fallback for local development).
- django-admin-interface, CKEditor 5, Taggit, django-import-export, django-countries, easy-thumbnails, and Razorpay SDK.
- Sentry SDK for observability, WhiteNoise for static assets, `django-ratelimit` + `django-honeypot` for abuse prevention.

## Getting Started

### 1. Requirements
- Python 3.10+
- Pip / virtualenv (or uv/Poetry if you prefer)
- PostgreSQL 13+ (recommended) or SQLite (default)

### 2. Clone & bootstrap
```bash
git clone git@github.com:pvanfas/interval.git
cd interval/intervaledu
python -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

### 3. Environment variables
Create a `.env` next to `manage.py` and populate the required secrets. Defaults in `settings.py` keep local dev simple, but production must override them.

| Variable | Default | Notes |
| --- | --- | --- |
| `SECRET_KEY` | auto-generated dev key | Always override in prod. |
| `DEBUG` | `True` | Set `False` outside local. |
| `ALLOWED_HOSTS` | `*` | Comma-separated domains. |
| `CSRF_TRUSTED_ORIGINS` | _empty_ | Include scheme, e.g., `https://app.example.com`. |
| `DB_ENGINE` | `django.db.backends.sqlite3` | Switch to `django.db.backends.postgresql`. |
| `DB_NAME` | `db.sqlite3` | For Postgres, use database name. |
| `DB_USER` / `DB_PASSWORD` | _empty_ | Postgres credentials. |
| `DB_HOST` | `localhost` | Hostname or connection string. |
| `RAZORPAY_API_KEY` | placeholder live key | Replace with project-specific Razorpay keys. |
| `RAZORPAY_API_SECRET` | placeholder live secret | Keep out of source control. |
| `USE_PROXY_SSL_HEADER` | `False` | Enable when behind HTTPS proxy/load balancer. |
| `SESSION_COOKIE_SECURE` etc. | controlled via env | Only respected when `DEBUG=False`. |

Optional: set `SENTRY_DSN` via environment and remove the hard-coded DSN before shipping to production.

### 4. Database & cache
```bash
python manage.py migrate
python manage.py createcachetable
python manage.py loaddata fixtures/2025_14_34_10_03_AM.json  # optional demo content
python manage.py createsuperuser
```

### 5. Run the server
```bash
python manage.py runserver
```
Visit `http://127.0.0.1:8000/` for the public site and `http://127.0.0.1:8000/admin/` for content authoring.

## Static & Media Assets
- Static assets live in `static/` and are collected into `assets/` via `python manage.py collectstatic` for deployment.
- WhiteNoise is enabled, so `collectstatic` must run as part of your release pipeline.
- Uploaded content persists under `media/`; configure cloud storage (S3, GCS, etc.) before going live.

## Content Management Workflows
- **Academic Programs**: manage via `web.AcademicProgram` to attach benefits, features, FAQs, CTAs, and hero imagery.
- **Blog/News**: pick from three templates, add SEO meta fields, tags, and CTA overlays.
- **Geographies & Boards**: use `Country`, `Board`, `Location`, and `Subject` models to craft localized journeys.
- **Smart Tests**: create `smartest.Subject` + `TestLink` records to expose curated assessments filtered by board, class, and subject.

## Quality & Tooling
- Linting: `ruff check .`
- Formatting: `black .`
- Tests: `python manage.py test`
- Performance utilities: see `web/performance_utils.py` for cache helpers.

## Deployment Notes
1. Ensure `DEBUG=False`, `ALLOWED_HOSTS`, CSRF origins, and SSL headers are configured.
2. Point `DB_ENGINE` to PostgreSQL (or your managed database) and run migrations.
3. Run `collectstatic` and upload the `media/` directory to persistent storage.
4. Enable `django.middleware.security.SecurityMiddleware` settings via env flags (HSTS, secure cookies, etc.).
5. Provision Razorpay + Sentry credentials per environment.
6. Review `PRE_DEPLOYMENT_CHECKLIST.md` for final hardening steps.

## Troubleshooting
- **Static files missing:** confirm `collectstatic` executed and `STATIC_ROOT` is served by your web tier.
- **Forms blocked:** honeypot (`HONEYPOT_FIELD_NAME`) or `django-ratelimit` may reject suspicious requests; inspect logs.
- **Slow responses:** database cache requires `django_cache_table`; re-run `python manage.py createcachetable` after schema resets.
- **Images not appearing:** validate Pillow + easy-thumbnails dependencies and ensure media storage is writable.

## Contributing
1. Fork and branch from `main`.
2. Keep changes formatted (`black`) and linted (`ruff`).
3. Add/adjust tests inside `web/tests.py` or `smartest/tests.py` when touching business logic.
4. Open a PR describing intent, screenshots for UI tweaks, and database migration notes if applicable.

## License
Internal project. Contact the Interval team for usage permissions.