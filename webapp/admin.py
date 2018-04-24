# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from models import platformcluster,platformcomponent,platformtemplate,platformhosts
from models import ImageRegistry

class PlatformClusterAdmin(admin.ModelAdmin):
    list_display = ('name','version','createtime')
    
class PlatformComponentAdmin(admin.ModelAdmin):
    list_display = ('cluster','name','host','netmode','image',
                    'cport','hport','env','volume','template','status')
    
class PlatformtemplateAdmin(admin.ModelAdmin):
    list_display = ('name','label','type','netmode','image','cport',
                    'hport','env','volume','createtime')
    
class PlatformHostsAdmin(admin.ModelAdmin):
    list_display = ('hostname','address','sversion','dversion',
                    'ddriver','ddata','cpu','mem','disk','status','createtime')

class ImageRegistryAdmin(admin.ModelAdmin):
    list_display = ('address','label','type','count','createtime','status')  
    
# class MonitorTemplateAdmin(admin.ModelAdmin):
#     list_display = ('name','items','interval','cpu','memory','disk','network')  
#     
# class MonitorHostAdmin(admin.ModelAdmin):
#     list_display = ('name','address','port','template','status','monitor_agent')  
#     
# class MonitorNotifyPolicyAdmin(admin.ModelAdmin):
#     list_display = ('name','warning_threshold','danger_threshold','promote')
#     
# class MonitorProblemAdmin(admin.ModelAdmin):
#     list_display = ('name','time','address','level','status')
#     
# class MonitorNotifyDetailAdmin(admin.ModelAdmin):
#     list_display = ('mode','theme','content','send_to','status')

admin.site.register(platformcluster, PlatformClusterAdmin)
admin.site.register(platformcomponent, PlatformComponentAdmin)
admin.site.register(platformtemplate, PlatformtemplateAdmin)
admin.site.register(platformhosts, PlatformHostsAdmin)
admin.site.register(ImageRegistry,ImageRegistryAdmin)
# admin.site.register(MonitorTemplate,MonitorTemplateAdmin)
# admin.site.register(MonitorHost,MonitorHostAdmin)
# admin.site.register(MonitorNotifyPolicy,MonitorNotifyPolicyAdmin)
# admin.site.register(MonitorProblem,MonitorProblemAdmin)
# admin.site.register(MonitorNotifyDetail,MonitorNotifyDetailAdmin)