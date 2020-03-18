from application import app, db
from flask import redirect, render_template, request, url_for
from application.courses.models import Course

@app.route("/courses", methods=["GET"])
def courses_index():
    return render_template("courses/list.html", courses = Course.query.all())

@app.route("/courses/new/")
def courses_form():
    return render_template("courses/new.html")

@app.route("/courses/<course_id>", methods=["POST"])
def courses_update(course_id):

    c = Course.query.get(course_id)
    c.registrationsopen = True
    db.session().commit()
    
    return redirect(url_for("courses_index"))

@app.route("/courses/", methods=["POST"])
def courses_create():
    a = Course(request.form.get("name"), request.form.get("coursecode"), \
        request.form.get("language"), request.form.get("level"), request.form.get("spots"), \
        request.form.get("description"), request.form.get("registrationsopen"))

    db.session().add(a)
    db.session().commit()

    return redirect(url_for("courses_index"))
