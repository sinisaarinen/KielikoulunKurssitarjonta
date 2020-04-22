from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, BooleanField, IntegerField, RadioField, validators
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from application.locations.models import Location
from application.courses.models import Course
from application.registrations.models import Registration

class CourseForm(FlaskForm):
    name = StringField("Course name", [validators.DataRequired(message="Field cannot be empty")])
    coursecode = StringField("Course code", [validators.DataRequired(message="Field cannot be empty")])
    language = StringField("Language", [validators.DataRequired(message="Field cannot be empty")])
    level = RadioField("Level", [validators.DataRequired(message="Choose a level")], choices=[("Beginner", "Beginner"), ("Intermediate", "Intermediate"), ("Advanced", "Advanced")])
    spots = IntegerField("Spots", [validators.NumberRange(min=5, max=100, message="Number must be between 5 and 100")])
    course_location = QuerySelectField(u'Location', query_factory=Location.get_location_list, get_label='cityname')
    description = StringField("Description", [validators.DataRequired(message="Field cannot be empty")])
    registrationsopen = BooleanField("Registrations open")

    class Meta:
        csrf = False

class CourseSearchForm(FlaskForm):
    choices = [("Course name", "Course name"), ("Course code", "Course code"),
               ("Language", "Language"), ("Level", "Level"),]
    select = SelectField("Search for a course:", choices=choices)
    search = StringField('')
