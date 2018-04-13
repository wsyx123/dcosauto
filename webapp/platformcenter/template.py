#!/usr/bin/env python
#_*_ coding:utf-8 _*_
'''
Created on 2018年3月19日

@author: yangxu
'''
from django.shortcuts import render_to_response
from webapp.models import platformtemplate
from webapp.common.page import page
from webapp.forms.template import TemplateForm

def template(request):
    if request.method == 'POST':
        TemplateForm(request.POST,platformtemplate)
    
    try:
        datarow = int(request.GET.get('datarow'))
    except:
        datarow = 10
    try:
        pagenum = int(request.GET.get('pagenum'))
    except:
        pagenum = 1
    
    templates = platformtemplate.objects.all()
    
    return render_to_response('platform/template.html',{'templates':page(templates, pagenum, datarow)})

def edit_template(request,name):
    template = platformtemplate.objects.get(name=name)
    return render_to_response('platform/edit_template.html',{'template':template})
    
        