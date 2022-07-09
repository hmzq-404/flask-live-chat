from sqlalchemy.sql import func
from . import db



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
    username = db.Column(db.String(16))
    password_hash = db.Column(db.String(256))
    messages = db.relationship("Message", backref="author") # message.author
    rooms_owned = db.relationship("Room", backref="host") # room.host
    rooms_joined = db.relationship("Room", secondary=room_participants, backref="participants") # room.participants


class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.Text(1024), nullable=False)
    posted = db.Column(db.DateTime(timezone=True), default=func.now())
    author_id = db.Column(db.Integer, db.ForeignKey("user.id")) 
    room_id = db.Column(db.Integer, db.ForeignKey("room.id"))
    

class Room(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, nullable=False)
    description = db.Column(db.String(512))
    host_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    messages = db.relationship("Message", backref="room") # message.room
