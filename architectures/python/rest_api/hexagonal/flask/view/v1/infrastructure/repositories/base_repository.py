import pymongo
from pymongo.errors import ConnectionFailure


class BaseMongoRepoitory:
    __name__ = "BaseMongoRepository"

    def connect(self, configuration) -> None:
        client = pymongo.MongoClient(
        host=configuration.MONGODB_HOSTNAME,
        port=int(configuration.MONGODB_PORT),
        # username=configuration["MONGODB_USER"],
        # password=configuration["MONGODB_PASSWORD"],
        # authSource="admin",
        )
    
        try:
            # The ping command is cheap and does not require auth.
            client.admin.command('ping')
        except ConnectionFailure:
            print("Server not available")

        self.db = client[configuration.APPLICATION_DB]
        return self.db



