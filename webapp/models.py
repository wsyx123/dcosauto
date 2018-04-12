# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import django.utils.timezone as timezone

# Create your models here.
class platformhosts(models.Model):
    hostname = models.CharField(max_length=32,null=True,blank=True,verbose_name='主机名')
    address = models.CharField(max_length=32,unique=True,verbose_name='IP地址')
    sversion = models.CharField(max_length=32,null=True,blank=True,verbose_name='系统版本')
    dversion = models.CharField(max_length=32,null=True,blank=True,verbose_name='docker版本')
    ddriver = models.CharField(max_length=32,null=True,blank=True,verbose_name='docker存储驱动')
    ddata = models.CharField(max_length=32,null=True,blank=True,verbose_name='docker存储目录')
    cpu = models.CharField(max_length=32,null=True,blank=True,verbose_name='CPU')
    mem = models.CharField(max_length=32,null=True,blank=True,verbose_name='内存')
    disk = models.CharField(max_length=32,null=True,blank=True,verbose_name='磁盘')
    status = models.CharField(max_length=10,default='down',verbose_name='状态')
    createtime = models.DateTimeField(auto_now_add=True,verbose_name='创建时间')
    
    def __unicode__(self):
        return '%s' %(self.address)

class ImageRegistry(models.Model):
    address = models.CharField(max_length=32,unique=True,verbose_name="IP地址")
    label = models.CharField(max_length=32,verbose_name="备注")
    type = models.CharField(max_length=30,verbose_name="API类型")
    count = models.IntegerField(verbose_name="镜像数量")
    status = models.CharField(default='up',max_length=10,verbose_name="状态")
    createtime = models.DateTimeField(auto_now_add=True,verbose_name='创建时间')
    
    def __unicode__(self):
        return '%s' %(self.address)

class platformcluster(models.Model):
    name = models.CharField(max_length=32,unique=True,verbose_name='集群名')
    version = models.CharField(max_length=32,verbose_name='版本')
    createtime = models.DateTimeField(auto_now_add=True,verbose_name='创建时间')
    
    
    def __unicode__(self):
        return '%s' %(self.name)   

    
class platformtemplate(models.Model):
    name =  models.CharField(max_length=20,unique=True,verbose_name='模版名')
    label = models.CharField(max_length=64,verbose_name='说明')
    type = models.CharField(max_length=20,verbose_name='模版类型')
    image = models.CharField(max_length=255,verbose_name='镜像名')
    netmode = models.CharField(max_length=32,verbose_name='网络模式')
    cport = models.CharField(max_length=10,verbose_name='容器端口')
    hport = models.CharField(max_length=10,verbose_name='主机端口')
    env  = models.TextField(null=True,blank=True,verbose_name='环境变量')
    volume = models.TextField(max_length=512,null=True,blank=True,verbose_name='卷映射')
    dockerfile = models.TextField(null=True,blank=True)
    createtime = models.DateTimeField(auto_now_add=True,verbose_name='创建时间')
    
    def __unicode__(self):
        return '%s' %(self.name)

class platformcomponent(models.Model):
    cluster = models.ForeignKey('platformcluster',verbose_name='集群')
    template = models.ForeignKey('platformtemplate',verbose_name='模版')
    name = models.CharField(max_length=20,unique=True,verbose_name='容器名')
    host = models.ForeignKey('platformhosts',on_delete=models.PROTECT,verbose_name='主机IP')
    netmode = models.CharField(max_length=32,verbose_name='网络模式')
    image = models.CharField(max_length=255,verbose_name='镜像名')
    cport = models.CharField(max_length=10,verbose_name='容器端口')
    hport = models.CharField(max_length=10,verbose_name='主机端口')
    env  = models.CharField(max_length=512,null=True,blank=True,verbose_name='环境变量')
    volume = models.CharField(max_length=512,null=True,blank=True,verbose_name='卷映射')
    createtime = models.DateTimeField(auto_now_add=True,verbose_name='创建时间')
    status = models.CharField(max_length=5,default='up',verbose_name='状态')
    
    def __unicode__(self):
        return '%s' %(self.name)

# class MonitorTemplate(models.Model):
#     name =  models.CharField(max_length=20,unique=True,verbose_name='名称')
#     items = models.CharField(max_length=255,verbose_name='监控项')
#     policy = models.CharField(max_length=255,null=True,blank=True,verbose_name='告警策略')
#     interval = models.CharField(max_length=5,verbose_name='监控频率')
#     cpu = models.CharField(max_length=64,null=True,blank=True,verbose_name='cpu')
#     memory = models.CharField(max_length=64,null=True,blank=True,verbose_name='memory')
#     disk = models.CharField(max_length=225,null=True,blank=True,verbose_name='disk')
#     network = models.CharField(max_length=64,null=True,blank=True,verbose_name='network')
#     
#     def __unicode__(self):
#         return '%s' %(self.name)
#     
# class MonitorHost(models.Model):
#     name = models.CharField(max_length=64,unique=True,verbose_name='名称')
#     address = models.CharField(max_length=32,unique=True,verbose_name='IP地址')
#     port = models.CharField(max_length=32,unique=True,verbose_name='端口')
#     template = models.ForeignKey('MonitorTemplate',on_delete=models.PROTECT,verbose_name='模版')
#     status = models.CharField(max_length=15,default='enabled',verbose_name='状态')
#     agent = models.CharField(max_length=5,default='down',verbose_name='Agent状态')
#     
#     def __unicode__(self):
#         return '%s' %(self.name)
# 
# class MonitorProblem(models.Model):
#     name = models.CharField(max_length=255,verbose_name='名称')
#     time = models.DateTimeField(default = timezone.now,verbose_name='时间')
#     address = models.CharField(max_length=32,verbose_name='主机')
#     level = models.CharField(max_length=16,verbose_name='级别')
#     status = models.CharField(max_length=16,default='unconfirmed',verbose_name='状态')
#     
#     def __unicode__(self):
#         return '%s' %(self.name)
#     
# class MonitorNotifyDetail(models.Model):
#     mode = models.CharField(max_length=10,verbose_name='通知方式')
#     theme = models.CharField(max_length=32,verbose_name='主题')
#     content = models.TextField(verbose_name="内容")
#     send_to = models.CharField(max_length=64,verbose_name="接收人")
#     status = models.CharField(max_length=10,default='send',verbose_name="发送状态")
#     
#     def __unicode__(self):
#         return '%s' %(self.name)
#     
# class MonitorNotifyPolicy(models.Model):
#     name = models.CharField(max_length=255,verbose_name='名称')
#     warning_threshold = models.CharField(max_length=255,verbose_name='warning阀值')
#     danger_threshold = models.CharField(max_length=255,verbose_name='danger阀值')
#     promote = models.CharField(max_length=255,verbose_name='告警升级/次')
#     
#     def __unicode__(self):
#         return '%s' %(self.name)
        