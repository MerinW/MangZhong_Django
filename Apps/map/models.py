# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime
from django.db import models
from users.models import UserProfile

# Create your models here.


class LandMessage(models.Model):
    land_id = models.IntegerField(default=0)
    land_x = models.CharField(default=0,max_length=50)
    land_y = models.CharField(default=0,max_length=50)
    title = models.CharField(max_length=64, verbose_name=u'标题')
    content = models.CharField(max_length=1000,verbose_name=u'描述')
    author = models.ForeignKey(UserProfile)
    view_count = models.IntegerField()
    favorite_count = models.IntegerField()
    image = models.ImageField(upload_to="image/map", default=u'image/null.gif', max_length=100, blank=True)
    phone = models.CharField(default=0,max_length=100,verbose_name="联系方式")
    address = models.CharField(max_length=100,default=0,verbose_name='地址')
    search_id = models.IntegerField(default=0,verbose_name='搜索号')
    emotion = models.IntegerField(default=0,verbose_name='情感系数')
    cover = models.IntegerField(default=0.1,verbose_name='配送距离')
    class Meta():
        verbose_name = u'农田信息'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.title


class UserFavorite(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name=u'用户')
    land = models.ForeignKey(LandMessage, verbose_name=u'地块')

    class Meta():
        verbose_name = u'用户收藏'
        verbose_name_plural = verbose_name


class Price(models.Model):
    province = models.CharField(max_length=50,verbose_name=u'省份')
    name = models.CharField(max_length=50,verbose_name=u"省份名")
    price = models.FloatField(verbose_name=u'平均价格',default=0)

    class Meta():
        verbose_name = u'平均价格'
        verbose_name_plural = verbose_name


class landComment(models.Model):
    content = models.ForeignKey(LandMessage, verbose_name=u'地块')
    comments = models.CharField(max_length=200, verbose_name=u'评论')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')
    author = models.ForeignKey(UserProfile, default=1)

    class Meta():
        verbose_name = u'评论'
        verbose_name_plural = verbose_name


class Goods(models.Model):
    land = models.ForeignKey(LandMessage, verbose_name=u"地块")
    goods_name = models.CharField(max_length=50,verbose_name=u"商品名称")
    goods_price = models.CharField(max_length=20,verbose_name=u"商品价格")
    goods_image = models.ImageField(upload_to="image/map", max_length=100, blank=False)

    class Meta():
        verbose_name = u'商品信息'
        verbose_name_plural = verbose_name