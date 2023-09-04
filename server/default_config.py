"""Default application settings"""


class DefaultConfig:
    """Default configuration"""
    API_TITLE = "Planets API"
    API_VERSION = 0.1
    OPENAPI_VERSION = "3.0.3"
    OPENAPI_URL_PREFIX = "/"
    OPENAPI_SWAGGER_UI_PATH = "/swagger-ui"
    OPENAPI_SWAGGER_UI_URL = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = "sqlite:///app.db"
    PROPAGATE_EXCEPTIONS = True
    DEBUG = True
