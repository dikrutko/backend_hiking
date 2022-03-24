import peewee
from plugins.core.base_model import BaseModel
from plugins.area.models import Area


class Place(BaseModel):
    name = peewee.CharField(index=True)
    description = peewee.TextField()
    latitude = peewee.FloatField()
    longitude = peewee.FloatField()
    type_object = peewee.CharField(index=True)
    area = peewee.ForeignKeyField(Area, backref='places')
    picture = peewee.TextField()
