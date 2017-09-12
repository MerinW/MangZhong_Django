# -*- coding:utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.


class UserProfile(AbstractUser):
    nick_name = models.CharField(verbose_name=u'名称', max_length=20, default=u'', null=True, blank=True)
    gender = models.CharField(verbose_name=u'性别', max_length=10, choices=(('male', u'男'), ('female', u'女')),
                              default='female')
    description = models.CharField(verbose_name=u'个人简介', max_length=200, default=u'', null=True, blank=True)
    address = models.CharField(verbose_name=u'所在地', max_length=100, default=u'', null=True, blank=True)
    SEquestion = models.CharField(verbose_name=u'密保问题', max_length=50, default=u'', null=True, blank=True)
    SEanswer = models.CharField(verbose_name=u'密保答案', max_length=50, default=u'', null=True, blank=True)
    image = models.ImageField(upload_to="image/%Y/%m", default=u'image/default.png', max_length=100, blank=True)
    user_type = models.IntegerField(choices=((1, '个体经营户'), (2, '小型农场'), (3, '大型种植业基地'),(4, '个体养殖业'),(5, '大型养殖业')), default=1, verbose_name=u'用户类型')
    kind = models.IntegerField(default=1)

    class Meta:
        verbose_name = u'用户信息'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.username
