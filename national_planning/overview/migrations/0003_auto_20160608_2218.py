# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('overview', '0002_overview_place'),
    ]

    operations = [
        migrations.RenameField(
            model_name='overview',
            old_name='place',
            new_name='executor',
        ),
    ]
