from django import forms
from .models import VehicleType

class VehicleTypeForm(forms.ModelForm):
    class Meta:
        model = VehicleType
        fields = ['vehicle_type', 'fair']  # These are the fields to be included in the form

        labels = {
            'vehicle_type': 'Vehicle Type',
            'fair': 'Fair (in currency)',
        }
