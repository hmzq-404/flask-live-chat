from flask import render_template, Blueprint


views_blueprint = Blueprint("views", __name__)


@views_blueprint.route("/")
def home():
    return render_template("home.html")
