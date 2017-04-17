# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicbox', '0006_choice'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='song',
            name='album',
        ),
        migrations.AddField(
            model_name='song',
            name='publisher',
            field=models.CharField(max_length=100, verbose_name='Publisher', blank=True),
        ),
        migrations.AlterField(
            model_name='song',
            name='artist',
            field=models.CharField(max_length=100, verbose_name='Artist'),
        ),
        migrations.AlterField(
            model_name='song',
            name='file',
            field=models.FileField(null=True, upload_to=b'music'),
        ),
        migrations.AlterField(
            model_name='song',
            name='genre',
            field=models.CharField(max_length=50, verbose_name='Genre'),
        ),
        migrations.AlterField(
            model_name='song',
            name='rating',
            field=models.IntegerField(default=0, verbose_name='Rating'),
        ),
    ]
