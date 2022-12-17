from flask import request
from flask_restx import Resource, Namespace

from app.dao.model.directors import DirectorSchema
from app.implemented import directors_service
from app.service.autorization import auth_required, admin_required

director_ns = Namespace('directors')

director_schema = DirectorSchema()
directors_schema = DirectorSchema(many=True)


@director_ns.route("/")
class DirectorView(Resource):
    """
    Методы get и post для "/director"
    POST director:
        {
            id: Int,
            title: Str,
            description: Str,
            trailer: Str,
            year: Int,
            rating: Float,
            director_id: Int,
            director_id: Int
        }
    """
    @auth_required
    def get(self):
        directors = directors_service.get_all()
        return directors_schema.dump(directors), 200

    @admin_required
    def post(self):
        data = request.json
        directors_service.create(data)

        return "", 201



@director_ns.route("/<int:uid>")
class DirectorView(Resource):
    """
    Методы get, put, delite
    для "directors/<int:uid>"
    """

    @auth_required
    def get(self, uid: int):
        director = directors_service.get_one(uid)
        return director_schema.dump(director), 200

    @admin_required
    def put(self, uid: int):
        update_rows = request.json
        update_rows["id"] = uid
        directors_service.update(update_rows)
        return "Updated", 204

    @admin_required
    def patch(self, uid: int):
        update_rows = request.json
        update_rows["id"] = uid
        directors_service.update(update_rows)
        return "Updated", 204

    @admin_required
    def delete(self, uid:int):
        directors_service.delete(uid)
        return "Delete", 204