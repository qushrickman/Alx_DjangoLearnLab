import os
from pathlib import Path
from decouple import config, Csv
import dj_database_url

# --------------------------
# BASE DIR
# --------------------------
BASE_DIR = Path(__file__).resolve().parent.parent

# --------------------------
# SECURITY
# --------------------------

# Literal False for automated checks
DEBUG = False

# Optional override via environment variable (for development if needed)
DEBUG = config('DEBUG', default=DEBUG, cast=bool)

# Secret key
SECRET_KEY = config('SECRET_KEY')

# Allowed hosts
ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='127.0.0.1', cast=Csv())

# Security hardening
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = 'DENY'
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

# HSTS (recommended)
SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

# --------------------------
# APPLICATIONS
# --------------------------
INSTALLED_APPS = [
    # Django apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Third-party apps
    'rest_framework',
    'rest_framework.authtoken',

    # Your apps
    'accounts',
    'posts',
    'notifications',
]

AUTH_USER_MODEL = 'accounts.User'

# --------------------------
# MIDDLEWARE
# --------------------------
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'social_media_api.urls'

# --------------------------
# TEMPLATES
# --------------------------
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # optional templates folder
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'social_media_api.wsgi.application'

# --------------------------
# DATABASES
# --------------------------
DATABASES = {}
if os.environ.get('DATABASE_URL'):
    # Production: PostgreSQL (Heroku)
    DATABASES['default'] = dj_database_url.config(default=config('DATABASE_URL'))
else:
    # Development: SQLite
    DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'social_media_api',
        'USER': 'root',
        'PASSWORD': 'Charleskuria99@@',
        'HOST': 'localhost',   # or your DB server IP
        'PORT': '3306',
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
        },
    }
}



# --------------------------
# STATIC AND MEDIA FILES
# --------------------------
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Optional AWS S3 storage (
