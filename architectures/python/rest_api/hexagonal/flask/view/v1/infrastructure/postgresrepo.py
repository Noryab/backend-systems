from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from view.v1.domain import entity_1
from view.v1.infrastructure.postgres_objects import Base, Entity


class PostgresRepo:
    def __init__(self, configuration):
        connection_string = "postgresql+psycopg2://{}:{}@{}:{}/{}".format(
            configuration["POSTGRES_USER"],
            configuration["POSTGRES_PASSWORD"],
            configuration["POSTGRES_HOSTNAME"],
            configuration["POSTGRES_PORT"],
            configuration["APPLICATION_DB"],
        )

        self.engine = create_engine(connection_string)
        Base.metadata.create_all(self.engine)
        Base.metadata.bind = self.engine

    def _create_room_objects(self, results):
        return [
            Entity.Room(
                code=q.code,
                size=q.size,
                price=q.price,
                latitude=q.latitude,
                longitude=q.longitude,
            )
            for q in results
        ]

    def list(self, filters=None):
        DBSession = sessionmaker(bind=self.engine)
        session = DBSession()

        query = session.query(Entity)

        if filters is None:
            return self._create_room_objects(query.all())

        if "code__eq" in filters:
            query = query.filter(Entity.code == filters["code__eq"])

        if "price__eq" in filters:
            query = query.filter(Entity.price == filters["price__eq"])

        if "price__lt" in filters:
            query = query.filter(Entity.price < filters["price__lt"])

        if "price__gt" in filters:
            query = query.filter(Entity.price > filters["price__gt"])

        return self._create_room_objects(query.all())
