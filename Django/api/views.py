from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from .serializer import EspecialidadSerializer
from .models import Especialidad

class EspecialidadViewSet(viewsets.ModelViewSet):
    queryset=Especialidad.objects.all()
    serializer_class= EspecialidadSerializer

from .serializer import EspecialistaSerializer
from .models import Especialista

class EspecialistaViewSet(viewsets.ModelViewSet):
    queryset=Especialista.objects.all()
    serializer_class= EspecialistaSerializer

from .serializer import HorarioDeAtencionSerializer
from .models import HorarioDeAtencion

class HorarioDeAtencionViewSet(viewsets.ModelViewSet):
    queryset=HorarioDeAtencion.objects.all()
    serializer_class= HorarioDeAtencionSerializer   

from .serializer import turnosPorEspecialistaSerializer
from .models import turnosPorEspecialista

class turnoPorEspecialistaViewSet(viewsets.ModelViewSet):
    queryset=turnosPorEspecialista.objects.all()
    serializer_class= turnosPorEspecialistaSerializer 

from .serializer import PacienteSerializer
from .models import Paciente

class PacienteViewSet (viewsets.ModelViewSet):
    queryset=Paciente.objects.all()
    serializer_class= PacienteSerializer 

from .serializer import RevervaDeTurnoSerializer
from .models import ReservaDeTurno

class ReservaDeTurnoViewSet(viewsets.ModelViewSet):
    queryset=ReservaDeTurno.objects.all()
    serializer_class= RevervaDeTurnoSerializer

from .serializer import PagoSerializer
from .models import Pago

class PagoViewSet(viewsets.ModelViewSet):
    queryset=Pago.objects.all()
    serializer_class= PagoSerializer
