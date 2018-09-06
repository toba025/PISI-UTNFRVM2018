# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-03 20:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_auto_20180703_1657'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consulta',
            name='estado',
            field=models.CharField(choices=[('I', 'Iniciada'), ('C', 'Cancelada'), ('T', 'Terminada')], default='Iniciada', max_length=40),
        ),
        migrations.AlterField(
            model_name='consulta',
            name='fecha',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='consulta',
            name='hora',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='consulta',
            name='iphost',
            field=models.GenericIPAddressField(blank=True, null=True),
        ),
    ]
