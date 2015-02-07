import wtforms_json
from flask import Flask

from server.routes.routes import define_routes
from server.login_manager import login_manager
from server.models import db


def create_app() -> Flask:
    """Creates and returns the Flask WSGI application
    and initializes helping components"""
    # Initialize json support for wtforms
    wtforms_json.init()

    # Define the WSGI Application object
    app = Flask(
        __name__,
        template_folder="../../",
        static_folder="../../static"
    )

    # Configurations
    app.config.from_object('server.config')

    # Initialize database with application
    db.init_app(app)
    with app.test_request_context():
        db.create_all()

    # Initialize login manager with application
    login_manager.init_app(app)

    # Setup the routes
    define_routes(app)

    return app
