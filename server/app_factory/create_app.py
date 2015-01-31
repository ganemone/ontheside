import wtforms_json
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app():

    wtforms_json.init()

    # Define the WSGI Application object
    app = Flask(
        __name__,
        template_folder="../../",
        static_folder="../../static"
    )

    # Configurations
    app.config.from_object('config')

    db.init_app(app)
    with app.test_request_context():
        db.create_all()

    return app
