# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-05-13 08:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WhatYouGet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, verbose_name='Название')),
                ('description', models.CharField(blank=True, max_length=500, null=True, verbose_name='Описание')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Данные обновлены')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Данные созданы')),
            ],
            options={
                'ordering': ['-updated', '-created'],
            },
        ),
    ]
