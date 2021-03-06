import peewee
from plugins.core.base_model import BaseModel


""" class Point(BaseModel):
    latitude = peewee.DoubleField()
    longitude = peewee.DoubleField()
 """

class Area(BaseModel):
    name = peewee.CharField(index=True)
    description = peewee.TextField()
    #point = peewee.ForeignKeyField(Point, backref='area')
    latitude = peewee.DoubleField()
    longitude = peewee.DoubleField()
    picture = peewee.TextField()


""" __all__ = [
    'Point',
    'Area',
] """