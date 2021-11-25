import peewee
from models.base_model import BaseModel


class News(BaseModel):
    name = peewee.CharField(index=True)
    datetime = peewee.DateTimeField(index=True)
    description = peewee.TextField()
    lenght = peewee.FloatField()
    lenght_time = peewee.CharField()
    link_on_registration = peewee.CharField()
    price = peewee.DoubleField(default=0)
