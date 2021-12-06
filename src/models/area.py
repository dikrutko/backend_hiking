import peewee
from models.base_model import BaseModel


class Area(BaseModel):
    name = peewee.CharField(index=True)
    description = peewee.TextField()
    latitude = peewee.DoubleField()
    longitude = peewee.DoubleField()
    picture = peewee.TextField()
