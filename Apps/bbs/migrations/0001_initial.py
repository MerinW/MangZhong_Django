# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-07-30 13:17
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BBS',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64, verbose_name='\u6807\u9898')),
                ('summary', models.CharField(blank=True, max_length=256, verbose_name='\u6982\u8981')),
                ('content', models.CharField(max_length=1000)),
                ('view_count', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '\u8bba\u575b',
                'verbose_name_plural': '\u8bba\u575b',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comments', models.CharField(max_length=200, verbose_name='\u8bc4\u8bba')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='\u6dfb\u52a0\u65f6\u95f4')),
                ('bbs_content', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bbs.BBS', verbose_name='\u5185\u5bb9')),
            ],
            options={
                'verbose_name': '\u8bc4\u8bba',
                'verbose_name_plural': '\u8bc4\u8bba',
            },
        ),
        migrations.CreateModel(
            name='Cotegory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
            ],
            options={
                'verbose_name': '\u76ee\u5f55',
                'verbose_name_plural': '\u76ee\u5f55',
            },
        ),
        migrations.AddField(
            model_name='bbs',
            name='cotegory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bbs.Cotegory'),
        ),
    ]
