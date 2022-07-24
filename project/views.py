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
def create_room():
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
        new_room.description = form.description.data.strip()
        new_room.host = current_user
        db.session.add(new_room)
        db.session.commit()
        flash("Room successfully created.")
        return redirect(url_for("views.home"))

    return render_template("create_room.html", form=form, method="create")



@views_blueprint.route("/edit-room", methods=["GET", "POST"])
@login_required
def edit_room():
    form = CreateRoomForm()

    if form.validate_on_submit():
        print("form is submitted and room is now being edited")
        room = Room.query.filter_by(id=request.args.get("id")).first()
        room.name = form.name.data
        room.description = form.description.data.strip()
        db.session.add(room)
        db.session.commit()
        flash("Room successfully edited.")
        return redirect(url_for("views.home"))

    try:
        room = Room.query.filter_by(id=request.args.get("id")).first()
        # If current user owns this room
        if room.host == current_user:
            form.name.data = room.name
            form.description.data = room.description
            return render_template("create_room.html", form=form, method="edit")
        # If current owner doesn't own this room
        else:
            return redirect(url_for("views.home"))
    # If room doesn't exist
    except AttributeError:
        return redirect(url_for("views.home"))



@views_blueprint.route("/delete-room/<int:id>")
@login_required
def delete_room(id):
    # Will come back to this 
    return render_template("delete_room.html", id=request.args.get("id"))
