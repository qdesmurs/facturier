# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-23 09:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20170622_0834'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='name',
            field=models.CharField(default='yolo', max_length=50),
            preserve_default=False,
        ),
    ]
