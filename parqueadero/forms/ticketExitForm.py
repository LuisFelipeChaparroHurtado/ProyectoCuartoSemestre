from django import forms
from parqueadero.models import Ticket

class ticketExitForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = [
            'cash_id',
            'bay_id',
            'vehicle_id',
            'entry_time',
            'departure_time',
            'date'
        ]
