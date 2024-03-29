# Generated by Django 4.2.1 on 2023-05-18 14:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='turnosPorEspecialista',
            fields=[
                ('id_Turnos', models.AutoField(primary_key=True, serialize=False)),
                ('fecha', models.DateField(max_length=20)),
                ('horarioDeInicio', models.TextField(max_length=1000)),
                ('horarioDeFin', models.TextField(max_length=1000)),
                ('horarioDeTurno', models.TimeField(max_length=20)),
            ],
            options={
                'verbose_name': ' turnos para Especialista Médico',
                'verbose_name_plural': 'turnosPorEspecialistas',
                'db_table': 'turnosPorEspecialista',
            },
        ),
        migrations.CreateModel(
            name='Especialista',
            fields=[
                ('id_Especialista', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=40)),
                ('especialidad', models.CharField(max_length=50)),
                ('horariosDeAtencion', models.TextField(max_length=1000)),
                ('id_Turnos', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.turnosporespecialista')),
            ],
            options={
                'verbose_name': 'Especialista Médico',
                'verbose_name_plural': 'Especialistas',
                'db_table': 'especialista',
            },
        ),
    ]
