#!/usr/bin/env python
#_*_ coding:utf-8 _*_
'''
Created on 2018年3月23日

@author: yangxu
'''
from django.core.paginator import Paginator

def page(obj,pagenum,datarow):
    pagelist = []
    pagedict = {'pagecount':None,'pagenum':None,'itemcount':None,'pagedata':None}
    for item in obj:
        pagelist.append(item)
    p = Paginator(pagelist,datarow)
    itemcount = p.count
    pagecount = p.num_pages
    pagedata = p.page(pagenum).object_list
    pagedict['pagecount']= pagecount
    pagedict['pagenum'] = pagenum
    pagedict['itemcount'] = itemcount
    pagedict['pagedata'] = pagedata
    return pagedict