from flask_restless import ProcessingException
from flask_login import current_user

from server.forms import RegistrationForm
from server.models import User, Keyword, Language, Project


def project_owned_by_current_user(instance_id):
    """Preprocessor for api project DELETE endpoint which
    ensures project can only be deleted by a user with role 'owner'

    :param instance_id: id of instance to be deleted
    :raises ProcessingException: if current_user is not an owner of the project
    :return:None
    :rtype: None
    """
    project = Project.query.filter_by(id=instance_id).first()
    owners = project.get_owners()
    if current_user not in owners:
        raise ProcessingException('Only project owners can delete projects')


def validate_with_form(form_class):
    """Preprocessor which validates a request based on a form"""
    def preprocessor(data=None):
        form = form_class.from_json(data)
        if not form.validate():
            raise ProcessingException

    return preprocessor


def remove_props(props):
    def preprocessor(data=None):
        for prop in props:
            del data[prop]

    return preprocessor


def login_required_preprocessor(*args, **kwargs):
    if not current_user.is_authenticated():
        raise ProcessingException(
            description='Not Authorized',
            code=401
        )
    return True


api_config = [
    {
        'model': User,
        'methods': ['GET', 'POST', 'DELETE'],
        'preprocessors': {
            'POST': [
                validate_with_form(RegistrationForm),
                remove_props(['confirm'])
            ],
        }
    },
    {
        'model': Keyword,
        'methods': ['GET', 'POST', 'DELETE'],
        'preprocessors': {
            'POST': [login_required_preprocessor],
            'DELETE': [login_required_preprocessor]
        }
    },
    {
        'model': Language,
        'methods': ['GET', 'POST', 'DELETE'],
        'preprocessors': {
            'POST': [login_required_preprocessor],

        }
    },
    {
        'model': Project,
        'methods': ['GET', 'POST', 'DELETE'],
        'preprocessors': {
            'POST': [login_required_preprocessor],
            'DELETE': [
                login_required_preprocessor,
                project_owned_by_current_user
            ]

        },
        'include_columns': ['id',
                            'name',
                            'description',
                            'source',
                            'type',
                            'users',
                            'keywords',
                            'languages',
                            'favorite_users']
    }
]
