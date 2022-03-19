import peewee
from plugins.core.base_model import BaseModel
from plugins.area.models import Point

class Treck(BaseModel):
    min_hight = peewee.DoubleField()
    max_hoght = peewee.DoubleField()
    color = peewee.CharField()
    points = peewee.ManuToManyField(Point, backref='treck')