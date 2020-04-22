from application import db
from application.models import Base
from application.locations.models import Location
from application.registrations.models import Registration
from flask import render_template

from sqlalchemy.sql import text

class Course(Base):
    
    name = db.Column(db.String(144), nullable=False)
    coursecode = db.Column(db.String(144), nullable=False)
    language = db.Column(db.String(144), nullable=False)
    level = db.Column(db.String, nullable=False)
    spots = db.Column(db.Integer, nullable=False)
    course_location = db.Column(db.Integer, db.ForeignKey('location.id', ondelete='CASCADE'), nullable=False)
    description = db.Column(db.String(144), nullable=False)
    registrationsopen = db.Column(db.Boolean, nullable=False)

    registrations = db.relationship("Registration", backref="Course", lazy=True, cascade="all,delete")

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
    def get_course_list():
        return Course.query


    @staticmethod
    def count_courses_per_location():
        stmt = text("SELECT location.cityname, COUNT(Course.id) FROM Course LEFT JOIN location ON Course.course_location=location.id GROUP BY location.cityname")
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"cityname":row[0], "coursecount":row[1]})

        return response

    @staticmethod
    def find_location_name():
        stmt = text("SELECT location.cityname FROM Course JOIN location ON Course.course_location=location.id GROUP BY location.cityname")
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"cityname":row[0]})

        return response
