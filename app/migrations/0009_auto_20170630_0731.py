# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-30 07:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_project_ref'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='ref',
            field=models.CharField(max_length=50),
        ),
    ]
