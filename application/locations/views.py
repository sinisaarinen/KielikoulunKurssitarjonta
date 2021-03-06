from application import app, db, login_required
from flask_login import current_user
from flask import redirect, render_template, request, url_for
from application.locations.models import Location
from application.locations.forms import LocationForm

@app.route("/locations", methods=["GET"])
def locations_index():
    return render_template("locations/list.html", locations = Location.query.all())

@app.route("/locations/new/")
@login_required(["ADMIN"])
def locations_form():
    return render_template("locations/new.html", form = LocationForm())

@app.route("/locations/", methods=["POST"])
@login_required(["ADMIN"])
def locations_create():
    form = LocationForm(request.form)

    if not form.validate():
        return render_template("locations/new.html", form = form)

    locationExists = Location.query.filter_by(location=form.location.data).first()
    if locationExists:
        return render_template("locations/new.html", form = form, error = "Location already exists")

    location = Location(form.cityname.data, form.location.data)

    db.session().add(location)
    db.session().commit()

    return redirect(url_for("locations_index"))

@app.route("/locations/delete/<location_id>", methods=["POST"])
@login_required(["ADMIN"])
def locations_delete(location_id):

    location = Location.query.get(location_id)
    db.session.delete(location)
    db.session().commit()

    return redirect(url_for("locations_index"))

@app.route("/locations/edit/<location_id>", methods=["POST"])
@login_required(["ADMIN"])
def locations_edit(location_id):

    location = Location.query.get(location_id)

    form = LocationForm(request.form, obj=location)

    return render_template("locations/edit.html", location = location, form = form)

    location.cityname = form.cityname.data
    location.location = form.location.data
    db.session().commit()

    return redirect(url_for("locations_update"))

@app.route("/locations/update/<location_id>", methods=["POST"])
@login_required(["ADMIN"])
def locations_update(location_id):

    location = Location.query.get(location_id)

    form = LocationForm(request.form, obj=location)

    if not form.validate():
        return render_template("locations/edit.html", location = location, form = form)

    location.cityname = form.cityname.data
    location.location = form.location.data
    db.session().commit()

    return redirect(url_for("locations_index"))

