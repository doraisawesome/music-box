# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('musicbox', '0010_song_genre'),
    ]

    operations = [
        migrations.AddField(
            model_name='genre',
            name='creation_date',
            field=models.DateTimeField(auto_now_add=True),
            preserve_default=False,
        ),
    ]
