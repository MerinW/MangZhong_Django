# -*- coding: utf-8 -*-
from django.shortcuts import render
from form import *
import models
from map.models import LandMessage
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.


def bbs_index(request):
    bbs_list = models.BBS.objects.all()
    bbs_list1 = bbs_list[::-1]
    user = request.user
    cate = models.Category.objects.all()
    try:
        page = request.GET.get('page', 1)
    except PageNotAnInteger:
        page = 1
    # Provide Paginator with the request object for complete querystring generation
    p = Paginator(bbs_list1, 5, request=request)
    bbs_list2 = p.page(page)
    # return render_to_response('index.html',{'bbs_list':bbs_list,'user':user},)
    return render(request, "bbs_index.html", {'bbs_list': bbs_list2, 'user': user, 'cate': cate})


def get_details(request, bbs_id):
    bbs = models.BBS.objects.get(id=bbs_id)
    user = bbs.author
    n = 0
    try:
        bbs_count = models.BBS.objects.all()
        for bbs_u in bbs_count:
            if bbs_u.author == user:
                n = n + 1
    except models.BBS.DoesNotExist:
        n = 0
    comment_list = models.Comment.objects.all()
    m = 0
    for cn in comment_list:
        if cn.bbs_content_id == long(bbs_id):
            m = m + 1
    return render(request, 'bbs_detail.html', {'bbs_obj': bbs, 'bbs_com': comment_list, 'bbs_count': n, 'com_count': m})


def get_filter(request, cate_id):
    bbs = models.BBS.objects.filter(category_id=cate_id)
    bbs_list1 = bbs[::-1]
    user = request.user
    cate = models.Category.objects.all()
    try:
        page = request.GET.get('page', 1)
    except PageNotAnInteger:
        page = 1
    # Provide Paginator with the request object for complete querystring generation
    p = Paginator(bbs_list1, 5, request=request)
    bbs_list2 = p.page(page)
    # return render_to_response('index.html',{'bbs_list':bbs_list,'user':user},)
    return render(request, "bbs_index.html", {'bbs_list': bbs_list2, 'user': user, 'cate': cate})
    pass


def del_bbs(request, bbsid):
    bbs = models.BBS.objects.get(id=bbsid)
    bbs.delete()
    bbs = models.BBS.objects.filter(author=request.user)
    bbs1 = bbs[::-1]
    n = len(bbs)
    com = models.Comment.objects.filter(author=request.user)
    m = len(com)
    return render(request, 'bbs_person_detail.html', {'bbs': bbs1, 'com': com, 'bbs_num': n, 'com_num': m})


def updata_bbs(request, bbsid):
    bbs = models.BBS.objects.get(id=bbsid)
    cate = models.Category.objects.all()
    return render(request, "bbs_updata.html", {'bbs_list': bbs, 'user': request.user, "category": cate})
    pass


def bbs_updata_save(request, bbsid):
    bbs = models.BBS.objects.get(id=bbsid)
    user = request.user
    title = request.POST.get('title', '')
    summary = request.POST.get('summary', '')
    content = request.POST.get("content", '')
    cate = request.POST.get("select", '')
    category = models.Category.objects.get(name=cate)
    bbs.title = title
    bbs.summary = summary
    bbs.content = content
    bbs.category = category
    bbs.save()
    up_image = UpLoadImage(request.POST, request.FILES, instance=bbs)
    if up_image.is_valid():
        up_image.save()
    n = 0
    try:
        bbs_count = models.BBS.objects.all()
        for bbs_u in bbs_count:
            if bbs_u.author == user:
                n = n + 1
    except models.BBS.DoesNotExist:
        n = 0
    comment_list = models.Comment.objects.all()
    m = 0
    for cn in comment_list:
        if cn.bbs_content_id == long(bbsid):
            m = m + 1
    return render(request, 'bbs_detail.html', {'bbs_obj': bbs, 'bbs_com': comment_list, 'bbs_count': n, 'com_count': m})

    pass


def bbs_publish(request):
    user = request.user
    cate = models.Category.objects.all()
    land = LandMessage.objects.filter(author=user)
    return render(request, 'bbs_publish.html', {"category": cate, "land": land})
    pass


def bbs_publish_save(request):
    title = request.POST.get('title', '')
    summary = request.POST.get('summary', '')
    author = request.user
    content = request.POST.get("content", '')
    cate = request.POST.get("select", '其他')
    land_id = request.POST.get("select_land", '0')
    land = LandMessage.objects.get(search_id=int(land_id))
    category = models.Category.objects.get(name=cate)
    models.BBS.objects.create(
        title=title,
        summary=summary,
        author=author,
        category=category,
        content=content,
        view_count=0,
        land=land,
    )
    bbs = models.BBS.objects.get(author=author, title=title)
    up_image = UpLoadImage(request.POST, request.FILES, instance=bbs)
    if up_image.is_valid():
        up_image.save()
    bbs = models.BBS.objects.filter(author=request.user)
    bbs1 = bbs[::-1]
    n = len(bbs)
    com = models.Comment.objects.filter(author=request.user)
    m = len(com)
    return render(request, 'bbs_person_detail.html', {'bbs': bbs1, 'com': com, 'bbs_num': n, 'com_num': m})


def add_comment(request, bbs_id):
    comment = request.POST.get("comment")
    author = request.user
    bbs = models.BBS.objects.get(id=bbs_id)
    models.Comment.objects.create(
        bbs_content=bbs,
        comments=comment,
        author=author
    )
    user = bbs.author
    n = 0
    try:
        bbs_count = models.BBS.objects.all()
        for bbs_u in bbs_count:
            if bbs_u.author == user:
                n = n + 1
    except models.BBS.DoesNotExist:
        n = 0
    comment_list = models.Comment.objects.all()
    m = 0
    for cn in comment_list:
        if cn.bbs_content_id == long(bbs_id):
            m = m + 1
    return render(request, 'bbs_detail.html', {'bbs_obj': bbs, 'bbs_com': comment_list, 'bbs_count': n, 'com_count': m})


def bbs_com_del(request, comid, bbsid):
    com = models.Comment.objects.get(id=comid)
    com.delete()
    bbs = models.BBS.objects.get(id=bbsid)
    user = bbs.author
    n = 0
    try:
        bbs_count = models.BBS.objects.all()
        for bbs_u in bbs_count:
            if bbs_u.author == user:
                n = n + 1
    except models.BBS.DoesNotExist:
        n = 0
    comment_list = models.Comment.objects.all()
    m = 0
    for cn in comment_list:
        if cn.bbs_content_id == long(bbsid):
            m = m + 1
    return render(request, 'bbs_detail.html', {'bbs_obj': bbs, 'bbs_com': comment_list, 'bbs_count': n, 'com_count': m})
    pass


def bbs_person_deatail(request):
    bbs = models.BBS.objects.filter(author=request.user)
    bbs1 = bbs[::-1]
    n = len(bbs)
    com = models.Comment.objects.filter(author=request.user)
    m = len(com)
    return render(request, 'bbs_person_detail.html', {'bbs': bbs1, 'com': com, 'bbs_num': n, 'com_num': m})
    pass


def bbs_search(request):
    search = request.POST.get("search", '')
    bbs_list = models.BBS.objects.filter(title__icontains=search)
    bbs_list1 = bbs_list[::-1]
    user = request.user
    return render(request, "bbs_index.html", {'bbs_list': bbs_list1, 'user': user})
    pass
