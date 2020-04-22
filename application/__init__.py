from flask import Flask, flash, url_for, redirect
from flask_login import current_user
app = Flask(__name__)

from flask_sqlalchemy import SQLAlchemy

import os

if os.environ.get("HEROKU"):
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
else:
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///courses.db"    
    app.config["SQLALCHEMY_ECHO"] = True

db = SQLAlchemy(app)

# login functionality
from os import urandom
app.config["SECRET_KEY"] = urandom(32)

from flask_login import LoginManager, current_user
login_manager = LoginManager()
login_manager.setup_app(app)

login_manager.login_view = "auth_login"
login_manager.login_message = "Please login to use this functionality."

# roles in login_required
from functools import wraps

def login_required(roles=None):
    if roles is None:
        roles = ["ANY"]

    def wrapper(fn):
        @wraps(fn)
        def decorated_view(*args, **kwargs):
            if not current_user:
                return login_manager.unauthorized()

            if not current_user.is_authenticated:
                return login_manager.unauthorized()
            
            unauthorized = False

            if "ANY" not in roles:
                unauthorized = True
                
                for user_role in current_user.roles():
                    if user_role in roles:
                        unauthorized = False
                        break

            if unauthorized:
                flash('You do not have permission to use this functionality.')
                return redirect(url_for('index'))
            
            return fn(*args, **kwargs)
        return decorated_view
    return wrapper

#load application content
from application import views

from application.courses import models
from application.courses import views

from application.auth import models
from application.auth import views

from application.locations import models
from application.locations import views

from application.registrations import models
from application.registrations import views

# login functionality, part 2
from application.auth.models import User

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


# database creation
try: 
    db.create_all()
except:
    pass
