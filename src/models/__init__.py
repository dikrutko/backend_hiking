from models.base_model import db
from models.news import News
from models.area import Area
from models.route import Route
 


db.connect()
db.create_tables([
    News,
    Area,
    Route,
])
