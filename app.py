from server.app_factory import create_app, create_api, db
from server.api import api_config

# Create the flask app
app = create_app()

api_manager = create_api(app, db, api_config)

if __name__ == "__main__":
    app.run(debug=True)
