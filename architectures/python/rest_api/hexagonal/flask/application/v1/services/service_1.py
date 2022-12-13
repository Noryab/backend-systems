from view.v1.domain.entity_1 import Entity
import json



class EntityEncoder(json.JSONEncoder):
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

    def to_dict(self):
            """
            to_dict method to dump public attributes.
            """

            self._jsonable = (int, list, str, dict)

            _dict = dict()
            for attr in dir(self):
                value = getattr(self, attr)
                if attr.startswith("_") or attr in getattr(EntityEncoder, "_ignored_json_keys", []):
                    continue
                elif isinstance(value, self._jsonable) or value is None or hasattr(value, 'to_dict'):
                    # to_dict method is used as serialization method.
                    value = value
                else:
                    continue
                _dict[attr] = value
            return _dict            


class Service1:
    def __init__(self) -> None:
        pass

    def get(self, input, repository) -> dict:

        entity = Entity(
            code=input["code"],
            size=input["size"],
            price=input["price"],
            longitude=input["longitude"],
            latitude=input["latitude"],
        )
        response = repository.list()

        print(response["result"])
        # data = json.dumps(response["result"], cls=EntityEncoder)
        # data = dict(map(EntityEncoder().default, response["result"]))
        data = [element.to_dict() for element in response["result"]]
        data = response["result"][0].to_dict()

        return {"data": data, "status": response["status"]}, 200

    def post(self, input, repository) -> dict:

        entity = [Entity.from_dict(element) for element in input]                    
        response = repository.insert(entity)
        
        return {"data": None, "status": response["status"]}, 200
