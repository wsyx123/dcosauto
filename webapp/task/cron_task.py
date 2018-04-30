#!/usr/bin/env python
#_*_ coding:utf-8 _*_
'''
Created on 2018年4月30日

@author: yangxu
'''
from django.shortcuts import render_to_response

def cron_task(request):
    return render_to_response('task/cron.html', {})