import peewee
from models.base_model import BaseModel
from models.area import Area


class Route(BaseModel):
    name = peewee.CharField(index=True)
    description = peewee.TextField()
    lenght = peewee.DoubleField()
    high = peewee.DoubleField()
    area = peewee.ForeignKeyField(Area, backref='routes')
