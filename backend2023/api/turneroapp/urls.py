from django import urls
from django.urls import path, include, re_path
from .views import  LogoutView, SignupView, ProfileView, ListarUsuarios, agregarEspecialidad, verEspecialidad, verEspecialista, verHorarioDeAtencion

urlpatterns = [
#     path('auth/login/',
#          LoginView.as_view(), name='auth_login'),

    path('auth/logout/',
         LogoutView.as_view(), name='auth_logout'),
    path('auth/reset/',
         include('django_rest_passwordreset.urls',
                 namespace='password_reset')),
    path('auth/registro/',
         SignupView.as_view(), name='auth_signup'),
    path('user/profile/',
         ProfileView.as_view(), name='user_profile'),
    path('usuarios/',
         ListarUsuarios.as_view(), name='listar_usuarios'),
    path('agregarespecialidad/',
         agregarEspecialidad.as_view(), name='agregar_especialidad'),
    path('especialidades/',
         verEspecialidad.as_view(), name='ver_especialidades'),
    path('especialistas/',
         verEspecialista.as_view(), name='ver_especialistas'),
    path('HorarioDeAtencion/',
         verHorarioDeAtencion.as_view(), name='ver_HorariosDeAtencion'),
]