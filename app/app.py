from flask import Flask
from .apis import api
from .config import Config
from .database.create_data import make_bd
from app.database.database import db
import os


def create_app(config: Config) -> Flask:
    new_app = Flask(__name__)
    new_app.config.from_object(config)
    new_app.app_context().push()
    return new_app

def configute_app(app: Flask):
    api.init_app(app)
    db.init_app(app)
    if not(os.path.isfile('app/database/test.db')):
        make_bd()