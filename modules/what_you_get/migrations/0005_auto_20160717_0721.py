# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-07-17 07:21
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('what_you_get', '0004_auto_20160514_0744'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='whatyouget',
            options={'ordering': ['updated', 'created'], 'verbose_name': 'Что вы получите', 'verbose_name_plural': 'Что вы получите'},
        ),
    ]
