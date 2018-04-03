#!/usr/bin/env python
#_*_ coding:utf-8 _*_
'''
Created on 2018年3月23日

@author: yangxu
'''

from django.shortcuts import render_to_response
def system(request):
    return render_to_response("system/system.html",)