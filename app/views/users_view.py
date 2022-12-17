from flask import request, jsonify
from flask_restx import Resource, Namespace

from app.dao.model.users import UserSchema
from app.implemented import users_service
from app.service.autorization import admin_required

users_ns = Namespace('/')

user_schema = UserSchema()
users_schema = UserSchema(many=True)


@users_ns.route("/users/")
class UserView(Resource):
    """
    Методы get и post для "/users/"
    POST user:
        {
            username: Str,
            password: Str,
            role: Str
        }
    Создает пользователя, передавая словарь.
    Возвращает словарь пользователя с хешированным паролем.
    """

    @admin_required
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
    Методы get и post для "/auth/"
    """
    def post(self):
        """
        Проверяет наличие пользователья с парой username, password в БД
        возвращает словарь: {access_token: , refresh_token: }

        POST user:
            {
                username: Str,
                password: Str
            }
            """
        data = request.json
        user_data = users_service.get_user(data)
        user = users_schema.dump(user_data)
        token = users_service.check_user(user)

        return token, 200


    def put(self):
        """
        Получает token, проверяет его валидность
        и возвращает обновленный словарь {access_token: , refresh_token: }
        или 401
        :param self:
        :return: dict
        """
        data = request.json
        return users_service.check_token(data)


