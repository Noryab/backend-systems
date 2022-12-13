import pymongo

from view.v1.domain import entity_1
from view.v1.infrastructure.repositories.base_repository import BaseMongoRepoitory


class MongoRepo(BaseMongoRepoitory):

    @classmethod
    def init(cls, configuration):
        cls.db = BaseMongoRepoitory().connect(configuration)

    def _create_entity_objects(self, results):        
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
            result = collection.find_one()
        else:
            mongo_filter = {}
            for key, value in filters.items():
                key, operator = key.split("__")

                filter_value = mongo_filter.get(key, {})
                
                filter_value["${}".format(operator)] = value
                mongo_filter[key] = filter_value

            result = collection.find(mongo_filter)
        response = dict(status=True, result=self._create_entity_objects(result))        
        return response

    def insert(self, entity, filters=None):
        collection = self.db.refrigerators        

        if filters is None:
            result = collection.find_one()
        else:
            mongo_filter = {}
            for key, value in filters.items():
                key, operator = key.split("__")

                filter_value = mongo_filter.get(key, {})
                
                filter_value["${}".format(operator)] = value
                mongo_filter[key] = filter_value

            result = collection.find(mongo_filter)
        response = dict(status=True, result=self._create_entity_objects(result))        
        return response
