# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-07-17 07:21
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='new',
            options={'ordering': ['-updated', '-created'], 'verbose_name': 'Новость', 'verbose_name_plural': 'Новости'},
        ),
    ]
