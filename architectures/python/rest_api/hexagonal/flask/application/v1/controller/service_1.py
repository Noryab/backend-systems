import logging

from flask import request
from flask_restx import Resource
from flask_restx import reqparse

from application.v1 import Service1
from view.v1.infrastructure.mongorepo import MongoRepo

from application.v1.DTOs.namespace_entity import EntityDto
from typing import Dict, Tuple

api = EntityDto.api
_input_data = EntityDto.expected_input_model

parser = reqparse.RequestParser()
# Look only in the querystring
parser.add_argument(
    "code",
    type=str,    
    help="code",
    required=False,
    location="args",
)
parser.add_argument(
    "size",
    type=str,    
    help="size",
    required=False,
    location="args",
)
parser.add_argument(
    "price",
    type=str,    
    help="price",
    required=False,
    location="args",
)

parser.add_argument(
    "latitude",
    type=str,    
    help="latitude",
    required=False,
    location="args",
)
parser.add_argument(
    "longitude",
    type=str,    
    help="longitude",
    required=False,
    location="args",
)

# Look only in the POST body
parser.add_argument(
    "field",
    type=str,
    action="split",
    help="field",
    required=False,
    location="form",
)

# Look only in the POST body
parser.add_argument(
    "entities",
    type=list,    
    help="entities",
    required=False,
    location="json",
)


@api.route("/")
class Entity(Resource):

    @api.expect(parser, validate=True)    
    @api.response(code=409, description="Service problem")
    @api.doc("list of entities")
    def get(self) -> Tuple[Dict[str, str], int]:
        """Entity"""

        data = request.json
        print(data)
        dict_data = parser.parse_args()
        print(dict_data)
        # code = parser.parse_args()["code"]        
        # dict_data = dict(code=code, price=price, size=size, latitude=latitude, longitude=longitude)

        logging.info(f"""List all entities""")        
        response, code = Service1().get(input=dict_data, repository=MongoRepo())
        return response, code

    
    # @api.expect(_input_data, validate=True)
    @api.expect(parser, validate=True)
    @api.response(code=409, description="Service problem")
    @api.doc("post of entities")
    def post(self) -> Tuple[Dict[str, str], int]:
        """POST Entities"""

        # data = request.json
        entities = parser.parse_args()["entities"]        
        print(entities)

        logging.info(f"""post all entities""")        
        response, code = Service1().post(input=entities, repository=MongoRepo())
        return response, code
