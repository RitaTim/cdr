# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-07-17 07:21
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('filials', '0005_auto_20160516_1003'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='filial',
            options={'verbose_name': 'Филиал', 'verbose_name_plural': 'Филиалы'},
        ),
    ]
