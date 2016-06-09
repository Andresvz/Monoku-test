# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('executors', '0002_executor_overview'),
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='executor',
            field=models.OneToOneField(default=1, to='executors.Executor'),
            preserve_default=False,
        ),
    ]
