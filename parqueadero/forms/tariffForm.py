from django import forms
from parqueadero.models import Tariff

class tariffForm(forms.ModelForm):
    class Meta:
        model = Tariff
        fields = [
            'cost',
        ]
