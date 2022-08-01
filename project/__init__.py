from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_socketio import SocketIO
from flask_migrate import Migrate
from dotenv import load_dotenv
import os


load_dotenv()

login_manager = LoginManager()
db = SQLAlchemy()
socketio = SocketIO()
migrate = Migrate()


def create_app():
    app = Flask(__name__)
    app.config.update(
        SECRET_KEY=os.getenv("SECRET_KEY"),
        SQLALCHEMY_DATABASE_URI="sqlite:///database.db",
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
    )

    from .views import views_blueprint
    from .auth import auth_blueprint

    app.register_blueprint(views_blueprint)
    app.register_blueprint(auth_blueprint)

    login_manager.init_app(app)
    login_manager.login_view = "auth.login"
    db.init_app(app)
    socketio.init_app(app)
    migrate.init_app(app, db)

    return (app, socketio)
