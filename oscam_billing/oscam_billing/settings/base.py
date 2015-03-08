"""Common settings and globals."""

from os.path import abspath, basename, dirname, join, normpath
from sys import path

########## PATH CONFIGURATION
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
DJANGO_ROOT = dirname(dirname(abspath(__file__)))
BASE_DIR = dirname(dirname(__file__))
SITE_ROOT = dirname(DJANGO_ROOT)
SITE_NAME = basename(DJANGO_ROOT)

# Add our project to our pythonpath, this way we don't need to type our project
# name in our dotted import paths:
path.append(DJANGO_ROOT)
########## END PATH CONFIGURATION

DEBUG = False
# See: https://docs.djangoproject.com/en/dev/ref/settings/#template-debug
TEMPLATE_DEBUG = DEBUG

########## MEDIA CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#media-root
MEDIA_ROOT = normpath(join(SITE_ROOT, 'media'))

# See: https://docs.djangoproject.com/en/dev/ref/settings/#media-url
MEDIA_URL = '/media/'
########## END MEDIA CONFIGURATION


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

########## STATIC FILE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#static-root
STATIC_ROOT = normpath(join(SITE_ROOT, 'assets'))

# See: https://docs.djangoproject.com/en/dev/ref/settings/#static-url
STATIC_URL = '/static/'

# See: https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#std:setting-STATICFILES_DIRS
STATICFILES_DIRS = (
    normpath(join(SITE_ROOT, 'static')),
)

# See: https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#staticfiles-finders
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)
########## END STATIC FILE CONFIGURATION

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'qzc!0(4%ise8+la*zgs+j39u1l=b0c%yiu!5rttb(_4q9i7p1o'

########## TEMPLATE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#template-context-processors
TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.request',    
    'context.get_menu',
)

# See: https://docs.djangoproject.com/en/dev/ref/settings/#template-loaders
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

# See: https://docs.djangoproject.com/en/dev/ref/settings/#template-dirs
TEMPLATE_DIRS = (
    normpath(join(SITE_ROOT, 'templates')),
)
########## END TEMPLATE CONFIGURATION

path.insert(0, normpath(join(BASE_DIR, 'apps')) )

# Application definition
DJANGO_APPS = (
    #'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

# Apps specific for this project go here.
LOCAL_APPS = (    
    'crispy_forms',
    'user_profile',
    'billing'
)

CRISPY_TEMPLATE_PACK = 'bootstrap3'

# See: https://docs.djangoproject.com/en/dev/ref/settings/#installed-apps
INSTALLED_APPS = DJANGO_APPS + LOCAL_APPS

ROOT_URLCONF = 'oscam_billing.urls'

WSGI_APPLICATION = 'oscam_billing.wsgi.application'

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#    }
#}

SESSION_ENGINE = 'django.contrib.sessions.backends.signed_cookies'
#SESSION_ENGINE = 'django.contrib.sessions.backends.file'
#SESSION_FILE_PATH = 'c:\\temp\\tmp\\sessions'
#SESSION_SERIALIZER = 'django.contrib.sessions.serializers.PickleSerializer'

#SESSION_ENGINE = 'mongoengine.django.sessions'

#AUTH_USER_MODEL = 'mongo_auth.MongoUser'

#MONGOENGINE_USER_DOCUMENT = 'mongoengine.django.auth.User'

LOGIN_REDIRECT_URL = '/'