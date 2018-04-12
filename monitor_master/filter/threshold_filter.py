#!/usr/bin/env python
#_*_ coding:utf-8 _*_
'''
Created on 2018年4月11日

@author: yangxu
'''
'''
1 根据监控数据中的 host 查询使用的模版
2 根据模版查询 告警策略
3 根据告警策略定义的阀值 过滤数据，如果大于阀值，组装信息写入MonitorProblem 表

'''

from monitor_master.models import MonitorHost,MonitorTemplate,MonitorNotifyPolicy,MonitorNotifyDetail
from monitor_master.serializers import ProblemSerializer,DetailSerializer
import problem_format,notifyDetail_format
from monitor_master.alarm import email_way,alarm_msg_template

class ThresholdFilter(object):
    def __init__(self,host):
        self.host = host
        self.policy_dict = self.get_policy()
        
        
    def get_policy(self):
        policy_dict = {}
        template_name =  MonitorHost.objects.get(name=self.host).template
        policys_obj = MonitorTemplate.objects.get(name=template_name).policy.all()
        for policy in policys_obj:
            name = str(policy.name.split('_')[0])
            policy_dict[name] = {}
            policy_obj = MonitorNotifyPolicy.objects.get(name=policy.name)
            policy_dict[policy.name.split('_')[0]]['warning'] = policy_obj.warning_threshold
            policy_dict[policy.name.split('_')[0]]['danger'] = policy_obj.danger_threshold
        return policy_dict
    
    def get_threshold(self,policy_name):
        threshold_dict = {'begin_warning':None,'end_warning':None,'danger':None}
        if self.policy_dict.get(policy_name,None):
            begin_warning = (self.policy_dict[policy_name]['warning'].split('~')[0]).split('%')[0]
            end_warning = (self.policy_dict[policy_name]['warning'].split('~')[1]).split('%')[0]
            danger = (self.policy_dict[policy_name]['danger'].split('>')[1]).split('%')[0]
            threshold_dict['begin_warning']=begin_warning
            threshold_dict['end_warning']=end_warning
            threshold_dict['danger']=danger
        return threshold_dict
        
    def cpu(self,usage,date):
        problem_data = problem_format.cpu_problem_format.copy()
        threshold_dict = self.get_threshold('cpu')
        usage = usage*100
        if usage >= float(threshold_dict['begin_warning']) and usage < float(threshold_dict['end_warning']):
            self.handle(usage, date, 'CPU', 'warning')
            
        elif usage >= float(threshold_dict['danger']):
            print 'danger'
            
    def memory(self,usage):
        print self.get_threshold('memory')
        
    
    def handle(self,usage,date,monitor_type,level):
        problem_data = problem_format.cpu_problem_format.copy()
        problem_data['name'] = u'{} utilization:{}%'.format(monitor_type,usage)
        problem_data['type'] = monitor_type
        problem_data['host'] = str(self.host)
        problem_data['time'] = date
        
        message = alarm_msg_template.email_template.format(date,self.host,problem_data['name'],level)
        content = notifyDetail_format.notify_detail_content.format(date,self.host,problem_data['name'],level)
        send_email_result = email_way.send_email_dispatch(to='18508503875@139.com', subject=u'{} 利用率告警'.format(monitor_type), message=message)
        if send_email_result['status']:
            notify_detail_data = notifyDetail_format.generate_detail_data("Email", "{} 利用率告警".format(monitor_type), content, "18508503875@139.com", "SEND","")
            notifyDetail_format.write_notify(notify_detail_data)
        else:
            notify_detail_data = notifyDetail_format.generate_detail_data("Email", "{} 利用率告警".format(monitor_type), content, "18508503875@139.com", "UNSEND",send_email_result['msg'])
            notifyDetail_format.write_notify(notify_detail_data)
            
        serializer = ProblemSerializer(data=problem_data)
        if serializer.is_valid():
            serializer.save()
        
            
            
        
        
        