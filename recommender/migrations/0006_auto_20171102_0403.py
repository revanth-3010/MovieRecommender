# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-02 04:03
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recommender', '0005_auto_20171101_1925'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rating',
            old_name='movie_id',
            new_name='movie',
        ),
        migrations.RenameField(
            model_name='rating',
            old_name='user_id',
            new_name='user',
        ),
    ]
