from django import forms
from .models import DepartementModel, ProfesseurModel
from .validators import validate_phone_number

class DepartementForm(forms.ModelForm):
    class Meta:
        model = DepartementModel
        fields = '__all__'

    numero_departement = forms.CharField(
        required=True,
        validators=[validate_phone_number]
    )


class ProfessorForm(forms.ModelForm):
    date_d_adhesion = forms.DateField(
        input_formats=["%d/%m/%Y"],
        label="Date d'adhésion (JJ/MM/AAAA)"
    )
    contact_prof = forms.CharField(
        required=True,
        validators=[validate_phone_number]
    )

    class Meta:
        model = ProfesseurModel
        fields = '__all__'

