# -*- coding: utf-8 -*-
_date_ = '' '下午4:31'
_auth_ = 'merin'
import xadmin
from .models import BBS,Comment,Category


class BBSAdmin(object):
    list_display = ['title','summary','content','author','view_count','created_at','update_at']
    search_fields = ['title']
    list_filter = ['title','author','view_count','created_at','update_at']
    pass


class commentAdmin(object):
    pass


class cotegoryAdmmin(object):
    list_display = ['name', 'color', ]
    pass


xadmin.site.register(BBS, BBSAdmin)
xadmin.site.register(Comment, commentAdmin)
xadmin.site.register(Category, cotegoryAdmmin)
