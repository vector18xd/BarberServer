# Generated by Django 3.2.4 on 2022-07-26 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_auto_20220726_1337'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientes',
            name='foto',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='trabajadores',
            name='foto',
            field=models.URLField(blank=True, null=True),
        ),
    ]
