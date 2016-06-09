# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('overview', '0004_remove_overview_executor'),
        ('executors', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='executor',
            name='overview',
            field=models.OneToOneField(default=1, to='overview.Overview'),
            preserve_default=False,
        ),
    ]
