from project.models import User, Message, Room
from project import db


def reset_db():
    User.query.delete()
    Message.query.delete()
    Room.query.delete()
    db.session.commit()
    db.create_all()
