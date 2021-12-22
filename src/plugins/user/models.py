import peewee
from plugins.core.base_model import BaseModel


class User(BaseModel):
    name = peewee.CharField(index=True)
    date = peewee.DateField(index=True)
    phone = peewee.CharField(index=True)
    email = peewee.CharField(index=True)
    password = peewee.CharField()
    checkPass = peewee.CharField()
    photo = peewee.TextField()
    promo = peewee.CharField()
