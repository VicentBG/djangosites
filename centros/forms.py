from django import forms

from .models import Bono

class BonoForm(forms.ModelForm):

    class Meta:
        model = Bono
        fields = ('codigo', 'email', 'centro', 'nombre_centro', 'agente', 'nombre_agente', 
        'codpost', 'poblacion',)
