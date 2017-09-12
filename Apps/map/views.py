# -*- coding: utf-8 -*-
from django.shortcuts import render
from form import *
import models
import urllib2, time
import json
from django.http import HttpResponse


# Create your views here.


def map_edit(request):
    land = models.LandMessage.objects.all()
    user = request.user
    user1 = user.user_type
    return render(request, "map_editland.html", {"land": land, "user_type": user1})


def map_index(request):
    land = models.LandMessage.objects.all()
    return render(request, "index.html", {"land": land})


def map_add_land(request):
    tilte = request.POST.get("title", '')
    content = request.POST.get("desc", '')
    address = request.POST.get("add", '')
    user = request.user
    land_id = request.POST.get("land_ID", '')
    x = request.POST.get("position_x", '')
    y = request.POST.get("position_y", '')
    view_c = 0
    favo_c = 0
    phone = request.POST.get("phone", '')
    cover = request.POST.get("cover",'')
    models.LandMessage.objects.create(
        author=user,
        search_id=land_id,
        land_x=x,
        land_y=y,
        title=tilte,
        content=content,
        view_count=view_c,
        favorite_count=favo_c,
        phone=phone,
        address=address,
        cover = cover,
    )
    land = models.LandMessage.objects.get(author=user, title=tilte)
    up_image = UpLoadImage(request.POST, request.FILES, instance=land)
    if up_image.is_valid():
        up_image.save()
    land = models.LandMessage.objects.filter(author=request.user)
    return render(request, "map_editland.html", {"land": land})
    pass


def get_map_detail(request, search_id):
    lands = models.LandMessage.objects.get(search_id=search_id)
    user = request.user
    fav = models.UserFavorite.objects.filter(user=user, land=lands)
    goods = models.Goods.objects.filter(land=lands)
    has_fav = False
    if fav:
        has_fav = True
    mapx = lands.land_x
    mapy = lands.land_y
    cover = lands.cover
    cover1 = cover/50.0
    view = lands.view_count
    lands.view_count = view + 1
    lands.save()
    return render(request, "map_detail.html",
                  {"mapx": mapx, "mapy": mapy,"cover":cover1, "land": lands, "fav": has_fav, "goods": goods,'search':search_id})
    pass


def map_search(request):
    text = request.POST.get("search", '')
    land_list = models.LandMessage.objects.filter(title__icontains=text)
    pass


def land_updata(request):
    user = request.user
    land = models.LandMessage.objects.filter(author=user)
    return render(request, 'map_landMessage_updata.html', {"land": land})
    pass


def land_collection(request):
    use_fav = models.UserFavorite.objects.filter(user=request.user)
    return render(request, 'map_collection.html', {'land': use_fav})
    pass


def land_goods(request):
    user = request.user
    land = models.LandMessage.objects.filter(author=user)
    return render(request, 'map_goods.html', {"land": land})
    pass


def land_delete(request):
    user = request.user
    land = models.LandMessage.objects.filter(author=user)
    return render(request, 'map_landMessage_delete.html', {"land": land})
    pass


def map_delete_save(request):
    title = request.POST.get("select", '')
    user = request.user
    land = models.LandMessage.objects.get(title=title, author=user)
    land.delete()
    land1 = models.LandMessage.objects.filter(author=user)
    return render(request, 'map_landMessage_delete.html', {"land": land1})
    pass


def map_updata_save(request):
    title = request.POST.get("select", '')
    user = request.user
    desc = request.POST.get("describe", '')
    address = request.POST.get("address", '')
    phone = request.POST.get("phone", '')
    land = models.LandMessage.objects.get(title=title, author=user)
    land.title = title
    land.content = desc
    land.phone = phone
    land.address = address
    land.save()
    up_image = UpLoadImage(request.POST, request.FILES, instance=land)
    if up_image.is_valid():
        up_image.save()
    land = models.LandMessage.objects.filter(author=request.user)
    return render(request, "map_editland.html", {"land": land})
    pass


def map_goods_delete(request):
    goods1 = models.Goods.objects.filter(land__author=request.user)
    return render(request, 'map_goods_delete.html', {'goods': goods1})
    pass


def map_goods_delete_save(request):
    name = request.POST.get('select', '')
    goods = models.Goods.objects.get(goods_name=name)
    goods.delete()
    goods1 = models.Goods.objects.filter(land__author=request.user)
    return render(request, 'map_goods_delete.html', {'goods': goods1})
    pass


