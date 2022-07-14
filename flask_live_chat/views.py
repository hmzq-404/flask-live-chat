from flask import render_template, Blueprint
from flask_login  import login_required


views_blueprint = Blueprint("views", __name__)


@views_blueprint.route("/")
@login_required
def home():
    return render_template("home.html")
