#!/usr/bin/env python
#_*_ coding:utf-8 _*_
'''
Created on 2018年3月25日

@author: yangxu
'''
from django.shortcuts import render_to_response,HttpResponse
from webapp.forms.monitor import TemplateForm,HostForm,ItemForm,PolicyForm
from monitor_master.models import MonitorHost,MonitorTemplate,MonitorNotifyPolicy
import json
from monitor_master.models import MonitorProblem,MonitorNotifyDetail,MonitorItem,SystemConfig,MonitorNotifyConfig
from format_es_data import FormatData

def monitor_configure(request):
    hosts = MonitorHost.objects.all()
    templates = MonitorTemplate.objects.all()
    items = MonitorItem.objects.all()
    policys = MonitorNotifyPolicy.objects.all()
    serverapi = SystemConfig.objects.get(name='Server API')
    esapi = SystemConfig.objects.get(name='ES API')
    return render_to_response("monitor/monitor.html",{'hosts':hosts,'templates':templates,'items':items,'policys':policys,'serverapi':serverapi,'esapi':esapi})

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

def edit_host(request,name):
    name = name
    host = MonitorHost.objects.get(name=name)
    return render_to_response("monitor/editHost.html",{'host':host})

def add_template(request):
    if request.method == 'POST':
        data = json.loads(request.POST.get('template'))
        TemplateForm(data)
    items = MonitorItem.objects.all()
    policys = MonitorNotifyPolicy.objects.all()
    return render_to_response("monitor/addTemplate.html",{'policys':policys,'items':items})

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

        
def edit_tempate(request,name):
    name = name
    template = MonitorTemplate.objects.get(name=name)
    items = template.items.all()
    policys = template.policy.all()
    return render_to_response("monitor/editTemplate.html",{'template':template,'items':items,'policys':policys})

def add_item(request):
    if request.method == 'POST':
        data = json.loads(request.POST.get('item'))
        ItemForm(data)
    return render_to_response("monitor/addItem.html")

def del_item(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        try:
            MonitorItem.objects.get(name=name).delete()
        except Exception as e:
            print e
            return HttpResponse(json.dumps({'status':False,'msg':str(e)}))
        else:
            return HttpResponse(json.dumps({'status':True}))

def edit_item(request,name):
    name = name
    item = MonitorItem.objects.get(name=name)
    return render_to_response("monitor/editItem.html",{'item':item})        


def add_policy(request):
    if request.method == 'POST':
        data = json.loads(request.POST.get('policy'))
        PolicyForm(data)
    return render_to_response("monitor/addPolicy.html")

def del_policy(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        try:
            MonitorNotifyPolicy.objects.get(name=name).delete()
        except Exception as e:
            print e
            return HttpResponse(json.dumps({'status':False,'msg':str(e)}))
        else:
            return HttpResponse(json.dumps({'status':True}))
        
def edit_policy(request,name):
    name = name
    policy = MonitorNotifyPolicy.objects.get(name=name)
    return render_to_response("monitor/editPolicy.html",{'policy':policy})

def monitor_graph(request):
    if request.method == 'POST':
        data = json.loads(request.POST.get("data"))
        formatobj = FormatData(data)
        return_data = formatobj.dispatch()
        print return_data
        return HttpResponse(json.dumps(return_data))
    hosts = MonitorHost.objects.all()
    return render_to_response("monitor/graph.html",{'hosts':hosts})

def monitor_notify(request):
    problems = MonitorProblem.objects.all().order_by('-time')
    notifys = MonitorNotifyDetail.objects.all().order_by('-time')
    notifyconfigs = MonitorNotifyConfig.objects.all()
    return render_to_response("monitor/notify.html",{'problems':problems,'notifys':notifys,'notifyconfigs':notifyconfigs})

def add_notify(request):
    if request.method == 'POST':
        pass
    hosts = MonitorHost.objects.all()
    return render_to_response("monitor/addNotify.html",{'hosts':hosts})