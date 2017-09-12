# -*- coding: utf-8 -*-
_date_ = ''
_auth_ = 'merin'
import xadmin
from models import *


class landMessageAdmin(object):
    list_display = ['title', 'content', 'author', 'view_count', 'favorite_count', 'image', 'land_x', 'land_y',
                    'land_id', "search_id", "phone", "address","cover"]
    search_fields = ['title']
    list_filter = ['title', 'author', 'view_count']
    pass


class userFavoriteAdmin(object):
    list_display = ["land", "user"]

    pass


class priceAdmin(object):
    list_display = ["province", "name", 'price']

    pass


class goodsAdmin(object):
    list_display = ["goods_name", "goods_price", 'goods_image']

    pass



xadmin.site.register(LandMessage, landMessageAdmin)
xadmin.site.register(UserFavorite, userFavoriteAdmin)
xadmin.site.register(Price, priceAdmin)
xadmin.site.register(Goods, goodsAdmin)