# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-05-11 08:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=30, null=True, verbose_name='Название')),
                ('title_h1', models.CharField(blank=True, max_length=30, null=True, verbose_name='Главный заголовок')),
                ('title_h2', models.CharField(blank=True, max_length=50, null=True, verbose_name='Заголовок второго уровня')),
                ('title_btn', models.CharField(blank=True, max_length=10, null=True, verbose_name='Название кнопки')),
                ('href_btn', models.CharField(blank=True, max_length=40, null=True, verbose_name='Ссылка кнопки')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Данные обновлены')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Данные созданы')),
            ],
        ),
    ]
