"""
URL configuration for turneroWeb project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from rest_framework import routers



router = routers.DefaultRouter()
# router.register('Especilaista', vistas.Especialista, basename='Especialista')
# router.register('Especilaidad', vistas.Especialidad, basename='Especialidad')
# router.register('HorarioDeAtencion', vistas.HorarioDeAtencion, basename='HorarioDeAtencion')
# router.register('turnosPorEspecilaista', vistas.turnosPorEspecialista, basename='turnosPorEspecialista')
# router.register('ReservaDeTurno', vistas.ReservaDeTurno, basename='ReservaDeTurno')
# router.register('Pago', vistas.Pago, basename='Pago')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1', include('api.urls')),
    path('api/', include(router.urls)),
]

    # path('api/Especialista', include('api.urls')),
    # path('api/Especialidad', include('api.urls')),
    # path('api/HorarioDeAtencion', include('api.urls')),
    # path('api/turnosPorEspecialista', include('api.urls')),
    # path('api/ReservaDeTurno', include('api.urls')),
    # path('api/Pago', include('api.urls')),