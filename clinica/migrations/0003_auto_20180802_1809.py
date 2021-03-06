# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-08-03 00:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clinica', '0002_auto_20180731_2346'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='localasignado',
            name='empleado',
        ),
        migrations.RemoveField(
            model_name='localasignado',
            name='local',
        ),
        migrations.RemoveField(
            model_name='pagolocal',
            name='localasignado',
        ),
        migrations.AddField(
            model_name='empleado',
            name='local',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='clinica.Local'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pagolocal',
            name='local',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='clinica.Local'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='LocalAsignado',
        ),
    ]
