# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-03-16 22:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0003_auto_20190316_2205'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postad',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]
