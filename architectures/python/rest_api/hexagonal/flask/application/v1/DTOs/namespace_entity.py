from flask_restx import Namespace, fields


class EntityDto:
    api = Namespace("entity", description="device related operations")
    input_model = api.model(
        "InputModel",
        {
            "dateLog": fields.DateTime(required=True, description="fecha: string"),
            "idAction": fields.Integer(required=True, description="fecha: Integer"),
            "user": fields.String(required=True, description="user: platfor user"),
            "document": fields.Raw(),
        },
    )
    output_model = api.model(
        "OutputModel",
        {
            "error": fields.List(
                fields.Integer(required=False, description="id error web catalog")
            ),
            "exito": fields.List(
                fields.Integer(required=False, description="id error web catalog"),
                required=False,
            ),
        },
    )
    input_user_action_logs_model = api.model(
        "UserActionLogsModel",
        {
            "data": fields.List(
                fields.Nested(input_model, skip_none=True), required=True
            ),
        },
    )
