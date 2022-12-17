from flask import Flask
from flask_restx import Api

from app.created_db import make_db
from config import Config
from app.setup_db import db

from app.views.directors_view import director_ns
from app.views.genre_view import genre_ns
from app.views.movies_view import movies_ns
from app.views.users_view import users_ns

# функция создания основного объекта app
def create_app(config):
    application = Flask(__name__)
    application.config.from_object(config)
    application.app_context().push()
    register_extensions(application)
    return application


# функция подключения расширений (Flask-SQLAlchemy, Flask-RESTx, ...)
def register_extensions(app):
    db.init_app(app)
    api = Api(app)
    api.add_namespace(director_ns)
    api.add_namespace(genre_ns)
    api.add_namespace(movies_ns)
    api.add_namespace(users_ns)
    make_db()


if __name__ == '__main__':
    app_config = Config()
    app = create_app(app_config)
    app.run(host="127.0.0.1", port=8080, debug=True)
    # app.run(host="localhost", port=10001, debug=True)
