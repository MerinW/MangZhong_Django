# -*- coding: utf-8 -*-
_date_ = ''
_auth_ = 'merin'
from django import forms
from map.models import *


class UpLoadImage(forms.ModelForm):
    class Meta:
        model = LandMessage
        fields = ['image']


class UpLoadImage1(forms.ModelForm):
    class Meta:
        model = Goods
        fields = ['goods_image']



