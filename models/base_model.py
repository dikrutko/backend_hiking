import peewee
from os import environ
import urllib.parse


if 'DATABASE_URL' in environ:
    urllib.parse.uses_netloc.append('postgres')
    url = urllib.parse.urlparse(environ['DATABASE_URL'])
    db = peewee.PostgresqlDatabase(
        database=url.path[1:],
        user=url.username,
        password=url.password,
        host=url.hostname,
        port=url.port
    )
else:
    db = peewee.SqliteDatabase('people.db')


class BaseModel(peewee.Model):
    class Meta:
        database = db
