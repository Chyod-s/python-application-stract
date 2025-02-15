from src.main.app import create_app
from os import environ

def main():
    from src.main.controllers.routes import register_routes
    app = create_app()

    register_routes(app)

    SERVER_HOST = environ.get('SERVER_HOST', 'localhost')
    app.run(host=SERVER_HOST, port=5500, debug=True)

if __name__ == '__main__':
    main() 
