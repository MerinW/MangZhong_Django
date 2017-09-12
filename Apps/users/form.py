#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/7/10 10:37
# @Author  : May
# @Site    : 
# @File    : form.py
# @Software: PyCharm

from django import forms
from users.models import UserProfile


class LoginForm1(forms.Form):
    email1 = forms.EmailField(required=True)
    password1 = forms.CharField(required=True, min_length=8)


class SignupForm(forms.Form):
    email2 = forms.EmailField(required=True)
    password2 = forms.CharField(required=True, min_length=8)
    password3 = forms.CharField(required=True, min_length=8)


class UpLoadImage(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['image']


class UpdateInfo(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['nick_name', 'gender', 'description', 'address']
