import json
import uuid

from template.view.v1.serializers.encoder import EntityJsonEncoder
from template.view.v1.domain.entity_1 import Entity


def test_serialize_domain_room():
    code = uuid.uuid4()

    room = Entity(
        code=code,
        size=200,
        price=10,
        longitude=-0.09998975,
        latitude=51.75436293,
    )

    expected_json = f"""
        {{
            "code": "{code}",
            "size": 200,
            "price": 10,
            "longitude": -0.09998975,
            "latitude": 51.75436293
        }}
    """

    json_room = json.dumps(room, cls=EntityJsonEncoder)

    assert json.loads(json_room) == json.loads(expected_json)
