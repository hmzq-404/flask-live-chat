from flask import render_template, flash, redirect, url_for, request, Blueprint
from flask_login import login_user, login_required, current_user, logout_user
from werkzeug.security import generate_password_hash, check_password_hash
from .forms import RegistrationForm, LoginForm
from .models import User
from . import db, login_manager


auth_blueprint = Blueprint("auth", __name__, url_prefix="/auth")


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


@auth_blueprint.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        flash("Already logged in.")
        return redirect(url_for("views.home"))

    form = RegistrationForm()
    if form.validate_on_submit():
        if User.query.filter_by(username=form.username.data).first():
            flash("A user with this username already exists. Please login.")
            return redirect(url_for("auth.login"))

        new_user = User()
        new_user.username = form.username.data
        new_user.password_hash = generate_password_hash(form.password.data, "sha256", salt_length=32)
        db.session.add(new_user)
        db.session.commit()
        login_user(new_user, remember=True)
        flash("Account successfully created.")
        return redirect(url_for("views.home"))

    return render_template("register.html", form=form)


@auth_blueprint.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        flash("Already logged in.")
        return redirect(url_for("views.home"))

    form = LoginForm()
    if form.validate_on_submit():
        existing_user = User.query.filter_by(username=form.username.data).first()

        if existing_user and check_password_hash(existing_user.password_hash, form.password.data):
            login_user(existing_user, remember=True)
            flash("Successfully logged in.")
            return redirect(url_for("views.home"))

        else:
            flash("Invalid username or password.")
            form = LoginForm()

    return render_template("login.html", form=form)


@auth_blueprint.route("/logout", methods=["GET", "POST"])
@login_required
def logout():
    logout_user()
    flash("Successfully logged out.")
    return redirect(url_for("auth.login"))
