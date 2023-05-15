from django.contrib import admin

from .models import Persona
from .models import Paciente
from .models import ReservaDeTurno
from .models import TurnoPorEspecialista
from .models import HorarioEspecialista
from .models import Especialista
from .models import Administrador
from .models import ObraSocial
from .models import Pago

# Register your models here.
admin.site.register(Persona,Paciente,ReservaDeTurno,
TurnoPorEspecialista,HorarioEspecialista,Especialista,
Administrador,ObraSocial,Pago)