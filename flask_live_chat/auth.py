from flask import render_template, request, Blueprint
from .forms import RegistrationForm
from .models import User
from . import login_manager


auth_blueprint = Blueprint("auth", __name__, url_prefix="/auth")


@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)


@auth_blueprint.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if request.method == "GET":
        return render_template("register.html", form=form)


@auth_blueprint.route("/login", methods=["GET", "POST"])
def login():
    return render_template("login.html")


@auth_blueprint.route("/logout", methods=["GET", "POST"])
def logout():
    pass
