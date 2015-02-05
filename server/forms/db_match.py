from wtforms.validators import ValidationError


def db_match(model, message, query_fields, match_fields=None):
    """Custom validator for matching fields in a database

    :param model: model to execute the query on
    :type model: flask.ext.sqlalchemy.Model
    :param message:
    :type message: str
    :param query_fields: list of fields to query against
    :type query_fields: list
    :param match_fields: list of fields to match against
    :type match_fields: list
    :return: function
    """

    def _db_match(form, field):
        """Validator function called by the wtforms api

        :param form: wtform on which validation is called
        :type form: wtforms.form
        :param field: form field being validated
        :type field: wtforms.Field
        :raises ValidationError: if the form field fails the validation
        :return: None
        """
        query_args = {field: form[field].data for field in query_fields}
        result = model.query.filter_by(**query_args).first()
        if result is None:
            raise ValidationError(message)
        if match_fields is not None:
            for key in match_fields:
                if (not hasattr(result, key) or
                            result.key != match_fields[key]):
                    raise ValidationError(message)

    return _db_match
