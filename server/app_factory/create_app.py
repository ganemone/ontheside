import wtforms_json
import logging
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
db = SQLAlchemy()

logging.basicConfig()
# logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)


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
    with app.app_context():
        db.create_all()

    return app
