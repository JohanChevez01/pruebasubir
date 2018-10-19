# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-08-08 02:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clinica', '0007_auto_20180807_1800'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='prescripcion',
            name='medicamento',
        ),
        migrations.AddField(
            model_name='prescripcion',
            name='medicamento',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='clinica.Medicamento'),
            preserve_default=False,
        ),
    ]
