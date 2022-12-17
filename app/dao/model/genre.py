from marshmallow import Schema, fields
from app.setup_db import db

class Genre(db.Model):
    """ Модель БД genre """
    __tablename__ = 'genre'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))


class GenreSchema(Schema):
    """ CBV БД genre """
    id = fields.Int(dump_only=True)
    name = fields.Str()
