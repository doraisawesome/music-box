# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicbox', '0018_auto_20151207_1721'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='total_rating',
            field=models.IntegerField(default=0, verbose_name='Total Rating'),
        ),
    ]
