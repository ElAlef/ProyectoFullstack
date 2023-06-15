from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password

class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True)
    nombre = serializers.CharField()
    apellido = serializers.CharField()
    fechaNacimiento = serializers.CharField()
    dni = serializers.CharField()
    username = serializers.CharField(
        required=True)
    password = serializers.CharField(
        min_length=8)

    class Meta:
        model = get_user_model()
        fields = ('email', 'nombre', 'apellido', 'fechaNacimiento', 'dni', 'username', 'password')
    def validate_password(self, value):
        return make_password(value)