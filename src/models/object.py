import peewee
from models.base_model import BaseModel
from src.models.route import Route
from src.models.area import Area


class Object(BaseModel):
    name = peewee.CharField(index=True)
    description = peewee.TextField()
    latitude = peewee.FloatField()
    longitude = peewee.FloatField()
    link_on_youTube = peewee.CharField()
    type_object = peewee.CharField(index=True)
    route = peewee.ForeignKeyField(Route, backref='areas')
    area = peewee.ForeignKeyField(Area, backref='routes')