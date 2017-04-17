# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('musicbox', '0004_auto_20151130_1641'),
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name_first', models.CharField(max_length=10)),
                ('name_last', models.CharField(max_length=10)),
                ('password', models.CharField(max_length=50)),
                ('repassword', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(blank=True, max_length=15, validators=[django.core.validators.RegexValidator(regex=b'^1?\\D*(\\d{3})\\D*(\\d{3})\\D*(\\d{4})$', message=b'phone number must be in the format XXX-XXX-XXXX')])),
            ],
        ),
    ]
