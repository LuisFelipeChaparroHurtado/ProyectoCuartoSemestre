from django import forms
from parqueadero.models import Bay

class bayForm(forms.ModelForm):
    class Meta:
        model = Bay
        fields = [
            'par_id',
            'number',
            'available'
        ]
