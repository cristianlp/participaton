# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-22 15:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('convocatoria', '0003_convocatoria_imagen'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='convocatoria',
            options={'ordering': ['fecha_hasta']},
        ),
        migrations.RemoveField(
            model_name='convocatoria',
            name='tematicas',
        ),
        migrations.AlterField(
            model_name='convocatoria',
            name='actualizada_el',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='convocatoria',
            name='fecha_desde',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='convocatoria',
            name='fecha_hasta',
            field=models.DateField(),
        ),
    ]
