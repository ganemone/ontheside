from flask import Flask, render_template

from flask.ext.sqlalchemy import SQLAlchemy

# Define the WSGI Application object
app = Flask(__name__, template_folder="../", static_folder="../static")

# Configurations
app.config.from_object('config')

# Define the database object which is imported
# by modules and controllers
db = SQLAlchemy(app)


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
