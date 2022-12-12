import flask
import logging


from flask import Flask
from flask_cors import CORS

from application.config import config_by_name
from view.v1.infrastructure.mongorepo import MongoRepo


logging.basicConfig(
    format="%(asctime)s || %(name)s || %(levelname)s || %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    level=logging.DEBUG,
)
logging.info(flask.__version__)


def create_app(config_name: str) -> Flask:    
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])
    MongoRepo().init(config_by_name[config_name])

    CORS(app)
    return app
