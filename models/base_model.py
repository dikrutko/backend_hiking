import peewee


db = peewee.SqliteDatabase('people.db')


class BaseModel(peewee.Model):
    class Meta:
        database = db
