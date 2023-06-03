from django.urls import path, include
from rest_framework import routers

<<<<<<< HEAD
from api import views
=======
#from Especialidad.views import EspecialidadViewSet
from api import views

router= routers.DefaultRouter()
router.register(r'Especialidad',views.EspecialidadViewSet)
router.register(r'Especialista',views.EspecialistaViewSet)
router.register(r'HorarioDeAtencion',views.HorarioDeAtencionViewSet)
router.register(r'turnosPorEspecialista',views.turnoPorEspecialistaViewSet)

#from Especilaidad.views import EspecialidadViewSet
from turneroWeb  import views
>>>>>>> RamaAlejandro

router= routers.DefaultRouter()
router.register(r'Especialidad',views.EspecialidadViewSet)

#----
urlpatterns = [
     path('', include(router.urls)),
]