def map_goods_save(request):
    a = request.FILES['image']
    image = "image/map/" + a._name
    title = request.POST.get("select", '')
    user = request.user
    land = models.LandMessage.objects.get(title=title, author=user)
    name = request.POST.get("goods_name", '')
    price = request.POST.get("price", '')
    models.Goods.objects.create(
        land=land,
        goods_name=name,
        goods_price=price,
        goods_image=image
    )
    goods = models.Goods.objects.get(goods_name=name, goods_price=price)
    # up_image1 = UpLoadImage1(request.POST, request.FILES, instance=goods)
    # if up_image1.is_valid():
    #     up_image1.save()
    # land = models.LandMessage.objects.filter(author=request.user)
    #
    # return render(request, "map_editland.html", {"land": land})
    search_id = goods.land.search_id
    lands = models.LandMessage.objects.get(search_id=search_id)
    user = request.user
    fav = models.UserFavorite.objects.filter(user=user, land=lands)
    goods = models.Goods.objects.filter(land=lands)
    has_fav = False
    if fav:
        has_fav = True
    mapx = lands.land_x
    mapy = lands.land_y
    view = lands.view_count
    lands.view_count = view + 1
    lands.save()
    return render(request, "map_detail.html",{"mapx": mapx, "mapy": mapy, "land": lands, "fav": has_fav, "goods": goods})
    pass


def map_count_rice(request, year):
    year = int(year)
    f = "f9"
    if year == 2000:
        f = "f9"
    elif year == 2001:
        f = "f10"
    elif year == 2001:
        f = "f11"
    f1 = "{" + f + "}"
    return render(request, "map_count_rice.html", {"year": f, "filed": f1, "year1": year})


def map_get_price(request, type):
    import urllib2, time
    import json
    time = time.strftime('%Y-%m-%d', time.localtime(time.time()))
    province = ["安徽省", "北京市", "福建省", "甘肃省", "广东省", "广西壮族自治区", "贵州省", "海南省", "河北省", "河南省", "黑龙江省", "湖北省",
                "湖南省", "吉林省", "江苏省", "江西省", "辽宁省", "内蒙古自治区", "宁夏回族自治区", "青海省", "山东省", "山西省", "陕西省", "上海市", "四川省",
                "天津市", "西藏自治区", "新疆维吾尔自治区", "云南省", "浙江省", "重庆市"]
    for province in province:
        strHtml = urllib2.urlopen(
            'http://www.3w3n.com/showPriceCount?pageNo=1&typeId=' + type + '&province=' + province + '&date=' + time).read()
        price = json.loads(strHtml)
        price1 = price['avgPrice']
        get_price = models.Price.objects.get(province=province)
        if price1 is not None:
            get_price.price = price1
        else:
            get_price.price = 0
        get_price.save()
    avgPrice = models.Price.objects.all()
    kind = u'蔬菜'
    type = int(type)
    if type == 2:
        kind = u'西红柿'
    elif type == 3:
        kind = u'大白菜'
    elif type == 4:
        kind = u'土豆'
    elif type == 6:
        kind = u'青椒'
    elif type == 7:
        kind = u'韭菜'
    elif type == 8:
        kind = u'茄子'
    elif type == 10:
        kind = u'大蒜'
    elif type == 11:
        kind = u'白萝卜'
    elif type == 12:
        kind = u'姜'
    return render(request, "map_count_price.html", {"price": avgPrice, "type": kind})
    pass


def map_get_elevation(request):
    return render(request, "map_elevation.html")


def map_get_3D(request,id):
    LandMessage = models.LandMessage.objects.get(search_id=id)
    X = LandMessage.land_x
    Y = LandMessage.land_y
    return render(request, "3Dmap.html",{'x':X,'y':Y})


def map_get_way(request,id):
    LandMessage = models.LandMessage.objects.get(search_id=id)
    X = LandMessage.land_x
    Y = LandMessage.land_y
    return render(request, "map_way.html",{'x':X,'y':Y})


def map_get_scan(request):
    land = models.LandMessage.objects.all()
    return render(request, "map_count_scan.html", {"scan": land})
    pass


def map_get_favo(request):
    land = models.LandMessage.objects.all()
    return render(request, "map_count_favorite.html", {"scan": land})
    pass


def user_favorite(request):
    """用户收藏"""
    landID = request.POST.get("fav_id")
    has_fav = False
    user = request.user
    land = models.LandMessage.objects.get(search_id=landID)
    use_f = models.UserFavorite.objects.filter(user=user, land=land)
    if use_f:
        land.favorite_count = land.favorite_count - 1
        land.save()
        use_f.delete()
        return HttpResponse('{"status":"success","msg":"收藏"}', content_type='application/json')
    else:
        use_favo = UserFavorite()
        use_favo.user = user
        use_favo.land = land
        use_favo.save()
        land.favorite_count = land.favorite_count + 1
        land.save()
        has_fav = True
        return HttpResponse('{"status":"success","msg":"已收藏"}', content_type='application/json')

    pass
