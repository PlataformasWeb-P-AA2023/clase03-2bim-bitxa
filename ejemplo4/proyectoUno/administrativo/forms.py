from django.forms import ModelForm
from administrativo.models import Estudiante, NumeroTelefonico


class EstudianteForm(ModelForm): 
    class Meta:
        model = Estudiante 
        fields = ['nombre', 'apellido', 'cedula'] 


class NumeroTelefonicoForm(ModelForm): 
    class Meta:
        model = NumeroTelefonico
        fields = ['telefono', 'tipo', 'estudiante'] 


