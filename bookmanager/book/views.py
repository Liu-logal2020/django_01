from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
"""
视图
所谓的视图其实就是python函数
视图函数有两个要求：
      1、视图函数的第一个参数就是接收请求，这个请求其实就是HttpResponse的类对象
      2、必须返回一个相应 return
    
"""

#我们希望用户输入http://127.0.0.1:8000/index/
#来访问视图函数

def index(request):

    return HttpResponse('OK!')
