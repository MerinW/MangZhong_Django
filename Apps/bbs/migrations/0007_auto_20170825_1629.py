# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-08-25 16:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bbs', '0006_comment_color'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='color',
        ),
        migrations.AddField(
            model_name='category',
            name='color',
            field=models.CharField(default=None, max_length=20, verbose_name='\u6837\u5f0f\u989c\u8272'),
        ),
    ]
