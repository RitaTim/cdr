# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-05-20 07:02
from __future__ import unicode_literals

import country.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=400, verbose_name='Название')),
                ('logo', models.ImageField(blank=True, null=True, upload_to=country.models.get_uploaded_file_name, verbose_name='Флаг')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Данные обновлены')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Данные созданы')),
            ],
        ),
    ]
