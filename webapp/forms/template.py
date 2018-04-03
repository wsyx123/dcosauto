#!/usr/bin/env python
#_*_ coding:utf-8 _*_
'''
Created on 2018年3月25日

@author: yangxu
'''
class TemplateForm(object):
    def __init__(self,data,modelname):
        self.data = data
        self.field_key = ['name','label','type','image','netmode',
                          'cport','hport','env','volume','dockerfile']
        self.modelname = modelname
        self.set_field_value()
        
    def set_field_value(self):
        self.modelobj = self.modelname()
        for field in self.field_key:
            value = self.data.get(field)
            setattr(self.modelobj, field, value)
        self.modelobj.save()
