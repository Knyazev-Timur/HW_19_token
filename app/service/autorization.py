import jwt

from app.constants import ALGORYTHM, SECRET
from flask import request, abort
from app.implemented import users_service


def auth_required(func):
    """
    Декорирующая функция, проверят наличие токена и его срок действия
    :param func:
    :return: dict
    """
    def wrapper(*args, **kwargs):
        if "Authorization" not in request.headers:
            abort(401)

        data = request.headers['Authorization']
        token = data.split('Bearer ')[-1]

        try:
            jwt.decode(token, SECRET, ALGORYTHM)
            users_service.check_token(token)
        except Exception as error:
            print("JWT Deocde Error", error)
            abort(401)
        return func(*args, **kwargs)

    return wrapper


def admin_required(func):
    """
       Декорирующая функция, проверят наличие токена и его срок действия,
       а так же соответствие роли администратора
       :param func:
       :return: dict
       """
    def wrapper(*args, **kwargs):
        if "Authorization" not in request.headers:
            abort(401)

        data = request.headers['Authorization']
        token = data.split('Bearer ')[-1]

        try:
            data_token = jwt.decode(token, SECRET, ALGORYTHM)
            users_service.check_token(token)
            if data_token.get("role") != "admin":
                abort(401)

        except Exception:
            abort(401)
        return func(*args, **kwargs)

    return wrapper
