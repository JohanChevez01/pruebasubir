# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-08-10 10:58
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clinica', '0010_ventamedicamento_estado'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='detalleventa',
            name='descuento',
        ),
    ]
