from flask import Config


class DevConfig(Config):
    """ Standard Developer API configuration

    Attributes:
        ENV (str): neme of session.
        DEBUG (bool): API start mode, which show more information about process.
        DEBUG_TB_ENABLE (bool): Enable the toolbar.
        ASERT_DEBUG (bool): activation.
        CACHE_TYPE (str): type of cache
    """
    ENV = 'dev'
    DEBUG = True
    DEBUG_TB_ENABLE = True
    ASERT_DEBUG = True
    CACHE_TYPE = 'simple'




