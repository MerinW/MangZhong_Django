# -*- coding: utf-8 -*-
"""Esri URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
import xadmin
from django.conf import settings
from django.conf.urls.static import static
from users.views import *
from bbs.views import *
from map.views import *

urlpatterns = [
                  # 后台管理
                  url(r'^xadmin/', xadmin.site.urls),
                  # 登录
                  url(r'^$', Log_View.as_view(), name='log_sign'),
                  url(r'^log/$', Log_View.as_view(), name='log'),
                  # 登出
                  url(r'^logout/$', logout_view, name='logout'),
                  # 注册
                  url(r'^sign/$', Sign_View.as_view(), name='sign'),
                  url(r'^signinfo/$', Signinfo_View.as_view(), name='signinfo'),
                  # 忘记密码
                  url(r'^reget/step1/$', Reget1_View.as_view(), name='reget_step1'),
                  url(r'^reget/step2/$', Reget2_View.as_view(), name='reget_step2'),
                  # 首页
                  url(r'^index/$', map_index, name='index'),
                  # 个人中心
                  url(r'^space/$', Space_info_View.as_view(), name='space_info'),
                  # 更新地块
                  url(r'^landUpdata/$', land_updata, name='land_updata'),
                  url(r'^landCollection/$', land_collection, name='land_collection'),
                  url(r'^mapUpdataSave/$', map_updata_save, name='map_updata_save'),
                  # 添加商品
                  url(r'^landGoods/$', land_goods, name='land_goods'),
                  url(r'^mapGoodsSave/$', map_goods_save, name='map_goods_save'),
                  url(r'^mapGoodsDelete/$', map_goods_delete, name='map_goods_delete'),
                  url(r'^mapGoodsDeleteSave/$', map_goods_delete_save, name='map_goods_delete_save'),
                  # 删除地块
                  url(r'^landDelete/$', land_delete, name='land_delete'),
                  url(r'^mapDeleteSave/$', map_delete_save, name='map_delete_save'),

                  # 更新个人信息
                  url(r'^space/edit/$', Space_edit_View.as_view(), name='space_info_edit'),
                  url(r'^space/security1/$', Space_security1_View.as_view(), name='space_security1'),
                  url(r'^space/security2/$', Space_security2_View.as_view(), name='space_security2'),
                  # 论坛首页
                  url(r'^bbsIndex/$', bbs_index, name='bbs_index'),
                  url(r'^searchBBS/$', bbs_search, name='bbs_search'),
                  # 详情
                  url(r'^details/(\d+)/$', get_details, name='bbs_detail'),
                  url(r'^bbs_filter/(\d+)/$', get_filter, name='bbs_filter'),
                  url(r'^bbsDel/(\d+)/$', del_bbs, name='del_bbs'),
                  # 更新
                  url(r'^bbsUpdata/(\d+)/$', updata_bbs, name='updata_bbs'),
                  url(r'^bbsUpdataSave/(\d+)$', bbs_updata_save, name='bbs_updata_save'),
                  # 发布
                  url(r'^bbsPublish/$', bbs_publish, name='bbs_publish'),
                  url(r'^bbsPublishSave/$', bbs_publish_save, name='bbs_publish_save'),
                  url(r'^bbsPersonMessage/$', bbs_person_deatail, name='bbs_person_detail'),
                  # 添加评论
                  url(r'^addComment/(\d+)/$', add_comment, name='add_comment'),
                  url(r'^bbsCommentDel/(\d+)/(\d+)/$', bbs_com_del, name='bbs_com_del'),
                  # 地图编辑
                  url(r'^mapEdit/$', map_edit, name='map_editland'),
                  # 用户收藏
                  url(r'^mapAddFavo/$', user_favorite, name='map_add_favorite'),
                  # 稻谷统计
                  url(r'^mapCountRice/(\d+)/$', map_count_rice, name='map_count_rice'),
                  url(r'^mapAddLand/$', map_add_land, name='map_add_land'),
                  url(r'^personalLand/(\d+)/$', get_map_detail, name='map_detail'),
                  # 统计数据
                  url(r'^mapGetPrice/(\d+)/$', map_get_price, name='map_get_price'),
                  url(r'^mapGetScan/$', map_get_scan, name='map_get_Scan'),
                  url(r'^mapGetFavo/$', map_get_favo, name='map_get_favo'),
                  # 高程
                  url(r'^mapElevation/$', map_get_elevation, name='map_get_elevation'),
url(r'^3Dmap/(\d+)/$', map_get_3D, name='map_get_3D'),
url(r'^map_way/(\d+)/$', map_get_way, name='map_get_way'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
