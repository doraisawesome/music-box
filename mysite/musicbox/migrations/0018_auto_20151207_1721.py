# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicbox', '0017_auto_20151207_1714'),
    ]

    operations = [
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('choice_text', models.CharField(max_length=200)),
                ('votes', models.IntegerField(default=0)),
            ],
        ),
        migrations.AlterField(
            model_name='song',
            name='rating',
            field=models.IntegerField(default=0, verbose_name='Rating'),
        ),
        migrations.DeleteModel(
            name='RateValue',
        ),
        migrations.AddField(
            model_name='choice',
            name='rateValue',
            field=models.ForeignKey(to='musicbox.Song'),
        ),
    ]
