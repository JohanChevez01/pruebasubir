# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-08-08 00:00
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clinica', '0006_auto_20180807_1747'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Preescripcion',
            new_name='Prescripcion',
        ),
    ]
