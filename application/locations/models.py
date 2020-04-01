from application import db
from application.models import Base

class Location(Base):

    cityname = db.Column(db.String(144), nullable=False)
    location = db.Column(db.String(144), nullable=False)

    courses = db.relationship("Course", backref='course', lazy=True)

    def __init__(self, cityname, location):
        self.cityname = cityname
        self.location = location
