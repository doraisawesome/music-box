# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicbox', '0002_music'),
    ]

    operations = [
        migrations.CreateModel(
            name='Phonebook',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('genre_name', models.CharField(max_length=50)),
                ('genre_type', models.CharField(max_length=50)),
                ('notes', models.TextField()),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['genre_name'],
            },
        ),
    ]
