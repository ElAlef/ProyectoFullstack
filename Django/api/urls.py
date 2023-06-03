from django.urls import path, include
from rest_framework import routers
#from Especialidad.views import EspecialidadViewSet
from api import views

router= routers.DefaultRouter()
router.register(r'Especialidad',views.EspecialidadViewSet)
router.register(r'Especialista',views.EspecialistaViewSet)
router.register(r'HorarioDeAtencion',views.HorarioDeAtencionViewSet)
router.register(r'turnosPorEspecialista',views.turnoPorEspecialistaViewSet)
#router.register(r'Paciente',views.PacienteViewSet)
#----
urlpatterns = [
     path('', include(router.urls)),
]
