# -*- coding: utf-8 -*-
_date_ = ''
_auth_ = 'merin'
from django import forms
from bbs.models import *


class UpLoadImage(forms.ModelForm):
    class Meta:
        model = BBS
        fields = ['image']
