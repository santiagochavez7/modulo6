from django import forms
from .models import Automovil  # Asegúrate de que el modelo Automovil exista en models.py

class AutomovilForm(forms.ModelForm):
    class Meta:
        model = Automovil  # Utiliza el modelo Automovil
        fields = ['marca', 'modelo', 'serial_carroceria', 'serial_motor', 'categoria', 'precio']
