# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-30 07:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_project_line_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='ref',
            field=models.CharField(default='FS201705-47', max_length=50),
            preserve_default=False,
        ),
    ]
