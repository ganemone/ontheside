import wtforms_json

from flask import render_template
from flask.ext.restless import APIManager
from models import User, Keyword, Language, Project
from app_factory import db, create_app

# Initialize JSON Support for WTForms
wtforms_json.init()

# Create the flask app
app = create_app()


# Create the Flask-Restless API Manager
manager = APIManager(app, flask_sqlalchemy_db=db)

project_columns = ['id', 'description',
                   'source', 'type']

# Create API endpoints, available at /api/<tablename> by default.
manager.create_api(User, methods=['GET', 'POST', 'DELETE'])
manager.create_api(Keyword, methods=['GET', 'POST', 'DELETE'])
manager.create_api(Language, methods=['GET', 'POST', 'DELETE'])
manager.create_api(Project,
                   methods=['GET', 'POST', 'DELETE'],
                   include_columns=project_columns)


@app.route("/")
def index():
    return render_template('index.html')


@app.route('/statics/<path:path>')
def handle_test(path):
    return render_template('index.html')


# Serve Static Assets
# TODO: Do this with apache or nginx
@app.route('/static/<path:file_path>.<extension>')
def static_proxy(file_path, extension):
    file_path = file_path.rstrip('/') + "." + extension
    app.logger.info('File Path: %s' % file_path)
    return app.send_static_file(file_path)


if __name__ == "__main__":
    app.run(debug=True)
