# -*- coding: utf-8 -*-

from django.db import models

# Create your models here.
class platformhosts(models.Model):
    HOST_STATUS = (('up','up',),('down','down'))
    hostname = models.CharField(max_length=32,null=True,blank=True,verbose_name='主机名')
    address = models.CharField(max_length=32,unique=True,verbose_name='IP地址')
    sversion = models.CharField(max_length=32,null=True,blank=True,verbose_name='系统版本')
    dversion = models.CharField(max_length=32,null=True,blank=True,verbose_name='docker版本')
    ddriver = models.CharField(max_length=32,null=True,blank=True,verbose_name='docker存储驱动')
    ddata = models.CharField(max_length=32,null=True,blank=True,verbose_name='docker存储目录')
    cpu = models.CharField(max_length=32,null=True,blank=True,verbose_name='CPU')
    mem = models.CharField(max_length=32,null=True,blank=True,verbose_name='内存')
    disk = models.CharField(max_length=32,null=True,blank=True,verbose_name='磁盘')
    status = models.CharField(max_length=10,default='down',choices=HOST_STATUS,verbose_name='状态')
    createtime = models.DateTimeField(auto_now_add=True,verbose_name='创建时间')
    
    def __unicode__(self):
        return '%s' %(self.address)

'''--------------资产管理表 共6张表---------------'''
class AssetHost(models.Model):
    HOST_STATUS = (('up','up',),('down','down'))
    PLATFORM = (('Linux','Linux'),('Windows','Windows'))
    hostname = models.CharField(max_length=32,unique=True,verbose_name='主机名')
    label = models.CharField(max_length=32,null=True,blank=True,verbose_name='备注')
    pri_address = models.CharField(max_length=32,unique=True,verbose_name='私网IP')
    pub_address = models.CharField(max_length=32,unique=True,verbose_name='公网IP')
    port = models.IntegerField(verbose_name='端口')
    serial_number = models.CharField(max_length=32,verbose_name='序列号')
    asset_number = models.CharField(max_length=32,verbose_name='资产编号')
    manufacturer = models.CharField(max_length=64,verbose_name='制造商')
    model = models.CharField(max_length=64,verbose_name=' 型号')
    cpu = models.CharField(max_length=32,null=True,blank=True,verbose_name='CPU')
    memory = models.CharField(max_length=32,null=True,blank=True,verbose_name='内存')
    disk = models.CharField(max_length=32,null=True,blank=True,verbose_name='磁盘')
    platform = models.CharField(max_length=10,choices=PLATFORM,verbose_name='系统平台')
    version = models.CharField(max_length=32,null=True,blank=True,verbose_name='系统版本')
    status = models.CharField(max_length=10,default='down',choices=HOST_STATUS,verbose_name='状态')
    owner = models.ForeignKey('Employee',verbose_name='使用者')
    group = models.ForeignKey('AssetGroup',verbose_name='资产组')
    creator = models.CharField(max_length=16,verbose_name='创建人')
    createtime = models.DateTimeField(auto_now_add=True,verbose_name='创建时间')
    '''
    host被systemuser 关联 且是manytomany ， 想知道自己被哪些  systemuser关联，可以使用 '反向查询':
    hostobj = AssetHost.objects.get(hostname='keystone')
    hostobj.SystemUser_set.all()
    '''
    
    def __unicode__(self):
        return '%s' %(self.address)

class AssetGroup(models.Model):
    name = models.CharField(max_length=16,verbose_name='组名')
    label = models.CharField(max_length=64,verbose_name='备注')
    maintainer = models.ForeignKey('Employee',verbose_name='运维人员')
    creator = models.CharField(max_length=16,verbose_name='创建人')
    

class SystemUser(models.Model):
    name = models.CharField(max_length=16,verbose_name='帐号')
    label = models.CharField(max_length=64,verbose_name='备注')
    group = models.CharField(max_length=16,verbose_name='组')
    enable = models.BooleanField(default=False,verbose_name='启用')
    creator = models.CharField(max_length=16,verbose_name='创建人')
    host = models.ManyToManyField('AssetHost',verbose_name='关联主机')
    createtime = models.DateTimeField(auto_now_add=True,verbose_name='创建时间')
    expiretime = models.DateTimeField(auto_now_add=True,verbose_name='创建时间')

class Departments(models.Model):
    name = models.CharField(max_length=32,verbose_name='部门名称')
    label = models.CharField(max_length=64,verbose_name='职能范围')
    super_department = models.ForeignKey('self',verbose_name='上级部门')
    leader = models.ForeignKey('Employee',verbose_name='领导')
    
class Projects(models.Model):
    PROJECT_PROGRESS = (('需求分析','需求分析'),('原型设计','原型设计'))
    name = models.CharField(max_length=32,verbose_name='项目名')
    department = models.ForeignKey('Departments',verbose_name='所属部门')
    leader = models.ForeignKey('Employee',verbose_name='负责人')
    progress = models.CharField(max_length=64,choices=PROJECT_PROGRESS,verbose_name='阶段')

class Employee(models.Model):
    JOB=(('FRONTEND','FRONTEND'),('BACKEND','BACKEND'))
    name = models.CharField(max_length=32,verbose_name='员工')
    department = models.ForeignKey('Departments',verbose_name='部门')
    project = models.ManyToManyField('Projects',verbose_name='项目')
    job = models.CharField(max_length=15,choices=JOB,verbose_name='职务')
    tel = models.IntegerField(verbose_name='电话')
    email = models.EmailField(verbose_name='邮箱')
    
'''--------------end 资产管理表---------------'''   
    
'''--------------作业中心表---------------''' 

class ExecuteCmdRecord(models.Model):
    pass

class SendFileRecord(models.Model):
    pass

class CronTask(models.Model):
    pass

class CronTaskRecord(models.Model):
    pass

'''--------------end 作业中心表---------------''' 

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
    template = models.ForeignKey('platformtemplate',related_name='temp',verbose_name='模版')
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

        