import peewee
from plugins.core.base_model import BaseModel


class User(BaseModel):
    name = peewee.CharField(index=True)
    birthday = peewee.DateField(index=True, formats=['%Y-%m-%d'])
    phone = peewee.CharField(index=True)
    email = peewee.CharField(index=True)
    password = peewee.CharField()
    photo = peewee.TextField()
    active = peewee.BooleanField(default=False)
