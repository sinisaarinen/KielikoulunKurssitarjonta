from application import app, db, login_required
from flask_login import current_user
from flask import redirect, render_template, request, url_for, flash
from application.registrations.models import Registration
from application.registrations.forms import RegistrationForm
from application.locations.models import Location
from application.courses.models import Course
from application.courses.forms import CourseForm

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

    course = Registration(form.name.data, form.phonenumber.data, form.email.data, form.course_name.data.id)
    course.account_id = current_user.id
    db.session().add(course)
    db.session().commit()

    return redirect(url_for("registrations_index"))

@app.route("/registrations/", methods=["GET"])
def registrations_index():
    return render_template("courses/registrations_list.html", registrations = Registration.query.all(), find_course=Registration.find_course_name(current_user.id))

