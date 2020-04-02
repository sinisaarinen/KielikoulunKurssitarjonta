from application import db
from application.models import Base

class Location(Base):

    __tablename__ = "course_location"

    cityname = db.Column(db.String(144), nullable=False)
    location = db.Column(db.String(144), nullable=False)

    courses = db.relationship("Course", backref='course_location', lazy=True)

    def __init__(self, cityname, location):
        self.cityname = cityname
        self.location = location
