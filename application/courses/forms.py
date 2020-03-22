from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, IntegerField, validators

class CourseForm(FlaskForm):
    name = StringField("Course name", [validators.Length(min=2)])
    coursecode = StringField("Course code", [validators.Length(min=2)])
    language = StringField("Language", [validators.Length(min=2)])
    level = StringField("Level", [validators.Length(min=2)])
    spots = IntegerField("Spots")
    description = StringField("Description", [validators.Length(min=2)])
    registrationsopen = BooleanField("Registrations open")
 
    class Meta:
        csrf = False

