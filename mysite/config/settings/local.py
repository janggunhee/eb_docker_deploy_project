import random
import string
import logging


from .base import *

# log
logger = logging.getLogger(__name__)

DEBUG = False
# logger.debug()
# logger.info()
# logger.error()

ALLOWED_HOSTS = [
    # 'localhost',
    # '127.0.0.1',
    '.elasticbeanstalk.com',
    'test.janggunhee.com',
]

# logger.debug()

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3')
    }
}

SECRET_KEY = ''.join(
    [random.choice(string.ascii_lowercase) for i in range(40)])

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'root': {
        'level': 'WARNING',
        'handlers': [
            'sentry',
        ],
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': os.path.join(ROOT_DIR, '.log', 'django.log'),
        },
        'sentry': {
            'level': 'ERROR',
            'class': 'raven.contrib.django.raven_compat.handlers.SentryHandler',
            'tags': {
                'custom-tag': 'x'
            },
        }
    },
    'loggers': {
        'django': {
            'handlers': [
                'console',
                'file',
            ],
            'level': 'DEBUG',
            'propagate': True,
        },
        'member': {
            # member.views.
        }
    },
}
