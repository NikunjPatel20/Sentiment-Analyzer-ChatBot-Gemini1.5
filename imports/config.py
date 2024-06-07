import logging.config

MY_LOGGING_CONFIG = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'default_formatter': {
            'format': '[%(levelname)s:%(asctime)s %(module)s:%(lineno)s %(funcName)s] %(message)s'
        },
    },
    'handlers': {
        'stream_handler': {
            'class': 'logging.StreamHandler',
            'formatter': 'default_formatter',
        },
        'file_handler': {
            'class': 'logging.FileHandler',
            'filename': 'app.log',
            'formatter': 'default_formatter',
        },
    },
    'loggers': {
        'mylogger': {
            'handlers': ['stream_handler', 'file_handler'],
            'level': 'INFO',
            'propagate': True
        }
    }
}

logging.config.dictConfig(MY_LOGGING_CONFIG)
logger = logging.getLogger('mylogger')
logger.info('info log')