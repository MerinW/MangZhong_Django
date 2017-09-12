# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.generic.base import View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from django.contrib.auth.hashers import make_password
from django.http import HttpResponseRedirect

from models import UserProfile
from form import LoginForm1, SignupForm, UpLoadImage, UpdateInfo


# Create your views here.
# 用于验证用户
class CustomBackend(ModelBackend):
    def authenticate(self, username=None, password=None, **kwargs):
        try:
            user = UserProfile.objects.get(Q(username=username) | Q(email=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None


# 登录
class Log_View(View):
    def get(self, request):
        return render(request, "log_sign.html", {"tab": "logIn"})

    def post(self, request):
        login_form = LoginForm1(request.POST)
        # if login_form.is_valid():
        user_name = request.POST.get("email1", "")
        pass_word = request.POST.get("password1", "")
        user = authenticate(username=user_name, password=pass_word)
        if user is not None:
            # 自带登录函数
            login(request, user)
            return HttpResponseRedirect('/index/')
        else:
            return render(request, "log_sign.html", {"msg": "用户名或密码错误", "tab": "logIn", "login_form": login_form})
            # else:
            #     return render(request, "log_sign.html", {"login_form": login_form})


# 注册信息
class Sign_View(View):
    def get(self, request):
        return render(request, 'log_sign.html', {'tab': 'signUp'})

    def post(self, request):
        signup_form = SignupForm(request.POST)
        if signup_form.is_valid():
            user_name = request.POST.get("email2", "")
            pass_word = request.POST.get("password2", "")
            re_pass_word = request.POST.get("password3", "")
            if pass_word == re_pass_word:
                # 返回错误信息
                if UserProfile.objects.filter(username=user_name):
                    return render(request, "log_sign.html", {'tab': 'signUp', 'flag': "true", "msg2": "该邮箱已存在"})
                else:
                    user_profile = UserProfile()
                    user_profile.username = user_name
                    user_profile.email = user_name
                    # 对密码进行加密
                    user_profile.password = make_password(pass_word)
                    user_profile.save()
                    user = authenticate(username=user_name, password=pass_word)
                    login(request, user)
                    return render(request, "sign_info.html", {})
            else:
                return render(request, "log_sign.html",
                              {'flag': "true", "msg2": "两次密码不一致", 'tab': 'signUp', "signup_form": signup_form})
        else:
            return render(request, "log_sign.html", {'tab': 'signUp', 'flag': "true", "signup_form": signup_form})


# 保存用户信息
class Signinfo_View(View):
    def get(self, request):
        return render(request, "sign_info.html", {})

    def post(self, request):
        if request.user.is_authenticated():
            # user_name = request.user
            up_nick_name = request.POST.get('nick_name', '')
            up_gender = request.POST.get('gender', '')
            up_question = request.POST.get('SEquestion', '')
            up_answer = request.POST.get('SEanswer', '')
            up_desc = request.POST.get('desc', '')
            up_type = request.POST.get('type', '')
            up_province = request.POST.get('input_province', '')
            up_city = request.POST.get('input_city', '')
            up_area = request.POST.get('input_area', '')
            up_address = up_province + up_city + up_area

            up_image = UpLoadImage(request.POST, request.FILES, instance=request.user)
            if up_image.is_valid():
                up_image.save()
            # 获取当前用户对象
            user = UserProfile.objects.get(username=request.user)
            user.nick_name = up_nick_name
            user.gender = up_gender
            user.description = up_desc
            user.address = up_address
            user.SEquestion = up_question
            user.SEanswer = up_answer
            user.user_type = up_type
            # 保存
            user.save()

            return HttpResponseRedirect('/index/')


class Reget1_View(View):
    def get(self, request):
        return render(request, "reget_step1.html", {})

    def post(self, request):
        user_name = request.POST.get('email', '')
        if UserProfile.objects.filter(username=user_name):
            SEquestion = UserProfile.objects.get(username=user_name).SEquestion
            return render(request, "reget_step2.html", {'SEquestion': SEquestion, 'email': user_name})
        else:
            return render(request, "reget_step1.html", {'error': '该邮箱不存在'})


# 忘记密码
class Reget2_View(View):
    def get(self, request):
        user_name = request.POST.get('email', '')
        SEquestion = request.POST.get('SEquestion', '')
        return render(request, "reget_step2.html", {'SEquestion': SEquestion, 'email': user_name})

    def post(self, request):
        user_name = request.POST.get('email', '')
        SEquestion = request.POST.get('SEquestion', '')
        SEanswer = request.POST.get('SEanswer', '')
        pass_word1 = request.POST.get('password1', '')
        pass_word2 = request.POST.get('password2', '')
        user = UserProfile.objects.get(username=user_name)
        if user.SEanswer == SEanswer:
            if pass_word1 == pass_word2:
                user.password = make_password(pass_word1)
                user.save()
                return render(request, "log_sign.html", {"tab": "logIn"})
            else:
                return render(request, "reget_step2.html",
                              {'error': '两次密码不一致', 'SEquestion': SEquestion, 'email': user_name})
        else:
            return render(request, "reget_step2.html",
                          {'error': '回答错误', 'SEquestion': SEquestion, 'email': user_name})


class Index_View(View):
    def get(self, request):
        return render(request, "index.html", {})

    def post(self, request):
        pass


class Space_info_View(View):
    def get(self, request):
        return render(request, "space_info.html", {})

    def post(self, request):
        pass


# 个人中心
class Space_edit_View(View):
    def get(self, request):
        return render(request, "space_info_edit.html", {})

    def post(self, request):
        up_nick_name = request.POST.get('nick_name', '')
        up_gender = request.POST.get('gender', '')
        up_address = request.POST.get('address', '')
        up_desc = request.POST.get('desc', '')
        up_image = UpLoadImage(request.POST, request.FILES, instance=request.user)
        if up_image.is_valid():
            up_image.save()

        user = UserProfile.objects.get(username=request.user)
        user.nick_name = up_nick_name
        user.gender = up_gender
        user.address = up_address
        user.description = up_desc
        user.save()

        return HttpResponseRedirect('/space/')


class Space_security1_View(View):
    def get(self, request):
        user = UserProfile.objects.get(username=request.user)
        u = user.SEquestion
        return render(request, "space_security1.html", {'user': user})

    def post(self, request):
        answer = request.POST.get('SEanswer', '')
        if UserProfile.objects.get(username=request.user).SEanswer == answer:
            return render(request, "space_security2.html", {})
        else:
            return render(request, "space_security1.html", {'error': '回答错误'})


class Space_security2_View(View):
    def get(self, request):
        pass
        # return render(request, "space_security2.html", {})

    def post(self, request):
        if 'button1' in request.POST:
            SEquestion = request.POST.get('SEquestion', '')
            SEanswer = request.POST.get('SEanswer', '')
            user = UserProfile.objects.get(username=request.user)
            user.SEquestion = SEquestion
            user.SEanswer = SEanswer
            user.save()
            return render(request, "space_security2.html", {'info': '修改成功'})

        if 'button2' in request.POST:
            pass_word1 = request.POST.get('password1', '')
            pass_word2 = request.POST.get('password2', '')
            if pass_word1 == pass_word2:
                user = UserProfile.objects.get(username=request.user)
                user.password = make_password(pass_word1)
                user.save()
                return render(request, "space_security2.html", {'info': '修改成功'})
            else:
                return render(request, "space_security2.html", {'error': '两次密码不一致'})


def logout_view(request):
    logout(request)
    return render(request, "log_sign.html", )
