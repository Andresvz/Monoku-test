# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('overview', '0003_auto_20160608_2218'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='overview',
            name='executor',
        ),
    ]
