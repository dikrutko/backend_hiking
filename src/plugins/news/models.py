import peewee
from plugins.core.base_model import BaseModel

class News(BaseModel):
    name = peewee.CharField(index=True)
    datetime = peewee.DateTimeField(index=True, formats=['%Y-%m-%d %H:%M:%S'])
    description = peewee.TextField()
    lenght = peewee.FloatField(index=True)
    lenght_time = peewee.CharField(index=True)
    link_on_registration = peewee.CharField()
    price = peewee.DoubleField(default=0, index=True)
    picture = peewee.TextField()
