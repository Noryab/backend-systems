import pymongo
from pymongo.errors import ConnectionFailure

from view.v1.domain import entity_1


class MongoRepo:
    @classmethod
    def init(cls, configuration):
        client = pymongo.MongoClient(
            host=configuration["MONGODB_HOSTNAME"],
            port=int(configuration["MONGODB_PORT"]),
            # username=configuration["MONGODB_USER"],
            # password=configuration["MONGODB_PASSWORD"],
            # authSource="admin",
        )
        
        try:
            # The ping command is cheap and does not require auth.
            client.admin.command('ping')
        except ConnectionFailure:
            print("Server not available")

        cls.db = client[configuration["APPLICATION_DB"]]

    def _create_room_objects(self, results):
        
        return [
            entity_1.Entity(
                code=q["mac"],
                size=q["SB"],
                price=q["NOM_SUN"],
                latitude=q["mac"],
                longitude=q["SB"],
            )
            for q in [results]
        ]

    def list(self, filters=None):
        collection = self.db.refrigerators

        if filters is None:
            result = collection.find()
        else:
            mongo_filter = {}
            for key, value in filters.items():
                key, operator = key.split("__")

                filter_value = mongo_filter.get(key, {})

                if key == "price":
                    value = int(value)

                filter_value["${}".format(operator)] = value
                mongo_filter[key] = filter_value

            result = collection.find(mongo_filter)
        
        return self._create_room_objects(result)

    def insert(self, filters=None):
        collection = self.db.refrigerators
        print(collection)

        if filters is None:
            result = collection.find_one()
        else:
            mongo_filter = {}
            for key, value in filters.items():
                key, operator = key.split("__")

                filter_value = mongo_filter.get(key, {})

                if key == "price":
                    value = int(value)

                filter_value["${}".format(operator)] = value
                mongo_filter[key] = filter_value

            result = collection.find(mongo_filter)
        response = dict(status=True, result=self._create_room_objects(result))
        print(response)
        return response
