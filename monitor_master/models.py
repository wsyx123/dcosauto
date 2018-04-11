# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import django.utils.timezone as timezone

# Create your models here.


class MonitorTemplate(models.Model):
    TEMPLATE_INTERVAL_CHOICE=(('60s','60'),('120s','120'))
    name =  models.CharField(max_length=20,unique=True,verbose_name='名称')
    items = models.ManyToManyField('MonitorItem')
    policy = models.ManyToManyField('MonitorNotifyPolicy')
    interval = models.CharField(max_length=5,choices=TEMPLATE_INTERVAL_CHOICE,verbose_name='监控频率')
    
    def get_policy(self):
        return "\n".join([p.name for p in self.policy.all()])
    get_policy.short_description = '告警策略'
    def get_items(self):
        return "\n".join([p.name for p in self.items.all()]) 
    get_items.short_description ='监控项'
    
    def __unicode__(self):
        return '%s' %(self.name)
    
class MonitorItem(models.Model):
    name =  models.CharField(max_length=20,unique=True,verbose_name='名称')
    value = models.CharField(max_length=255,verbose_name='键值')
    
    def __unicode__(self):
        return '%s' %(self.name)
    
class MonitorHost(models.Model):
    HOST_STATUS = (('UP','UP'),('DOWN','DOWN'))
    name = models.CharField(max_length=64,unique=True,verbose_name='名称')
    address = models.CharField(max_length=32,unique=True,verbose_name='IP地址')
    port = models.CharField(max_length=32,verbose_name='端口')
    template = models.ForeignKey('MonitorTemplate',on_delete=models.PROTECT,verbose_name='模版')
    status = models.CharField(max_length=5,default='DOWN',choices=HOST_STATUS,verbose_name='状态')
    agent = models.CharField(max_length=5,default='DOWN',choices=HOST_STATUS,verbose_name='Agent状态')
    
    def __unicode__(self):
        return '%s' %(self.name)

class MonitorProblem(models.Model):
    PROBLEM_STATUS = (('CONFIRMED','CONFIRMED'),('UNCONFIRMED','UNCONFIRMED'))
    PROBLEM_LEVEL = (('WARNING','WARNING'),('DANGER','DANGER'))
    PROBLEM_TYPE = (('CPU','CPU'),('NETWORK','NETWORK'),('DISK','DISK'),('MEMORY','MEMORY'))
    name = models.CharField(max_length=255,verbose_name='名称')
    type = models.CharField(max_length=15,choices=PROBLEM_TYPE,verbose_name='类型')
    time = models.DateTimeField(default = timezone.now,verbose_name='时间')
    host = models.CharField(max_length=32,verbose_name='主机')
    level = models.CharField(max_length=16,default='WARNING',choices=PROBLEM_LEVEL,verbose_name='级别')
    status = models.CharField(max_length=16,default='UNCONFIRMED',choices=PROBLEM_STATUS,verbose_name='状态')
    
    def __unicode__(self):
        return '%s' %(self.name)
    
class MonitorNotifyDetail(models.Model):
    NOTIFY_WAY = (('Email','Email'),('SMS','SMS'))
    SEND_STATUS = (('SEND','SEND'),('UNSEND','UNSEND'))
    mode = models.CharField(max_length=10,default='Email',choices=NOTIFY_WAY,verbose_name='通知方式')
    theme = models.CharField(max_length=32,verbose_name='主题')
    content = models.TextField(verbose_name="内容")
    send_to = models.CharField(max_length=64,verbose_name="接收人")
    status = models.CharField(max_length=10,default='SEND',choices=SEND_STATUS,verbose_name="发送状态")
    
    def __unicode__(self):
        return '%s' %(self.name)
    
class MonitorNotifyPolicy(models.Model):
    name = models.CharField(max_length=255,verbose_name='名称')
    warning_threshold = models.CharField(max_length=255,verbose_name='warning阀值')
    danger_threshold = models.CharField(max_length=255,verbose_name='danger阀值')
    promote = models.CharField(max_length=255,verbose_name='告警升级/次')
    
    def __unicode__(self):
        return '%s' %(self.name)
        