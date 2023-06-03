from rest_framework import serializers

from .models import Especialidad
from .models import Especialista
from .models import HorarioDeAtencion
from .models import turnosPorEspecialista
from .models import Paciente

class EspecialidadSerializer(serializers.ModelSerializer):
    class Meta:
        model= Especialidad
        #fields='__all__'
        fields=('nombre')

class EspecialistaSerializer(serializers.ModelSerializer):
    class Meta:
        model= Especialista
        #fields='__all__'
        fields=('nombre')


class HorarioDeAtencionSerializer(serializers.ModelSerializer):
    class Meta:
        model= HorarioDeAtencion
        fields=('dia_de_la_semana')

class turnosPorEspecialistaSerializer(serializers.ModelSerializer):
    class Meta:
        model= turnosPorEspecialista
        fields=('fecha') 

class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model= Paciente
        fields=('nombre')