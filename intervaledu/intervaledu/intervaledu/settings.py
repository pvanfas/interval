from pathlib import Path
import sentry_sdk

from decouple import config


sentry_sdk.init(
    dsn="https://25ed775ffbf91c4c98936f8ff7aed6a4@o4508419881697280.ingest.us.sentry.io/4508422358499328",
    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for tracing.
    traces_sample_rate=1.0,
    _experiments={
        # Set continuous_profiling_auto_start to True
        # to automatically start the profiler on when
        # possible.
        "continuous_profiling_auto_start": True,
    },
)


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config(
    "SECRET_KEY",
    default="django-insecure-s!0*h8z8(fqj7&jax2rq$+utv!k*(vd*u49w934u+g7jbu&6q8",
)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config("DEBUG", default=True, cast=bool)

# Hosts and origins
_allowed_hosts = config("ALLOWED_HOSTS", default="*")
ALLOWED_HOSTS = [h.strip() for h in _allowed_hosts.split(",") if h.strip()]

# CSRF trusted origins require scheme (e.g., https://example.com)
_csrf_trusted = config("CSRF_TRUSTED_ORIGINS", default="")
CSRF_TRUSTED_ORIGINS = [o.strip() for o in _csrf_trusted.split(",") if o.strip()]


# Application definition

INSTALLED_APPS = [
    "admin_interface",
    "colorfield",
    "import_export",
    "django_ckeditor_5",
    "taggit",
    "honeypot",
    "easy_thumbnails",
    "django_extensions",
    "django_countries",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sites",
    "django.contrib.redirects",
    "web",
    "smartest",
]

SITE_ID = 1
# X_FRAME_OPTIONS = "SAMEORIGIN"
SILENCED_SYSTEM_CHECKS = ["security.W019"]
CKEDITOR_UPLOAD_PATH = "media/uploads/"

MIDDLEWARE = [
    "django.middleware.gzip.GZipMiddleware",  # Compress responses
    "django.middleware.http.ConditionalGetMiddleware",  # Handle ETags
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",  # Serve static files efficiently
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.contrib.redirects.middleware.RedirectFallbackMiddleware",
]

ROOT_URLCONF = "intervaledu.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,  # Must be False when using custom loaders
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "web.context_processors.main_context",
            ],
        },
    },
]

WSGI_APPLICATION = "intervaledu.wsgi.application"

# Caching Configuration
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.db.DatabaseCache",
        "LOCATION": "django_cache_table",
        "TIMEOUT": 300,  # 5 minutes default
        "OPTIONS": {"MAX_ENTRIES": 1000},
    }
}

# Session caching
SESSION_ENGINE = "django.contrib.sessions.backends.cached_db"
SESSION_CACHE_ALIAS = "default"


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": config("DB_ENGINE", default="django.db.backends.sqlite3"),
        "NAME": config("DB_NAME", default=BASE_DIR / "db.sqlite3"),
        "USER": config("DB_USER", default=""),
        "PASSWORD": config("DB_PASSWORD", default=""),
        "HOST": config("DB_HOST", default="localhost"),
        "PORT": "5432",
        "OPTIONS": {},
        "CONN_MAX_AGE": 600,  # Connection pooling: keep connections alive for 10 minutes
        "CONN_HEALTH_CHECKS": True,  # Enable connection health checks
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "en-us"
TIME_ZONE = "Asia/Kolkata"
USE_I18N = True
USE_L10N = True
USE_TZ = True


USE_L10N = False
DATE_INPUT_FORMATS = (
    "%d/%m/%Y",
    "%d-%m-%Y",
    "%d/%m/%y",
    "%d %b %Y",
    "%d %b, %Y",
    "%d %b %Y",
    "%d %b, %Y",
    "%d %B, %Y",
    "%d %B %Y",
)
DATETIME_INPUT_FORMATS = (
    "%d/%m/%Y %H:%M:%S",
    "%d/%m/%Y %H:%M",
    "%d/%m/%Y",
    "%d/%m/%y %H:%M:%S",
    "%d/%m/%y %H:%M",
    "%d/%m/%y",
    "%Y-%m-%d %H:%M:%S",
    "%Y-%m-%d %H:%M",
    "%Y-%m-%d",
)

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"
STATIC_URL = "/static/"
STATIC_FILE_ROOT = BASE_DIR / "static"
STATICFILES_DIRS = ((BASE_DIR / "static"),)
STATIC_ROOT = BASE_DIR / "assets"

# WhiteNoise Configuration for Optimized Static File Serving
# STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# Browser caching headers (set in production web server)
if not DEBUG:
    # WhiteNoise handles static file caching automatically
    # Static files: Cache-Control: public, max-age=31536000 (immutable)
    # Media files: Cache-Control: public, max-age=2592000
    WHITENOISE_MAX_AGE = 31536000  # 1 year for static files
    WHITENOISE_ALLOW_ALL_ORIGINS = False
    WHITENOISE_SKIP_COMPRESS_EXTENSIONS = ["jpg", "jpeg", "png", "gif", "webp", "zip", "gz", "tgz", "bz2", "tbz", "xz", "br", "swf", "flv", "woff", "woff2"]

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

