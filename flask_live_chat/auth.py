from flask import render_template, Blueprint
from flask_login import LoginManager
from .models import User


login_manager = LoginManager()
auth_blueprint = Blueprint("auth", __name__, url_prefix="/auth")


@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)


@auth_blueprint.route("/register", methods=["GET", "POST"])
def register():
    return render_template("register.html")


@auth_blueprint.route("/login", methods=["GET", "POST"])
def login():
    return render_template("login.html")


@auth_blueprint.route("/logout", methods=["GET", "POST"])
def logout():
    pass
