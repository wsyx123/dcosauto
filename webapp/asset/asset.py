#!/usr/bin/env python
#_*_ coding:utf-8 _*_
'''
Created on 2018年3月23日

@author: yangxu
'''
from webapp.models import platformhosts
from webapp.common.page import page
from webapp.common.dockerapi125 import DockerOps
from webapp.forms.asset import AssetForm
from django.shortcuts import render_to_response,HttpResponse
import json
from dwebsocket import accept_websocket
from ssh_client.client import connect

def asset(request):
    if request.method == 'POST':
        address = request.POST.get('address')
        try:
            collection = request.POST.get('collection')
        except:
            collection = 'no'
        if collection == 'yes':
            result = DockerOps.info(address, 6071)
            if result['code'] == 200:
                AssetForm(result['result'],platformhosts,address)
#                 platformhosts.objects.create(address=address)
                return HttpResponse(json.dumps({'status':'success'}))
            else:
                return HttpResponse(json.dumps({'status':'failure','msg':result['result']}))
        else:
            platformhosts.objects.create(address=address)
    if request.method == 'DELETE':
        try:
            address = request.body.split('=')[1]
            platformhosts.objects.get(address=address).delete()
        except Exception as e:
            return HttpResponse(json.dumps({'status':'failure','msg':e}))
        else:
            return HttpResponse(json.dumps({'status':'success'}))
            
    hosts = platformhosts.objects.all()
    hosts = page(hosts, 1, 10)
    return render_to_response("asset/asset.html",{'hosts':hosts})

def asset_detail(request,host):
    hostobj = platformhosts.objects.filter(hostname=host).first()
    return render_to_response("asset/asset_detail.html",{'host':hostobj})

def asset_system_user(request):
    return render_to_response("asset/asset_system_user.html",{})

def asset_system_user_detail(request,user):
    return render_to_response("asset/asset_system_user_detail.html",{})

def organization(request):
    return render_to_response("asset/organization.html",{})

def organization_department_detail(request,deid):
    print deid
    return render_to_response("asset/organization_department_detail.html",{})

@accept_websocket
def asset_connect(request,addr):
    if request.is_websocket():
        connect(request)
    return render_to_response("asset/terminal.html",{'address':addr})
