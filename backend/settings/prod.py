from .common import *

env = environ.Env()
environ.Env.read_docker_secrets()

DEBUG = False

SECRET_KEY = env("DJANGO_SECRET_KEY")

ALLOWED_HOSTS = env("ALLOWED_HOSTS")

CORS_ALLOWED_ORIGINS = env.list("CORS_ALLOWED_ORIGINS")

DATABASES = {
    "default": env.db("DJANGO_POSTGRESQL_URL"),  # default = 'DATABASE_URL'
}

AZURE_ACCOUNT_NAME = env("AZURE_ACCOUNT_NAME")
AZURE_ACCOUNT_KEY = env("AZURE_ACCOUNT_KEY")

STATICFILES_STORAGE = "backend.storages.StaticAzureStorage"
DEFAULT_FILE_STORAGE = "backend.storages.MediaAzureStorage"


# djangorestframework-jwt 설정
JWT_AUTH = {
    "JWT_SECRET_KEY": env("JWT_SECRET_KEY"),
    "JWT_ALGORITHM": "HS256",
    "JWT_ALLOW_REFRESH": True,
    "JWT_EXPIRATION_DELTA": datetime.timedelta(seconds=300),
    "JWT_REFRESH_EXPIRATION_DELTA": datetime.timedelta(days=7),
}

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "console": {
            "level": "ERROR",
            "class": "logging.StreamHandler",
        }
    },
    "loggers": {
        "django": {
            "handlers": ["console"],
            "level": "ERROR",
        }
    },
}