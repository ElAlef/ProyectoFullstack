from django.db import models

# Create your models here.

class Especialidad(models.Model):
    id_Especialidad = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=40, blank=False)

    class Meta:
        db_table = "especialidad"
        verbose_name = "Especialidad Médica"
        verbose_name_plural = "Especialidades"
    def __unicode__(self):
        return self.nombre
    def __str__(self):
        return self.nombre
    
class Especialista(models.Model):
    id_Especialista = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=40, blank=False)
    id_Especialidad = models.ForeignKey(Especialidad,to_field="id_Especialidad", on_delete=models.CASCADE )

    class Meta:
        db_table = "especialista"
        verbose_name = "Especialista Médico"
        verbose_name_plural = "Especialistas"
    def __unicode__(self):
        return self.nombre
    def __str__(self):
        return self.nombre

class HorarioDeAtencion(models.Model):
    id_Horario = models.AutoField(primary_key=True)
    n_dia_uk = models.IntegerField(u'Número de dia de la setmana a UK (0=diumenge)', unique=True) 
    n_dia_ca = models.IntegerField(u'Número de dia de la setmana aquí (0=dilluns)', unique=True) 
    dia_2_lletres = models.CharField("Dia",max_length=6, unique=True)
    dia_de_la_setmana = models.CharField("Dia de la setmana",max_length=45, unique=True)
    hora_inici = models.DateTimeField(blank=False) 
    hora_fi = models.DateTimeField(blank=False)
    id_Especialista = models.ForeignKey(Especialista,to_field="id_Especialista", on_delete=models.CASCADE )
    nom_franja = models.CharField(max_length=45, blank=True) 

    class Meta:
        db_table = "HorarioDeAtencion"
        verbose_name = " horarios semanales por cada especialista"
        verbose_name_plural = "HorariosDeAtención"
        
    def __unicode__(self):
        return self.dia_de_la_setmana
        return self.hora_inici
        return self.hora_fi
        # return self.nom_franja if unicode(self.nom_franja) else  unicode(self.hora_inici)[0:5] + ' a ' unicode(self.hora_fi)[0:5]
    def __str__(self):
        return self.dia_de_la_setmana
        return self.hora_inicio
        return self.hora_fi
        # return self.hora_inici.strftime("%H:%M")
    
class turnosPorEspecialista(models.Model):
    id_Turnos = models.AutoField(primary_key=True)
    fecha = models.DateField( max_length=20, blank=False)
    horarioDeInicio = models.TextField(max_length=1000, blank=False)
    horarioDeFin = models.TextField(max_length=1000, blank=False)
    id_Horario = models.ForeignKey(HorarioDeAtencion,to_field="id_Horario", on_delete=models.CASCADE )

    class Meta:
        db_table = "turnosPorEspecialista"
        verbose_name = " turnos para Especialista Médico"
        verbose_name_plural = "turnosPorEspecialistas"
    def __unicode__(self):
        return self.fecha
    def __str__(self):
        return self.horarioDeInicio
    
    