from wtforms.validators import ValidationError


def db_match(model, message, query_fields, match_fields=None):
    """Custom validator for matching fields in a database"""
    def _db_match(form, field):
        """Validator function called by the wtforms api"""
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
