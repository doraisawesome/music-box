# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicbox', '0019_song_total_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='sumitted_count',
            field=models.IntegerField(default=0, verbose_name='Total Rating Submmited'),
        ),
    ]
