from .base import *  # noqa

# Ruxsat etilgan hostlar va debug rejimi
ALLOWED_HOSTS = ["*"]
DEBUG = True

# Local debugging uchun
INTERNAL_IPS = ["127.0.0.1"]

# Ilovalar
INSTALLED_APPS += ["debug_toolbar"]  # noqa: F405

# Middleware
MIDDLEWARE += ["debug_toolbar.middleware.DebugToolbarMiddleware"]  # noqa: F405

# Ma'lumotlar bazasi
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",  # noqa: F405
    }
}

# Statik va media fayllar uchun sozlamalar
STATIC_URL = "static/"
STATICFILES_DIRS = [BASE_DIR / "static"]  # noqa: F405

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"  # noqa: F405

# Django REST Framework (DRF) sozlamalari
REST_FRAMEWORK = {
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.IsAuthenticated",  # Tizimga kirgan foydalanuvchilar uchun
    ],
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.SessionAuthentication",
        "rest_framework.authentication.BasicAuthentication",
    ],
}

# Loglash
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "{levelname} {asctime} {module} {message}",
            "style": "{",
        },
        "simple": {
            "format": "{levelname} {message}",
            "style": "{",
        },
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "simple",
        },
    },
    "root": {
        "handlers": ["console"],
        "level": "DEBUG",
    },
}

# Debug Toolbar sozlamalari (Qo'shimcha sozlash)
DEBUG_TOOLBAR_CONFIG = {
    "SHOW_TOOLBAR_CALLBACK": lambda request: DEBUG,  # faqat debug rejimida
}

# Email debugging uchun
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

# Keshlash (lokal muhit uchun oddiy sozlama)
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
        "LOCATION": "unique-snowflake",
    }
}
