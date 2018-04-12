#!/usr/bin/env python
#_*_ coding:utf-8 _*_
'''
Created on 2018年3月31日

@author: yangxu
'''
from django import template

register = template.Library()

@register.filter
def item_manytomany(templateobj):
    item_str = ""
    itemsobj = templateobj.items.all()
    for item in itemsobj:
        print item
        item_str = item_str+item.name+'\n'
    return item_str

@register.filter
def policy_manytomany(templateobj):
    policy_str = ""
    policysobj = templateobj.policy.all()
    for policy in policysobj:
        policy_str = policy_str+policy.name+'\n'
    return policy_str

@register.inclusion_tag('monitor/_notify_detail.html')
def notify_content(content):
    content_list = content.split('\n')
    return {'content_list':content_list}

@register.inclusion_tag('monitor/_template_detail.html')
def show_template_detail(templateobj):
    # TODO(Thai): once domain switching is support, need to revisit
    result_dict = {}
#     for item in  str(templateobj.items).split(','):
#         result_dict[item] = getattr(templateobj, item)
#     return {'result_dict':result_dict}
    
