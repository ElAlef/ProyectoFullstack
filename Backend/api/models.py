from django.db import models

# Create your models here.
class turnosPorEspecialista(models.Model):
    id_Turnos = models.AutoField(primary_key=True)
    fecha = models.DateField(max_length=20, blank=False)
    horarioDeInicio = models.TextField(max_length=255, blank=False)
    horarioDeFin = models.TextField(max_length=255, blank=False)
    horarioDeTurno = models.TimeField(max_length=20, blank=False)

    class Meta:
        db_table = "turnosPorEspecialista"
        verbose_name = " turnos para Especialista Médico"
        verbose_name_plural = "turnosPorEspecialistas"
    def __unicode__(self):
        return self.fecha
    def __str__(self):
        return self.horarioDeInicio
    
class Especialista(models.Model):
    id_Especialista = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=40, blank=False)
    especialidad = models.CharField(max_length=50, blank=False)
    horariosDeAtencion = models.TextField(max_length=1000, blank=False)
    id_Turnos = models.ForeignKey(turnosPorEspecialista,to_field="id_Turnos", on_delete=models.CASCADE )

    class Meta:
        db_table = "especialista"
        verbose_name = "Especialista Médico"
        verbose_name_plural = "Especialistas"
    def __unicode__(self):
        return self.nombre
    def __str__(self):
        return self.nombre
    