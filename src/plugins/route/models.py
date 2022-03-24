import peewee
from plugins.core.base_model import BaseModel
from plugins.area.models import Area


class Route(BaseModel):
    name = peewee.CharField(index=True)
    description = peewee.TextField()
    short_description = peewee.TextField()
    lenght = peewee.DoubleField(index=True)
    height = peewee.DoubleField(index=True)
    hours = peewee.DoubleField(index=True)
    #link_on_youTube = peewee.CharField()
    color_route = peewee.CharField(index=True)
    area = peewee.ForeignKeyField(Area, backref='routes')
    #points = peewee.ManyToManyField(Point, backref='routes')
