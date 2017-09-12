# -*- coding: utf-8 -*-
# @Time    : 2017/7/9 11:06
# @Author  : May
# @Site    :
# @File    : adminx.py
# @Software: PyCharm

import xadmin
from xadmin import views
from models import *


# 设置全局样式


class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


class GlobalSetting(object):
    site_title = u'芒种后台管理'
    site_footer = 'Mangzhong'
    menu_style = 'accordion'
    # 设置菜单栏要在apps和init中修改


class userAdmin(object):
    list_display = ["nick_name", "gender", "description", "address", "user_type"]


# 主题注册
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSetting)
xadmin.site.register(UserProfile, userAdmin)
