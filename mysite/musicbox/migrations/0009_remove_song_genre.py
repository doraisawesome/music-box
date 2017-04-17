# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicbox', '0008_auto_20151206_1533'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='song',
            name='genre',
        ),
    ]
