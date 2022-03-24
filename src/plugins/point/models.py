import peewee
from plugins.core.base_model import BaseModel

class Point(BaseModel):
    latitude = peewee.DoubleField()
    longitude = peewee.DoubleField()
