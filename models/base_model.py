import peewee
from os import environ
from playhouse.cockroachdb import CockroachDatabase


if 'DATABASE_URL' in environ:
    db = CockroachDatabase(environ['DATABASE_URL'])
else:
    db = peewee.SqliteDatabase('people.db')


class BaseModel(peewee.Model):
    class Meta:
        database = db
