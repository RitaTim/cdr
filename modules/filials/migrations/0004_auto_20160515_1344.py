# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-05-15 13:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filials', '0003_auto_20160514_1240'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='filial',
            name='timetable',
        ),
        migrations.AddField(
            model_name='filial',
            name='timetable_adults',
            field=models.TextField(blank=True, null=True, verbose_name='Расписание (взрослые)'),
        ),
        migrations.AddField(
            model_name='filial',
            name='timetable_children',
            field=models.TextField(blank=True, null=True, verbose_name='Расписание (дети)'),
        ),
    ]
