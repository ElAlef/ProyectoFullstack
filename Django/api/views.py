from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import UserSerializer
from .models import Especialidad, Especialista, HorarioDeAtencion, turnosPorEspecialista, Paciente, ReservaDeTurno, Pago, CustomUser
from rest_framework.permissions import IsAdminUser, AllowAny, IsAuthenticated
from rest_framework import viewsets
# Create your views here.
from rest_framework import viewsets

from .serializer import EspecialidadSerializer
from .models import Especialidad

class EspecialidadViewSet(viewsets.ModelViewSet):
    queryset=Especialidad.objects.all()
    serializer_class= EspecialidadSerializer

from .serializer import EspecialistaSerializer
from .models import Especialista

class EspecialistaViewSet(viewsets.ModelViewSet):
    queryset=Especialista.objects.all()
    serializer_class= EspecialistaSerializer

from .serializer import HorarioDeAtencionSerializer
from .models import HorarioDeAtencion

class HorarioDeAtencionViewSet(viewsets.ModelViewSet):
    queryset=HorarioDeAtencion.objects.all()
    serializer_class= HorarioDeAtencionSerializer   

from .serializer import turnosPorEspecialistaSerializer
from .models import turnosPorEspecialista

class turnoPorEspecialistaViewSet(viewsets.ModelViewSet):
    queryset=turnosPorEspecialista.objects.all()
    serializer_class= turnosPorEspecialistaSerializer 

from .serializer import PacienteSerializer
from .models import Paciente

class PacienteViewSet (viewsets.ModelViewSet):
    queryset=Paciente.objects.all()
    serializer_class= PacienteSerializer 

from .serializer import RevervaDeTurnoSerializer
from .models import ReservaDeTurno

class ReservaDeTurnoViewSet(viewsets.ModelViewSet):
    queryset=ReservaDeTurno.objects.all()
    serializer_class= RevervaDeTurnoSerializer

from .serializer import PagoSerializer
from .models import Pago

class PagoViewSet(viewsets.ModelViewSet):
    queryset=Pago.objects.all()
    serializer_class= PagoSerializer

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
