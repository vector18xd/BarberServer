# Generated by Django 3.2.4 on 2022-08-08 22:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_auto_20220726_1510'),
    ]

    operations = [
        migrations.AddField(
            model_name='calificacion',
            name='comentario',
            field=models.CharField(max_length=180, null=True),
        ),
    ]
