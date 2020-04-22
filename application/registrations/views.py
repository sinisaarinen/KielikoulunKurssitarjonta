from application import app, db, login_required
from flask_login import current_user
from flask import redirect, render_template, request, url_for, flash
from application.registrations.models import Registration
from application.registrations.forms import RegistrationForm, RegistrationSearchForm
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
@login_required(["CLIENT"])
def registrations_index():
    return render_template("registrations/registrations_list.html", registrations = Registration.query.all(), find_course=Registration.find_course_name(current_user.id))

@app.route("/registrations_all/", methods=['GET', 'POST'])
@login_required(["ADMIN"])
def registrations_all():

    search = RegistrationSearchForm(request.form)

    if request.method == 'POST':
        return registration_search_results(search)

    return render_template("registrations/registrations_list_all.html", registrations = Registration.query.all(), form=search)

@app.route("/registrations_all/view/", methods=['GET', 'POST'])
@login_required(["ADMIN"])
def registration_search_results(search):

    results = []
    search_string = search.data['search']

    if search_string:
        if search.data['select'] == 'Course name':
            query = db.session().query(Course).filter(Course.name.contains(search_string))
            results = query.all()
        elif search.data['select'] == 'Client name':
            query = db.session().query(Registration).filter(Registration.name.contains(search_string))
            results = query.all()
        elif search.data['select'] == 'Phone number':
            query = db.session().query(Registration).filter(Registration.phonenumber.contains(search_string))
            results = query.all()
        elif search.data['select'] == 'Email address':
            query = db.session().query(Registration).filter(Registration.email.contains(search_string))
            results = query.all()
    if not results:
        flash('No results')
        return redirect(url_for("registrations_all"))
    else:
        return render_template("registrations/registrations_list_all.html", registrations = Registration.query.all(), form=search)
