from sqlalchemy.sql import func
from .field_constraints import user_constraints, message_constraints, room_constraints
from . import db
import json


# Each column has foreign keys that refer to other tables
room_participants = db.Table("room_participants",
    db.Column("room_id", db.Integer, db.ForeignKey("room.id")),
    db.Column("participant_id", db.Integer, db.ForeignKey("user.id"))
)


"""
relationship and backref -> placed on parent (one)
foreign key -> placed on children (to many)
"""
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(user_constraints["username"]["max"]))
    password_hash = db.Column(db.String(user_constraints["password_hash"]["max"]))
    messages = db.relationship("Message", backref="author") # message.author
    rooms_owned = db.relationship("Room", backref="host") # room.host
    # rooms_owned will not be included in rooms_joined
    rooms_joined = db.relationship("Room", secondary=room_participants, backref="participants") # room.participants


class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.Text(message_constraints["body"]["max"]), nullable=False)
    posted = db.Column(db.DateTime(timezone=True), default=func.now())
    author_id = db.Column(db.Integer, db.ForeignKey("user.id")) 
    room_id = db.Column(db.Integer, db.ForeignKey("room.id"))
    

class Room(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(room_constraints["name"]["max"]), unique=True, nullable=False)
    description = db.Column(db.String(room_constraints["description"]["max"]))
    host_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    messages = db.relationship("Message", backref="room") # message.room
    