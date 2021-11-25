from models.base_model import db
from models.news import News


db.connect()
db.create_tables([News])
