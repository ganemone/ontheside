import pytest
from flask.ext.fixtures import Fixtures
from models import User, Keyword, Language, Project
from app_factory import create_app, create_api, db
app = create_app()

api_manager = create_api(app, db, [
    {'model': User, 'methods': ['GET', 'POST', 'DELETE']},
    {'model': Keyword, 'methods': ['GET', 'POST', 'DELETE']},
    {'model': Language, 'methods': ['GET', 'POST', 'DELETE']},
    {'model': Project, 'methods': ['GET', 'POST', 'DELETE'],
        'include_columns': ['id', 'description',
                            'source', 'type']}
])

fixtures = Fixtures(app, db, True)

pytest.main('tests/')
