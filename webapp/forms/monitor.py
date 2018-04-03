#!/usr/bin/env python
#_*_ coding:utf-8 _*_
'''
Created on 2018年3月31日

@author: yangxu
'''

from webapp.models import MonitorTemplate,MonitorHost


class TemplateForm(object):
    def __init__(self,data):
        self.data = data
        self.modelname = MonitorTemplate
        self.fields = ['name','interval','policy','cpu','memory','disk','network']
        self.save()
        
    def save(self):
        modelobj = self.modelname()
        items = ''
        for field in self.fields:
            if self.data.has_key(field):
                if field != 'name' and field != 'interval' and field != 'policy':
                    items = items + field + ','
                if field == 'network':
                    value = self.data.get(field).split(',')
                else:
                    value = self.data.get(field)
                setattr(modelobj, field, value)
        items = items.strip(',')
        setattr(modelobj, 'items', items)
        modelobj.save()

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
                else:
                    value = self.data.get(field)
                setattr(modelobj, field, value)
        modelobj.save()
                