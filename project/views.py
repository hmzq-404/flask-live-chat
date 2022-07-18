from flask import render_template, Blueprint, flash, redirect, url_for, request
from flask_login import login_required, current_user
from .forms import CreateRoomForm
from .models import Room
from . import db


views_blueprint = Blueprint("views", __name__)


@views_blueprint.route("/")
@login_required
def home():
    rooms = Room.query.all()
    return render_template("home.html", rooms=rooms)


@views_blueprint.route("/create-room", methods=["GET", "POST"])
@login_required
def create_room(name="", description=""):
    # Prefill data
    form = CreateRoomForm(
        name=request.args.get("name"), description=request.args.get("description")
    )

    if form.validate_on_submit():
        # If a room with that name already exists
        if Room.query.filter_by(name=form.name.data).first():
            flash("A room with this name already exists.")
            return redirect(
                url_for(
                    "views.create_room",
                    name=form.name.data,
                    description=form.description.data,
                )
            )

        new_room = Room()
        new_room.name = form.name.data
        new_room.description = form.description.data
        new_room.host = current_user
        db.session.add(new_room)
        db.session.commit()
        flash("Room successfully created.")
        return redirect(url_for("views.home"))

    return render_template("create_room.html", form=form)


@views_blueprint.route("/delete-room")
@login_required
def delete_room():
    pass
