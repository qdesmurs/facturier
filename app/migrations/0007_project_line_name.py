# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-23 09:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_project_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='project_line',
            name='name',
            field=models.CharField(default='arhg', max_length=50),
            preserve_default=False,
        ),
    ]
