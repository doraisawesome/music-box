# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicbox', '0016_auto_20151207_1454'),
    ]

    operations = [
        migrations.CreateModel(
            name='RateValue',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rate_value', models.CharField(max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='choice',
            name='rateValue',
        ),
        migrations.AlterModelOptions(
            name='genre',
            options={},
        ),
        migrations.AlterField(
            model_name='song',
            name='rating',
            field=models.ForeignKey(default=0, to='musicbox.RateValue', null=True),
        ),
        migrations.DeleteModel(
            name='Choice',
        ),
    ]
