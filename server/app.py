from flask import render_template
from app_factory import create_app, create_api, db
from models import User, Keyword, Language, Project

# Create the flask app
app = create_app()

api_manager = create_api(app, db, [
    {'model': User, 'methods': ['GET', 'POST', 'DELETE']},
    {'model': Keyword, 'methods': ['GET', 'POST', 'DELETE']},
    {'model': Language, 'methods': ['GET', 'POST', 'DELETE']},
    {'model': Project, 'methods': ['GET', 'POST', 'DELETE'],
        'include_columns': ['id', 'description',
                            'source', 'type']}
])


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

some_user = User.query.filter_by(id=1)

if __name__ == "__main__":
    app.run(debug=True)
