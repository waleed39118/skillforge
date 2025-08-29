from .settings import *
DEBUG = False
ALLOWED_HOSTS = ['your-domain.com', 'your-app.onrender.com']
CSRF_TRUSTED_ORIGINS = ['https://your-domain.com', 'https://your-app.onrender.com']

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_SSL_REDIRECT = True

STATIC_ROOT = BASE_DIR / 'staticfiles'



MIDDLEWARE = ['whitenoise.middleware.WhiteNoiseMiddleware', *MIDDLEWARE]
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


import os
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('DB_NAME'),
        'USER': os.environ.get('DB_USER'),
        'PASSWORD': os.environ.get('DB_PASSWORD'),
        'HOST': os.environ.get('DB_HOST', 'localhost'),
        'PORT': os.environ.get('DB_PORT', '5432'),
    }
}
