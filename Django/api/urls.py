from django.urls import path, include
#from rest_framework import routers

from .views import LoginView, LogoutView, SignupView, ProfileView, ListarUsuarios


urlpatterns = [
     #path('', include(router.urls)),

     path('auth/login/',
          LoginView.as_view(), name='auth_login'),
     path('auth/logout/',
         LogoutView.as_view(), name='auth_logout'),
    #  path('auth/reset/',
    #      include('django_rest_passwordreset.urls',
    #              namespace='password_reset')),
     path('auth/registro/',
         SignupView.as_view(), name='auth_signup'),
     path('user/profile/',
         ProfileView.as_view(), name='user_profile'),
     path('usuarios/',
         ListarUsuarios.as_view(), name='listar_usuarios'),
         ]
