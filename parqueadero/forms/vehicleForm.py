from django import forms
from parqueadero.models import Vehicle

class vehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = [
            'person_id',
            'typevehicle_id',
            'brand',
            'model',
            'license_plate',
            'vehicle_photo',
        ]
