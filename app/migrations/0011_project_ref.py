# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-30 07:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_remove_project_ref'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='ref',
            field=models.CharField(default='alo', max_length=50),
            preserve_default=False,
        ),
    ]
