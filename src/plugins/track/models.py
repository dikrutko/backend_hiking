import peewee
from plugins.core.base_model import BaseModel

class Track(BaseModel):
    min_hight = peewee.DoubleField()
    max_hight = peewee.DoubleField()
    lenght = peewee.DoubleField()
    latitude = peewee.TextField()
    longitude = peewee.TextField()
    #points = peewee.ManyToManyField(Point, backref='track')