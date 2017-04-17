# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicbox', '0020_song_sumitted_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='overall_rating',
            field=models.IntegerField(default=0, verbose_name='Overall Rating'),
        ),
    ]
