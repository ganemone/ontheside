import json
import wtforms_json
from server.app_factory import create_app, create_api, db
from server.api import api_config
from flask.ext.fixtures import Fixtures

fixtures = Fixtures(create_app(), db, True)


class SimpleTestCase:

    def setup(self):
        wtforms_json.init()


class FlaskTestCase(SimpleTestCase):

    def setup(self):
        super(FlaskTestCase, self).setup()

        flaskapp = create_app()
        flaskapp.config['TESTING'] = True

        self.test_client = flaskapp.test_client()
        self.api_manager = create_api(flaskapp, db, api_config)
        self.app = flaskapp.test_client()
        self.flaskapp = flaskapp

        # Ensure that all requests have Content-Type set to "application/json"
        # unless otherwise specified.
        for methodname in ('get', 'put', 'patch', 'post', 'delete'):
            # Create a decorator for the test client request methods that adds
            # a JSON Content-Type by default if none is specified.
            def set_content_type(func):
                def new_func(*args, **kw):
                    if 'content_type' not in kw:
                        kw['content_type'] = 'application/json'
                    return func(*args, **kw)
                return new_func
            # Decorate the original test client request method.
            old_method = getattr(self.app, methodname)
            setattr(self.app, methodname, set_content_type(old_method))

    def api_request(self, method, *args, **kwargs):
        func = getattr(self.test_client, method)
        response = func(*args, **kwargs)
        json_data = json.loads(response.get_data().decode('utf-8'))
        return (response, json_data)
