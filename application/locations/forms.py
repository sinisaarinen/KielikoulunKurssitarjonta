from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, IntegerField, validators

class LocationForm(FlaskForm):
    cityname = StringField("City", [validators.DataRequired(message="Field cannot be empty")])
    location = StringField("Location (address, name of language school, etc.)", [validators.DataRequired(message="Field cannot be empty")])

    class Meta:
        csrf = False


