import peewee
from models.base_model import BaseModel
from models.area import Area


class Route(BaseModel):
    name = peewee.CharField(index=True)
    description = peewee.TextField()
    short_description = peewee.TextField()
    lenght = peewee.DoubleField(index=True)
    height = peewee.DoubleField(index=True)
    hours = peewee.CharField()
    link_on_youTube = peewee.CharField()
    color_route = peewee.CharField(index=True)
    area = peewee.ForeignKeyField(Area, backref='routes')
