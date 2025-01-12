from django import forms
from .models import DepartementModel, ProfesseurModel

class DepartementForm(forms.ModelForm):
    class Meta:
        model = DepartementModel
        fields = '__all__'


class ProfessorForm(forms.ModelForm):
    date_d_adhesion = forms.DateField(
        input_formats=["%d/%m/%Y"],
        label="Date d'adhésion (JJ/MM/AAAA)"
    )

    class Meta:
        model = ProfesseurModel
        fields = '__all__'

