# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-08 19:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0032_auto_20170108_2022'),
    ]

    operations = [
        migrations.CreateModel(
            name='Major',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('bachelorcollege', 'Bachelor College'), ('appliedmathematics', 'Applied Mathematics'), ('appliedphysics', 'Applied Physics'), ('architecture', 'Architecture, Urbanism and Building Sciences'), ('automotive', 'Automotive'), ('biomedicalengineering', 'Biomedical Engineering'), ('chemicalengineering', 'Chemical Engineering'), ('computerscience', 'Computer Science'), ('electricalengineering', 'Electrical Engineering'), ('industrialdesign', 'Industrial Design'), ('industrialengineering', 'Industrial Engineering'), ('mechanicalengineering', 'Mechanical Engineering'), ('psychologyandtechnology', 'Psychology and Technology'), ('sustainableinnovation', 'Sustainable Innovation')], default='computerscience', max_length=45)),
            ],
        ),
        migrations.AlterField(
            model_name='course',
            name='major',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Major'),
        ),
        migrations.AlterField(
            model_name='resource',
            name='course',
            field=smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='major', chained_model_field='major', on_delete=django.db.models.deletion.CASCADE, to='main.Course'),
        ),
        migrations.AlterField(
            model_name='resource',
            name='major',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Major'),
        ),
    ]
