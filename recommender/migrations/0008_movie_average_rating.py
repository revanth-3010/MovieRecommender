# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-11 16:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recommender', '0007_auto_20171111_0549'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='average_rating',
            field=models.IntegerField(default=0),
        ),
    ]
