from flask_restx import Namespace, fields


class EntityDto:
    api = Namespace("entity", description="device related operations")
    input_model = api.model(
        "InputModel",
        {
            "code": fields.DateTime(required=True, description="fecha: string"),
            "size": fields.Float(required=True, description="fecha: Integer"),
            "price": fields.Float(required=True, description="user: platfor user"),
            "latitude": fields.Float(),
            "longitude": fields.Float(),
            "longitude": fields.Float(),
        },
    )
    expected_input_model = api.model(
        "ExpectedModel",
        {            
            "entities": fields.List(
                fields.Nested(input_model, skip_none=True), required=False
            ),
        },
    )

    output_model = api.model(
        "OutputModel",
        {
            "codes": fields.List(
                fields.Integer(required=False, description="id error web catalog")
            ),
            "fields": fields.List(
                fields.Integer(required=False, description="id error web catalog"),
                required=False,
            ),
        },
    )
    response_model = api.model(
        "ResponseModel",
        {
            "status": fields.String(required=True, description="user: platfor user"),
            "error": fields.String(required=True, description="user: platfor user"),
            "message": fields.String(required=True, description="user: platfor user"),
            "data": fields.List(
                fields.Nested(output_model, skip_none=True), required=True
            ),
        },
    )
