from application import app, db
from flask_login import login_required
from flask import redirect, render_template, request, url_for
from application.courses.models import Course
from application.courses.forms import CourseForm
from application.locations.models import Location

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

    course = Course.query.get(course_id)
    course.registrationsopen = True
    db.session().commit()
    
    return redirect(url_for("courses_index"))

@app.route("/courses/delete/<course_id>", methods=["POST"])
@login_required
def courses_delete(course_id):

    course = Course.query.get(course_id)
    db.session.delete(course)
    db.session().commit()

    return redirect(url_for("courses_index"))

@app.route("/courses/edit/<course_id>", methods=["POST"])
@login_required
def courses_edit(course_id):

    course = Course.query.get(course_id)

    form = CourseForm(request.form)

    if not form.validate():
        return render_template("courses/edit.html", course = course, form = form)

    course.name = form.name.data
    course.coursecode = form.coursecode.data
    course.language = form.language.data
    course.level = form.level.data
    course.spots = form.spots.data
    course.description = form.spots.data
    course.registrationsopen = form.registrationsopen.data

    db.session.commit()    

   
    return redirect(url_for("courses_index"))

@app.route("/courses/", methods=["POST"])
@login_required
def courses_create():
    form = CourseForm(request.form)
    
    if not form.validate():
        return render_template("courses/new.html", form = form)

    course = Course(form.name.data, form.coursecode.data, form.language.data, \
        form.level.data, form.spots.data, form.description.data, form.registrationsopen.data)
    course.registrationsopen = form.registrationsopen.data
    course.location.id = Location.query.get(id)
    formm = CourseForm(request.POST, obj=course.location.id)
    formm.course_location.choices = [(l.id, l.cityname) for l in Location.query.order_by('cityname')]
    db.session().add(course)
    db.session().commit()

    return redirect(url_for("courses_index"))
