from django.contrib import admin
from .models import Especialista
from .models import turnosPorEspecialista
from .models import HorarioDeAtencion
from .models import Especialidad

# Register your models here.

class EspecialidadAdmin(admin.ModelAdmin):
    display = ("nombre")
class EspecialistaAdmin(admin.ModelAdmin):
    list_display = ("nombre", "id_Especialidad")
class HorarioDeAtencionAdmin(admin.ModelAdmin):
    list_display = ("dia_de_la_setmana", "hora_inici", "hora_fi")
class turnosPorEspecialistaAdmin(admin.ModelAdmin):
    list_display = ("fecha","horarioDeInicio","horarioDeFin","id_Horario")


admin.site.register(Especialidad, EspecialidadAdmin)
admin.site.register(Especialista, EspecialistaAdmin)
admin.site.register(HorarioDeAtencion, HorarioDeAtencionAdmin)
admin.site.register(turnosPorEspecialista, turnosPorEspecialistaAdmin)
