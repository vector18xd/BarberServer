# Generated by Django 3.2.4 on 2022-06-15 04:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_trabajadores_state'),
    ]

    operations = [
        migrations.RenameField(
            model_name='citas',
            old_name='fecha',
            new_name='fechaRegistroCita',
        ),
        migrations.RenameField(
            model_name='citas',
            old_name='hora',
            new_name='horaRegistroCita',
        ),
        migrations.RemoveField(
            model_name='citas',
            name='idTrabajador',
        ),
        migrations.AlterField(
            model_name='trabajadores',
            name='direccion',
            field=models.CharField(blank=True, max_length=70, null=True),
        ),
        migrations.AlterField(
            model_name='trabajadores',
            name='nom_local',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.CreateModel(
            name='horarios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('horaInicio', models.TimeField()),
                ('fecha', models.DateField()),
                ('horaFinalizacion', models.TimeField()),
                ('estado', models.CharField(max_length=30, null=True)),
                ('idTrabajador', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.trabajadores')),
            ],
        ),
    ]
