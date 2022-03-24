import peewee
from plugins.core.base_model import BaseModel
from plugins.point.models import Point

class Track(BaseModel):
    min_hight = peewee.DoubleField()
    max_hight = peewee.DoubleField()
    lenght = peewee.DoubleField()
    points = peewee.ForeignKeyField(Point, backref='track')
    #points = peewee.ManyToManyField(Point, backref='track')