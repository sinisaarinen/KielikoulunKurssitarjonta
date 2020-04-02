from application import db
from application.models import Base
from application.locations.models import Location

class Course(Base):
    
    name = db.Column(db.String(144), nullable=False)
    coursecode = db.Column(db.String(144), nullable=False)
    language = db.Column(db.String(144), nullable=False)
    level = db.Column(db.String(144), nullable=False)
    spots = db.Column(db.Integer, nullable=False)
    course_location = db.Column(db.Integer, db.ForeignKey('location.id'), nullable=False)
    description = db.Column(db.String(144), nullable=False)
    registrationsopen = db.Column(db.Boolean, nullable=False)

    def __init__(self, name, coursecode, language, level, spots, course_location, description, registrationsopen):
        self.name = name
        self.coursecode = coursecode
        self.language = language
        self.level = level
        self.spots = spots
        self.course_location = course_location
        self.description = description
        self.registrationsopen = False
