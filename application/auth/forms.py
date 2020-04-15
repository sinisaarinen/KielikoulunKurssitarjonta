from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, RadioField, validators
  
class LoginForm(FlaskForm):
    name = StringField("Name", [validators.DataRequired()])
    username = StringField("Username", [validators.DataRequired("Enter username")])
    password = PasswordField("Password", [validators.DataRequired("Enter password")])
  
    class Meta:
        csrf = False

class SignUpForm(FlaskForm):
    name = StringField("Name", [validators.DataRequired(message="Name cannot be empty")])
    username = StringField("Username", [validators.DataRequired(), validators.Length(min=6, max=12, message="Username needs to be between 6 and 12 characters")], render_kw={'maxlength': 12})
    password = PasswordField("Password", [validators.Length(min=5, max=20, message="Password needs to be between 5 and 20 characters")])
    role = RadioField("Role", [validators.DataRequired(message="Choose a role")],
                      choices=[("ADMIN", "Admin"), ("ORGANIZER", "Organizer"), ("CLIENT", "Client")])
  
    class Meta:
        csrf = False

