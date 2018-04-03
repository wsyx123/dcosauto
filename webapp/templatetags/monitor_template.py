#!/usr/bin/env python
#_*_ coding:utf-8 _*_
'''
Created on 2018年3月31日

@author: yangxu
'''
from django import template

register = template.Library()

@register.filter
def show_detail(templateobj):
    html_start = "<table class='table table-bordered'>"
    html_content = ""
#     <tr><th width='80'>cpu:</th><td><pre>{{template.cpu}}</pre></td></tr>
#     <tr><th width='80'>memory:</th><td><pre>{{template.memory}}</pre></td></tr>
#     <tr><th width='80'>disk:</th><td><pre>{{template.disk}}</pre></td></tr>
#     <tr><th width='80'>network:</th><td><pre>{{template.network}}</pre></td></tr>
    html_end = "</table>"
    for item in  str(templateobj.items).split(','):
        html_content = html_content+"<tr><th width='80'>{}:</th><td><pre>{}</pre></td></tr>".format(item,getattr(templateobj, item))
    
    html = html_start+html_content+html_end 
    return html

@register.inclusion_tag('monitor/_template_detail.html')
def show_template_detail(templateobj):
    # TODO(Thai): once domain switching is support, need to revisit
    result_dict = {}
    for item in  str(templateobj.items).split(','):
        result_dict[item] = getattr(templateobj, item)
    return {'result_dict':result_dict}
    
