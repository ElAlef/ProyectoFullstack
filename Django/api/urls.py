from django.urls import path, include
from rest_framework import routers
#from Especilaidad.views import EspecialidadViewSet
from turneroWeb  import views

router= routers.DefaultRouter()
router.register(r'Especialidad',views.EspecialidadViewSet)
#----
urlpatterns = [
     path('', include(router.urls)),
]
