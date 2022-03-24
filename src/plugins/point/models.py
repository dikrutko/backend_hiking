import peewee
from plugins.core.base_model import BaseModel

class Point(BaseModel):
    latitude = peewee.TextField()
    longitude = peewee.TextField()
