# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-09 15:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taggit', '0002_auto_20150616_2121'),
        ('convocatoria', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Desafio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=250)),
                ('descripcion', models.TextField()),
                ('contexto', models.TextField(blank=True, null=True)),
                ('objetivos', models.TextField(blank=True, null=True)),
                ('votable', models.BooleanField(default=False)),
                ('publicado', models.BooleanField(default=False)),
                ('creado_el', models.DateTimeField()),
                ('actualizado_el', models.DateTimeField()),
                ('convocatoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='convocatoria.Convocatoria')),
                ('tematicas', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
            options={
                'verbose_name': 'desafio',
                'verbose_name_plural': 'desafios',
            },
        ),
    ]
