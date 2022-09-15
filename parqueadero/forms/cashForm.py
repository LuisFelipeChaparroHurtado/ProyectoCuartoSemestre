from django import forms
from parqueadero.models import Cash


class cashForm(forms.ModelForm):
    class Meta:
        model = Cash
        fields = [
            'name',
            'base_money',
            'total_income',
            'total_money',
            'user',
            'opening_date',
            'state'
        ]
