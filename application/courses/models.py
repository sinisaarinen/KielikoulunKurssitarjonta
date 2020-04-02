from application import db
from application.models import Base
from application.locations.models import Location
from flask import render_template

from sqlalchemy.sql import text

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

    @staticmethod
    def count_courses_per_location():
        stmt = text("SELECT location.cityname, COUNT(Course.id) FROM Course LEFT JOIN location ON Course.course_location=location.id GROUP BY location.cityname")
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"location.cityname":row[0], "COUNT(Course.id)":row[1]})

        return response
