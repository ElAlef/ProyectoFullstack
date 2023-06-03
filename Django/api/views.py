from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .serializer import EspecialidadSerializer
from .models import Especialidad


class EspecialidadViewSet(viewsets.ModelViewSet):
 queryset=Especialidad.objects.all()
 serializer_class= EspecialidadSerializer
