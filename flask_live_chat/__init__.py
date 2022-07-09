from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
import os
from .views import views_blueprint
from .auth import auth_blueprint



load_dotenv()


app = Flask(__name__)
app.config.update(
    SECRET_KEY=os.getenv("SECRET_KEY"), 
    SQLALCHEMY_DATABASE_URI="sqlite:///database.db"
)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

app.register_blueprint(views_blueprint)
app.register_blueprint(auth_blueprint)