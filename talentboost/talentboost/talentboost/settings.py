from pathlib import Path

from decouple import config

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config("SECRET_KEY", default="django-insecure-*fz9^hj5h-c_@m)_hqp!ec2sw7^d)41mcpe-&)$av&&6zbi0d1")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config("DEBUG", default=True, cast=bool)

ALLOWED_HOSTS = ["*"]


# Application definition
INSTALLED_PLUGINS = [
    "admin_interface",
    "colorfield",
    "compressor",
    "crispy_bootstrap5",
    "crispy_forms",
    "django_extensions",
    "django_filters",
    "django_tables2",
    "import_export",
    "registration",
    "tinymce",
    "versatileimagefield",
]
DJANGO_APPS = [
    "django.contrib.admin",
    "django.contrib.humanize",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sessions",
]
MODULES = [
    "main",
    "users",
    "web",
]

INSTALLED_APPS = INSTALLED_PLUGINS + DJANGO_APPS + MODULES

AUTH_USER_MODEL = "users.CustomUser"
X_FRAME_OPTIONS = "SAMEORIGIN"
SILENCED_SYSTEM_CHECKS = ["security.W019", "admin.E410"]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "web.middleware.Custom404Middleware",
]

ROOT_URLCONF = "talentboost.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "web.context_processors.main_context",
                "main.context_processors.main_context",
            ]
        },
    }
]

WSGI_APPLICATION = "talentboost.wsgi.application"

VERSATILEIMAGEFIELD_SETTINGS = {
    "cache_length": 2592000,
    "cache_name": "versatileimagefield_cache",
    "jpeg_resize_quality": 70,
    "sized_directory_name": "__sized__",
    "filtered_directory_name": "__filtered__",
    "placeholder_directory_name": "__placeholder__",
    "create_images_on_demand": True,
    "image_key_post_processor": None,
    "progressive_jpeg": False,
}

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
SHORT_DATETIME_FORMAT = "d/m/Y g:i A"
SHORT_DATE_FORMAT = "d/m/Y"

ACCOUNT_ACTIVATION_DAYS = 7
REGISTRATION_AUTO_LOGIN = True
SEND_ACTIVATION_EMAIL = False
REGISTRATION_EMAIL_SUBJECT_PREFIX = ""

REGISTRATION_OPEN = False
LOGIN_URL = "/accounts/login/"
LOGOUT_URL = "/accounts/logout/"
LOGIN_REDIRECT_URL = "/"

CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"
STATIC_URL = "/static/"
STATIC_FILE_ROOT = BASE_DIR / "static"
STATICFILES_DIRS = ((BASE_DIR / "static"),)
STATIC_ROOT = BASE_DIR / "assets"


APP_SETTINGS = {
    "logo": "/static/app/config/talentboost.png",
    "logo_mini": "/static/app/config/talentboost.png",
    "favicon": "/static/app/config/favicon.png",
    "site_name": "Interval Talent Boost",
    "site_title": "Interval Talent Boost",
    "site_description": "This is your moment to shine and make a mark",
    "site_keywords": "This is your moment to shine and make a mark",
    "background_image": "/static/app/config/background.jpg",
}

ORG_DATA = {
    "company_name": "Interval Talent Boost",
    "company_address": "Areakode, Malappuram Kerala, India",
    "company_mobile": "+91 000 000 000",
    "company_mail": "info@intervaledu.com",
}

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

STUDENT_PAYMENT_AMOUNT = 250
SCHOOL_PAYMENT_AMOUNT = 0

RAZORPAY_API_KEY = config("RAZORPAY_API_KEY", default="rzp_live_JRLvPZ6gHNoX0z")
RAZORPAY_API_SECRET = config("RAZORPAY_API_SECRET", default="ZrLwGIDH7k9DY7HgqIp0Jyei")

WHATSAAP_API_URL = config("WHATSAAP_API_URL", default="https://server.gallabox.com/devapi/messages/whatsapp")
WHATSAPP_CHANNEL_ID = config("WHATSAPP_CHANNEL_ID", default="66a8cc997b7b9b0eeb2dbd2d")
WHATSAPP_API_KEY = config("WHATSAPP_API_KEY", default="66a626d44b3986c19203b203")
WHATSAPP_API_SECRET = config("WHATSAPP_API_SECRET", default="3a1772a781dd4140b7d61a18cf85bbb9")
