from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from .serializer import EspecialidadSerializer
from .models import Especialidad

from .serializer import EspecialistaSerializer
from .models import Especialista

from .serializer import HorarioDeAtencionSerializer
from .models import HorarioDeAtencion

from .serializer import turnosPorEspecialistaSerializer
from .models import turnosPorEspecialista

from .serializer import PacienteSerializer
from .models import Paciente

from .serializer import ReservaDeTurnoSerializer
from .models import ReservaDeTurno

from .serializer import PagoSerializer
from .models import Pago
class EspecialidadViewSet(viewsets.ModelViewSet):
    queryset=Especialidad.objects.all()
    serializer_class= EspecialidadSerializer

class EspecialistaViewSet(viewsets.ModelViewSet):
    queryset=Especialista.objects.all()
    serializer_class= EspecialistaSerializer

class HorarioDeAtencionViewSet(viewsets.ModelViewSet):
    queryset=HorarioDeAtencion.objects.all()
    serializer_class= HorarioDeAtencionSerializer    

class turnoPorEspecialistaViewSet(viewsets.ModelViewSet):
    queryset=turnosPorEspecialista.objects.all()
    serializer_class= turnosPorEspecialistaSerializer    

class PacienteViewSet (viewsets.ModelViewSet):
    queryset=Paciente.objects.all()
    serializer_class= PacienteSerializer 

class ReservaDeTurnoViewSet(viewsets.ModelViewSet):
    queryset=ReservaDeTurno.objects.all()
    serializer_class=ReservaDeTurnoSerializer

class PagoViewSet(viewsets.ModelViewSet):
    queryset=Pago.objects.all()
    serializer_class=PagoSerializer