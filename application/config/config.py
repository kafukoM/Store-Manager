class Development(object):
    DEBUG = True
    TESTING = False
    ENV = 'development'

class Production(object):
    DEBUG = False
    TESTING = False
    ENV = 'production'

app_config = {
    'development': Development,
    'production': Production,
}
