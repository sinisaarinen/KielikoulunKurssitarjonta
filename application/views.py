from flask import render_template
from application import app
from application.courses.models import Course
from application.registrations.models import Registration

@app.route("/")
def index():
    return render_template("index.html", count_courses=Course.count_courses_per_location(), count_registrations=Registration.count_registrations_per_course())
