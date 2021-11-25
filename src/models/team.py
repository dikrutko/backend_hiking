import peewee
from models.base_model import BaseModel


class Team(BaseModel):
    fio = peewee.CharField(index=True)
    description = peewee.TextField()
