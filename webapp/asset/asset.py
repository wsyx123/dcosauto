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

