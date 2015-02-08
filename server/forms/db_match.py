from wtforms import Form, Field
from flask_sqlalchemy import Model
from types import FunctionType
from wtforms.validators import ValidationError


def db_match(model: Model, message: str, query_fields: list, match_fields: list=None) -> FunctionType:
    """Custom validator for matching fields in a database

    :param model: model to execute the query on
    :param message:
    :param query_fields: list of fields to query against
    :param match_fields: list of fields to match against
    :return: function
    """

    def _db_match(form: Form, field: Field) -> None:
        """Validator function called by the wtforms api

        :param form: wtform on which validation is called
        :param field: form field being validated
        :raises ValidationError: if the form field fails the validation
        :return: None
        """
        query_args = {field: form[field].data for field in query_fields}
        result = model.query.filter_by(**query_args).first()
        if result is None:
            raise ValidationError(message)
        if match_fields is not None:
            for key in match_fields:
                if not hasattr(result, key) or result.key != match_fields[key]:
                    raise ValidationError(message)

    return _db_match
