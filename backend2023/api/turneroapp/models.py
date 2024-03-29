from django.db import models
from datetime import datetime
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.dispatch import receiver
from django.db.models.signals import post_save
from rest_framework.authtoken.models import Token
# # Create your models here.

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

class CustomUser(AbstractUser):
    email = models.EmailField(max_length=150, unique=True)
    nombre = models.CharField(max_length=40, blank=False)
    apellido = models.CharField(max_length=40, blank=False)
    fechaNacimiento = models.CharField(max_length=40, blank=False)
    dni = models.CharField(max_length=40, blank=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'password']
    def __str__(self):
        return self.username

class Especialidad(models.Model):
    id_Especialidad = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=40, blank=False)

    class Meta:
        db_table = "especialidad"
        verbose_name = "EspecialidadMédica"
        verbose_name_plural = "Especialidades"
    def __unicode__(self):
        return self.nombre
    def __str__(self):
        return self.nombre
    
class Especialista(models.Model):
    id_Especialista = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=40, blank=False)
    id_Especialidad = models.ForeignKey(Especialidad,to_field='id_Especialidad', on_delete=models.CASCADE )

    class Meta:
        db_table = "especialista"
        verbose_name = "EspecialistaMédico"
        verbose_name_plural = "Especialistas"
    def __unicode__(self):
        return self.nombre
    def __str__(self):
        return self.nombre

class HorarioDeAtencion(models.Model):
    id_Horario = models.AutoField(primary_key=True)
    dia_de_la_semana = models.CharField("Dia de la semana",max_length=45)
    hora_inici = models.DateTimeField(blank=False) 
    hora_fi = models.DateTimeField(blank=False)
    id_Especialista = models.ForeignKey(Especialista,to_field='id_Especialista', on_delete=models.CASCADE )

    class Meta:
        db_table = "HorarioDeAtencion"
        verbose_name = " horariosSemanalesPorCadaEspecialista"
        verbose_name_plural = "HorariosDeAtención"
        
    def __unicode__(self):
        return self.dia_de_la_semana
        
    def __str__(self):
        return self.dia_de_la_semana
        
    
class TurnosPorEspecialista(models.Model):
    id_Turnos = models.AutoField(primary_key=True)
    fecha = models.DateField( max_length=20, blank=False)
    horarioDeInicio = models.TextField(max_length=1000, blank=False)
    horarioDeFin = models.TextField(max_length=1000, blank=False)
    id_Horario = models.ForeignKey(HorarioDeAtencion,to_field='id_Horario', on_delete=models.CASCADE )

    class Meta:
        db_table = "turnosPorEspecialista"
        verbose_name = " turnosParaEspecialistaMédico"
        verbose_name_plural = "turnosPorEspecialistas"
    def __unicode__(self):
        return self.horarioDeInicio
    def __str__(self):
        return self.horarioDeInicio
    
class Paciente(models.Model):
    dni_paciente = models.CharField(primary_key=True, max_length=8)
    nombre = models.CharField(max_length=40, blank=False)
    apellidos = models.CharField(max_length=60, blank=False)
    telefono = models.CharField(max_length=20)
    email = models.EmailField (max_length=50)
    usuario = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    
    class Meta:
        db_table = "paciente"
        verbose_name = "paciente usuario"
        verbose_name_plural = "pacientes"
    def __unicode__(self):
        return self.nombre

class ReservaDeTurno(models.Model):
    id_Reserva = models.AutoField(primary_key=True)
    email = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    id_Turnos = models.ForeignKey(TurnosPorEspecialista,to_field='id_Turnos', on_delete=models.CASCADE )

    class Meta:
        db_table = "reservaDeTurno"
        verbose_name = " Turnos reservados por pacientes"
        verbose_name_plural = "ReservasDeTurnos"
    def __unicode__(self):
        return self.id_Turnos
    # def __str__(self):
    #     return self.id_Turnos

class Pago(models.Model):
    id_pago = models.AutoField(primary_key=True)
    monto = models.IntegerField()
    fecha = models.DateField(default = datetime.now)
    hora = models.TimeField(default = datetime.now)
    id_Reserva = models.ForeignKey(ReservaDeTurno,to_field='id_Reserva', on_delete=models.CASCADE )


    class Meta:
        db_table = "pago"
        verbose_name = " Pago de turns reservado por paciente"
        verbose_name_plural = "PagosDeTurnos"
    def __unicode__(self):
        return self.monto
    # def __str__(self):
    #     return self.monto


