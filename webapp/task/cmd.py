#!/usr/bin/env python
#_*_ coding:utf-8 _*_
'''
Created on 2018年4月30日

@author: yangxu
'''
from django.shortcuts import render_to_response
import json

def cmd(request):
    if request.method == 'POST':
        execute_data = json.loads(request.POST.get('execute_data'))
        print execute_data['model']
    return render_to_response('task/cmd.html', {})