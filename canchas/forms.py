# forms.py

from django import forms
from .models import Horario

class HorarioForm(forms.ModelForm):
    class Meta:
        model = Horario
        fields = ['dia', 'horario_apertura', 'horario_cierre']
        widgets = {
            'dia': forms.DateInput(attrs={'type': 'date'}),
            'horario_apertura': forms.TimeInput(attrs={'type': 'time'}),
            'horario_cierre': forms.TimeInput(attrs={'type': 'time'}),
        }
