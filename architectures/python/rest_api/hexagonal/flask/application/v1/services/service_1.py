from view.v1.domain.entity_1 import Entity
import json



class RefrigeratorEncoder(json.JSONEncoder):
    def default(self, o):
        try:
            to_serialize = {
                "code": str(o.code),
                "size": o.size,
                "price": o.price,
                "latitude": o.latitude,
                "longitude": o.longitude,
            }
            return to_serialize
        except AttributeError:  # pragma: no cover
            return super().default(o)

class Service1:
    def __init__(self) -> None:
        pass

    def do(self, input, repository) -> dict:

        entity = Entity(
            code=input["code"],
            size=input["size"],
            price=input["price"],
            longitude=input["longitude"],
            latitude=input["latitude"],
        )
        response = repository.insert()

        print(response["result"])
        data = json.dumps(response["result"], cls=RefrigeratorEncoder)
        return {"data": data, "status": response["status"]}, 200
