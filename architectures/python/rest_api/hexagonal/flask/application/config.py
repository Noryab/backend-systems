import os


class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "my_precious_secret_key")
    ENV = "development"
    DEBUG = True
    JSON_SORT_KEYS = False
    POSTGRES_CONFIGURATION = {
    "POSTGRES_USER": os.environ.get("POSTGRES_USER", "noryab"),
    "POSTGRES_PASSWORD": os.environ.get("POSTGRES_PASSWORD", "noryab"),
    "POSTGRES_HOSTNAME": os.environ.get("POSTGRES_HOSTNAME", "noryab"),
    "POSTGRES_PORT": os.environ.get("POSTGRES_PORT", "noryab"),
    "APPLICATION_DB": os.environ.get("APPLICATION_DB", "noryab"),
}
    MONGO_CONFIGURATION= {
    "MONGODB_HOSTNAME": os.environ.get("POSTGRES_USER", "localhost"),
    "MONGODB_PORT": os.environ.get("POSTGRES_PASSWORD", 27017),
    "MONGODB_USER": os.environ.get("POSTGRES_HOSTNAME", "noryab"),
    "MONGODB_PASSWORD": os.environ.get("POSTGRES_PORT", "noryab"),    
    "APPLICATION_DB":os.environ.get("POSTGRES_PORT", "local"),   
}
    MONGODB_HOSTNAME =os.environ.get("POSTGRES_USER", "localhost"),
    MONGODB_PORT = os.environ.get("POSTGRES_PASSWORD", 27017)
    APPLICATION_DB = os.environ.get("POSTGRES_PORT", "local")

class DevelopmentConfig(Config):
    ENV = "development"
    JSON_SORT_KEYS = False
    COLLECTION_USER_ACTION_LOGS = "devUserActionLogs"
    LOG_LEVEL = "DEBUG"


class LocalDevelopmentConfig(Config):
    ENV = "local"
    JSON_SORT_KEYS = False
    COLLECTION_USER_ACTION_LOGS = "devUserActionLogs"
    LOG_LEVEL = "DEBUG"


class TesConfig(Config):
    ENV = "test"
    JSON_SORT_KEYS = False
    COLLECTION_USER_ACTION_LOGS = "testUserActionLogs"
    LOG_LEVEL = "DEBUG"


class ProductionConfig(Config):
    DEBUG = False
    ENV = "production"
    JSON_SORT_KEYS = False
    COLLECTION_USER_ACTION_LOGS = "userActionLogs"
    LOG_LEVEL = "INFO"


config_by_name = dict(
    development=DevelopmentConfig,
    test=TesConfig,
    local=LocalDevelopmentConfig,
    production=ProductionConfig,
)

key = Config.SECRET_KEY
