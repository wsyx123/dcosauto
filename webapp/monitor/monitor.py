#!/usr/bin/env python
#_*_ coding:utf-8 _*_
'''
Created on 2018年3月25日

@author: yangxu
'''
from django.shortcuts import render_to_response,HttpResponse
from webapp.forms.monitor import TemplateForm,HostForm
from monitor_master.models import MonitorHost,MonitorTemplate,MonitorNotifyPolicy
import json
from monitor_master.models import MonitorProblem,MonitorNotifyDetail

def monitor_configure(request):
    hosts = MonitorHost.objects.all()
    templates = MonitorTemplate.objects.all()
    policys = MonitorNotifyPolicy.objects.all()
    return render_to_response("monitor/monitor.html",{'hosts':hosts,'templates':templates,'policys':policys})

def add_host(request):
    if request.method == 'POST':
        data = json.loads(request.POST.get('host'))
        HostForm(data)
    templates = MonitorTemplate.objects.all()
    return render_to_response("monitor/addHost.html",{'templates':templates})
def del_host(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        try:
            MonitorHost.objects.get(name=name).delete()
        except Exception as e:
            print e
            return HttpResponse(json.dumps({'status':False,'msg':e}))
        else:
            return HttpResponse(json.dumps({'status':True}))

def add_template(request):
    if request.method == 'POST':
        data = json.loads(request.POST.get('template'))
        TemplateForm(data)
    policys = MonitorNotifyPolicy.objects.all()
    return render_to_response("monitor/addTemplate.html",{'policys':policys})

def del_template(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        try:
            MonitorTemplate.objects.get(name=name).delete()
        except Exception as e:
            print e
            return HttpResponse(json.dumps({'status':False,'msg':str(e)}))
        else:
            return HttpResponse(json.dumps({'status':True}))

def monitor_graph(request):
    return render_to_response("monitor/graph.html")

def monitor_notify(request):
    problems = MonitorProblem.objects.all().order_by('-time')
    notifys = MonitorNotifyDetail.objects.all().order_by('-time')
    return render_to_response("monitor/notify.html",{'problems':problems,'notifys':notifys})