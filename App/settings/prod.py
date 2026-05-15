from .base import *

import os

DEBUG = False

ALLOWED_HOSTS = ["urik.qzz.io"]

CSRF_TRUSTED_ORIGINS = [
    "urik.qzz.io",
]

STATIC_ROOT = BASE_DIR / "staticfiles"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ.get("DB_NAME"),
        "USER": os.environ.get("DB_USER"),
        "PASSWORD": os.environ.get("DB_PASSWORD"),
        "HOST": os.environ.get("DB_HOST", "db"),
        "PORT": os.environ.get("DB_PORT", "5432"),
    }
}
