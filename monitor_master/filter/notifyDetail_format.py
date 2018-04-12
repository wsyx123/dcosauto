#!/usr/bin/env python
#_*_ coding:utf-8 _*_
'''
Created on 2018年4月12日

@author: yangxu
'''
import httplib
import json


def generate_detail_data(mode,theme,content,send_to,status,message):
    notify_detail_format = {
        "mode": "{}".format(mode),
        "theme": "{}".format(theme),
        "content": "{}".format(content),
        "send_to": "{}".format(send_to),
        "status": "{}".format(status),
        "message": "{}".format(message)
    }
    return notify_detail_format

notify_detail_content = '时间:{}\n 主机:{}\n 事件:{}\n 等级:{}'

def write_notify(data):
    conn = httplib.HTTPConnection('localhost',9000)
    url_context = '/master/api/details/'
    body=json.dumps(data)
    try:
        conn.request('POST', url_context, body, {'Content-Type': 'application/json'})
    except Exception as e:
        print e
    else:
        httpres = conn.getresponse()
        return {'code':httpres.status,'result':httpres.read()}
    
    
    
    