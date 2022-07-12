from flask import Flask
from dotenv import load_dotenv
import os


load_dotenv()


def create_app():
    app = Flask(__name__)
    app.config.update(
        SECRET_KEY=os.getenv("SECRET_KEY"), 
        SQLALCHEMY_DATABASE_URI="sqlite:///database.db"
    )

    from .views import views_blueprint
    from .auth import auth_blueprint

    app.register_blueprint(views_blueprint)
    app.register_blueprint(auth_blueprint)

    from .models import db, migrate
    from .auth import login_manager

    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)

    return app
