from application import app, db
from flask_login import login_required
from flask import redirect, render_template, request, url_for
from application.courses.models import Course
from application.courses.forms import CourseForm

@app.route("/courses", methods=["GET"])
def courses_index():
    return render_template("courses/list.html", courses = Course.query.all())

@app.route("/courses/new/")
@login_required
def courses_form():
    return render_template("courses/new.html", form = CourseForm())

@app.route("/courses/<course_id>", methods=["POST"])
@login_required
def courses_update(course_id):

    c = Course.query.get(course_id)
    c.registrationsopen = True
    db.session().commit()
    
    return redirect(url_for("courses_index"))

@app.route("/courses/", methods=["POST"])
@login_required
def courses_create():
    form = CourseForm(request.form)
    
    if not form.validate():
        return render_template("courses/new.html", form = form)

    c = Course(form.name.data, form.coursecode.data, form.language.data, \
        form.level.data, form.spots.data, form.description.data, form.registrationsopen.data)

    db.session().add(c)
    db.session().commit()

    return redirect(url_for("courses_index"))
