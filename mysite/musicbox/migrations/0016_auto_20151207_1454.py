# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicbox', '0015_remove_song_genre'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='genre',
            options={'ordering': ['genre_name']},
        ),
        migrations.AddField(
            model_name='song',
            name='genre',
            field=models.ForeignKey(to='musicbox.Genre', null=True),
        ),
    ]
