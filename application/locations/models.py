from application import db
from application.models import Base

class Location(Base):

    __tablename__ = 'location'

    cityname = db.Column(db.String(144), nullable=False)
    location = db.Column(db.String(144), nullable=False)

    courses = db.relationship("Course", backref="location", lazy=True, cascade="all,delete")

    def __init__(self, cityname, location):
        self.cityname = cityname
        self.location = location

    @staticmethod
    def get_location_list():
        return Location.query
