from flask_restx import Api
from flask import Blueprint

from application.v1.services import Service1
from application.v1.controller.service_1 import api as service_1_ns


blueprint = Blueprint("api", __name__)
authorizations = {"apikey": {"type": "apiKey", "in": "header", "name": "Authorization"}}

api = Api(
    blueprint,
    title="FLASK RESTX API: Title",
    version="1.0",
    description="A flask restx web service for CRUD with hexagonal architecture",
    doc="/docs",
    authorizations=authorizations,
    security="apikey",
)

api.add_namespace(service_1_ns, path="")
