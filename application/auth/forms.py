from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, validators
  
class LoginForm(FlaskForm):
    name = StringField("Name", [validators.Length(min=4)])
    username = StringField("Username", [validators.Length(min=4)])
    password = PasswordField("Password", [validators.Length(min=5)])
  
    class Meta:
        csrf = False

class SignUpForm(FlaskForm):
    name = StringField("Name", [validators.Length(min=4)])
    username = StringField("Username", [validators.Length(min=4)])
    password = PasswordField("Password", [validators.Length(min=5)])
  
    class Meta:
        csrf = False

