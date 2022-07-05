"""
This file configures the app so that it can be imported and executed in main.py
"""

from flask import Flask
from .views import views_blueprint
from .auth import auth_blueprint


app = Flask(__name__)
app.register_blueprint(views_blueprint)
app.register_blueprint(auth_blueprint)
