#!/usr/bin/env python
#_*_ coding:utf-8 _*_
'''
Created on 2018年4月9日

@author: yangxu
'''
from rest_framework import serializers
from models import MonitorHost,MonitorItem,MonitorNotifyDetail,\
MonitorNotifyPolicy,MonitorProblem,MonitorTemplate,SystemConfig,MonitorNotifyConfig

class HostSerializer(serializers.ModelSerializer):
    class Meta:
        model = MonitorHost
        #fields = ('address', 'agemonitor_agentname','port','status','template')
        fields = '__all__'
        
class DetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = MonitorNotifyDetail
        fields = '__all__'
        
class PolicySerializer(serializers.ModelSerializer):
    class Meta:
        model = MonitorNotifyPolicy
        fields = '__all__'
        
class ProblemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MonitorProblem
        fields = '__all__'
        
class TemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = MonitorTemplate
        fields = '__all__'

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MonitorItem
        fields = '__all__'
        
class ConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = SystemConfig
        fields = '__all__'
        
class NotifyConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = MonitorNotifyConfig
        fields = '__all__'