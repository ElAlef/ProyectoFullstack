from django.contrib import admin
from .models import Especialista
from .models import turnosPorEspecialista
# Register your models here.

class turnosPorEspecialistaAdmin(admin.ModelAdmin):
    list_display = ("fecha","horarioDeInicio","horarioDeFin","horarioDeTurno")
class EspecialistaAdmin(admin.ModelAdmin):
    list_display = ("nombre", "especialidad","horariosDeAtencion","id_Turnos")


admin.site.register(Especialista, EspecialistaAdmin)
admin.site.register(turnosPorEspecialista, turnosPorEspecialistaAdmin)
