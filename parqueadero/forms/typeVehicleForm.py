from django import forms
from parqueadero.models import TypeVehicle

class typeVehicleForm(forms.ModelForm):
    class Meta:
        model = TypeVehicle
        fields = [
            'tariff_id',
            'vehicle_class',
            'description',
        ]
