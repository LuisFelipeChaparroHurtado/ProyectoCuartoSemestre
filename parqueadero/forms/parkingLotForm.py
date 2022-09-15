from django import forms
from parqueadero.models import ParkingLot

class parkingLotForm(forms.ModelForm):
    class Meta:
        model = ParkingLot
        fields = [
            'name',
            'location',
            'description',
            'image'
        ]
