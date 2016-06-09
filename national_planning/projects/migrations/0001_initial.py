# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='fecha de creacion')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='fecha de modificacion')),
                ('deleted', models.BooleanField(default=False, verbose_name='eliminado')),
                ('name', models.CharField(max_length=255)),
                ('advance', models.CharField(max_length=255)),
                ('residue', models.CharField(max_length=255)),
                ('liabilities', models.CharField(max_length=255)),
                ('obligation', models.CharField(max_length=255)),
                ('payments', models.CharField(max_length=255)),
                ('source', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Proyecto',
                'verbose_name_plural': 'Proyectos',
            },
        ),
    ]
