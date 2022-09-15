from django import forms
from parqueadero.models import Person

class personForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = [
            'name',
            'surname',
            'doc_number',
            'phone_number',
        ]
