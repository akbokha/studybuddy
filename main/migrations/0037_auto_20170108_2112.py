# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-08 20:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0036_auto_20170108_2057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resource',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Course'),
        ),
    ]
