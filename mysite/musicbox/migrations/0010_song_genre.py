# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('musicbox', '0009_remove_song_genre'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='genre',
            field=models.ForeignKey(default=1, to='musicbox.Genre'),
            preserve_default=False,
        ),
    ]
