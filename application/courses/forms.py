from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, IntegerField, validators
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from application.locations.models import Location

class CourseForm(FlaskForm):
    name = StringField("Course name", [validators.Length(min=2)])
    coursecode = StringField("Course code", [validators.Length(min=2)])
    language = StringField("Language", [validators.Length(min=2)])
    level = StringField("Level", [validators.Length(min=2)])
    spots = IntegerField("Spots")
    course_location = QuerySelectField(u'Location', query_factory=Location.get_location_list, get_label='cityname')
    description = StringField("Description", [validators.Length(min=2)])
    registrationsopen = BooleanField("Registrations open")

    class Meta:
        csrf = False

