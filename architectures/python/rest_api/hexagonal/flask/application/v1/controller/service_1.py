import logging

from flask import request
from flask_restx import Resource

from application.v1 import Service1
from view.v1.infrastructure.mongorepo import MongoRepo

from application.v1.DTOs.namespace_entity import EntityDto
from typing import Dict, Tuple

api = EntityDto.api
# _input_user_action_logs = UserActionLogsDto.input_user_action_logs_model


@api.route("/")
class Entity(Resource):

    # @api.expect(_input_user_action_logs, validate=True)
    @api.response(code=409, description="Service problem")
    @api.doc("list of entities")
    def get(self) -> Tuple[Dict[str, str], int]:
        """Entity"""

        # data = request.json
        code = request.args.get("code")        
        price = request.args.get("price")
        size = request.args.get("size")
        latitude=request.args.get("latitude")
        longitude=request.args.get("longitude")
        dict_data = dict(code=code, price=price, size=size, latitude=latitude, longitude=longitude)

        logging.info(f"""List all devices""")        
        response, code = Service1().do(input=dict_data, repository=MongoRepo())
        return response, code
