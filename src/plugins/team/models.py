import peewee
from plugins.core.base_model import BaseModel

class Team(BaseModel):
    fio = peewee.CharField(index=True)
    description = peewee.TextField()
    picture = peewee.TextField()
