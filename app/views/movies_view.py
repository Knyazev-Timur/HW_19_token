from flask import request
from flask_restx import Resource, Namespace

from app.dao.model.movies import MovieSchema
from app.implemented import movie_service
from app.service.autorization import auth_required, admin_required

movies_ns = Namespace('movies')

movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)


@movies_ns.route("/")
class MoviesView(Resource):
    """
        Методы get и post для "/movies"
        POST movies:
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
        director = request.args.get("director_id")
        genre = request.args.get("genre_id")
        year = request.args.get("year")

        data = {
            "director_id": director,
            "genre_id": genre,
            "year": year
        }

        movies_data = movie_service.get_all(data)
        movies = movies_schema.dump(movies_data)
        return movies, 200

    @admin_required
    def post(self):
        data = request.json
        movie = movie_service.create(data)
        return "", 201, {"location": f"/movies/{movie.id}"}



@movies_ns.route("/<int:mid>")

class MovieView(Resource):
    """
    Методы get, put, delite
    для "movies/<int:uid>"
    """

    @auth_required
    def get(self, mid: int):
        movie = movie_service.get_one(mid)
        return movie_schema.dump(movie), 200

    @admin_required
    def put(self, mid: int):
        update_rows = request.json
        update_rows["id"] = mid
        movie_service.update(update_rows)
        return "Updated", 204

    @admin_required
    def patch(self, mid: int):
        update_rows = request.json
        update_rows["id"] = mid
        movie_service.update(update_rows)
        return "Updated", 204

    @admin_required
    def delete(self, mid:int):
        movie_service.delete(mid)
        return "Delete", 204
