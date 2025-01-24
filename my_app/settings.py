"""
Django settings for mysite project.

Generated by 'django-admin startproject' using Django 5.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path
import dj_database_url
import os
from datetime import timedelta

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("DJANGO_SECRET_KEY", "fallback-secret-key")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv("DEBUG", "False") == "True"

ALLOWED_HOSTS = os.getenv(
    "DJANGO_ALLOWED_HOSTS",
    "127.0.0.1,localhost,grnlite.onrender.com,.render.com,0.0.0.0,",
).split(",")

USE_TZ = True  # Ensure this is set

# Application definition
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
    "my_app",
    "my_custom_app",
    "corsheaders",
    "rest_framework_simplejwt.token_blacklist",
    "rest_framework_simplejwt",
    "rest_framework.authtoken",
    "djoser",
    "drf_yasg",
    "rest_framework_swagger",
    "social_django",
    "django.contrib.sites",
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    "allauth.socialaccount.providers.google",
    "allauth.socialaccount.providers.auth0",
    "crispy_forms",
    "register.apps.RegisterConfig",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "corsheaders.middleware.CorsMiddleware",
]

ROOT_URLCONF = "my_app.urls"

AUTHENTICATION_BACKENDS = (
    "social_core.backends.google.GoogleOAuth2",
    "social_core.backends.facebook.FacebookOAuth2",
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
)

SITE_ID = 1

ACCOUNT_EMAIL_VERIFICATION = "none"
ACCOUNT_EMAIL_REQUIRED = True
SOCIALACCOUNT_EMAIL_VERIFICATION = "none"
SOCIALACCOUNT_EMAIL_REQUIRED = False

LOGIN_REDIRECT_URL = "/"
LOGOUT_REDIRECT_URL = "/"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "Templates")],
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

WSGI_APPLICATION = "my_app.wsgi.application"

DJOSER = {
    "LOGIN_FIELD": "email",
    "USER_CREATE_PASSWORD_RETYPE": True,
    "SERIALIZERS": {
        "user_create": "my_app.serializers.UserSerializer",
        "user": "my_app.serializers.UserSerializer",
    },
}

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
        "rest_framework.authentication.TokenAuthentication",
    ),
}

CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://localhost:8000",
    "http://localhost:8080",
    "http://localhost:5000",
]

# JWT SETTING
SIMPLE_JWT = {
    "AUTH_HEADER_TYPES": ("Bearer",),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=15),
    # ... other JWT configuration options ...
}

# OAuth settings
SECRET_KEY = os.getenv("DJANGO_SECRET_KEY", "fallback-secret-key")
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = os.getenv(
    "SOCIAL_AUTH_GOOGLE_OAUTH2_KEY", "default-value-or-None"
)
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = os.getenv(
    "SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET", "default-value-or-None"
)

AUTH_USER_MODEL = "my_app.CustomUser"

# LOGIN_REDIRECT_URL = "/"
# LOGOUT_REDIRECT_URL = "/"

AUTH0_DOMAIN = os.getenv("AUTH0_DOMAIN", "default-value-or-None")
AUTH0_CLIENT_ID = os.getenv("AUTH0_CLIENT_ID", "default-value-or-None")
AUTH0_CLIENT_SECRET = os.getenv("AUTH0_CLIENT_SECRET", "default-value-or-None")

# Add your Google OAuth credentials
SOCIALACCOUNT_PROVIDERS = {
    "google": {
        "SCOPE": [
            "profile",
            "email",
        ],
        "AUTH_PARAMS": {
            "access_type": "online",
        },
        "OAUTH_PKCE_ENABLED": True,  # Enables PKCE for Google OAuth
    },
    "auth0": {
        "DOMAIN": os.getenv("AUTH0_DOMAIN"),  # Environment variable for Auth0 domain
        "CLIENT_ID": os.getenv(
            "AUTH0_CLIENT_ID"
        ),  # Environment variable for Auth0 client ID
        "SECRET": os.getenv(
            "AUTH0_CLIENT_SECRET"
        ),  # Environment variable for Auth0 client secret
        "SCOPE": ["openid", "profile", "email"],  # Scopes for Auth0
    },
}

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
        },
    },
    "loggers": {
        "django.template": {
            "handlers": ["console"],
            "level": "DEBUG",
            "propagate": True,
        },
        "social_core": {
            "handlers": ["console"],
            "level": "DEBUG",
        },
        "django.db.backends": {
            "level": "DEBUG",
            "handlers": ["console"],
    },
}

SOCIALACCOUNT_ADAPTER = "myapp.adapters.MySocialAccountAdapter"

SOCIAL_AUTH_PIPELINE = (
    "social_core.pipeline.social_auth.social_details",
    "social_core.pipeline.social_auth.social_uid",
    "social_core.pipeline.social_auth.auth_allowed",
    "social_core.pipeline.social_auth.social_user",
    "social_core.pipeline.user.get_username",
    "social_core.pipeline.user.create_user",
    "social_core.pipeline.social_auth.associate_user",
    "social_core.pipeline.social_auth.load_extra_data",
    "social_core.pipeline.user.user_details",
)


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.getenv("DB_NAME"),
        "USER": os.getenv("DB_USER"),
        "PASSWORD": os.getenv("DB_PASSWORD"),
        "HOST": os.getenv("DB_HOST"),
        "PORT": os.getenv("DB_PORT"),
    }
}

print(f"DATABASE: {os.getenv('DB_NAME')} USER: {os.getenv('DB_USER')}")
print(f"GOOGLE KEY: {os.getenv('SOCIAL_AUTH_GOOGLE_OAUTH2_KEY')}")


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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

# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = "/static/"
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_URL = "/media/"

CRISPY_TEMPLATE_PACK = 'bootstrap4'

EMAIL_BACKEND = 'django.core.mail.backends.smt.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'kelseaconrad19@outlook.com'
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')