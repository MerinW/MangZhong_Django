# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime
from django.db import models
from users.models import UserProfile
from map.models import LandMessage


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=32)
    color = models.CharField(max_length=20, default=None, verbose_name=u'样式颜色')

    class Meta():
        verbose_name = u'目录'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name
    pass


class BBS(models.Model):
    title = models.CharField(max_length=64, verbose_name=u'标题')
    summary = models.CharField(max_length=256, blank=True, verbose_name=u'概要')
    content = models.CharField(max_length=1000)
    author = models.ForeignKey(UserProfile)
    category = models.ForeignKey(Category)
    land = models.ForeignKey(LandMessage,default=None)
    view_count = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="image/BBS", default=u'image/null.gif', max_length=100, blank=True)

    class Meta():
        verbose_name = u'论坛'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.title


class Comment(models.Model):
    bbs_content = models.ForeignKey(BBS, verbose_name=u'内容')
    comments = models.CharField(max_length=200, verbose_name=u'评论')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')
    author = models.ForeignKey(UserProfile, default=1)


    class Meta():
        verbose_name = u'评论'
        verbose_name_plural = verbose_name

