# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-07-17 07:21
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0002_auto_20160520_0735'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='about',
            options={'verbose_name': 'О школе', 'verbose_name_plural': 'О школе'},
        ),
    ]
