from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_rename_id_especialidad_horariodeatencion_id_especialista'),
    ]

    operations = [
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('dni_paciente', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=40)),
                ('apellidos', models.CharField(max_length=60)),
                ('telefono', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=50)),
                ('usuario', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name': 'paciente usuario',
                'verbose_name_plural': 'pacientes',
                'db_table': 'paciente',
            },
        ),
    ]
