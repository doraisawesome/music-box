# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import musicbox.utils


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('file', models.FileField(upload_to=musicbox.utils.get_file_upload_path, verbose_name='File')),
                ('file_size', models.IntegerField(verbose_name='File size', editable=False)),
                ('duration', models.IntegerField(default=0, verbose_name='Song duration in seconds', editable=False)),
                ('title', models.CharField(max_length=100, verbose_name='Title')),
                ('artist', models.CharField(max_length=100, verbose_name='Artist', blank=True)),
                ('album', models.CharField(max_length=100, verbose_name='Album name', blank=True)),
                ('track_number', models.SmallIntegerField(null=True, verbose_name='Track number', blank=True)),
                ('track_total', models.SmallIntegerField(null=True, verbose_name='Total track count', blank=True)),
                ('genre', models.CharField(max_length=50, verbose_name='Genre', blank=True)),
                ('disc_number', models.SmallIntegerField(null=True, verbose_name='Disc number', blank=True)),
                ('disc_total', models.SmallIntegerField(null=True, verbose_name='Total disc count', blank=True)),
                ('year', models.CharField(max_length=4, verbose_name='Year', blank=True)),
                ('publisher', models.CharField(max_length=100, verbose_name='Publisher', blank=True)),
                ('play_count', models.IntegerField(default=0, verbose_name='Play count')),
                ('added_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
