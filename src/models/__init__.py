from models.base_model import db
from models.news import News
from models.area import Area
from models.route import Route
from models.team import Team
from models.object import Object
 


db.connect()
db.create_tables([
    News,
    Area,
    Route,
    Object,
    Team,
])
