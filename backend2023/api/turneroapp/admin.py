from django.contrib import admin
from .models import Especialista
from .models import turnosPorEspecialista
from .models import HorarioDeAtencion
from .models import Especialidad
from .models import Paciente
from .models import ReservaDeTurno
from .models import Pago
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

# Register your models here.

class EspecialidadAdmin(admin.ModelAdmin):
    display = ('nombre')
class EspecialistaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'id_Especialidad')
class HorarioDeAtencionAdmin(admin.ModelAdmin):
    list_display = ('dia_de_la_semana', 'hora_inici', 'hora_fi', 'id_Especialista')
class turnosPorEspecialistaAdmin(admin.ModelAdmin):
    list_display = ('fecha','horarioDeInicio','horarioDeFin','id_Horario')
class PacienteAdmin(admin.ModelAdmin):
    list_display = ('dni_paciente','nombre', 'apellidos','telefono','email')

class ReservaDeTurnoAdmin(admin.ModelAdmin):
    list_display = ('dni_paciente','id_Turnos')
class PagoAdmin(admin.ModelAdmin):
    list_display = ('monto','fecha','hora','id_Reserva')

@admin.register(get_user_model())
class CustomUserAdmin(UserAdmin):
    pass

# admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Especialidad, EspecialidadAdmin)
admin.site.register(Especialista, EspecialistaAdmin)
admin.site.register(HorarioDeAtencion, HorarioDeAtencionAdmin)
admin.site.register(turnosPorEspecialista, turnosPorEspecialistaAdmin)
admin.site.register(Paciente, PacienteAdmin)
admin.site.register(ReservaDeTurno, ReservaDeTurnoAdmin)
admin.site.register(Pago, PagoAdmin)