from flask import request
from flask_restx import Resource, Namespace
from app.implemented import genre_service

from app.dao.model.genre import GenreSchema
from app.service.autorization import auth_required, admin_required

genre_ns = Namespace('genres')

genre_schema = GenreSchema()
genres_schema = GenreSchema(many=True)


@genre_ns.route("/")
class GenreView(Resource):
    """
    Методы get и post для "/genres"
    POST genre:
        {
            id: Int,
            title: Str,
            description: Str,
            trailer: Str,
            year: Int,
            rating: Float,
            director_id: Int,
            genre_id: Int
        }
    """

    @auth_required
    def get(self):
        genres = genre_service.get_all()
        return genres_schema.dump(genres), 200

    @admin_required
    def post(self):
        data = request.json
        genre_service.create(data)
        return "", 201



@genre_ns.route("/<int:gid>")
class GenreView(Resource):
    """
    Методы get, put, delite
    для "genres/<int:uid>"
    """

    @auth_required
    def get(self, gid: int):
        genre = genre_service.get_one(gid)
        return genre_schema.dump(genre), 200

    @admin_required
    def put(self, gid: int):
        update_rows = request.json
        update_rows["id"] = gid
        genre_service.update(update_rows)
        return "Updated", 204

    @admin_required
    def patch(self, gid: int):
        update_rows = request.json
        update_rows["id"] = gid
        genre_service.update(update_rows)
        return "Updated", 204

    @admin_required
    def delete(self, gid:int):
        genre_service.delete(gid)
        return "Delete", 204