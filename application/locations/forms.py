from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, IntegerField, validators

def possible_locations():
    return Location.query.with_entities(location.id)

class LocationForm(FlaskForm):
    cityname = StringField("City", [validators.Length(min=2)])
    location = StringField("Location (address, name of language school, etc.)", [validators.Length(min=2)])

    class Meta:
        csrf = False


