from flask_login import UserMixin
from .. import db

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    contacts = db.relationship('Book', backref='owner')
    active = db.Column(db.Boolean)
