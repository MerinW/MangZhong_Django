# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-08-14 18:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0005_landmessage_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='landmessage',
            name='address',
            field=models.CharField(default=0, max_length=100, verbose_name='\u5730\u5740'),
        ),
        migrations.AlterField(
            model_name='landmessage',
            name='content',
            field=models.CharField(max_length=1000, verbose_name='\u63cf\u8ff0'),
        ),
        migrations.AlterField(
            model_name='landmessage',
            name='phone',
            field=models.IntegerField(default=0, verbose_name='\u63cf\u8ff0'),
        ),
        migrations.AlterField(
            model_name='landmessage',
            name='search_id',
            field=models.IntegerField(default=0, verbose_name='\u641c\u7d22\u53f7'),
        ),
    ]
