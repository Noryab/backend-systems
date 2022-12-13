import uuid
import dataclasses


@dataclasses.dataclass
class Entity:
    # code: uuid.UUID
    code: str
    size: int
    price: float
    longitude: float
    latitude: float    

    @classmethod
    def from_dict(self, d):
        return self(**d)

    def to_dict(self):
        return dataclasses.asdict(self)
