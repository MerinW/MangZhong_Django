# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-07-30 15:54
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bbs', '0002_auto_20170730_1511'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bbs',
            old_name='cotegory',
            new_name='category',
        ),
    ]
