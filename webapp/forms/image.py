#!/usr/bin/env python
#_*_ coding:utf-8 _*_
'''
Created on 2018年3月27日

@author: yangxu
'''
from webapp.common.dockerhubv2api import dockerhubv2
from webapp.models import ImageRegistry

class ImageForm(object):
    def __init__(self,data):
        self.data = data
        self.address = self.data.get("address")
        self.label = self.data.get("label")
        self.type = self.data.get("type")
        self.status = self.data.get("status")
        self.count = None
        self.save()
        
    def set_count(self):
        if self.status == 'up':
            host = str(self.address.split(":")[0])
            port = str(self.address.split(":")[1])
            instancev2 = dockerhubv2(host,port)
            self.count = instancev2.countImageAmount()
        else:
            self.count = 0
            
    def save(self):
        self.set_count()
        try:
            ImageRegistry.objects.create(address=self.address,
                                         label=self.label,
                                         type=self.type,
                                         count=self.count,
                                         status=self.status)
        except Exception as e:
            print e
        