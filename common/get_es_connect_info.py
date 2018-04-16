#!/usr/bin/env python
#_*_ coding:utf-8 _*_
'''
Created on 2018年4月16日

@author: yangxu
'''
import httplib
import json

def get_es_connect_info(monitor_host,monitor_port,url_context):
    conn = httplib.HTTPConnection(monitor_host,monitor_port)
    conn.request('GET', url_context)
    httpres = conn.getresponse()
    value = json.loads(httpres.read())['value']
    return value[7:].split(':')
    
    