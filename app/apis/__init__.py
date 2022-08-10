from flask_restx import Api

from .genres_api.genres_api import api as genres_api
from .directors_api.directors_api import api as directors_api
from .movies_api.movies_api import api as movies_api

api = Api()

api.add_namespace(genres_api)
api.add_namespace(directors_api)
api.add_namespace(movies_api)
