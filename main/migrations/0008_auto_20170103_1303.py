# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-03 12:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20170103_1300'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resource',
            name='major',
        ),
        migrations.AddField(
            model_name='resource',
            name='major',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='main.Major'),
        ),
    ]