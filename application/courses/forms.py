from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, IntegerField, validators
from wtforms.ext.sqlalchemy.fields import QuerySelectField

class CourseForm(FlaskForm):
    name = StringField("Course name", [validators.Length(min=2)])
    coursecode = StringField("Course code", [validators.Length(min=2)])
    language = StringField("Language", [validators.Length(min=2)])
    level = StringField("Level", [validators.Length(min=2)])
    spots = IntegerField("Spots")
    location_list =  QuerySelectField('location_list',query_factory=possible_locations,get_label='cityname',allow_blank=False)
    description = StringField("Description", [validators.Length(min=2)])
    registrationsopen = BooleanField("Registrations open")
 
    class Meta:
        csrf = False

