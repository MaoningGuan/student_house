#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django import forms

import re

from .models import Student


class StudentForm(forms.ModelForm):
    # 增加QQ号必须为纯数字的校验
    def clean_qq(self):
        cleaned_data = self.cleaned_data['qq']
        if not cleaned_data.isdigit():
            raise forms.ValidationError('必须是数字！')
        return int(cleaned_data)

    # 增加手机号是否合法的验证
    def clean_phone(self):
        """
        通过正则表达式验证手机号码是否合法
        :return: 手机号码
        """
        mobile = self.cleaned_data['phone']
        mobile_regex = r'^1[34578]\d{9}$'
        p = re.compile(mobile_regex)
        if p.match(mobile):
            return int(mobile)
        else:
            raise forms.ValidationError('请填入有效的手机号码。', code='invalid mobile')

    class Meta:
        model = Student  # 复用models.py里面的代码
        fields = (
            'name', 'sex', 'profession',
            'email', 'qq', 'phone'
        )

    # name = forms.CharField(label='姓名', max_length=128)
    # sex = forms.ChoiceField(label='性别', choices=Student.SEX_ITEMS)
    # profession = forms.CharField(label='专业', max_length=128)
    # email = forms.EmailField(label='邮箱', max_length=128)
    # qq = forms.CharField(label='QQ', max_length=128)
    # phone = forms.CharField(label='手机', max_length=128)
