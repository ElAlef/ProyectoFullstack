# Generated by Django 4.2.1 on 2023-05-31 18:58

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_remove_horariodeatencion_dia_de_la_setmana_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReservaDeTurno',
            fields=[
                ('id_Reserva', models.AutoField(primary_key=True, serialize=False)),
                ('dni_paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.paciente')),
                ('id_Turnos', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.turnosporespecialista')),
            ],
            options={
                'verbose_name': ' Turnos reservados por pacientes',
                'verbose_name_plural': 'ReservasDeTurnos',
                'db_table': 'reservaDeTurno',
            },
        ),
        migrations.CreateModel(
            name='Pago',
            fields=[
                ('id_pago', models.AutoField(primary_key=True, serialize=False)),
                ('monto', models.IntegerField()),
                ('fecha', models.DateField(default=datetime.datetime.now)),
                ('hora', models.TimeField(default=datetime.datetime.now)),
                ('id_Reserva', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.reservadeturno')),
            ],
            options={
                'verbose_name': ' Pago de turns reservado por paciente',
                'verbose_name_plural': 'PagosDeTurnos',
                'db_table': 'pago',
            },
        ),
    ]