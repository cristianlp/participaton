# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-22 15:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('convocatoria', '0004_auto_20170822_1547'),
    ]

    operations = [
        migrations.AlterField(
            model_name='convocatoria',
            name='actualizada_el',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
