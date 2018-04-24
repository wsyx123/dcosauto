#!/usr/bin/env python
#_*_ coding:utf-8 _*_
'''
Created on 2018年3月18日

@author: yangxu
'''

from django.shortcuts import render_to_response,HttpResponse
from webapp.models import platformcomponent,platformtemplate,platformcluster,platformhosts
from webapp.common.docker_create_pull import create_pull,delete_container
from webapp.forms.component import ComponentForm
from webapp.common.page import page
import json
from webapp.common.dockerapi125 import DockerOps
import threading

def component(request):
    if request.method == 'POST':
        host = request.POST.get('host')
        name = request.POST.get('name')
        componentformobj = ComponentForm(request.POST)
        save_result = componentformobj.save_component()
        if save_result['status']:
            data = componentformobj.generate_docker_json()
            resultmsg = create_pull(host, '6071', name, data)
            if resultmsg['status'] == 'failure':
                platformcomponent.objects.get(name=name).delete()
            return HttpResponse(json.dumps(resultmsg))
        else:
            return HttpResponse(json.dumps({'status':'failure','msg':save_result['msg']}))
        
    try:
        datarow = int(request.GET.get('datarow'))
    except:
        datarow = 10
    try:
        pagenum = int(request.GET.get('pagenum'))
    except:
        pagenum = 1
    components = page(platformcomponent.objects.all(), pagenum, datarow)
    templates = platformtemplate.objects.values('name')
    clusters = platformcluster.objects.values('name')
    hosts = platformhosts.objects.values('address')
    return render_to_response('platform/component.html',{'components':components,'templates':templates,
                                                         'clusters':clusters,'hosts':hosts})
def component_status(request):
    status = {}
    component_obj = platformcomponent.objects.all()
    for component in component_obj:
        get_container_status(component)
#         t = threading.Thread(target=get_container_status,args=(component,))
#         t.start()
    component_obj = platformcomponent.objects.all()
    for component in component_obj:
        status[component.name] = component.status
    return HttpResponse(json.dumps(status))

def get_container_status(containerobj):
    host = str(containerobj.host)
    container_name = str(containerobj.name)
    status = DockerOps.status(host=host, port='6071', container_name=container_name,alls=False)
    if status == 'running':
        platformcomponent.objects.filter(name=container_name).update(status='up')
    else:
        platformcomponent.objects.filter(name=container_name).update(status='down')
        
def component_delete(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        host = request.POST.get('host')
        delete_result = delete_container(host, '6071', name)
        if delete_result['code'] == 204:
            platformcomponent.objects.get(name=name).delete()
            return HttpResponse(json.dumps({'status':'success'}))
        else:
            return HttpResponse(json.dumps({'status':'failure','msg':delete_result['reason']}))
        