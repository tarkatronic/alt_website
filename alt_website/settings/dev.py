from .base import *

MANAGERS = ADMINS
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

TEMPLATE_DEBUG = DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'alt_web.db'
    }
}
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}
