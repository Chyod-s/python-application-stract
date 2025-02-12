from src.main.routes.routes import app as application
from os import environ

if __name__ == '__main__':
    SERVER_HOST = environ.get('SERVER_HOST', 'localhost')
    application.run(host=SERVER_HOST,port=5500, debug=True)
