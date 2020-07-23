import os

from fb_post_learning.settings.base import *
from fb_post_learning.settings.base_swagger_utils import *


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '^d*66-07r)+k7-rvvhc1c2!j*cyud&a)v69_8+d7*xg&q!5gk#'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# swagger utils

PRINT_REQUEST_RESPONSE_TO_CONSOLE = True

################# Databases ##################


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases
import uuid

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        'TEST': {
            'NAME': '/tmp/%s.sqlite3' % str(uuid.uuid4()),
            'ENGINE': 'django.db.backends.sqlite3'
        }
    }
}

# ********************** Static Files *************************
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/


STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

LOGGING['loggers'].update(
    {

        '': {
            'handlers': ['console', 'sentry'],
            'level': 'INFO',
            'propagate': False,
        },
        'dsu.error': {
            'handlers': ['console', 'sentry'],
            'level': 'ERROR',
            'propagate': False,
        },
        'dsu.debug': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'LogAPI200': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'LogAPINON200': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'LogNONAPI': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'pynamodb': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': False,
        },
        'django.db.backends': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': False,
        }

    }
)

LOGGING['handlers'] = {
    'sentry': {
        'level': 'ERROR',
        'class': 'raven.contrib.django.handlers.SentryHandler',
        'filters': ["request_id", "user_id", "path_info",
                        "aws_request_id", "stage"]
    },
    'console': {
        'level': 'DEBUG',
        'class': 'logging.StreamHandler',
        'formatter': 'console',
        'filters': ["request_id", "user_id", "path_info",
                        "aws_request_id", "stage"]
    }
}