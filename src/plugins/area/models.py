import peewee
from plugins.core.base_model import BaseModel
from plugins.point.models import Point


""" class Point(BaseModel):
    latitude = peewee.DoubleField()
    longitude = peewee.DoubleField()
 """

class Area(BaseModel):
    name = peewee.CharField(index=True)
    description = peewee.TextField()
    point = peewee.ForeignKeyField(Point, backref='area')
    picture = peewee.TextField()


__all__ = [
    'Point',
    'Area',
]