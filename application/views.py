from flask import render_template
from application import app
from application.courses.models import Course, Registration

@app.route("/")
def index():
    return render_template("index.html", count_courses=Course.count_courses_per_location())
