import peewee
from plugins.core.base_model import BaseModel
from plugins.area.models import Point

class Treck(BaseModel):
    min_hight = peewee.DoubleField()
    max_hight = peewee.DoubleField()
    lenght = peewee.DoubleField()
    points = peewee.ManyToManyField(Point, backref='treck')