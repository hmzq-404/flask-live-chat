from flask import Flask


app = Flask(__name__)


def create_app():
    from .views import views_blueprint
    
    app.register_blueprint(views_blueprint)
    return app
