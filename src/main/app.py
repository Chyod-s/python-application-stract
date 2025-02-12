from flask import Flask
from src.main.swagger.config import api

def create_app():
    app = Flask(__name__)

    api.init_app(app)

    return app