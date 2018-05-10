#!/usr/bin/env python
#_*_ coding:utf-8 _*_
'''
Created on 2018年3月19日

@author: yangxu
'''
from django.shortcuts import render_to_response,HttpResponse
from webapp.models import platformtemplate
from webapp.common.page import page
from webapp.forms.template import TemplateForm,editTemplateForm
import json

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
    
    templates = platformtemplate.objects.all().order_by('-createtime')
#     print templates.filter(platformcomponent__name='icloud')   反向查询(单个)
    
    return render_to_response('platform/template.html',{'templates':page(templates, pagenum, datarow)})

def edit_template(request,name):
    if request.method == 'POST':
        try:
            editTemplateForm(request.POST,platformtemplate,name)
        except Exception as e:
            print e
        return HttpResponse('ok')
    template = platformtemplate.objects.get(name=name)
    return render_to_response('platform/edit_template.html',{'template':template})
    
def del_platform_template(request):
    if request.method == 'POST':
        del_result_dict={}
        data = request.POST.get('template_name_list')
        for template_name in json.loads(data):
            try:
                platformtemplate.objects.get(name=template_name).delete()
            except Exception as e:
                del_result_dict[template_name]=e
            else:
                del_result_dict[template_name]='success'
    return HttpResponse(json.dumps(del_result_dict))
                