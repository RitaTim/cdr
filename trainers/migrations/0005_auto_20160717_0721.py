# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-07-17 07:21
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trainers', '0004_auto_20160514_1243'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='trainer',
            options={'verbose_name': 'Инструктора', 'verbose_name_plural': 'Инструктор'},
        ),
    ]
