from pathlib import Path
from decouple import config as env

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = "django-insecure-odwcv0m7rd)p=i1^!s!u_gwbzc0u7(7q44oja5w(hrr=m5tg-i"

AUTH_USER_MODEL = "user.UserModel"

DEBUG = True

ALLOWED_HOSTS = ["*"]
CORS_ORIGIN_ALLOW_ALL = True


INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "user",
    "customer",
    "machine",
    "rest_framework.authtoken",
    "rest_framework",
    "corsheaders",
]

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "core_api.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "core_api.wsgi.application"


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": env("POSTGRES_DB"),
        "USER": env("POSTGRES_USER"),
        "PASSWORD": env("POSTGRES_PASSWORD"),
        "HOST": env("DB_HOST"),
        "PORT": env("DB_PORT"),
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

STATIC_URL = "static/"

if env("ENVIRONMENT", None) == "prd":
    DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

    AWS_ACCESS_KEY_ID = env("AWS_ACCESS_KEY_ID")
    AWS_SECRET_ACCESS_KEY = env("AWS_SECRET_ACCESS_KEY")

    PROD_APPS = ["django_s3_storage"]

    INSTALLED_APPS += PROD_APPS

    WHITENOISE_STATIC_PREFIX = "/static/"

    S3_BUCKET = "smtcmms-static"
    AWS_STORAGE_BUCKET_NAME = S3_BUCKET

    STATICFILES_STORAGE = "django_s3_storage.storage.StaticS3Storage"
    DEFAULT_FILE_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"
    AWS_S3_BUCKET_NAME_STATIC = S3_BUCKET

    AWS_S3_CUSTOM_DOMAIN = f"{S3_BUCKET}.s3.amazonaws.com"
    STATIC_URL = f"https://{AWS_S3_CUSTOM_DOMAIN}/"
    MEDIA_URL = AWS_S3_CUSTOM_DOMAIN
