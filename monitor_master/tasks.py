#!/usr/bin/env python
#_*_ coding:utf-8 _*_
'''
Created on 2018年4月23日

@author: yangxu
'''
from __future__ import absolute_import
from celery import shared_task
import httplib
import json

def set_agent(agent,status):
    agent["agent"] = status
    name = agent["name"]
    agent = json.dumps(agent)
    conn = httplib.HTTPConnection('192.168.10.1',9000)
    url_context = '/master/api/hosts/'+name+'/'
    print url_context
    conn.request('PUT', url_context, agent, {"Content-Type":"application/json"})
    
def check_agent(agent):
    host = str(agent['address'])
    port = int(agent['port'])
    status = str(agent['agent'])
    conn = httplib.HTTPConnection(host,port)
    try:
        conn.request('GET', '/')
    except:
        if status == 'UP':
            set_agent(agent, 'DOWN')
    else:
        if status == 'DOWN':
            set_agent(agent, 'UP')
        
    
def get_agents():
    conn = httplib.HTTPConnection('192.168.10.1',9000)
    conn.request('GET', '/master/api/hosts/')
    httpres = conn.getresponse()
    for agent in json.loads(httpres.read()):
        check_agent(agent) 
    

@shared_task
def test_celery():
    get_agents()
