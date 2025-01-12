from django.core.exceptions import ValidationError
import re

def validate_phone_number(value):
    """
    Valide un numéro de téléphone composé exactement de 9 chiffres.
    """
    if not re.match(r'^\d{9}$', value):
        raise ValidationError("Le numéro de téléphone doit contenir exactement 9 chiffres.")
    return value
