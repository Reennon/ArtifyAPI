from flask import Config


class DevConfig(Config):
    """
    Standard Developer API configuration
    """
    ENV = 'dev'
    DEBUG = True
    DEBUG_TB_ENABLE = True
    ASERT_DEBUG = True
    CACHE_TYPE = 'simple'




