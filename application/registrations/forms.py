from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, BooleanField, IntegerField, RadioField, validators
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from application.locations.models import Location
from application.courses.models import Course
from application.registrations.models import Registration

class RegistrationForm(FlaskForm):
    name = StringField("Full name", [validators.DataRequired(message="Field cannot be empty")])
    phonenumber = StringField("Phone number", [validators.Length(min=10, max=10, message="Enter a valid phone number (10 characters)")])
    email = StringField("Email address", [validators.DataRequired(message="Enter a valid email address")])
    course_name = QuerySelectField(u'Course', query_factory=Course.get_course_list, get_label='name')

    class Meta:
        csrf = False

class RegistrationSearchForm(FlaskForm):
    choices = [("Course name", "Course name"), ("Client name", "Client name"),
               ("Phone number", "Email address"), ("Email address", "Email address"),]
    select = SelectField("Search for a registration:", choices=choices)
    search = StringField('')

