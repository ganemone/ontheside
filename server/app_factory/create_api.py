from flask_restless import APIManager


def create_api(app, db, endpoints):
    # Create the Flask-Restless API Manager
    manager = APIManager(app, flask_sqlalchemy_db=db)

    # Create API endpoints, available at /api/<tablename> by default.
    for endpoint in endpoints:
        manager.create_api(**endpoint)

    return manager
