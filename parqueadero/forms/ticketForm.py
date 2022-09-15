from django import forms
from parqueadero.models import Ticket, Bay

class ticketForm(forms.ModelForm):
    #bay = forms.ModelChoiceField(queryset=Bay.objects.values_list('number',flat=True).filter(available=True).distinct())
    class Meta:
        model = Ticket
        fields = [
            'cash_id',
            'bay_id',
            'vehicle_id',
            'entry_time',
            'date'
        ]
