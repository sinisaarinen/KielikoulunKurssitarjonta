from application import app, db
from flask_login import login_required
from flask import redirect, render_template, request, url_for
from application.locations.models import Location
from application.locations.forms import LocationForm

@app.route("/locations/new/")
@login_required
def locations_form():
    return render_template("locations/new.html", form = LocationForm())

@app.route("/locations/", methods=["POST"])
def locations_create():
    form = LocationForm(request.form)

    if not form.validate():
        return render_template("locations/new.html", form = form)

    location = Location(form.cityname.data, form.location.data)

    db.session().add(location)
    db.session().commit()

    return redirect(url_for("locations_index"))

@app.route("/locations", methods=["GET"])
def locations_index():
    return render_template("locations/list.html", locations = Location.query.all())

@app.route("/locations/delete/<location_id>", methods=["POST"])
@login_required
def locations_delete(location_id):

    location = Location.query.get(location_id)
    db.session.delete(location)
    db.session().commit()

    return redirect(url_for("locations_index"))

@app.route("/locations/edit/<location_id>", methods=["POST"])
@login_required
def locations_edit(location_id):

    location = Location.query.get(location_id)

    form = LocationForm(request.form)

    if not form.validate():
        return render_template("locations/edit.html", location = location, form = form)

    location.cityname = form.cityname.data
    location.location = form.location.data
    db.session.commit()

    return redirect(url_for("locations_index"))
