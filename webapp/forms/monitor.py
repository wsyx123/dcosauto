#!/usr/bin/env python
#_*_ coding:utf-8 _*_
'''
Created on 2018年3月31日

@author: yangxu
'''

from monitor_master.models import MonitorTemplate,MonitorHost,MonitorItem,MonitorNotifyPolicy
from monitor_master.serializers import TemplateSerializer,ItemSerializer,PolicySerializer

class TemplateForm(object):
    def __init__(self,data):
        self.data = data
        self.template_data = {
                            "name": self.data.get('name'),
                            "interval": self.data.get('interval'),
                            "items": [],
                            "policy": []
                            }
        policy_id_list = []
        item_id_list = []
        for policy in self.data.get('policys'):
            policy_id_list.append(MonitorNotifyPolicy.objects.get(name=policy).id)
        for item in self.data.get('items'):
            item_id_list.append(MonitorItem.objects.get(name=item).id)
        self.template_data['policy'] = policy_id_list
        self.template_data['items'] = item_id_list
        tempserializer = TemplateSerializer(data=self.template_data)
        if tempserializer.is_valid():
            tempserializer.save()

class ItemForm(object): 
    def __init__(self,data):
        self.data = data
        itemserializer = ItemSerializer(data=self.data)
        if itemserializer.is_valid():
            itemserializer.save()
            
class PolicyForm(object): 
    def __init__(self,data):
        self.data = data
        policyserializer = PolicySerializer(data=self.data)
        if policyserializer.is_valid():
            policyserializer.save()
               
        
class HostForm(object):
    def __init__(self,data):
        self.data = data
        self.modelname = MonitorHost
        self.fields = ['name','address','port','template','status']
        self.save()
        
    def save(self):
        modelobj = self.modelname()
        for field in self.fields:
            if self.data.has_key(field):
                print self.data.get(field)
                if field == 'template':
                    value = MonitorTemplate.objects.get(name=self.data.get(field))
                elif field == 'status':
                    if self.data.get(field):
                        value = 'UP'
                    else:
                        value = 'DOWN'
                else:
                    value = self.data.get(field)
                setattr(modelobj, field, value)
        modelobj.save()
                