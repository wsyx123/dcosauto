#!/usr/bin/env python
#_*_ coding:utf-8 _*_
'''
Created on 2017年12月13日

@author: yangxu
'''
import httplib

def get(host,port,url_context=None):
    conn = httplib.HTTPConnection(host,port)
    try:
        conn.request("GET", url_context)
    except Exception as e:
        print e
        return {'code':10060,'result':'连接失败'}
    else:
        httpres = conn.getresponse()
        return {'code':200,'result':httpres.read()}

def post(host,port,url_context=None,body=None,headers=None):
    conn = httplib.HTTPConnection(host,port)
    try:
        conn.request("POST", url_context, body, headers)
    except Exception as e:
        return e
    httpres = conn.getresponse()
    return httpres.read()

def put(host,port,url_context=None,body=None,headers=None):
    conn = httplib.HTTPConnection(host,port)
    if body and  headers:
        conn.request("PUT", url_context,body,headers)
    elif headers and not body:
        conn.request("PUT", url_context,headers)
    elif body and not headers:
        conn.request("PUT", url_context,body)
    else:
        conn.request("PUT", url_context)
    httpres = conn.getresponse()
    return httpres.read()


# conn = httplib.HTTPConnection('10.153.160.4','6071')
# while True:
#     conn.request('POST', '/containers/61071b64e30e/attach?stream=1&stdout=1',headers={"Connection":"Upgrade"})
#     httpres=conn.getresponse()
#     print httpres.status
#     print httpres.reason
#     print httpres.read()
