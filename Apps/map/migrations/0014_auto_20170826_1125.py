# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-08-26 11:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0013_auto_20170826_1102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goods',
            name='goods_image',
            field=models.ImageField(upload_to='image/map_goods'),
        ),
    ]
