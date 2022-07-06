from . import db


""""
relationship and backref -> placed on parent (one)
foreign key -> placed on children (to many)
"""

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String())
    password_hash = db.Column(db.String())
    # backref allows things like message.author
    messages = db.relationship("Message", backref="author")
    rooms_owned = db.relationship("Room", backref="host")
    rooms_joined = one to many


class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String())
    timesince = db.Column()
    author_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    room_id = db.Column(db.Integer, db.ForeignKey("room.id"))
    

class Room(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    description = db.Column(db.String())
    host_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    participants = one to many
    messages = db.relationship("Message", backref="room")
