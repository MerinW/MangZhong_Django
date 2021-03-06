# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-08-26 10:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0011_auto_20170823_1613'),
    ]

    operations = [
        migrations.CreateModel(
            name='goods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goods_name', models.CharField(max_length=50, verbose_name='\u5546\u54c1\u540d\u79f0')),
                ('goods_price', models.CharField(max_length=20, verbose_name='\u5546\u54c1\u4ef7\u683c')),
                ('goods_image', models.ImageField(blank=True, default='image/null.gif', upload_to='image/map_goods')),
                ('land', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='map.LandMessage', verbose_name='\u5730\u5757')),
            ],
            options={
                'verbose_name': '\u5546\u54c1\u4fe1\u606f',
                'verbose_name_plural': '\u5546\u54c1\u4fe1\u606f',
            },
        ),
    ]
