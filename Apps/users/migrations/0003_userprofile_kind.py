# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-08-24 11:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_userprofile_user_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='kind',
            field=models.IntegerField(default=1),
        ),
    ]
