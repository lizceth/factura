# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
from __future__ import absolute_import
from os.path import join, normpath

from .base import*


DEBUG = True

TEMPLATE_DEBUG =DEBUG

EMAIL_BACKEND='django.core.mail.backends.console.EmailBackend'

#configuracion de la base de datos que utilizara el usuario o programador

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': normpath(join(DJANGO_ROOT, 'mydb.db')),
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

CACHES={
    'default': {
        'BACKEND':'django.core.cache.backends.locmem.LocMemCache',
    }
}

#instalacioon de aplicaciones que se agregaran al proyecto
INSTALLED_APPS += (
    'debug_toolbar',
)

MIDDLEWARE_CLASSES += (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)

DEBUG_TOOLBAR_PATCH_SETTINGS=False

INTERNAL_IPS=('127.0.0.1')
########## END TOOLBAR CONFIGURATION
