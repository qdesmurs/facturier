# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-30 07:38
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_project_ref'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='ref',
        ),
    ]
