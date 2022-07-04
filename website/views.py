from flask import render_template, Blueprint
from . import app


views_blueprint = Blueprint("views", __name__)


@app.route("/")
def index():
    return render_template("index.html")