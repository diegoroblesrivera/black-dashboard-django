# Generated by Django 4.2.9 on 2025-07-25 20:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Arbitro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_run', models.IntegerField()),
                ('dv_run', models.CharField(max_length=1)),
                ('pnombre', models.CharField(max_length=50)),
                ('snombre', models.CharField(max_length=50)),
                ('appaterno', models.CharField(max_length=50)),
                ('apmaterno', models.CharField(max_length=50)),
                ('nacionalidad', models.CharField(max_length=50)),
                ('fecha_nac', models.DateField()),
                ('telefono', models.CharField(max_length=20)),
                ('correo', models.EmailField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Cancha',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, unique=True)),
                ('ciudad', models.CharField(max_length=50)),
                ('comuna', models.CharField(max_length=30)),
                ('direccion', models.CharField(max_length=30, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Direccion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_calle', models.CharField(max_length=100)),
                ('num_calle', models.IntegerField()),
                ('comuna', models.CharField(max_length=100)),
                ('region', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Director_Tecnico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_run', models.IntegerField()),
                ('dv_run', models.CharField(max_length=1)),
                ('pri_nombre', models.CharField(max_length=20)),
                ('sec_nombre', models.CharField(blank=True, max_length=20)),
                ('pri_apellido', models.CharField(max_length=20)),
                ('sec_apellido', models.CharField(blank=True, max_length=20)),
                ('nacionalidad', models.CharField(max_length=30)),
                ('correo_electronico', models.EmailField(max_length=30, unique=True)),
                ('telefono', models.CharField(max_length=20)),
                ('id_direccion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='canchas.direccion')),
            ],
        ),
        migrations.CreateModel(
            name='Equipo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('puntos', models.IntegerField(default=0)),
                ('id_DT', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='id_DT', to='canchas.director_tecnico')),
            ],
        ),
        migrations.CreateModel(
            name='Fecha_Campeonato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_fecha', models.IntegerField()),
                ('dia_inicio_fecha', models.DateField(blank=True)),
                ('dia_final_fecha', models.DateField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Horario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dia', models.DateField()),
                ('horario_apertura', models.TimeField()),
                ('horario_cierre', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Jugador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_run', models.IntegerField()),
                ('dv_run', models.CharField(max_length=1)),
                ('pnombre', models.CharField(max_length=50)),
                ('snombre', models.CharField(blank=True, max_length=50)),
                ('appaterno', models.CharField(max_length=50)),
                ('apmaterno', models.CharField(max_length=50)),
                ('nacionalidad', models.CharField(max_length=50)),
                ('telefono', models.IntegerField()),
                ('fecha_nac', models.DateField()),
                ('id_direccion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='canchas.direccion')),
            ],
        ),
        migrations.CreateModel(
            name='Partido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hora', models.TimeField()),
                ('clima', models.CharField(max_length=50)),
                ('observaciones', models.TextField(max_length=500)),
                ('equipo_ganador', models.CharField(max_length=100)),
                ('equipo_local', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='partido_como_local', to='canchas.equipo')),
                ('equipo_visita', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='partido_como_visita', to='canchas.equipo')),
                ('id_arbitro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='canchas.arbitro')),
                ('id_cancha', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='canchas.cancha')),
                ('id_fecha', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='canchas.fecha_campeonato')),
            ],
        ),
        migrations.CreateModel(
            name='Torneo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Tarjeta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(choices=[('amarilla', 'Amarilla'), ('roja', 'Roja')], max_length=10)),
                ('minuto', models.IntegerField()),
                ('jugador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='canchas.jugador')),
                ('partido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='canchas.partido')),
            ],
        ),
        migrations.CreateModel(
            name='Gol',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('minuto', models.IntegerField()),
                ('jugador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='canchas.jugador')),
                ('partido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='canchas.partido')),
            ],
        ),
        migrations.AddField(
            model_name='fecha_campeonato',
            name='torneo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fechas', to='canchas.torneo'),
        ),
        migrations.CreateModel(
            name='Estadistica_Jugador_Torneo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_goles', models.IntegerField(default=0)),
                ('total_amarillas', models.IntegerField(default=0)),
                ('total_rojas', models.IntegerField(default=0)),
                ('jugador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='canchas.jugador')),
                ('torneo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='canchas.torneo')),
            ],
        ),
        migrations.AddField(
            model_name='cancha',
            name='id_horario',
            field=models.ManyToManyField(to='canchas.horario'),
        ),
        migrations.AddField(
            model_name='arbitro',
            name='id_direccion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='canchas.direccion'),
        ),
    ]
