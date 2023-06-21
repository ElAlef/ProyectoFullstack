from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password

from .models import Especialidad
from .models import Especialista
from .models import HorarioDeAtencion
from .models import turnosPorEspecialista
from .models import Paciente
from .models import ReservaDeTurno
from .models import Pago

class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    nombre = serializers.CharField()
    apellido = serializers.CharField()
    fechaNacimiento = serializers.CharField()
    dni = serializers.CharField()
    username = serializers.CharField(
        required=True)
    password = serializers.CharField(
        min_length=8, required=True)

    class Meta:
        model = get_user_model()
        fields = ('email', 'nombre', 'apellido', 'fechaNacimiento', 'dni', 'username', 'password')
    def validate_password(self, value):
        return make_password(value)

class EspecialidadSerializer(serializers.ModelSerializer):

    class Meta:
        model= Especialidad
        fields='__all__'
        # fields=('nombre')

class EspecialistaSerializer(serializers.ModelSerializer):
    class Meta:
        model= Especialista
        fields='__all__'
        # fields=('nombre')

class HorarioDeAtencionSerializer(serializers.ModelSerializer):
    class Meta:
        model= HorarioDeAtencion
        fields='__all__'

class turnosPorEspecialistaSerializer(serializers.ModelSerializer):
    class Meta:
        model= turnosPorEspecialista
        fields='__all__' 

class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model= Paciente
        fields='__all__'

class RevervaDeTurnoSerializer(serializers.ModelSerializer):
    class Meta:
        model= ReservaDeTurno
        fields='__all__'

class PagoSerializer(serializers.ModelSerializer):
    class Meta:
        model= Pago
        fields='__all__'              