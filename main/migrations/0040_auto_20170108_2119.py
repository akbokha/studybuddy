# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-08 20:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0039_auto_20170108_2115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='major',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Major'),
        ),
        migrations.AlterField(
            model_name='resource',
            name='major',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Major'),
        ),
    ]