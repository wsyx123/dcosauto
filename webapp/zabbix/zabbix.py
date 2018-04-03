#!/usr/bin/env python
#_*_ coding:utf-8 _*_
'''
Created on 2018年3月25日

@author: yangxu
'''
from django.shortcuts import render_to_response

def zabbix(request):
    return render_to_response("zabbix/zabbix.html")

def addHost(request):
    return render_to_response("zabbix/addHost.html")

def zabbix_graph(request):
    return render_to_response("zabbix/graph.html")