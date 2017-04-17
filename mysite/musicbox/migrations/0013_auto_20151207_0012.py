# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicbox', '0012_auto_20151207_0009'),
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('genre_name', models.CharField(max_length=50)),
            ],
            options={
                'ordering': ['genre_name'],
            },
        ),
        migrations.DeleteModel(
            name='Phonebook',
        ),
        migrations.AlterField(
            model_name='song',
            name='genre',
            field=models.ForeignKey(to='musicbox.Genre'),
        ),
    ]
