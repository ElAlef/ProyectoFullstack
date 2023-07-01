# Generated by Django 4.2.2 on 2023-06-28 18:59

import datetime
from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('email', models.EmailField(max_length=150, unique=True)),
                ('nombre', models.CharField(max_length=40)),
                ('apellido', models.CharField(max_length=40)),
                ('fechaNacimiento', models.CharField(max_length=40)),
                ('dni', models.CharField(max_length=40)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Especialidad',
            fields=[
                ('id_Especialidad', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=40)),
            ],
            options={
                'verbose_name': 'EspecialidadMédica',
                'verbose_name_plural': 'Especialidades',
                'db_table': 'especialidad',
            },
        ),
        migrations.CreateModel(
            name='Especialista',
            fields=[
                ('id_Especialista', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=40)),
                ('id_Especialidad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='turneroapp.especialidad')),
            ],
            options={
                'verbose_name': 'EspecialistaMédico',
                'verbose_name_plural': 'Especialistas',
                'db_table': 'especialista',
            },
        ),
        migrations.CreateModel(
            name='HorarioDeAtencion',
            fields=[
                ('id_Horario', models.AutoField(primary_key=True, serialize=False)),
                ('dia_de_la_semana', models.CharField(max_length=45, verbose_name='Dia de la semana')),
                ('hora_inici', models.DateTimeField()),
                ('hora_fi', models.DateTimeField()),
                ('id_Especialista', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='turneroapp.especialista')),
            ],
            options={
                'verbose_name': ' horariosSemanalesPorCadaEspecialista',
                'verbose_name_plural': 'HorariosDeAtención',
                'db_table': 'HorarioDeAtencion',
            },
        ),
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
        migrations.CreateModel(
            name='turnosPorEspecialista',
            fields=[
                ('id_Turnos', models.AutoField(primary_key=True, serialize=False)),
                ('fecha', models.DateField(max_length=20)),
                ('horarioDeInicio', models.TextField(max_length=1000)),
                ('horarioDeFin', models.TextField(max_length=1000)),
                ('id_Horario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='turneroapp.horariodeatencion')),
            ],
            options={
                'verbose_name': ' turnosParaEspecialistaMédico',
                'verbose_name_plural': 'turnosPorEspecialistas',
                'db_table': 'turnosPorEspecialista',
            },
        ),
        migrations.CreateModel(
            name='ReservaDeTurno',
            fields=[
                ('id_Reserva', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('id_Turnos', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='turneroapp.turnosporespecialista')),
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
                ('id_Reserva', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='turneroapp.reservadeturno')),
            ],
            options={
                'verbose_name': ' Pago de turns reservado por paciente',
                'verbose_name_plural': 'PagosDeTurnos',
                'db_table': 'pago',
            },
        ),
    ]
