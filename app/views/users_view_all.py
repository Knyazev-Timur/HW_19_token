from flask import request, jsonify
from flask_restx import Resource, Namespace

from app.dao.model.users import UserSchema
from app.implemented import users_service

users_ns = Namespace('/')

user_schema = UserSchema()
users_schema = UserSchema(many=True)


@users_ns.route("/users/")
class UserView(Resource):
    """
    Методы get и post для "/users/"
    POST user:
        {
            id: Int,
            username: Str,
            password: Str,
            role: Str
        }
    Создает пользователя, передавая словарь.
    Возвращает словарь пользователя с хешированным паролем.
    """
    def get(self):
        users = users_service.get_all()
        return users_schema.dump(users), 200

    def post(self):
        data = request.json
        hash_pass = users_service.create(data)
        return hash_pass, 201


@users_ns.route("/auth/")
class UserView(Resource):
    """
    Методы get и post для "/users/"
    POST user:
        {
            id: Int,
            username: Str,
            password: Str,
            role: Str
        }
    Создает пользователя, передавая словарь.
    Возвращает словарь пользователя с хешированным паролем.
    """
    def post(self):
        data = request.json
        return users_service.check_user(data)

    def put(self):
        data = request.json
        # data["id"] = uk
        return users_service.check_token(data)
        # return "Updated", 204


# {"id": 1, "username": "vasya", "password": "my_little_pony", "role": "user"}