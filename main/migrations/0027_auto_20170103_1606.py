# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-03 15:06
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0026_auto_20170103_1559'),
    ]

    operations = [
        migrations.RenameField(
            model_name='resource',
            old_name='courses',
            new_name='course',
        ),
    ]