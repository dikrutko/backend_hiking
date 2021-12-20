import peewee
from plugins.core.base_model import BaseModel
from plugins.route.models import Area


class Route(BaseModel):
    name = peewee.CharField(index=True)
    description = peewee.TextField()
    short_description = peewee.TextField()
    lenght = peewee.DoubleField(index=True)
    height = peewee.DoubleField(index=True)
    hours = peewee.DoubleField(index=True)
    link_on_youTube = peewee.CharField()
    color_route = peewee.CharField(index=True)
    area = peewee.ForeignKeyField(Area, backref='routes')
    picture = peewee.TextField()
