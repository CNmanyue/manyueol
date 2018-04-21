#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/21 12:31
# @Author  : zhouxw-home
# @File    : forms.py
# @Software: PyCharm

from captcha.fields import CaptchaField
from django import forms


class CaptchaTestForm(forms.Form):
    """
        1. 构建一个Form
    """
    error_message = {'invalid': "验证码不通过"}
    captcha = CaptchaField(error_messages=error_message)
