from django.db import models

# Create your models here.

class Persona(models.Model):
    nombre = models.CharField(max_lenght=100)
    apellido = models.CharField(max_lenght=50)
    nroDNI = models.PositiveBigIntegerField()
    telefono = models.PositiveBigIntegerField()
    email = models.CharField(max_lenght=100)
    esta_activo = models.BooleanField(default=True)

class Paciente(models.Model):
    contraseña = models.CharField(max_lenght=50)
    nroAfiliado = models.PositiveIntegerField()

class ReservaDeTurno(models.Model):
    paciente = Paciente
    fecha = models.DateField()
    hora = models.TimeField()
    id_reserva = models.PositiveIntegerField()

class TurnoPorEspecialista(models.Model):
   fecha = models.DateField()
   horaDesde = models.TimeField()
   horaHasta = models.TimeField()
   atencion = ReservaDeTurno

class HorarioEspecialista(models.Model):
    diaSemana = models.CharField(max_lenght=25)
    horaInicio = models.TimeField()
    horaFin = models.TimeField()

class Especialista(models.Model):
    nroMatricula = models.PositiveSmallIntegerField()
    servicio = models.CharField(max_lenght=50)
    costo = models.PositiveSmallIntegerField()
    horarioDeAtencion = models.DateTimeField()
    turnos = TurnoPorEspecialista
    esta_activo = models.BooleanField(default=True)

class Administrador(models.Model):
    cargo = models.CharField(max_lenght=50)
    especialistas = Especialista
    
class ObraSocial(models.Model):
    nombre = models.CharField(max_lenght=25)
    plan =  models.CharField(max_lenght=25)

class Pago(models.Model):
    reserva = ReservaDeTurno
    fecha = models.DateField()
    hora = models.TimeField()
    id_pago = models.PositiveIntegerField()
    monto = models.PositiveIntegerField()