# файл для создания DAO и сервисов чтобы импортировать их везде
from app.dao.directors_dao import DirectorDAO
from app.dao.ganre_dao import GenreDAO
from app.dao.movie_dao import MovieDAO
from app.dao.users_dao import UserDAO

from app.service.directors_service import DirectorService
from app.service.genre_service import GenreService
from app.service.movies_service import MovieService
from app.service.users_service import UserService

from setup_db import db


directors_dao = DirectorDAO(session=db.session)
directors_service = DirectorService(dao=directors_dao)

genre_dao = GenreDAO(session=db.session)
genre_service = GenreService(dao=genre_dao)

movie_dao = MovieDAO(session=db.session)
movie_service = MovieService(dao=movie_dao)

users_dao = UserDAO(session=db.session)
users_service = UserService(dao=users_dao)
