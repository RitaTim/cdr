# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-05-14 12:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trainers', '0002_auto_20160514_0745'),
    ]

    operations = [
        migrations.AddField(
            model_name='trainer',
            name='status',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Статус'),
        ),
    ]