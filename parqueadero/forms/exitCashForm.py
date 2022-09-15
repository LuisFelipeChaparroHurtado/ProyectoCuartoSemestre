from django import forms
from parqueadero.models import Cash


class cashFormExit(forms.ModelForm):
    closing_date = forms.CharField(required=False)
    class Meta:
        model = Cash
        fields = [
            'name',
            'base_money',
            'total_income',
            'total_money',
            'user',
            'opening_date',
            'closing_date',
            'state'
        ]
