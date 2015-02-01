import wtforms_json
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager

# Create db object so it can be shared throughout the application
db = SQLAlchemy()

# Create the login manager to be shared throughout the application
login_manager = LoginManager()


def create_app():
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
    app.config.from_object('config')

    # Initialize database with application
    db.init_app(app)
    with app.test_request_context():
        db.create_all()

    # Initialize login manager with application
    login_manager.init_app(app)

    return app
