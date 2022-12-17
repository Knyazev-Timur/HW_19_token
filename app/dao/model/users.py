from marshmallow import Schema, fields
from app.setup_db import db


class User(db.Model):
    """ Модель БД users """
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255))
    password = db.Column(db.String)
    role = db.Column(db.String(100))


class UserSchema(Schema):
    """ CBV БД user """
    id = fields.Int(dump_only=True)
    username = fields.Str()
    password = fields.Str()
    role = fields.Str()
