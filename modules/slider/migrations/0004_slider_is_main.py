# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-05-13 07:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('slider', '0003_auto_20160513_0720'),
    ]

    operations = [
        migrations.AddField(
            model_name='slider',
            name='is_main',
            field=models.BooleanField(default=False, verbose_name='Главный слайд'),
        ),
    ]
