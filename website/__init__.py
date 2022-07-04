from flask import Flask
from .views import views_blueprint


app = Flask(__name__)
app.register_blueprint(views_blueprint)
