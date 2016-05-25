# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-05-20 07:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import master.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('country', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Master',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=400, verbose_name='Имя')),
                ('apelido', models.CharField(blank=True, max_length=400, null=True, verbose_name='Апелиду')),
                ('photo', models.ImageField(blank=True, null=True, upload_to=master.models.get_uploaded_file_name, verbose_name='Фото')),
                ('cordao', models.CharField(blank=True, max_length=400, null=True, verbose_name='Шнур')),
                ('biography', models.TextField(blank=True, null=True, verbose_name='Биография')),
                ('date_birth', models.DateTimeField(blank=True, null=True, verbose_name='Дата рожения')),
                ('date_death', models.DateTimeField(blank=True, null=True, verbose_name='Дата смерти')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Данные обновлены')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Данные созданы')),
                ('country', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='country.Country', verbose_name='Страна')),
            ],
        ),
    ]