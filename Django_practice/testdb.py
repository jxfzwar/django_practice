# -*- coding: utf-8 -*-

from django.http import HttpResponse

from TestModel.models import Test
from django.shortcuts import render

# 数据库操作
def testdb(request):
    test1 = Test(name='runoob')
    test1.save()
    context = {}
    context['hello'] = '数据添加成功！!'
    return render(request, 'hello.html', context)

