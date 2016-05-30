# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-05-23 10:10
from __future__ import unicode_literals

from django.db import migrations, models
import history_articles.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=400, verbose_name='Название')),
                ('photo', models.ImageField(blank=True, null=True, upload_to=history_articles.models.get_uploaded_file_name, verbose_name='Фото')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('date_begin', models.DateTimeField(blank=True, null=True, verbose_name='Начало периода')),
                ('date_end', models.DateTimeField(blank=True, null=True, verbose_name='Конец периода')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Данные обновлены')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Данные созданы')),
            ],
        ),
    ]
