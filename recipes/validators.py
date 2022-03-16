import pint
from django.core.exceptions import ValidationError


valid_unit_measurments = ['pounds', 'lbs', 'oz', 'gram']

def validate_unit_of_measure(value):
    ureg = pint.UnitRegistry() 
    single_unit = ureg[value]
    # if value not in valid_unit_measurments:
    #     raise ValidationError(f"{value} is not a valid unit of measure")