customColorPalette = [
    {"color": "hsl(4, 90%, 58%)", "label": "Red"},
    {"color": "hsl(340, 82%, 52%)", "label": "Pink"},
    {"color": "hsl(291, 64%, 42%)", "label": "Purple"},
    {"color": "hsl(262, 52%, 47%)", "label": "Deep Purple"},
    {"color": "hsl(231, 48%, 48%)", "label": "Indigo"},
    {"color": "hsl(207, 90%, 54%)", "label": "Blue"},
]
CKEDITOR_5_CONFIGS = {
    "default": {"toolbar": ["heading", "bold", "italic", "highlight", "link", "bulletedList", "numberedList", "blockQuote", "imageUpload", "sourceEditing"]},
    "extends": {
        "blockToolbar": ["paragraph", "heading1", "heading2", "heading3", "heading4", "heading5", "|", "bulletedList", "numberedList", "|", "blockQuote", "mediaEmbed"],
        "toolbar": [
            "heading",
            "|",
            "bold",
            "italic",
            "link",
            "underline",
            "highlight",
            "code",
            "subscript",
            "superscript",
            "sourceEditing",
            "insertImage",
            "bulletedList",
            "numberedList",
            "todoList",
            "|",
            "blockQuote",
            "imageUpload",
            "|",
            "fontColor",
            "mediaEmbed",
            "removeFormat",
            "insertTable",
            "sourceEditing",
        ],
        "htmlSupport": {
            "allow": [
                {"name": "div", "attributes": {"class": True}, "classes": ["embed-container"], "styles": True},
                {
                    "name": "iframe",
                    "attributes": {"src": True, "frameborder": True, "allowfullscreen": True, "width": True, "height": True, "title": True, "allow": True, "referrerpolicy": True},
                    "classes": True,
                    "styles": True,
                },
                {"name": "style", "attributes": True},
            ]
        },
        "mediaEmbed": {"previewsInData": True},
        "image": {
            "toolbar": ["imageTextAlternative", "|", "imageStyle:alignLeft", "imageStyle:alignRight", "imageStyle:alignCenter", "imageStyle:side", "|"],
            "styles": ["full", "side", "alignLeft", "alignRight", "alignCenter"],
        },
        "table": {"contentToolbar": ["tableColumn", "tableRow", "mergeTableCells", "tableProperties", "tableCellProperties"]},
        "heading": {
            "options": [
                {"model": "paragraph", "title": "Paragraph", "class": "ck-heading_paragraph"},
                {"model": "heading1", "view": "h1", "title": "Heading 1", "class": "ck-heading_heading1"},
                {"model": "heading2", "view": "h2", "title": "Heading 2", "class": "ck-heading_heading2"},
                {"model": "heading3", "view": "h3", "title": "Heading 3", "class": "ck-heading_heading3"},
            ]
        },
    },
    "list": {"properties": {"styles": "true", "startIndex": "true", "reversed": "true"}},
}


RAZORPAY_API_KEY = config("RAZORPAY_API_KEY", default="rzp_live_JRLvPZ6gHNoX0z")
RAZORPAY_API_SECRET = config("RAZORPAY_API_SECRET", default="ZrLwGIDH7k9DY7HgqIp0Jyei")
HONEYPOT_FIELD_NAME = "xaddressx"

# FOR DEVELOPMENT PURPOSES ONLY
# DATABASES["default"]["ENGINE"] = "django.db.backends.sqlite3"
# DATABASES["default"]["NAME"] = BASE_DIR / "db.sqlite3"
# DATABASES["default"]["USER"] = ""

# ---------------------------------
# Production security and logging
# ---------------------------------

# Respect SSL termination at proxy if enabled
if config("USE_PROXY_SSL_HEADER", default=False, cast=bool):
    SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
    USE_X_FORWARDED_HOST = True

if not DEBUG:
    SESSION_COOKIE_SECURE = config("SESSION_COOKIE_SECURE", default=True, cast=bool)
    CSRF_COOKIE_SECURE = config("CSRF_COOKIE_SECURE", default=True, cast=bool)
    SECURE_SSL_REDIRECT = config("SECURE_SSL_REDIRECT", default=False, cast=bool)
    SECURE_CONTENT_TYPE_NOSNIFF = True
    SECURE_BROWSER_XSS_FILTER = True
    SECURE_HSTS_SECONDS = config("SECURE_HSTS_SECONDS", default=31536000, cast=int)  # 1 year
    SECURE_HSTS_INCLUDE_SUBDOMAINS = config("SECURE_HSTS_INCLUDE_SUBDOMAINS", default=True, cast=bool)
    SECURE_HSTS_PRELOAD = config("SECURE_HSTS_PRELOAD", default=True, cast=bool)
    X_FRAME_OPTIONS = "DENY"  # Prevent clickjacking
    SECURE_REFERRER_POLICY = "strict-origin-when-cross-origin"  # Better privacy

