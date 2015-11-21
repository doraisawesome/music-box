# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicbox', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Music',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('file', models.FileField(null=True, upload_to=b'music', blank=True)),
                ('title', models.CharField(max_length=15)),
                ('genre', models.CharField(max_length=15)),
                ('artist', models.CharField(max_length=15)),
            ],
        ),
    ]
