"""
Django settings for famille project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
PROJECT_DIR = os.path.dirname(__file__)
BASE_DIR = os.path.dirname(PROJECT_DIR)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: don't run with debug turned on in production!
ALLOWED_HOSTS = ["*"]
# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')


# Application definition

INSTALLED_APPS = (
    'grappelli',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.flatpages',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.sites',
    'django.contrib.staticfiles',
    'djrill',
    'bootstrap3',
    'south',
    'localflavor',
    'password_reset',
    'paypal.standard.ipn',
    'pagination',
    'postman',
    'storages',
    'tastypie',
    'tinymce',
    'verification',
    'social.apps.django_app.default',
    'famille',
)

AUTHENTICATION_BACKENDS = (
    'social.backends.open_id.OpenIdAuth',
    'social.backends.google.GoogleOpenId',
    'social.backends.google.GoogleOAuth2',
    'social.backends.google.GoogleOAuth',
    'social.backends.twitter.TwitterOAuth',
    'social.backends.yahoo.YahooOpenId',
    'django.contrib.auth.backends.ModelBackend',
)

MIDDLEWARE_CLASSES = (
    'log_request_id.middleware.RequestIDMiddleware',
    'famille.middlewares.ForceDefaultLanguageMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
    'pagination.middleware.PaginationMiddleware',
)

ROOT_URLCONF = 'famille.urls'

WSGI_APPLICATION = 'famille.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

import dj_database_url
DATABASES = {
    'default': dj_database_url.config()
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'fr'  # this is default and forced thanks to the ForceDefaultLanguageMiddleware

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(PROJECT_DIR, 'static'),
)

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(PROJECT_DIR, 'media')

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'django.contrib.staticfiles.finders.FileSystemFinder',
)

TEMPLATE_DIRS = (
    os.path.join(PROJECT_DIR, 'templates'),
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.request',
    'social.apps.django_app.context_processors.backends',
    'social.apps.django_app.context_processors.login_redirect',
    'famille.utils.context_processors.related_user',
    'famille.utils.context_processors.base',
)

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

MIN_VISIBILITY_SCORE = 0.9

bools = {
    "True": True,
    "False": False
}

for key in os.environ:
    value = os.environ[key]
    globals()[key] = bools.get(value, value)

NB_SEARCH_RESULTS = 5
POSTAL_CODE_DISTANCE = 20.0
NOREPLY_EMAIL = "ne-pas-repondre@uneviedefamille.fr"
CONTACT_EMAIL = "contact.uneviedefamille@gmail.com"
DEFAULT_FROM_EMAIL = NOREPLY_EMAIL
SERVER_EMAIL = "admin@uneviedefamille.fr"
CONTACT_ADDRESS = u"1 Sentier de l'Arpent Rouge, 92190 Meudon"
CONTACT_PHONE = "07 62 83 83 39"
ALLOW_BASIC_PLAN_IN_SEARCH = False
TARIF_RANGE = (3, 20)
if globals().get("ADMIN"):
    ADMINS = ((ADMIN, ADMIN), )

################################################################################
#                         Plugins settings                                     #
################################################################################

# flatpages
SITE_ID = 1

# tinymce
TINYMCE_DEFAULT_CONFIG = {
    'plugins': "spellchecker,paste,searchreplace",  # see http://www.tinymce.com/wiki.php/Plugins
}
TINYMCE_SPELLCHECKER = True
TINYMCE_COMPRESSOR = True

# social auth
SOCIAL_AUTH_LOGIN_REDIRECT_URL = "/mon-compte/"

# paypal
PAYPAL_RECEIVER_EMAIL = CONTACT_EMAIL
PAYPAL_SUBSCRIPTION_IMAGE = "https://www.paypal.com/fr_FR/i/btn/btn_subscribeCC_LG.gif"
PAYPAL_SUBSCRIPTION_SANDBOX_IMAGE = "https://www.sandbox.paypal.com/fr_FR/i/btn/btn_subscribeCC_LG.gif"
PAYPAL_IMAGE = "https://www.paypal.com/fr_FR/i/btn/btn_buynowCC_LG.gif"
PAYPAL_SANDBOX_IMAGE = "https://www.sandbox.paypal.com/fr_FR/i/btn/btn_buynowCC_LG.gif"

# postman
def get_user_pseudo_safely(user):
    """
    Safe wrapper to get a user pseudo, in order
    to avoid problems when importing settings.
    """
    from famille.models import get_user_pseudo  # importing here to not fail
    return get_user_pseudo(user)


POSTMAN_DISALLOW_ANONYMOUS = True
POSTMAN_DISALLOW_MULTIRECIPIENTS = False
POSTMAN_SHOW_USER_AS = get_user_pseudo_safely
POSTMAN_DISABLE_USER_EMAILING = False
POSTMAN_NOTIFIER_APP = None

# Support for X-Request-ID
# https://devcenter.heroku.com/articles/http-request-id-staging

LOG_REQUEST_ID_HEADER = 'HTTP_X_REQUEST_ID'
LOG_REQUESTS = True

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'request_id': {
            '()': 'log_request_id.filters.RequestIDFilter'
        }
    },
    'formatters': {
        'standard': {
            'format': '%(levelname)-8s [%(asctime)s] [%(request_id)s] %(name)s: %(message)s'
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'filters': ['request_id'],
            'formatter': 'standard',
        },
    },
    'loggers': {
        'log_request_id.middleware': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'django.request': {
            'handlers': ['console'],
            'level': 'ERROR',
            'propagate': False
        },
        'famille': {
            'handlers': ['console'],
            'level': 'INFO'
        }
    }
}
