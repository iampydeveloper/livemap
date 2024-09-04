# forms.py
from django import forms
from .models import Marker

class MarkerForm(forms.ModelForm):
    class Meta:
        model = Marker
        fields = ['title', 'event_type', 'description', 'latitude', 'longitude', 'image', 'video', 'start_date', 'end_date', 'is_permanent']
