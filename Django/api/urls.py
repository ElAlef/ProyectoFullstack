from django.urls import path, include
from rest_framework import routers
#from Especialidad.views import EspecialidadViewSet
from api import views

router= routers.DefaultRouter()
router.register('Especialidad',views.EspecialidadViewSet)
#----
urlpatterns = [
     path('', include(router.urls)),
]
