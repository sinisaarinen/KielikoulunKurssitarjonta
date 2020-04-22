from application import app, db, login_required
from flask_login import current_user
from flask import redirect, render_template, request, url_for, flash
from application.courses.models import Course, Registration
from application.courses.forms import CourseForm, RegistrationForm, CourseSearchForm
from application.locations.models import Location

@app.route("/courses", methods=['GET', 'POST'])
def courses_index():
    search = CourseSearchForm(request.form)
    if request.method == 'POST':
        return search_results(search)
    return render_template("courses/list.html", courses = Course.query.all(), form=search, find_location=Course.find_location_name())

@app.route("/courses/results")
def search_results(search):
    results = []
    search_string = search.data['search']

    if search_string:
        if search.data['select'] == 'Course name':
            query = db.session().query(Course).filter(Course.name.contains(search_string))
            results = query.all()
        elif search.data['select'] == 'Course code':
            query = db.session().query(Course).filter(Course.coursecode.contains(search_string))
            results = query.all()
        elif search.data['select'] == 'Language':
            query = db.session().query(Course).filter(Course.language.contains(search_string))
            results = query.all()
        elif search.data['select'] == 'Level':
            query = db.session().query(Course).filter(Course.level.contains(search_string))
            results = query.all()
    if not results:
        flash('No results')
        return redirect(url_for("courses_index"))
    else:
        return render_template("courses/list.html", courses = results, form=search, find_location=Course.find_location_name())

@app.route("/courses/new/")
@login_required(["ADMIN"])
def courses_form():
    return render_template("courses/new.html", form = CourseForm())

@app.route("/courses/<course_id>", methods=["POST"])
@login_required(["ORGANIZER", "ADMIN"])
def courses_update(course_id):

    course = Course.query.get(course_id)
    course.registrationsopen = True
    db.session().commit()
    
    return redirect(url_for("courses_index"))

@app.route("/courses/delete/<course_id>", methods=["POST"])
@login_required(["ADMIN"])
def courses_delete(course_id):

    course = Course.query.get(course_id)
    db.session.delete(course)
    db.session().commit()

    return redirect(url_for("courses_index"))

@app.route("/courses/edit/<course_id>", methods=["POST"])
@login_required(["ADMIN"])
def courses_edit(course_id):

    course = Course.query.get(course_id)

    form = CourseForm(request.form, obj=course)

    if not form.validate():
        return render_template("courses/edit.html", course = course, form = form)

    course.name = form.name.data
    course.coursecode = form.coursecode.data
    course.language = form.language.data
    course.level = form.level.data
    course.spots = form.spots.data
    course.course_location = form.course_location.data.id
    course.description = form.description.data
    course.registrationsopen = form.registrationsopen.data

    db.session().commit()

    return redirect(url_for("courses_index"))

@app.route("/courses/", methods=["POST"])
@login_required(["ADMIN"])
def courses_create():
    form = CourseForm(request.form)
    
    if not form.validate():
        return render_template("courses/new.html", form = form)

    courseExists = Course.query.filter_by(name=form.name.data).first()
    if courseExists:
        return render_template("courses/new.html", form = form, error = "Course already exists")
    
    courseCodeExists = Course.query.filter_by(coursecode=form.coursecode.data).first()
    if courseCodeExists:
        return render_template("courses/new.html", form = form, error = "Course code already exists")
    
    course = Course(form.name.data, form.coursecode.data, form.language.data, \
        form.level.data, form.spots.data, form.course_location.data.id, form.description.data, form.registrationsopen.data)
    course.registrationsopen = form.registrationsopen.data
    db.session().add(course)
    db.session().commit()

    return redirect(url_for("courses_index"))

@app.route("/courses/register/<course_id>")
@login_required(["CLIENT"])
def courses_register_form(course_id):

    course = Course.query.get(course_id)

    return render_template("courses/register.html", course_id=course_id, form=RegistrationForm(obj=course))

@app.route("/courses/register/<course_id>", methods=["POST"])
@login_required(["CLIENT"])
def courses_register(course_id):

    course = Course.query.get(course_id)

    form = RegistrationForm(request.form)

    if not form.validate():
        return render_template("courses/register.html", course = course, form = form)

    course = Registration(form.name.data, form.phonenumber.data, form.email.data)
    db.session().add(course)
    db.session().commit()

    return redirect(url_for("courses_index"))
