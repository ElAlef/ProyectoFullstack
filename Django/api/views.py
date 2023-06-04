from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import UserSerializer
from .models import CustomUser
from rest_framework.permissions import IsAdminUser, AllowAny, IsAuthenticated
# Create your views here.
from rest_framework import viewsets

from .serializer import EspecialidadSerializer
from .models import Especialidad

from .serializer import EspecialistaSerializer
from .models import Especialista

from .serializer import HorarioDeAtencionSerializer
from .models import HorarioDeAtencion

from .serializer import turnosPorEspecialistaSerializer
from .models import turnosPorEspecialista

from .serializer import PacienteSerializer
from .models import Paciente

class LoginView(APIView):
    permission_classes = [AllowAny] 
    def post(self, request):
        # Recuperamos las credenciales y autenticamos al usuario
        email = request.data.get('email', None)
        password = request.data.get('password', None)
        user = authenticate(email=email, password=password)
        # Si es correcto añadimos a la request la información de sesión
        if user:
            login(request, user)
            return Response(
                UserSerializer(user).data,
                status=status.HTTP_200_OK)
        # Si no es correcto devolvemos un error en la petición
        return Response(
            status=status.HTTP_404_NOT_FOUND)


class LogoutView(APIView):
    permission_classes = [AllowAny] 
    def post(self, request):
        # Borramos de la request la información de sesión
        logout(request)

        # Devolvemos la respuesta al cliente
        return Response(status=status.HTTP_200_OK)
class SignupView(generics.CreateAPIView):
    serializer_class = UserSerializer

class verEspecialidades(viewsets.ReadOnlyModelViewSet):
    permission_classes = [AllowAny] 
    queryset = Especialidad.objects.all()
    serializer_class = EspecialidadSerializer

class verEspecialistas(viewsets.ReadOnlyModelViewSet):
    permission_classes = [AllowAny]
    queryset = Especialista.objects.all()
    serializer_class = EspecialistaSerializer

class agregarEspecialidad(APIView):
    permission_classes = [IsAdminUser]
    def post(self, request, format=None):
        serializer = EspecialidadSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,
                        status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProfileView(generics.RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated] #Solo usuarios logueados pueden ver.
    serializer_class = UserSerializer
    http_method_names = ['get', 'patch']
    def get_object(self):
        if self.request.user.is_authenticated:
            return self.request.user
class ListarUsuarios(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    http_method_names = ['get']
    permission_classes = [IsAdminUser]
    def list(self, request):
        queryset = self.get_queryset()
        serializer = UserSerializer(queryset, many=True)
        if self.request.user.is_authenticated:
            return Response(serializer.data)


class EspecialidadViewSet(viewsets.ModelViewSet):
    queryset=Especialidad.objects.all()
    serializer_class= EspecialidadSerializer

class EspecialistaViewSet(viewsets.ModelViewSet):
    queryset=Especialista.objects.all()
    serializer_class= EspecialistaSerializer

class HorarioDeAtencionViewSet(viewsets.ModelViewSet):
    queryset=HorarioDeAtencion.objects.all()
    serializer_class= HorarioDeAtencionSerializer    

class turnoPorEspecialistaViewSet(viewsets.ModelViewSet):
    queryset=turnosPorEspecialista.objects.all()
    serializer_class= turnosPorEspecialistaSerializer    

class PacienteViewSet(viewsets.ModelViewSet):
    queryset=Paciente.objects.all()
    serializer_class= PacienteSerializer    