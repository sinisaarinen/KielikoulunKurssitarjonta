from application import db
from application.models import Base
from application.locations.models import Location
from flask import render_template

from sqlalchemy.sql import text

class Registration(Base):

    name = db.Column(db.String(144), nullable=False)
    phonenumber = db.Column(db.String, nullable=False)
    email = db.Column(db.String(144), nullable=False)

    course_name = db.Column(db.Integer, db.ForeignKey('course.id', ondelete='CASCADE'), nullable=False)
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'),
                           nullable=False)

    def __init__(self, name, phonenumber, email, course_name):
        self.name = name
        self.phonenumber = phonenumber
        self.email = email
        self.course_name = course_name

    @staticmethod
    def find_course_name(current_id):
        stmt = text("SELECT Course.name, Registration.name, Registration.phonenumber, Registration.email, Registration.id FROM Registration JOIN Course ON Registration.course_name=Course.id LEFT JOIN account ON account.id=Registration.account_id WHERE account.id = :current GROUP BY Course.name, Registration.name, Registration.phonenumber, Registration.email, Registration.id").params(current = current_id)
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"course_name":row[0], "name":row[1], "phonenumber":row[2], "email":row[3], "id":row[4]})

        return response

    @staticmethod
    def find_coursename():
        stmt = text("SELECT Course.name, Course.id FROM Registration JOIN Course ON Registration.course_name=Course.id GROUP BY Course.name, Course.id")
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"coursename":row[0], "id":row[1]})

        return response

    @staticmethod
    def count_registrations_per_course():
        stmt = text("SELECT course.name, COUNT(Registration.id) FROM Registration LEFT JOIN course ON Registration.course_name=course.id GROUP BY course.name")
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"coursename":row[0], "registrationcount":row[1]})

        return response

    @staticmethod
    def most_popular_courses():
        stmt = text("SELECT course.name, COUNT(Registration.id) FROM Registration LEFT JOIN course ON Registration.course_name=course.id GROUP BY course.name ORDER BY Count(Registration.id) DESC LIMIT 3")
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"coursename":row[0], "registrationcount":row[1]})

        return response
