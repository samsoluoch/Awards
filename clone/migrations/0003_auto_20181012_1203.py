# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-12 09:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clone', '0002_auto_20181012_1113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='url',
            field=models.URLField(max_length=100),
        ),
    ]
