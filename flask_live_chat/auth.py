from flask import render_template, Blueprint


auth_blueprint = Blueprint("auth", __name__, url_prefix="/auth")


@auth_blueprint.route("/register", methods=["GET", "POST"])
def register():
    return render_template("register.html")


@auth_blueprint.route("/login", methods=["GET", "POST"])
def login():
    return render_template("login.html")


@auth_blueprint.route("/logout", methods=["GET", "POST"])
def logout():
    pass
