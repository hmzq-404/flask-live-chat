from flask import render_template, Blueprint


views_blueprint = Blueprint("views", __name__)


@views_blueprint.route("/")
def index():
    return render_template("index.html")