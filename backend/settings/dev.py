from .common import *

env = environ.Env()
environ.Env.read_env()

DEBUG = True

SECRET_KEY = env("DJANGO_SECRET_KEY")

STATICFILES_DIRS = [BASE_DIR / "backend" / "_static"]  # add path for static-file-finder
MEDIA_ROOT = BASE_DIR / "backend" / "_media"  # media file save and find path

ALLOWED_HOSTS = []

# djangorestframework-jwt 설정
JWT_AUTH = {
    "JWT_SECRET_KEY": env("JWT_SECRET_KEY"),
    "JWT_ALGORITHM": "HS256",
    "JWT_ALLOW_REFRESH": True,
    "JWT_EXPIRATION_DELTA": datetime.timedelta(seconds=300),
    "JWT_REFRESH_EXPIRATION_DELTA": datetime.timedelta(days=7),
}

INSTALLED_APPS = [
    *INSTALLED_APPS,
    "debug_toolbar",
    "django_extensions",
]

MIDDLEWARE = [
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    *MIDDLEWARE,
]

INTERNAL_IPS = [
    "127.0.0.1",
]

CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
]

GRAPH_MODELS = {
    # "all_applications": True,
    "app_labels": ["accountapp", "instagramapp"],
    "group_models": True,
}
