from datetime import datetime
from marshmallow import Schema, fields, validates, ValidationError
from marshmallow.validate import Length, Range

def is_not_in_future(value):
    now = datetime.now().date()
    if value > now:
        raise ValidationError('Cannot use a date in the future!')

class AssetQuerySchema(Schema):
    """ /asset

    Parameters:
    - ticker (str)
    - date (date)
    """
    ticker = fields.Str(required=True, validate=Length(max=4))
    date = fields.Date(required=True, validate=is_not_in_future)
