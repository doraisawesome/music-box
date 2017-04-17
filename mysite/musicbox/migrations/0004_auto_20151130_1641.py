# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicbox', '0003_phonebook'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='song',
            name='disc_number',
        ),
        migrations.RemoveField(
            model_name='song',
            name='disc_total',
        ),
        migrations.RemoveField(
            model_name='song',
            name='publisher',
        ),
        migrations.RemoveField(
            model_name='song',
            name='track_number',
        ),
        migrations.RemoveField(
            model_name='song',
            name='track_total',
        ),
        migrations.AddField(
            model_name='song',
            name='rating',
            field=models.IntegerField(default=0, verbose_name='Rating', blank=True),
        ),
    ]
