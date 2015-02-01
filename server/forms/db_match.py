from wtforms.validators import ValidationError


def db_match(model, message, *args, **kwargs):
    fields = kwargs.pop('match_fields', None)
    result = model.query.filter_by(*args, **kwargs).first()
    if result is None:
        raise ValidationError(message)
    if fields is not None:
        for key in fields:
            if (not hasattr(result, key) or
                    result.key != fields[key]):
                raise ValidationError(message)
