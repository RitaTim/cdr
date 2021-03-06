# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-05-20 07:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('gallery', '0005_auto_20160519_1125'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Заголовок')),
                ('text', models.TextField(blank=True, null=True, verbose_name='Текст')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Данные обновлены')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Данные созданы')),
                ('photos', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='gallery.models.Photo', verbose_name='Фотграфии')),
            ],
        ),
    ]
